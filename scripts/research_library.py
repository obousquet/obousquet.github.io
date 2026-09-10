#!/usr/bin/env python3
"""Locate, search, index, and reserve papers in a configured shared library."""
from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import socket
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

DOMAINS = ('math', 'biomed', 'physics')


def read_json(path):
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}


def normalized_title(value):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode().lower())


def identifiers(data):
    """Read only bibliographic identity fields, never identifiers cited in notes."""
    found = set()
    for key in ('doi', 'DOI', 'arxiv', 'arxiv_id', 'arxiv_url', 'url', 'source_url', 'source_pdf', 'pdf_url', 'pmid', 'pmcid'):
        value = data.get(key)
        if not isinstance(value, (str, int)):
            continue
        text = unquote(str(value)).strip()
        if key.lower() == 'doi' or 'doi.org/' in text:
            match = re.search(r'10\.\d{4,9}/\S+', text, re.I)
            if match:
                found.add('doi:' + match.group().rstrip('.,;').lower())
        if key.startswith('arxiv') or 'arxiv.org/' in text:
            match = re.search(r'(\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?', text, re.I)
            if match:
                found.add('arxiv:' + match.group(1).lower())
        if key in ('pmid', 'pmcid'):
            found.add(key + ':' + text.lower())
    return sorted(found)


def citation_url(data):
    for key in ('url', 'source_url', 'doi', 'arxiv_url', 'arxiv', 'arxiv_id'):
        value = str(data.get(key) or '').strip()
        if value.startswith(('https://', 'http://')):
            return value
        if value.startswith('10.'):
            return 'https://doi.org/' + value
        if key.startswith('arxiv') and value:
            return 'https://arxiv.org/abs/' + value
    return ''


def configuration(start=None):
    start = Path(start or Path.cwd()).resolve()
    for directory in (start, *start.parents):
        path = directory / '.research-library.json'
        if path.exists():
            data = read_json(path)
            return directory, data
    return start, {}


def library_root(explicit=None):
    base, config = configuration()
    value = explicit or os.environ.get('RESEARCH_LIBRARY_ROOT') or config.get('root')
    if not value:
        raise ValueError('No shared library configured: set .research-library.json, RESEARCH_LIBRARY_ROOT, or --root')
    root = (base / value).resolve()
    if not root.is_dir():
        raise ValueError(f'Shared library is unavailable: {root}; do not create a local substitute')
    return root


def records(root):
    rows = []
    for domain in DOMAINS:
        base = root / domain
        if not base.exists():
            continue
        for packet in sorted(base.iterdir()):
            if not packet.is_dir() or packet.is_symlink():
                continue
            metadata = read_json(packet / 'metadata.json')
            record = read_json(packet / 'library-record.json')
            ids = sorted(set(identifiers(metadata)) | set(record.get('identifiers', [])))
            rows.append({'path': packet.relative_to(root).as_posix(), 'domain': domain,
                         'key': packet.name, 'title': metadata.get('title', packet.name),
                         'authors': metadata.get('authors', ''), 'year': metadata.get('year', ''),
                         'identifiers': ids, 'aliases': record.get('aliases', []),
                         'origins': record.get('origins', []),
                         'acquisition_status': metadata.get('acquisition_status', 'existing')})
    return rows


def write_catalog(root, rows):
    target = root / 'catalog.json'
    temporary = target.with_name(f'.catalog.{os.getpid()}.tmp')
    temporary.write_text(json.dumps({'papers': rows}, indent=2, ensure_ascii=False) + '\n')
    temporary.replace(target)


def matched_excerpt(content, query):
    terms = query.casefold().split()
    folded = content.casefold()
    position = folded.find(query.casefold())
    if position < 0:
        candidates = [match.start() for term in terms for match in list(re.finditer(re.escape(term), folded))[:40]]
        position = max(candidates, key=lambda start: sum(term in folded[max(0,start-100):start+500] for term in terms), default=0)
    start = max(0, position - 100)
    return content[start:position + 600].strip(), content.count('\n', 0, position) + 1


def search_library(root, query, include_sources=False):
    """Search bibliographic identity and succinct results before optional raw text."""
    terms = query.casefold().split()
    normalized = normalized_title(query)
    matches = []
    seen = set()
    for row in records(root):
        serialized = json.dumps(row, ensure_ascii=False).casefold()
        if all(term in serialized for term in terms) or (normalized and normalized in normalized_title(row['title'])):
            title_match = query.casefold() in str(row['title']).casefold()
            exact_id = any(query.casefold() == i.casefold() or query.casefold() == i.partition(':')[2].casefold() for i in row['identifiers'])
            matches.append({'kind': 'paper', 'path': row['path'], 'title': row['title'],
                            'identifiers': row['identifiers'], 'aliases': row['aliases'],
                            '_score': 100 if exact_id else 80 if title_match else 30})
        packet = root / row['path']
        paths = sorted(packet.rglob('*.md'))
        if include_sources:
            paths += sorted(packet.rglob('*.txt')) + sorted(packet.rglob('*.tex'))
        for path in paths:
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            content = path.read_text(encoding='utf-8', errors='replace')
            folded = content.casefold()
            if not all(term in folded for term in terms):
                continue
            excerpt, line = matched_excerpt(content, query)
            matches.append({'kind': 'extraction' if path.suffix == '.md' else 'source',
                            'paper': row['path'], 'path': path.relative_to(root).as_posix(),
                            'line': line, 'excerpt': excerpt,
                            '_score': (65 if query.casefold() in folded else 35) + (5 if path.name == 'merged-results.md' else 0)})
    notes = root / 'project-notes'
    if notes.exists():
        note_paths = list(notes.rglob('*.md'))
        if include_sources:
            note_paths += list(notes.rglob('*.txt')) + list(notes.rglob('*.tex'))
        for path in sorted(note_paths):
            if path.name == 'index.md':
                continue
            content = path.read_text(encoding='utf-8', errors='replace')
            if all(term in content.casefold() for term in terms):
                excerpt, line = matched_excerpt(content, query)
                matches.append({'kind': 'project-note' if path.suffix == '.md' else 'source', 'path': path.relative_to(root).as_posix(),
                                'line': line, 'excerpt': excerpt, '_score': 60 if query.casefold() in content.casefold() else 25})
    return matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, help='Override the configured shared library')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('locate')
    search = sub.add_parser('search'); search.add_argument('query')
    search.add_argument('--sources', action='store_true', help='Also search extracted source text and TeX')
    search.add_argument('--limit', type=int, default=20, help='Maximum hits (default: 20; 0 for all)')
    sub.add_parser('index')
    reserve = sub.add_parser('reserve')
    reserve.add_argument('--key', required=True)
    reserve.add_argument('--domain', choices=DOMAINS)
    reserve.add_argument('--title', required=True)
    reserve.add_argument('--doi'); reserve.add_argument('--arxiv'); reserve.add_argument('--pmid')
    args = parser.parse_args()
    try:
        root = library_root(args.root)
    except ValueError as error:
        parser.error(str(error))
    if args.command == 'locate':
        print(root); return 0
    if args.command == 'search':
        if not args.query.strip(): parser.error('Search terms must not be empty')
        matches = search_library(root, args.query, args.sources)
        matches.sort(key=lambda row: (-row.pop('_score', 0), row.get('paper', row.get('path',''))))
        print(json.dumps({'total_hits': len(matches), 'hits': matches[:args.limit] if args.limit > 0 else matches},
                         indent=2, ensure_ascii=False)); return 0
    with (root / '.catalog.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        rows = records(root)
        if args.command == 'index':
            write_catalog(root, rows); print(f'Indexed {len(rows)} papers in {root}'); return 0
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', args.key):
            parser.error('--key must be a single citation key without path separators')
        domain = args.domain or configuration()[1].get('default_domain')
        if domain not in DOMAINS:
            parser.error('Set --domain or default_domain in .research-library.json')
        metadata = {k: getattr(args, k) for k in ('title', 'doi', 'arxiv', 'pmid') if getattr(args, k)}
        wanted = set(identifiers(metadata)); title = normalized_title(args.title)
        matches = [r for r in rows if wanted.intersection(r['identifiers'])
                   or (len(title) >= 20 and title == normalized_title(r['title']))
                   or args.key == r['key'] or args.key in r['aliases']]
        if matches:
            print(json.dumps({'status': 'reuse-or-review', 'matches': matches}, indent=2, ensure_ascii=False)); return 0
        packet = root / domain / args.key
        packet.mkdir(parents=True, exist_ok=False)
        metadata.update(citation_key=args.key, acquisition_status='reserved',
                        reserved_at=datetime.now(timezone.utc).isoformat(), reserved_by=socket.gethostname())
        (packet / 'metadata.json').write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + '\n')
        write_catalog(root, records(root))
        print(json.dumps({'status': 'reserved', 'path': str(packet)}, indent=2)); return 0


if __name__ == '__main__':
    raise SystemExit(main())
