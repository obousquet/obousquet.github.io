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
import stat as statmod
import subprocess
import sys
import time
from collections import OrderedDict
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = 1
INDEX_VERSION = 4
QUERY_SCHEMA = 1
LOCK_TIMEOUT = 300
KINDS = {'theorem', 'lemma', 'example', 'counterexample', 'conjecture', 'idea', 'failed-approach', 'correction', 'definition'}
STATUSES = {'proved', 'established', 'conditional', 'computational', 'conjectural', 'refuted', 'withdrawn', 'open', 'unreviewed'}
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
        raw = self.path.read_bytes()
        self.registry_sha = digest(raw)
        self.data = json.loads(raw)
        self.lock_timeout = LOCK_TIMEOUT
        if self.data.get('version') != SCHEMA:
            raise ValueError('Unsupported registry version')
        self.base = self.path.parent
        self.sources = {}
        for row in self.data['sources']:
            if row['id'] in self.sources:
                raise ValueError('Duplicate source id: ' + row['id'])
            if row.get('type', 'text') not in ('text', 'json-records'):
                raise ValueError('Unsupported source type: ' + row['id'])
            collections = row.get('collections', [])
            if row.get('type') == 'json-records' and (not collections or
                    len({c['id'] for c in collections}) != len(collections)):
                raise ValueError('Structured sources need uniquely named collections: ' + row['id'])
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
        # Large FTS sorts may spill to disk. Use the cache filesystem rather than a
        # small RAM-backed /tmp; preserve an explicit SQLite temporary-directory override.
        os.environ.setdefault('SQLITE_TMPDIR', str(self.dbpath.parent))
        if write:
            self.dbpath.parent.mkdir(parents=True, exist_ok=True)
            conn = sqlite3.connect(self.dbpath, timeout=self.lock_timeout)
            conn.execute('PRAGMA journal_mode=WAL')
            conn.executescript('''
            CREATE TABLE IF NOT EXISTS files (key TEXT PRIMARY KEY, repo TEXT, path TEXT, sha TEXT, mtime INTEGER, size INTEGER);
            CREATE TABLE IF NOT EXISTS chunks (key TEXT PRIMARY KEY, filekey TEXT, repo TEXT, path TEXT,
                anchor TEXT, line INTEGER, title TEXT, body TEXT, meta TEXT, digest TEXT);
            CREATE INDEX IF NOT EXISTS chunks_filekey ON chunks(filekey);
            CREATE VIRTUAL TABLE IF NOT EXISTS search USING fts5(key UNINDEXED, title, body, aliases);
            CREATE TABLE IF NOT EXISTS state (key TEXT PRIMARY KEY, value TEXT);
            ''')
            query_schema(conn)
        else:
            if not self.dbpath.exists():
                raise ValueError('Index missing; run sync first')
            conn = sqlite3.connect(self.dbpath.as_uri() + '?mode=ro', uri=True, timeout=self.lock_timeout)
            # Hits, corrections and coverage must come from one committed generation.
            conn.execute('BEGIN')
        conn.row_factory = sqlite3.Row
        return conn


def query_schema(conn):
    """Install derived indexes transactionally; triggers also support older writers."""
    version = conn.execute("SELECT value FROM state WHERE key='query_schema'").fetchone()
    if version and int(version[0]) == QUERY_SCHEMA:
        return
    # Keep the smaller curated index separate so raw matches cannot crowd out cards.
    # SQL triggers maintain it even when an older distributed indexer writes chunks.
    conn.executescript('''
    BEGIN IMMEDIATE;
    CREATE INDEX IF NOT EXISTS chunks_result_id ON chunks(json_extract(meta, '$.id'));
    CREATE INDEX IF NOT EXISTS chunks_cards ON chunks(key)
        WHERE json_extract(meta, '$.id') IS NOT NULL;
    CREATE VIRTUAL TABLE IF NOT EXISTS card_search USING fts5(key UNINDEXED, title, body, aliases);
    CREATE TABLE IF NOT EXISTS correction_links (
        target TEXT, chunkkey TEXT, PRIMARY KEY(target, chunkkey));
    CREATE INDEX IF NOT EXISTS correction_chunk ON correction_links(chunkkey);
    CREATE TRIGGER IF NOT EXISTS chunks_query_delete AFTER DELETE ON chunks
    WHEN json_extract(old.meta, '$.id') IS NOT NULL BEGIN
        DELETE FROM card_search WHERE rowid=old.rowid;
        DELETE FROM correction_links WHERE chunkkey=old.key;
    END;
    ''')
    insert = '''
        INSERT INTO card_search(rowid,key,title,body,aliases)
        SELECT new.rowid,new.key,new.title,new.body,
            coalesce(json_extract(new.meta,'$.id'),'') || ' ' || new.anchor || ' ' ||
            coalesce((SELECT group_concat(value,' ') FROM json_each(new.meta,'$.aliases')),'') || ' ' ||
            coalesce((SELECT group_concat(value,' ') FROM json_each(new.meta,'$.assumptions')),'')
        WHERE json_extract(new.meta,'$.id') IS NOT NULL;
        INSERT OR IGNORE INTO correction_links(target,chunkkey)
        SELECT value,new.key FROM json_each(new.meta,'$.relations.corrects')
        UNION SELECT value,new.key FROM json_each(new.meta,'$.relations.refutes')
        UNION SELECT value,new.key FROM json_each(new.meta,'$.relations.supersedes');
    '''
    # execute (not executescript) keeps the migration in the transaction above.
    conn.execute('CREATE TRIGGER IF NOT EXISTS chunks_query_insert AFTER INSERT ON chunks BEGIN ' + insert + ' END')
    conn.execute('''CREATE TRIGGER IF NOT EXISTS chunks_query_update AFTER UPDATE ON chunks BEGIN
        DELETE FROM card_search WHERE rowid=old.rowid;
        DELETE FROM correction_links WHERE chunkkey=old.key;
    ''' + insert + ' END')
    conn.execute('DELETE FROM card_search')
    conn.execute('''INSERT INTO card_search(rowid,key,title,body,aliases)
        SELECT search.rowid,search.key,search.title,search.body,search.aliases FROM search
        JOIN chunks ON chunks.rowid=search.rowid WHERE json_extract(chunks.meta,'$.id') IS NOT NULL''')
    conn.execute('DELETE FROM correction_links')
    for relation in ('corrects', 'refutes', 'supersedes'):
        conn.execute('''INSERT OR IGNORE INTO correction_links(target,chunkkey)
            SELECT link.value,chunks.key FROM chunks,json_each(chunks.meta,?) AS link
            WHERE json_extract(chunks.meta,'$.id') IS NOT NULL''', ('$.relations.' + relation,))
    conn.execute('INSERT OR REPLACE INTO state VALUES (?,?)', ('query_schema', str(QUERY_SCHEMA)))
    conn.commit()


@contextmanager
def writer_lock(ws, progress=None):
    """Bound lock waits and leave the existing lock inode intact for other processes."""
    ws.dbpath.parent.mkdir(parents=True, exist_ok=True)
    started = last_notice = time.monotonic()
    with ws.dbpath.with_suffix('.lock').open('a+') as lock:
        while True:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                elapsed = time.monotonic() - started
                if elapsed >= ws.lock_timeout:
                    raise ValueError(f'Index writer busy after {elapsed:.1f}s; increase --lock-timeout or wait for the running sync')
                if progress and time.monotonic() - last_notice >= 15:
                    progress(f'Waiting for index writer ({elapsed:.0f}s)')
                    last_notice = time.monotonic()
                time.sleep(min(.1, max(0, ws.lock_timeout - elapsed)))
        try:
            yield time.monotonic() - started
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


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
            # os.walk(followlinks=False) already avoids directory symlinks. Filter
            # names before filesystem calls; canonical roots and unlinked parents
            # also make repeated realpath() calls unnecessary.
            dirs[:] = sorted(d for d in dirs if d not in SKIP
                             and not any((Path(parent) / d).relative_to(root).match(p) for p in source.get('exclude', [])))
            for name in sorted(names):
                p = Path(parent) / name
                rel = p.relative_to(root)
                selected = p.suffix in SUFFIXES or (p.suffix == '.json' and ('dashboard' in name or name in {'metadata.json', 'library-record.json'}))
                if source.get('include'):
                    selected = any(rel.match(pattern) for pattern in source['include'])
                if source.get('type') == 'json-records':
                    selected = any(rel.match(c['glob']) for c in source['collections'])
                    if str(rel) in {c.get('schema') for c in source['collections']}:
                        selected = False
                if not selected or any(rel.match(pattern) for pattern in source.get('exclude', [])):
                    continue
                try:
                    stat = p.lstat()
                    if statmod.S_ISLNK(stat.st_mode) or p in seen:
                        continue
                    if stat.st_size > source.get('max_bytes', 8_000_000):
                        issues.append({'repo': repo, 'path': str(rel), 'issue': 'oversized'})
                        continue
                except OSError as exc:
                    issues.append({'repo': repo, 'path': str(rel), 'issue': str(exc)})
                    continue
                seen.add(p)
                found.append((repo, str(rel), p, stat))
    return found, issues


def structured_records(ws, repo, found):
    """Read configured object-per-file collections without changing their authority or status."""
    source = ws.sources[repo]
    collections = {c['id']: c for c in source['collections']}
    records, lookup, schemas, issues, signature = {}, {}, {}, [], []
    for cid, spec in collections.items():
        if not spec.get('schema'):
            continue
        p = ws.source_path({'repo': repo, 'path': spec['schema']})
        if p.is_symlink():
            raise ValueError('Schema must not be a symlink: ' + spec['schema'])
        data = p.read_bytes()
        schemas[cid] = (json.loads(data), {'repo': repo, 'path': spec['schema'], 'sha256': digest(data)})
        signature.append((spec['schema'], digest(data)))
    for _, rel, path, _ in found:
        matches = [c for c in collections.values() if Path(rel).match(c['glob'])]
        if len(matches) != 1:
            raise ValueError('Record must match exactly one collection: ' + rel)
        spec = matches[0]
        try:
            data = path.read_bytes()
            signature.append((rel, digest(data)))
            record = json.loads(data)
            if not isinstance(record, dict):
                raise ValueError('Expected one JSON object per file')
            identifier = record.get(spec.get('id_field', 'id'))
            if isinstance(identifier, bool) or not isinstance(identifier, (str, int)) or str(identifier) == '':
                raise ValueError('Missing or invalid stable record ID')
            rid = f'{repo}:{spec["id"]}:{identifier}'
            if rid in records:
                raise ValueError('Duplicate record ID: ' + rid)
            records[rid] = (record, spec, rel, digest(data))
        except (ValueError, OSError) as exc:
            # Duplicate identities make the whole source ambiguous; do not pick one silently.
            if str(exc).startswith('Duplicate record ID:'):
                raise
            issues.append({'repo': repo, 'path': rel, 'issue': str(exc)})
    for cid, spec in collections.items():
        if not any(s['id'] == cid for _, s, _, _ in records.values()):
            issues.append({'repo': repo, 'collection': cid, 'issue': 'empty-collection'})
    # Build exactly the lookup keys requested by the consuming registry.
    for spec in collections.values():
        for ref in spec.get('references', {}).values():
            cid, field = ref['collection'], ref.get('key', 'id')
            if cid not in collections:
                raise ValueError('Unknown reference collection: ' + cid)
            if (cid, field) in lookup:
                continue
            table = lookup[cid, field] = {}
            for rid, (record, target, rel, sha) in records.items():
                if target['id'] != cid or field not in record:
                    continue
                key = str(record[field])
                if key in table:
                    raise ValueError('Ambiguous reference key: ' + cid + ':' + key)
                table[key] = (rid, record, rel, sha)
    output = {}
    for rid, (record, spec, rel, sha) in records.items():
        cid = spec['id']
        sources = [{'repo': repo, 'path': rel, 'sha256': sha}]
        aliases = []
        for field in spec.get('alias_fields', []):
            value = record.get(field, [])
            aliases.extend(str(x) for x in (value if isinstance(value, list) else [value]))
        title = str(record.get(spec.get('title_field', 'name')) or rid)
        status = record.get(spec.get('status_field', 'status')) or 'unreviewed'
        body = ['Structured source record; source status is not an independent proof review.',
                'Omitted fields remain unspecified; false, zero and missing are distinct.',
                '\nComplete record:\n' + json.dumps(record, ensure_ascii=False, indent=2)]
        schema, schema_source = schemas.get(cid, ({}, None))
        if schema_source:
            sources.append(schema_source)
        for column in schema.get('columns', []):
            field = column['name']
            if field not in record:
                continue
            meaning = column.get('description', '')
            enum = next((e.get('display_name', '') for e in column.get('enum', [])
                         if e['value'] == record[field]), '')
            if meaning or enum:
                body.append(f'Field {field}: {meaning}' + (f' Meaning of this value: {enum}' if enum else ''))
        links = []
        for field, ref in spec.get('references', {}).items():
            if field not in record or record[field] in (None, ''):
                continue
            value, prefix = str(record[field]), ref.get('prefix', '')
            key = value[len(prefix):] if value.startswith(prefix) else value
            target = lookup[ref['collection'], ref.get('key', 'id')].get(key)
            if not target:
                issue = {'repo': repo, 'path': rel, 'issue': 'unresolved-reference', 'field': field, 'target': value}
                issues.append(issue)
                body.append(f'UNRESOLVED REFERENCE {field}: {value}; inspect the owning database.')
                continue
            target_id, linked, linked_rel, linked_sha = target
            links.append(target_id)
            sources.append({'repo': repo, 'path': linked_rel, 'sha256': linked_sha})
            selected = {f: linked[f] for f in ref.get('fields', ['name']) if f in linked}
            body.append(f'Reference {field}: [{target_id}] ({repo}:{linked_rel})\n' +
                        json.dumps(selected, ensure_ascii=False, indent=2))
        meta = {'id': rid, 'title': title, 'kind': spec.get('kind', 'record'),
                'status': str(status), 'review': 'structured import; not independently verified',
                'aliases': aliases, 'sources': sources, 'relations': {'references': links},
                'origin_kind': 'structured', 'collection': cid}
        output[rel] = [(rid, 1, title, '\n\n'.join(body), meta)]
    return output, issues, digest(json.dumps(sorted(signature)))



def read_index_text(path, policy=None):
    """Read a pinned legacy source without guessing or rewriting its bytes.

    Exclusion is an explicit coverage disposition, not a successful parse.
    The reason is provenance evidence supplied by the registry owner.
    """
    if policy is None:
        return path.read_text(encoding='utf-8'), None
    if not isinstance(policy, dict) or not policy.get('reason'):
        raise ValueError('Text policy requires an explicit provenance reason')
    raw = path.read_bytes()
    sha = digest(raw)
    if not re.fullmatch(r'[0-9a-f]{64}', str(policy.get('sha256', ''))) or sha != policy['sha256']:
        raise ValueError('Text policy raw SHA256 mismatch; review source before refreshing')
    action = policy.get('action')
    evidence = {'action': action, 'raw_sha256': sha, 'reason': policy['reason']}
    if action == 'exclude':
        return None, evidence
    encodings = {'cp1252', 'cp1251', 'iso8859-2', 'iso8859-15'}
    encoding = policy.get('encoding')
    if action != 'decode' or encoding not in encodings:
        raise ValueError('Unsupported explicit text decoding policy')
    text = raw.decode(encoding, errors='strict')
    if text.encode(encoding, errors='strict') != raw:
        raise ValueError('Text decoding is not byte-reversible')
    evidence['encoding'] = encoding
    return text, evidence


def sync(ws, full=False, progress=None):
    started = time.monotonic()
    with writer_lock(ws, progress) as waited:
        # A queued writer must use the registry as it exists after acquiring the lock.
        if digest(ws.path.read_bytes()) != ws.registry_sha:
            timeout = ws.lock_timeout
            ws = Workspace(ws.path)
            ws.lock_timeout = timeout
        if progress:
            progress('Preparing query indexes and discovering sources')
        conn = ws.connect(True)
        changed = removed = 0
        found, issues = discover(ws)
        text_dispositions = []
        policy_seen = set()
        previous = {r['key']: r for r in conn.execute('SELECT * FROM files')}
        version = conn.execute("SELECT value FROM state WHERE key='indexer_version'").fetchone()
        force_reindex = not version or int(version[0]) != INDEX_VERSION
        full = full or force_reindex
        prior_state = conn.execute("SELECT value FROM state WHERE key='sync'").fetchone()
        prior_state = json.loads(prior_state[0]) if prior_state else {}
        # Profiles, pins, writeup registration and budgets do not alter indexed content.
        # Reparse only sources whose indexing configuration changed.
        source_signatures = {repo: digest(json.dumps({k: str(v) if k == 'root' else v
                            for k, v in source.items()}, sort_keys=True))
                             for repo, source in ws.sources.items()}
        prior_signatures = prior_state.get('source_signatures')
        if prior_signatures is None and prior_state.get('registry_sha256') == ws.registry_sha:
            prior_signatures = source_signatures
        reindex = {repo for repo, sig in source_signatures.items()
                   if sig != (prior_signatures or {}).get(repo)}
        structured, signatures, dirty = {}, {}, set()
        for repo, source in ws.sources.items():
            if source.get('type') != 'json-records':
                continue
            try:
                structured[repo], problems, signatures[repo] = structured_records(ws, repo, [f for f in found if f[0] == repo])
                issues.extend(problems)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                structured[repo] = {}
                issues.append({'repo': repo, 'issue': 'structured-import-failed: ' + str(exc)})
            if signatures.get(repo) != prior_state.get('structured_signatures', {}).get(repo):
                dirty.add(repo)
        seen = set()
        last_notice = time.monotonic()
        with conn:
            for scanned, (repo, rel, path, stat) in enumerate(found, 1):
                if progress and time.monotonic() - last_notice >= 15:
                    progress(f'Checked {scanned}/{len(found)} files; updated {changed}')
                    last_notice = time.monotonic()
                key = repo + ':' + rel
                if repo in structured and rel not in structured[repo]:
                    continue
                seen.add(key)
                old = previous.get(key)
                policy = ws.sources[repo].get('text_policies', {}).get(rel)
                if policy is not None:
                    policy_seen.add((repo, rel))
                if policy is None and not full and repo not in dirty and repo not in reindex and old and old['mtime'] == stat.st_mtime_ns and old['size'] == stat.st_size:
                    continue
                try:
                    content, disposition = read_index_text(path, policy)
                    if disposition is not None:
                        text_dispositions.append({'repo': repo, 'path': rel, **disposition})
                    if content is None:
                        seen.discard(key)
                        continue
                    parts = structured[repo][rel] if repo in structured else chunks(content, rel)
                except (OSError, ValueError) as exc:
                    issues.append({'repo': repo, 'path': rel, 'issue': str(exc)})
                    seen.discard(key)  # remove an older successful parse; never serve it as current
                    continue
                sha = disposition['raw_sha256'] if disposition else digest(content)
                if not force_reindex and repo not in dirty and repo not in reindex and old and old['sha'] == sha:
                    conn.execute('UPDATE files SET mtime=?,size=? WHERE key=?', (stat.st_mtime_ns, stat.st_size, key))
                    continue
                if old:
                    conn.execute('DELETE FROM search WHERE rowid IN (SELECT rowid FROM chunks WHERE filekey=?)', (key,))
                    conn.execute('DELETE FROM chunks WHERE filekey=?', (key,))
                conn.execute('INSERT OR REPLACE INTO files VALUES (?,?,?,?,?,?)', (key, repo, rel, sha, stat.st_mtime_ns, stat.st_size))
                for n, (anchor, line, title, body, meta) in enumerate(parts):
                    ck = digest(key + ':' + str(n))[:24]
                    conn.execute('INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?,?,?)',
                                 (ck, key, repo, rel, anchor, line, title, body, json.dumps({**meta, '_indexed_sha256': sha, **({'_text_decoding': disposition} if disposition else {})}), digest(body)))
                    aliases = ' '.join([meta.get('id', ''), *meta.get('aliases', []), *meta.get('assumptions', []), anchor])
                    rowid = conn.execute('SELECT rowid FROM chunks WHERE key=?', (ck,)).fetchone()[0]
                    conn.execute('INSERT INTO search(rowid,key,title,body,aliases) VALUES (?,?,?,?,?)', (rowid, ck, title, body, aliases))
                changed += 1
            for key in set(previous) - seen:
                conn.execute('DELETE FROM search WHERE rowid IN (SELECT rowid FROM chunks WHERE filekey=?)', (key,))
                conn.execute('DELETE FROM chunks WHERE filekey=?', (key,))
                conn.execute('DELETE FROM files WHERE key=?', (key,))
                removed += 1
            for repo, source in ws.sources.items():
                for rel in source.get('text_policies', {}):
                    if (repo, rel) not in policy_seen:
                        issues.append({'repo': repo, 'path': rel, 'issue': 'text-policy-target-not-discovered'})
            report = {'updated': now(), 'files': len(seen), 'changed': changed, 'removed': removed,
                      'chunks': conn.execute('SELECT count(*) FROM chunks').fetchone()[0], 'issues': issues,
                      'text_dispositions': text_dispositions,
                      'registry_sha256': ws.registry_sha,
                      'source_signatures': source_signatures,
                      'scan_seconds': round(time.monotonic() - started, 3),
                      'lock_wait_seconds': round(waited, 3),
                      'structured_signatures': signatures,
                      'sources': {r: sum(1 for key in seen if key.startswith(r + ':')) for r in ws.sources}}
            conn.execute('INSERT OR REPLACE INTO state VALUES (?,?)', ('sync', json.dumps(report)))
            conn.execute('INSERT OR REPLACE INTO state VALUES (?,?)', ('indexer_version', str(INDEX_VERSION)))
            if progress:
                progress(f'Source scan complete: {changed} updated; committing index and checkpointing')
        conn.close()
        report['duration_seconds'] = round(time.monotonic() - started, 3)
        if progress:
            progress(f"Index ready: {report['files']} files, {changed} updated, {removed} removed, {len(issues)} coverage issues ({report['duration_seconds']}s)")
        return report


def freshness(ws, meta):
    problems = []
    if not hasattr(ws, '_fingerprints'):
        ws._fingerprints, ws._source_text, ws._source_text_bytes = {}, OrderedDict(), 0
    for source in meta.get('sources', []):
        try:
            p = ws.source_path(source)
            stat = p.stat()
            stamp = (stat.st_mtime_ns, stat.st_size)
            cached = ws._fingerprints.get(str(p))
            text_entry = ws._source_text.get((str(p), stamp))
            text = text_entry[0] if text_entry else None
            if cached is None or cached[:2] != stamp or (source.get('anchor') and text is None):
                raw = p.read_bytes()
                cached = (*stamp, digest(raw))
                ws._fingerprints[str(p)] = cached
                text = raw.decode('utf-8', errors='replace')
                # Bound retained source text; large shared proofs often have many anchor checks.
                if len(raw) <= 16_000_000:
                    prior = ws._source_text.pop((str(p), stamp), None)
                    ws._source_text_bytes -= prior[1] if prior else 0
                    ws._source_text[(str(p), stamp)] = (text, len(raw))
                    ws._source_text_bytes += len(raw)
                    ws._source_text.move_to_end((str(p), stamp))
                    while ws._source_text_bytes > 16_000_000:
                        ws._source_text_bytes -= ws._source_text.popitem(last=False)[1][1]
            if cached[2] != source['sha256']:
                problems.append('changed: ' + source['repo'] + ':' + source['path'])
            if source.get('anchor') and source['anchor'] not in text:
                problems.append('missing anchor: ' + source['anchor'])
        except (OSError, ValueError, KeyError) as exc:
            problems.append('unavailable source: ' + str(exc))
    return problems


def allowed(ws, repo, private):
    return repo in ws.sources and (private or ws.sources[repo].get('visibility') != 'private')


def accessible(ws, row, private):
    return allowed(ws, row['repo'], private) and all(allowed(ws, s['repo'], private) for s in json.loads(row['meta']).get('sources', []))


def result(ws, row):
    meta = json.loads(row['meta'])
    evidence = {'sources': [*meta.get('sources', []),
                {'repo': row['repo'], 'path': row['path'], 'sha256': meta.get('_indexed_sha256', '')}]}
    return {'id': meta.get('id', row['key']), 'repo': row['repo'], 'path': row['path'],
            'line': row['line'], 'anchor': row['anchor'], 'title': row['title'],
            'kind': meta.get('kind', 'raw'), 'status': meta.get('status', 'unreviewed'),
            'origin_kind': meta.get('origin_kind', 'card' if meta.get('id') else 'raw'),
            'collection': meta.get('collection'),
            'authority': ws.sources.get(row['repo'], {}).get('authority', ''),
            'review': meta.get('review', 'unreviewed'), 'assumptions': meta.get('assumptions', []),
            'sources': meta.get('sources', []), 'relations': meta.get('relations', {}),
            'freshness_issues': freshness(ws, evidence), 'body': row['body']}


def all_cards(conn):
    return [r for r in conn.execute("SELECT * FROM chunks WHERE json_extract(meta, '$.id') IS NOT NULL")]


def attach_corrections(ws, conn, hit, private):
    related = []
    for row in conn.execute('''SELECT chunks.* FROM correction_links
            JOIN chunks ON chunks.key=correction_links.chunkkey WHERE target=? ORDER BY chunks.key''', (hit['id'],)):
        if not accessible(ws, row, private):
            continue
        related.append(result(ws, row))
    hit['corrections'] = related
    return hit


def index_health(ws, conn, coverage=None):
    states = dict(conn.execute('SELECT key,value FROM state'))
    coverage = coverage if coverage is not None else json.loads(states.get('sync', '{}'))
    updated = coverage.get('updated')
    age = (datetime.now(timezone.utc) - datetime.fromisoformat(updated)).total_seconds() if updated else None
    syncing = False
    lockpath = ws.dbpath.with_suffix('.lock')
    if lockpath.exists():
        with lockpath.open() as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_SH | fcntl.LOCK_NB)
            except BlockingIOError:
                syncing = True
    return {'updated': updated, 'age_seconds': round(age, 3) if age is not None else None,
            'registry_current': coverage.get('registry_sha256') == ws.registry_sha,
            'indexer_current': states.get('indexer_version') == str(INDEX_VERSION),
            'query_schema_current': states.get('query_schema') == str(QUERY_SCHEMA),
            'sync_in_progress': syncing, 'coverage_issues': len(coverage.get('issues', [])),
            'files': coverage.get('files', 0), 'chunks': coverage.get('chunks', 0)}


def status(ws):
    if not ws.dbpath.exists():
        return {'exists': False, 'action': 'Run sync to build the index'}
    conn = ws.connect()
    try:
        return {'exists': True, 'journal_mode': conn.execute('PRAGMA journal_mode').fetchone()[0],
                **index_health(ws, conn)}
    finally:
        conn.close()


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
    sql = f'''SELECT chunks.*,search.rank AS rank FROM search
              JOIN chunks ON chunks.rowid=search.rowid WHERE search MATCH ?
              AND search.rank MATCH 'bm25(0,4,1,3)' AND repo NOT IN ({marks})
              ORDER BY search.rank LIMIT 2000'''
    rows = list(conn.execute(sql, [expr, *excluded]))
    candidate_limit_reached = len(rows) == 2000
    # Curated records must not be lost behind thousands of matching raw chunks.
    card_sql = sql.replace('search', 'card_search').replace(' LIMIT 2000', '')
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
    selected = []
    for entry in groups[:limit]:
        hit = result(ws, entry['row'])
        hit['score'] = round(entry['score'], 4)
        hit['also_at'] = entry['also_at']
        selected.append(attach_corrections(ws, conn, hit, private))
    state = conn.execute("SELECT value FROM state WHERE key='sync'").fetchone()
    coverage = json.loads(state[0]) if state else None
    health = index_health(ws, conn, coverage)
    conn.close()
    return {'query': query, 'campaign': profile.get('id'), 'hits': selected, 'matches_considered': len(rows),
            'candidate_limit_reached': candidate_limit_reached, 'coverage': coverage, 'index': health}


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
    entry_dir = ws.source_path({'repo': repo, 'path': entry}).parent
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
                # Nested TeX inputs can be relative to the compilation entry,
                # even when they occur in a file in a subdirectory.
                options = [path.parent / name, entry_dir / name, ws.sources[repo]['root'] / name]
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


def source_registry(ws, private=False):
    return {'registry': str(ws.path), 'sources': [
        {**{k: v for k, v in source.items() if k != 'root'},
         'resolved_path': str(source['root']), 'type': source.get('type', 'text'),
         'available': source['root'].is_dir()}
        for repo, source in ws.sources.items() if allowed(ws, repo, private)]}


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
    profile_omitted = units(summary) > min(3000, budget // 3)
    if profile_omitted:
        heading += f"\nCampaign profile omitted ({units(summary)} bytes) to reserve retrieval space. Read it with profile --campaign {profile['id']}.\n"
    else:
        heading += '\nCampaign profile:\n' + summary + '\n'
    if units(heading) > budget - 300:
        raise ValueError('Task exceeds context budget; shorten it or increase --budget')
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
    def footer(count):
        health = response['index']
        text = f"\nIndex updated: {health['updated'] or 'unknown'}. Coverage issues: {health['coverage_issues']}. "
        if not health['registry_current']:
            text += 'Registry changed since sync. '
        if response['candidate_limit_reached']:
            text += 'Raw candidate limit reached. '
        text += f'{count} records omitted for budget; use search/inspect for full coverage. '
        return text + 'Budget uses conservative UTF-8 byte units.\n'
    reserve = units(footer(len(candidates)))
    seen = set()
    for hit in candidates:
        if hit['id'] in seen:
            continue
        seen.add(hit['id'])
        block = f"\n## {hit['title']} [{hit['id']}]\n{hit['repo']}:{hit['path']}:{hit['line']} | {hit['kind']} | {hit['status']}\n"
        block += 'Review: ' + hit.get('review', 'unreviewed') + '\n'
        if hit.get('authority'):
            block += 'Source ownership: ' + hit['authority'] + '\n'
        block += 'Freshness: ' + ('; '.join(hit['freshness_issues']) or 'no recorded source drift') + '\n'
        if hit.get('assumptions'):
            block += 'Assumptions: ' + '; '.join(hit['assumptions']) + '\n'
        body = hit['body']
        if hit['kind'] == 'raw' and units(body) > 1400:
            body = body[:500] + '\n[Partial raw excerpt; inspect the source for the complete statement and context.]'
        block += body + '\n'
        for correction in hit.get('corrections', []):
            block += f"\nCORRECTION/RELATED STATUS [{correction['id']}]: {correction['body']}\nSource: {correction['repo']}:{correction['path']}\n"
        if used + units(block) > budget - reserve:
            omitted.append(hit['id'])
            continue
        sections.append(block)
        used += units(block)
    text = ''.join(sections) + footer(len(omitted))
    assert units(text) <= budget
    return {'text': text, 'budget_units': units(text), 'omitted': omitted,
            'profile_omitted': profile_omitted, 'index': response['index'],
            'index_coverage': response['coverage']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config')
    parser.add_argument('--lock-timeout', type=float, default=LOCK_TIMEOUT,
                        help='Seconds to wait for a writer/SQLite lock (default: 300)')
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('sync'); p.add_argument('--full', action='store_true')
    p = sub.add_parser('search'); p.add_argument('query'); p.add_argument('--campaign'); p.add_argument('--limit', type=int, default=10); p.add_argument('--kind', action='append'); p.add_argument('--include-private', action='store_true')
    p = sub.add_parser('inspect'); p.add_argument('id'); p.add_argument('--include-private', action='store_true')
    p = sub.add_parser('context'); p.add_argument('--task', required=True); p.add_argument('--campaign', required=True); p.add_argument('--budget', type=int, default=6000); p.add_argument('--role', choices=['historian', 'literature', 'transfer']); p.add_argument('--include-private', action='store_true'); p.add_argument('--json', action='store_true')
    p = sub.add_parser('packet'); p.add_argument('work'); p.add_argument('--refresh', action='store_true')
    sub.add_parser('audit')
    sub.add_parser('status')
    p = sub.add_parser('profile'); p.add_argument('--campaign', required=True)
    p = sub.add_parser('sources'); p.add_argument('--include-private', action='store_true')
    args = parser.parse_args(argv)
    try:
        ws = Workspace(config_path(args.config))
        if args.lock_timeout < 0:
            raise ValueError('--lock-timeout must be nonnegative')
        ws.lock_timeout = args.lock_timeout
        if args.command == 'sync': output = sync(ws, args.full, lambda message: print(message, file=sys.stderr, flush=True))
        elif args.command == 'search': output = search(ws, args.query, args.campaign, args.limit, args.kind, args.include_private)
        elif args.command == 'inspect': output = inspect(ws, args.id, args.include_private)
        elif args.command == 'packet': output = packet(ws, args.work, args.refresh)
        elif args.command == 'audit': output = audit(ws)
        elif args.command == 'sources': output = source_registry(ws, args.include_private)
        elif args.command == 'status': output = status(ws)
        elif args.command == 'profile': output = ws.campaign(args.campaign)
        else:
            output = context(ws, args.task, args.campaign, args.budget, args.role, args.include_private)
            if not args.json:
                print(output['text']); return 0
        print(json.dumps(output, indent=2, ensure_ascii=False)); return 0
    except (ValueError, OSError, KeyError, sqlite3.Error) as exc:
        print('Error: ' + str(exc), file=sys.stderr); return 2

if __name__ == '__main__':
    raise SystemExit(main())
