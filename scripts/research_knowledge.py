#!/usr/bin/env python3
"""Index research sources, maintain internal packets, and build bounded context. Stdlib only."""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = 1
INDEX_VERSION = 2
KINDS = {'theorem', 'lemma', 'example', 'counterexample', 'conjecture', 'idea', 'failed-approach', 'correction', 'definition'}
STATUSES = {'proved', 'conditional', 'computational', 'conjectural', 'refuted', 'withdrawn', 'open', 'unreviewed'}
SKIP = {'.git', '.claude', '.agents', '.codex', '.venv', 'node_modules', '__pycache__', '.cache', 'submission', '.lake'}
SUFFIXES = {'.md', '.tex', '.txt'}

def digest(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()

def now():
    return datetime.now(timezone.utc).isoformat()

def read_json(path):
    return json.loads(Path(path).read_text())

def atomic(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + f'.{os.getpid()}.tmp')
    temp.write_text(content)
    temp.replace(path)

def json_write(path, data):
    atomic(path, json.dumps(data, indent=2, ensure_ascii=False) + '\n')

def config_path(explicit=None):
    if explicit or os.environ.get('RESEARCH_KNOWLEDGE_CONFIG'):
        return Path(explicit or os.environ['RESEARCH_KNOWLEDGE_CONFIG']).resolve()
    for base in (Path.cwd(), *Path.cwd().parents):
        pointer = base / '.research-knowledge.json'
        if pointer.exists():
            return (base / read_json(pointer)['config']).resolve()
        library = base / '.research-library.json'
        if library.exists():
            root = (base / read_json(library)['root']).resolve()
            candidate = root.parent / 'knowledge/workspace.json'
            if candidate.exists():
                return candidate
    raise ValueError('No knowledge registry: use --config, RESEARCH_KNOWLEDGE_CONFIG, or .research-knowledge.json')

class Workspace:
    def __init__(self, path):
        self.path = Path(path).resolve()
        self.data = read_json(self.path)
        if self.data.get('version') != SCHEMA:
            raise ValueError('Unsupported registry version')
        self.base = self.path.parent
        self.sources = {}
        for row in self.data['sources']:
            if row['id'] in self.sources:
                raise ValueError('Duplicate source id: ' + row['id'])
            self.sources[row['id']] = {**row, 'root': (self.base / row['path']).resolve()}
        self.dbpath = (self.base / self.data.get('cache', '.cache/knowledge.sqlite')).resolve()
        self.library = (self.base / self.data['library']).resolve()
        self.campaigns = self.data.get('campaigns', {})

    def source_path(self, source):
        root = self.sources[source['repo']]['root']
        path = (root / source['path']).resolve()
        if not path.is_relative_to(root):
            raise ValueError('Source escapes its configured root')
        return path

    def campaign(self, name):
        if not name:
            return {}
        if name == '.':
            cwd = Path.cwd().resolve()
            matches = [key for key, profile in self.campaigns.items()
                       if any(cwd.is_relative_to(self.sources[s]['root']) for s in profile.get('sources', []))]
            if len(matches) != 1:
                raise ValueError('Use an explicit campaign ID; current directory has no unique profile')
            name = matches[0]
        if name not in self.campaigns:
            raise ValueError('Unknown campaign: ' + name)
        return {'id': name, **self.campaigns[name]}

    def connect(self, write=False):
        if write:
            self.dbpath.parent.mkdir(parents=True, exist_ok=True)
            conn = sqlite3.connect(self.dbpath, timeout=60)
            conn.executescript('''
            CREATE TABLE IF NOT EXISTS files (key TEXT PRIMARY KEY, repo TEXT, path TEXT, sha TEXT, mtime INTEGER, size INTEGER);
            CREATE TABLE IF NOT EXISTS chunks (key TEXT PRIMARY KEY, filekey TEXT, repo TEXT, path TEXT,
                anchor TEXT, line INTEGER, title TEXT, body TEXT, meta TEXT, digest TEXT);
            CREATE INDEX IF NOT EXISTS chunks_filekey ON chunks(filekey);
            CREATE VIRTUAL TABLE IF NOT EXISTS search USING fts5(key UNINDEXED, title, body, aliases);
            CREATE TABLE IF NOT EXISTS state (key TEXT PRIMARY KEY, value TEXT);
            ''')
        else:
            if not self.dbpath.exists():
                raise ValueError('Index missing; run sync first')
            conn = sqlite3.connect(self.dbpath.as_uri() + '?mode=ro', uri=True, timeout=60)
        conn.row_factory = sqlite3.Row
        return conn


def parse_card(content):
    if not content.startswith('---\n{'):
        return None
    parts = content.split('\n---\n', 1)
    if len(parts) != 2:
        raise ValueError('Unclosed result card frontmatter')
    meta = json.loads(parts[0][4:])
    for field in ('id', 'title', 'kind', 'status', 'sources'):
        if not meta.get(field):
            raise ValueError('Missing card field: ' + field)
    if meta['kind'] not in KINDS or meta['status'] not in STATUSES:
        raise ValueError('Invalid card kind/status')
    if not isinstance(meta['sources'], list):
        raise ValueError('sources must be a list')
    for source in meta['sources']:
        if not all(source.get(k) for k in ('repo', 'path', 'sha256')):
            raise ValueError('Card source requires repo, path, sha256')
    if not parts[1].strip():
        raise ValueError('Empty card statement')
    return meta, parts[1].strip()


def chunks(content, path):
    card = parse_card(content)
    if card:
        meta, body = card
        return [(meta['id'], 1, meta['title'], body, meta)]
    # Preserve headings/TeX labels for navigation. Raw chunks are explicitly unreviewed.
    lines = content.splitlines(True)
    pieces = []
    start, title, anchor = 0, Path(path).stem, ''
    length = 0
    for i, line in enumerate(lines):
        heading = re.match(r'^(#{1,4})\s+(.+)|^\\(?:sub)*section\*?\{(.+)\}', line)
        if i > start and (heading or length > 10000):
            pieces.append((anchor, start + 1, title, ''.join(lines[start:i]), {}))
            start = i
            length = 0
        length += len(line)
        if heading:
            title = heading.group(2) or heading.group(3)
            anchor = title
        label = re.search(r'\\label\{([^}]+)\}', line)
        if label and not anchor:
            anchor = label.group(1)
    if start < len(lines):
        pieces.append((anchor, start + 1, title, ''.join(lines[start:]), {}))
    return pieces


def discover(ws):
    found, issues, seen = [], [], set()
    for repo, source in ws.sources.items():
        root = source['root']
        if not root.is_dir():
            issues.append({'repo': repo, 'issue': 'missing-root', 'path': str(root)})
            continue
        for parent, dirs, names in os.walk(root, followlinks=False, onerror=lambda exc: issues.append({'repo': repo, 'issue': str(exc)})):
            dirs[:] = sorted(d for d in dirs if d not in SKIP and not (Path(parent) / d).is_symlink()
                             and not any((Path(parent) / d).relative_to(root).match(p) for p in source.get('exclude', [])))
            for name in sorted(names):
                p = Path(parent) / name
                rel = p.relative_to(root)
                if p.is_symlink() or p.resolve() in seen:
                    continue
                selected = p.suffix in SUFFIXES or (p.suffix == '.json' and ('dashboard' in name or name in {'metadata.json', 'library-record.json'}))
                if source.get('include'):
                    selected = any(rel.match(pattern) for pattern in source['include'])
                if not selected or any(rel.match(pattern) for pattern in source.get('exclude', [])):
                    continue
                try:
                    stat = p.stat()
                    if stat.st_size > source.get('max_bytes', 8_000_000):
                        issues.append({'repo': repo, 'path': str(rel), 'issue': 'oversized'})
                        continue
                except OSError as exc:
                    issues.append({'repo': repo, 'path': str(rel), 'issue': str(exc)})
                    continue
                seen.add(p.resolve())
                found.append((repo, str(rel), p, stat))
    return found, issues


def sync(ws, full=False):
    ws.dbpath.parent.mkdir(parents=True, exist_ok=True)
    with ws.dbpath.with_suffix('.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        conn = ws.connect(True)
        changed = removed = 0
        found, issues = discover(ws)
        previous = {r['key']: r for r in conn.execute('SELECT * FROM files')}
        version = conn.execute("SELECT value FROM state WHERE key='indexer_version'").fetchone()
        full = full or not version or int(version[0]) != INDEX_VERSION
        seen = set()
        with conn:
            for repo, rel, path, stat in found:
                key = repo + ':' + rel
                seen.add(key)
                old = previous.get(key)
                if not full and old and old['mtime'] == stat.st_mtime_ns and old['size'] == stat.st_size:
                    continue
                try:
                    content = path.read_text(encoding='utf-8')
                    parts = chunks(content, rel)
                except (OSError, ValueError) as exc:
                    issues.append({'repo': repo, 'path': rel, 'issue': str(exc)})
                    seen.discard(key)  # remove an older successful parse; never serve it as current
                    continue
                sha = digest(content)
                if not full and old and old['sha'] == sha:
                    conn.execute('UPDATE files SET mtime=?,size=? WHERE key=?', (stat.st_mtime_ns, stat.st_size, key))
                    continue
                if old:
                    conn.execute('DELETE FROM search WHERE rowid IN (SELECT rowid FROM chunks WHERE filekey=?)', (key,))
                    conn.execute('DELETE FROM chunks WHERE filekey=?', (key,))
                conn.execute('INSERT OR REPLACE INTO files VALUES (?,?,?,?,?,?)', (key, repo, rel, sha, stat.st_mtime_ns, stat.st_size))
                for n, (anchor, line, title, body, meta) in enumerate(parts):
                    ck = digest(key + ':' + str(n))[:24]
                    conn.execute('INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?,?,?)',
                                 (ck, key, repo, rel, anchor, line, title, body, json.dumps({**meta, '_indexed_sha256': sha}), digest(body)))
                    aliases = ' '.join([meta.get('id', ''), *meta.get('aliases', []), *meta.get('assumptions', []), anchor])
                    rowid = conn.execute('SELECT rowid FROM chunks WHERE key=?', (ck,)).fetchone()[0]
                    conn.execute('INSERT INTO search(rowid,key,title,body,aliases) VALUES (?,?,?,?,?)', (rowid, ck, title, body, aliases))
                changed += 1
            for key in set(previous) - seen:
                conn.execute('DELETE FROM search WHERE rowid IN (SELECT rowid FROM chunks WHERE filekey=?)', (key,))
                conn.execute('DELETE FROM chunks WHERE filekey=?', (key,))
                conn.execute('DELETE FROM files WHERE key=?', (key,))
                removed += 1
            report = {'updated': now(), 'files': len(seen), 'changed': changed, 'removed': removed,
                      'chunks': conn.execute('SELECT count(*) FROM chunks').fetchone()[0], 'issues': issues,
                      'registry_sha256': digest(ws.path.read_bytes()),
                      'sources': {r: sum(1 for x in found if x[0] == r) for r in ws.sources}}
            conn.execute('INSERT OR REPLACE INTO state VALUES (?,?)', ('sync', json.dumps(report)))
            conn.execute('INSERT OR REPLACE INTO state VALUES (?,?)', ('indexer_version', str(INDEX_VERSION)))
        conn.close()
        return report


def freshness(ws, meta):
    problems = []
    if not hasattr(ws, '_fingerprints'): ws._fingerprints = {}
    for source in meta.get('sources', []):
        try:
            p = ws.source_path(source)
            stat = p.stat()
            cachekey = (str(p), stat.st_mtime_ns, stat.st_size)
            if cachekey not in ws._fingerprints:
                ws._fingerprints = {key: value for key, value in ws._fingerprints.items() if key[0] != str(p)}
                ws._fingerprints[cachekey] = digest(p.read_bytes())
            if ws._fingerprints[cachekey] != source['sha256']:
                problems.append('changed: ' + source['repo'] + ':' + source['path'])
            if source.get('anchor') and source['anchor'] not in p.read_text(encoding='utf-8', errors='replace'):
                problems.append('missing anchor: ' + source['anchor'])
        except (OSError, ValueError, KeyError) as exc:
            problems.append('unavailable source: ' + str(exc))
    return problems


def allowed(ws, repo, private):
    return private or ws.sources.get(repo, {}).get('visibility') != 'private'


def accessible(ws, row, private):
    return allowed(ws, row['repo'], private) and all(allowed(ws, s['repo'], private) for s in json.loads(row['meta']).get('sources', []))


def result(ws, row):
    meta = json.loads(row['meta'])
    evidence = meta if meta.get('sources') else {'sources': [{'repo': row['repo'], 'path': row['path'], 'sha256': meta.get('_indexed_sha256', '')}]}
    return {'id': meta.get('id', row['key']), 'repo': row['repo'], 'path': row['path'],
            'line': row['line'], 'anchor': row['anchor'], 'title': row['title'],
            'kind': meta.get('kind', 'raw'), 'status': meta.get('status', 'unreviewed'),
            'review': meta.get('review', 'unreviewed'), 'assumptions': meta.get('assumptions', []),
            'sources': meta.get('sources', []), 'relations': meta.get('relations', {}),
            'freshness_issues': freshness(ws, evidence), 'body': row['body']}


def all_cards(conn):
    return [r for r in conn.execute("SELECT * FROM chunks WHERE json_extract(meta, '$.id') IS NOT NULL")]


def attach_corrections(ws, conn, hit, private, cards=None):
    related = []
    for row in (cards if cards is not None else all_cards(conn)):
        if not accessible(ws, row, private):
            continue
        meta = json.loads(row['meta'])
        targets = sum((meta.get('relations', {}).get(k, []) for k in ('corrects', 'supersedes', 'refutes')), [])
        if hit['id'] in targets:
            related.append(result(ws, row))
    hit['corrections'] = related
    return hit


def search(ws, query, campaign=None, limit=10, kinds=None, private=False):
    if not query.strip():
        raise ValueError('Search query must not be empty')
    if not 1 <= limit <= 100:
        raise ValueError('--limit must be between 1 and 100')
    profile = ws.campaign(campaign)
    alternatives = [query]
    for group in profile.get('synonyms', []):
        if any(re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', query, re.I) for term in group):
            alternatives.extend(group)
    tokens = list(dict.fromkeys(re.findall(r'[\w]+', ' '.join(alternatives))))[:40]
    if not tokens:
        raise ValueError('Search needs a word or identifier')
    expr = ' OR '.join('"' + t.replace('"', '""') + '"' for t in tokens)
    conn = ws.connect()
    # Select by scope before limiting, so restricted/global matches cannot crowd out the campaign.
    excluded = [repo for repo in ws.sources if not allowed(ws, repo, private)]
    marks = ','.join('?' for _ in excluded) or "''"
    sql = f'''SELECT chunks.*,bm25(search,0,4,1,3) AS rank FROM search
              JOIN chunks ON chunks.key=search.key WHERE search MATCH ? AND repo NOT IN ({marks})
              ORDER BY rank LIMIT 2000'''
    rows = list(conn.execute(sql, [expr, *excluded]))
    # Curated records must not be lost behind thousands of matching raw chunks.
    card_sql = sql.replace('ORDER BY rank LIMIT 2000', "AND json_extract(meta, '$.id') IS NOT NULL ORDER BY rank")
    existing = {r['key'] for r in rows}
    rows.extend(r for r in conn.execute(card_sql, [expr, *excluded]) if r['key'] not in existing)
    primary, related = set(profile.get('sources', [])), set(profile.get('related', []))
    ranked = []
    for row in rows:
        if not accessible(ws, row, private):
            continue
        meta = json.loads(row['meta'])
        if kinds and meta.get('kind', 'raw') not in kinds:
            continue
        exact = query.casefold() in [str(v).casefold() for v in [meta.get('id', ''), *meta.get('aliases', [])]]
        term_coverage = sum(t.casefold() in (row['title'] + ' ' + row['body'] + ' ' + ' '.join(meta.get('assumptions', [])) + ' ' + ' '.join(meta.get('aliases', []))).casefold() for t in tokens) / len(tokens)
        score = -row['rank'] + 4 * term_coverage + (8 if exact else 0) + (2 if meta.get('id') else 0)
        owners = {row['repo']} | {source['repo'] for source in meta.get('sources', [])}
        score += 1 if owners & primary else .5 if owners & related else 0
        ranked.append((score, row))
    groups, seen = [], {}
    for score, row in sorted(ranked, key=lambda pair: (-pair[0], pair[1]['key'])):
        meta = json.loads(row['meta'])
        group = ('card:' + meta['id'] + ':' + row['digest']) if meta.get('id') else ('raw:' + row['digest'])
        if group in seen:
            seen[group]['also_at'].append({'repo': row['repo'], 'path': row['path'], 'line': row['line']})
            continue
        entry = {'row': row, 'score': score, 'also_at': []}
        seen[group] = entry
        groups.append(entry)
    cards = all_cards(conn)
    selected = []
    for entry in groups[:limit]:
        hit = result(ws, entry['row'])
        hit['score'] = round(entry['score'], 4)
        hit['also_at'] = entry['also_at']
        selected.append(attach_corrections(ws, conn, hit, private, cards))
    state = conn.execute("SELECT value FROM state WHERE key='sync'").fetchone()
    conn.close()
    return {'query': query, 'campaign': profile.get('id'), 'hits': selected, 'matches_considered': len(rows),
            'candidate_limit_reached': len(rows) >= 2000, 'coverage': json.loads(state[0]) if state else None}


def inspect(ws, identifier, private=False):
    conn = ws.connect()
    found = list(conn.execute("SELECT * FROM chunks WHERE key=? OR json_extract(meta, '$.id')=?", (identifier, identifier)))
    found = [r for r in found if accessible(ws, r, private)]
    if not found:
        raise ValueError('No accessible indexed record: ' + identifier)
    output = [attach_corrections(ws, conn, result(ws, r), private) for r in found]
    conn.close()
    return output


def source_entry(ws, repo, path):
    p = ws.source_path({'repo': repo, 'path': path})
    try:
        rev = subprocess.check_output(['git', '-C', str(ws.sources[repo]['root']), 'rev-parse', 'HEAD'], stderr=subprocess.DEVNULL, text=True).strip()
    except subprocess.CalledProcessError:
        rev = None
    sha = digest(p.read_bytes())
    clean = False
    if rev:
        try:
            prefix = subprocess.check_output(['git', '-C', str(ws.sources[repo]['root']), 'rev-parse', '--show-prefix'], text=True).strip()
            committed = subprocess.check_output(['git', '-C', str(ws.sources[repo]['root']), 'show', rev + ':' + prefix + path], stderr=subprocess.DEVNULL)
            clean = digest(committed) == sha
        except subprocess.CalledProcessError:
            pass
    return {'repo': repo, 'path': path, 'sha256': sha, 'revision': rev, 'working_tree_differs': not clean}


def dependencies(ws, repo, entry):
    pending, seen = [entry], set()
    while pending:
        rel = pending.pop()
        if rel in seen:
            continue
        seen.add(rel)
        path = ws.source_path({'repo': repo, 'path': rel})
        content = re.sub(r'(?<!\\)%[^\n]*', '', path.read_text())
        for command, value in re.findall(r'\\(input|include|bibliography)\s*\{([^}]+)\}', content):
            for name in value.split(','):
                if '\\' in name or '#' in name:
                    raise ValueError('Dynamic TeX dependency; register it explicitly: ' + name)
                suffix = '.bib' if command == 'bibliography' else '.tex'
                name = name.strip()
                name = name if Path(name).suffix else name + suffix
                options = [path.parent / name, ws.sources[repo]['root'] / name]
                dep = next((p for p in options if p.exists()), None)
                if dep is None:
                    raise ValueError('Missing dependency: ' + name)
                canonical = dep.resolve()
                root = ws.sources[repo]['root']
                if not canonical.is_relative_to(root):
                    raise ValueError('Cross-root dependency requires an explicit source entry: ' + str(dep))
                pending.append(str(canonical.relative_to(root)))
    return sorted(seen)


def packet(ws, work, refresh=False):
    works = ws.data.get('writeups', [])
    matches = [w for w in works if w['id'] == work]
    if len(matches) != 1:
        raise ValueError('Register a unique writeup ID in the workspace registry first')
    w = matches[0]
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', work) or w['domain'] not in ('math', 'biomed', 'physics'):
        raise ValueError('Invalid work ID/domain')
    target = ws.library / w['domain'] / work
    target.mkdir(parents=True, exist_ok=True)
    with (target / '.packet.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        manifest_path = target / 'source-manifest.json'
        if manifest_path.exists() and not refresh:
            raise ValueError('Packet exists; use --refresh to update extraction candidates')
        if (target / 'metadata.json').exists():
            old = read_json(target / 'metadata.json')
            if old.get('work_id') != work or old.get('origin_kind') != 'internal':
                raise ValueError('Existing packet has a different identity')
        sources = []
        for rel in sorted(set(dependencies(ws, w['repo'], w['entry']) + w.get('extra_sources', []))):
            sources.append(source_entry(ws, w['repo'], rel))
        content = ['# Extraction candidates: ' + w['title'], '',
                   'Unreviewed source excerpts. A theorem environment is not proof verification.', '']
        for s in sources:
            text = ws.source_path(s).read_text()
            pattern = r'\\begin\{(theorem|lemma|proposition|corollary|example|definition|conjecture|remark)\}(.*?)\\end\{\1\}'
            matches = list(re.finditer(pattern, text, flags=re.S))
            if matches:
                for match in matches:
                    line = text.count('\n', 0, match.start()) + 1
                    content.extend([f"## {s['repo']}:{s['path']}:{line}", '', match.group(), ''])
            elif ws.source_path(s).suffix == '.md':
                content.extend([f"## {s['repo']}:{s['path']}", '', text, ''])
        meta = {'title': w['title'], 'work_id': work, 'origin_kind': 'internal',
                'acquisition_status': 'complete', 'extraction_status': 'unreviewed', 'updated': now()}
        if (target / 'metadata.json').exists():
            meta = {**read_json(target / 'metadata.json'), **meta}
        atomic(target / 'extraction-candidates.md', '\n'.join(content))
        json_write(target / 'metadata.json', meta)
        json_write(manifest_path, {'work_id': work, 'updated': now(), 'sources': sources})
        # Source manifest is committed last. Cards and hand-authored key-results are never overwritten.
        render_results(target)
    return {'packet': str(target), 'sources': len(sources), 'extraction_status': 'unreviewed'}



def render_results(target):
    marker = '<!-- generated by research_knowledge.py; edit results/*.md -->'
    cards = sorted((target / 'results').glob('*.md'))
    overview = target / 'key-results.md'
    if not cards or (overview.exists() and not overview.read_text().startswith(marker)):
        return
    parts = [marker, '# Extracted results', '', 'Evidence status and extraction review are separate. Consult the original sources.', '']
    for path in cards:
        meta, body = parse_card(path.read_text())
        parts.extend([f"## {meta['title']}", '', f"[{meta['id']}](results/{path.name}) — {meta['status']}; extraction: {meta.get('review', 'unreviewed')}", '', body, ''])
    atomic(overview, '\n'.join(parts))

def audit(ws):
    conn = ws.connect()
    issues, ids = [], {}
    for row in all_cards(conn):
        meta = json.loads(row['meta'])
        ids.setdefault(meta['id'], []).append(row['path'])
        for problem in freshness(ws, meta):
            issues.append({'id': meta['id'], 'issue': problem})
    for identifier, paths in ids.items():
        if len(paths) > 1:
            issues.append({'id': identifier, 'issue': 'duplicate-id', 'paths': paths})
    for row in all_cards(conn):
        meta = json.loads(row['meta'])
        for relation, targets in meta.get('relations', {}).items():
            for target in targets:
                if target not in ids:
                    issues.append({'id': meta['id'], 'issue': 'unresolved-relation', 'relation': relation, 'target': target})
    registered = {(w['repo'], w['entry']) for w in ws.data.get('writeups', [])}
    for row in conn.execute('SELECT * FROM files'):
        try:
            stat = ws.source_path(row).stat()
            if stat.st_mtime_ns != row['mtime'] or stat.st_size != row['size']:
                issues.append({'repo': row['repo'], 'path': row['path'], 'issue': 'source-changed-since-sync'})
        except (OSError, ValueError):
            issues.append({'repo': row['repo'], 'path': row['path'], 'issue': 'source-missing-since-sync'})
    candidates = []
    for row in conn.execute("SELECT DISTINCT repo,path FROM chunks WHERE path LIKE '%.tex' AND instr(body, ?) > 0", ('\\documentclass',)):
        if (row['repo'], row['path']) not in registered:
            candidates.append(dict(row))
    for w in ws.data.get('writeups', []):
        p = ws.library / w['domain'] / w['id'] / 'source-manifest.json'
        if not p.exists():
            issues.append({'work': w['id'], 'issue': 'missing-packet'})
        else:
            for problem in freshness(ws, read_json(p)):
                issues.append({'work': w['id'], 'issue': problem})
    state = conn.execute("SELECT value FROM state WHERE key='sync'").fetchone()
    conn.close()
    coverage = json.loads(state[0]) if state else {}
    if coverage.get('registry_sha256') != digest(ws.path.read_bytes()):
        issues.append({'issue': 'registry-changed-since-sync'})
    return {'checked': now(), 'cards': len(ids), 'issues': issues, 'unregistered_writeup_candidates': candidates, 'coverage': coverage}


def units(text):
    # UTF-8 bytes are a conservative upper bound for common byte-tokenized model encodings.
    return len(text.encode('utf-8'))


def context(ws, task, campaign, budget=6000, role=None, private=False):
    profile = ws.campaign(campaign)
    if budget < 500:
        raise ValueError('Context budget must be at least 500 conservative token units')
    heading = f"# Research context: {profile.get('id', 'workspace')}\n\nTask: {task}\n"
    heading += '\nSources remain authoritative. Raw excerpts and unreviewed extractions are not proved inputs.\n'
    if role:
        instructions = {
            'historian': 'Find earlier results, aliases, failed mechanisms and corrections; do not develop another proof.',
            'literature': 'Locate extracted external results and state precise applicability and remaining source checks.',
            'transfer': 'Compare assumptions, quantifiers and notation; identify the exact missing transfer implication.'}
        heading += f'\nSpecialist role: {role}. {instructions[role]} Return source IDs, applicability, and search limitations.\n'
    summary = profile.get('summary', '')
    heading += '\nCampaign profile:\n' + summary + '\n'
    if units(heading) > budget - 300:
        raise ValueError('Task/profile exceeds budget; shorten it or increase --budget')
    sections, omitted, used = [heading], [], units(heading)
    candidates = []
    for pin in profile.get('pins', []):
        if isinstance(pin, str):
            candidates.extend(inspect(ws, pin, private))
        else:
            if not allowed(ws, pin['repo'], private):
                continue
            p = ws.source_path(pin)
            candidates.append({'id': pin['repo'] + ':' + pin['path'], 'title': pin.get('title', p.stem),
                               'body': p.read_text(), 'kind': 'raw', 'status': 'unreviewed',
                               'repo': pin['repo'], 'path': pin['path'], 'line': 1, 'corrections': [], 'freshness_issues': []})
    response = search(ws, task, campaign, limit=30, private=private)
    candidates.extend(response['hits'])
    seen = set()
    for hit in candidates:
        if hit['id'] in seen:
            continue
        seen.add(hit['id'])
        block = f"\n## {hit['title']} [{hit['id']}]\n{hit['repo']}:{hit['path']}:{hit['line']} | {hit['kind']} | {hit['status']}\n"
        block += 'Freshness: ' + ('; '.join(hit['freshness_issues']) or 'no recorded source drift') + '\n'
        if hit.get('assumptions'):
            block += 'Assumptions: ' + '; '.join(hit['assumptions']) + '\n'
        body = hit['body']
        if hit['kind'] == 'raw' and units(body) > 1400:
            body = body[:500] + '\n[Partial raw excerpt; inspect the source for the complete statement and context.]'
        block += body + '\n'
        for correction in hit.get('corrections', []):
            block += f"\nCORRECTION/RELATED STATUS [{correction['id']}]: {correction['body']}\nSource: {correction['repo']}:{correction['path']}\n"
        if used + units(block) > budget - 300:
            omitted.append(hit['id'])
            continue
        sections.append(block)
        used += units(block)
    footer = f'\nIndex updated: {(response.get("coverage") or {}).get("updated", "unknown")}. '
    footer += f'{len(omitted)} records omitted for budget; use search/inspect for full coverage. '
    footer += 'Budget uses conservative UTF-8 byte units, not an exact model tokenizer.\n'
    text = ''.join(sections) + footer
    assert units(text) <= budget
    return {'text': text, 'budget_units': units(text), 'omitted': omitted, 'index_coverage': response['coverage']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config')
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('sync'); p.add_argument('--full', action='store_true')
    p = sub.add_parser('search'); p.add_argument('query'); p.add_argument('--campaign'); p.add_argument('--limit', type=int, default=10); p.add_argument('--kind', action='append'); p.add_argument('--include-private', action='store_true')
    p = sub.add_parser('inspect'); p.add_argument('id'); p.add_argument('--include-private', action='store_true')
    p = sub.add_parser('context'); p.add_argument('--task', required=True); p.add_argument('--campaign', required=True); p.add_argument('--budget', type=int, default=6000); p.add_argument('--role', choices=['historian', 'literature', 'transfer']); p.add_argument('--include-private', action='store_true'); p.add_argument('--json', action='store_true')
    p = sub.add_parser('packet'); p.add_argument('work'); p.add_argument('--refresh', action='store_true')
    sub.add_parser('audit')
    args = parser.parse_args(argv)
    try:
        ws = Workspace(config_path(args.config))
        if args.command == 'sync': output = sync(ws, args.full)
        elif args.command == 'search': output = search(ws, args.query, args.campaign, args.limit, args.kind, args.include_private)
        elif args.command == 'inspect': output = inspect(ws, args.id, args.include_private)
        elif args.command == 'packet': output = packet(ws, args.work, args.refresh)
        elif args.command == 'audit': output = audit(ws)
        else:
            output = context(ws, args.task, args.campaign, args.budget, args.role, args.include_private)
            if not args.json:
                print(output['text']); return 0
        print(json.dumps(output, indent=2, ensure_ascii=False)); return 0
    except (ValueError, OSError, KeyError, sqlite3.Error) as exc:
        print('Error: ' + str(exc), file=sys.stderr); return 2

if __name__ == '__main__':
    raise SystemExit(main())
