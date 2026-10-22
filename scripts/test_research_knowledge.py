import json
import tempfile
import unittest
import fcntl
from pathlib import Path
import research_knowledge as k

class KnowledgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for d in ('campaign', 'related', 'private', 'library/math'):
            (self.root / d).mkdir(parents=True)
        self.config = self.root / 'workspace.json'
        self.data = {'version': 1, 'library': 'library', 'sources': [
            {'id': 'campaign', 'path': 'campaign'}, {'id': 'related', 'path': 'related'},
            {'id': 'library', 'path': 'library'}, {'id': 'private', 'path': 'private', 'visibility': 'private'}],
            'campaigns': {'test': {'sources': ['campaign'], 'related': ['related'],
                                  'summary': 'Finite objects; all ranks are unrestricted.',
                                  'synonyms': [['old vocabulary', 'new vocabulary']]}},
            'writeups': [{'id': 'internal-test', 'domain': 'math', 'title': 'Finite structures',
                         'repo': 'campaign', 'entry': 'main.tex'}]}
        self.config.write_text(json.dumps(self.data))
        self.ws = k.Workspace(self.config)
        (self.root / 'campaign/main.tex').write_text(r'\input{lemma}' + '\n')
        (self.root / 'campaign/lemma.tex').write_text(r'\begin{lemma}\label{lem:finite}Every finite X works.\end{lemma}')
    def tearDown(self):
        self.temp.cleanup()
    def card(self, identifier, body, **extra):
        meta = {'id': identifier, 'title': identifier, 'kind': 'theorem', 'status': 'proved',
                'sources': [k.source_entry(self.ws, 'campaign', 'lemma.tex')], **extra}
        path = self.root / 'library/math' / (identifier + '.md')
        path.write_text('---\n' + json.dumps(meta) + '\n---\n' + body)
        return path
    def test_incremental_uncommitted_deletion_and_missing_root(self):
        p = self.root / 'campaign/note.md'; p.write_text('# Discovery\nunique alpha beta')
        first = k.sync(self.ws)
        self.assertGreater(first['changed'], 0)
        self.assertEqual(k.sync(self.ws)['changed'], 0)
        self.assertEqual(k.search(self.ws, 'unique alpha beta')['hits'][0]['path'], 'note.md')
        p.unlink(); self.assertEqual(k.sync(self.ws)['removed'], 1)
        self.assertFalse(k.search(self.ws, 'unique')['hits'])
        (self.root / 'related').rmdir()
        self.assertTrue(any(i['issue'] == 'missing-root' for i in k.sync(self.ws)['issues']))
    def test_edited_chunks_replace_old_fts_rows(self):
        p = self.root / 'campaign/edit.md'
        p.write_text('# Before\nold_unique_term')
        k.sync(self.ws)
        p.write_text('# After\nnew_unique_term')
        k.sync(self.ws)
        self.assertFalse(k.search(self.ws, 'old_unique_term')['hits'])
        self.assertTrue(k.search(self.ws, 'new_unique_term')['hits'])
        p.write_text('# Corrected\nnew text after indexing')
        self.assertTrue(k.search(self.ws, 'new_unique_term')['hits'][0]['freshness_issues'])
    def test_packet_rejects_missing_dependency(self):
        (self.root / 'campaign/main.tex').write_text(r'\input{missing}')
        with self.assertRaises(ValueError):
            k.packet(self.ws, 'internal-test')
    def test_packet_tracks_nested_inputs_relative_to_entry_directory(self):
        paper = self.root / 'campaign/paper'
        (paper / 'sections').mkdir(parents=True)
        (paper / 'main.tex').write_text(r'\input{sections/setup}')
        (paper / 'sections/setup.tex').write_text(r'\input{sections/result}')
        (paper / 'sections/result.tex').write_text(
            r'\begin{lemma}\label{lem:nested}A nested result.\end{lemma}')
        self.data['writeups'][0]['entry'] = 'paper/main.tex'
        self.config.write_text(json.dumps(self.data))
        output = k.packet(k.Workspace(self.config), 'internal-test')
        manifest = json.loads((Path(output['packet']) / 'source-manifest.json').read_text())
        self.assertEqual({s['path'] for s in manifest['sources']},
                         {'paper/main.tex', 'paper/sections/setup.tex', 'paper/sections/result.tex'})
    def test_generated_overview_preserves_statement_and_review(self):
        out = k.packet(self.ws, 'internal-test')
        target = Path(out['packet'])
        (target / 'results').mkdir()
        card = self.card('A', 'Precise full statement.', review='extraction checked')
        (target / 'results/A.md').write_text(card.read_text())
        k.render_results(target)
        body = (target / 'key-results.md').read_text()
        self.assertIn('Precise full statement.', body)
        self.assertIn('extraction checked', body)
    def test_alias_and_cross_repo_search(self):
        (self.root / 'related/old.md').write_text('# Old result\nold vocabulary gives a universal construction')
        k.sync(self.ws)
        hits = k.search(self.ws, 'new vocabulary', 'test')['hits']
        self.assertTrue(any(h['repo'] == 'related' for h in hits))
    def test_curated_assumptions_survive_large_raw_candidate_set(self):
        (self.root / 'campaign/census.md').write_text(''.join(
            f'# Section {i}\n' + 'commonterm ' * 20 + '\n' for i in range(2100)))
        self.card('rare-card', 'Long explanation. ' * 300,
                  assumptions=['commonterm with a special nonempty proper inclusion'])
        k.sync(self.ws)
        response = k.search(self.ws, 'commonterm', kinds=['theorem'])
        self.assertTrue(response['candidate_limit_reached'])
        hits = response['hits']
        self.assertEqual(hits[0]['id'], 'rare-card')
        self.assertEqual(k.search(self.ws, 'nonempty proper inclusion')['hits'][0]['id'], 'rare-card')
    def test_correction_attached_even_without_query_words(self):
        self.card('result-A', 'Every finite structure has the property.', aliases=['finite extension'])
        self.card('correction-B', 'The proposed argument fails for a cyclic witness.', kind='correction',
                  status='refuted', relations={'corrects': ['result-A']})
        k.sync(self.ws)
        h = k.search(self.ws, 'result-A')['hits'][0]
        self.assertEqual(h['id'], 'result-A')
        self.assertEqual(h['corrections'][0]['id'], 'correction-B')
        packet = k.context(self.ws, 'result-A', 'test', 5000)
        self.assertIn('cyclic witness', packet['text'])
    def test_source_drift_and_duplicate_ids(self):
        p = self.card('result-A', 'A precise statement.')
        k.sync(self.ws)
        (self.root / 'campaign/lemma.tex').write_text('Corrected statement')
        self.assertTrue(k.inspect(self.ws, 'result-A')[0]['freshness_issues'])
        (self.root / 'related/duplicate.md').write_text(p.read_text())
        k.sync(self.ws)
        self.assertTrue(any(i['issue'] == 'duplicate-id' for i in k.audit(self.ws)['issues']))
    def test_private_sources_not_exposed_through_cards(self):
        (self.root / 'private/secret.md').write_text('private_unique_result')
        self.card('private-result', 'private_unique_result', sources=[k.source_entry(self.ws, 'private', 'secret.md')])
        k.sync(self.ws)
        self.assertFalse(k.search(self.ws, 'private_unique_result')['hits'])
        self.assertTrue(k.search(self.ws, 'private_unique_result', private=True)['hits'])

    def test_removed_sources_are_not_exposed_from_an_older_snapshot(self):
        (self.root / 'private/secret.md').write_text('private_removed_result')
        self.card('private-result', 'private_removed_result',
                  sources=[k.source_entry(self.ws, 'private', 'secret.md')])
        k.sync(self.ws)
        self.data['sources'] = [source for source in self.data['sources'] if source['id'] != 'private']
        self.config.write_text(json.dumps(self.data))
        current = k.Workspace(self.config)
        self.assertFalse(k.search(current, 'private_removed_result')['hits'])
        self.assertFalse(k.search(current, 'private_removed_result', private=True)['hits'])
    def test_context_does_not_truncate_card_and_respects_budget(self):
        self.card('large-result', 'Assumption: finite. ' + 'Detailed statement. ' * 2000)
        k.sync(self.ws)
        out = k.context(self.ws, 'large-result', 'test', 1000)
        self.assertLessEqual(k.units(out['text']), 1000)
        self.assertIn('large-result', out['omitted'])
        self.assertNotIn('Detailed statement.', out['text'])
    def test_packet_tracks_inputs_refresh_preserves_cards(self):
        out = k.packet(self.ws, 'internal-test')
        self.assertEqual(out['sources'], 2)
        p = Path(out['packet'])
        (p / 'key-results.md').write_text('Reviewed extraction')
        self.assertIn('Every finite X', (p / 'extraction-candidates.md').read_text())
        k.sync(self.ws)
        (self.root / 'campaign/lemma.tex').write_text(r'\begin{lemma}Only acyclic X.\end{lemma}')
        self.assertTrue(any(i.get('work') == 'internal-test' for i in k.audit(self.ws)['issues']))
        k.packet(self.ws, 'internal-test', refresh=True)
        self.assertEqual((p / 'key-results.md').read_text(), 'Reviewed extraction')
        self.assertIn('acyclic', (p / 'extraction-candidates.md').read_text())
    def test_broken_relation_and_invalid_card_reported(self):
        self.card('A', 'Content.', relations={'uses': ['missing']})
        k.sync(self.ws)
        self.assertTrue(any(i['issue'] == 'unresolved-relation' for i in k.audit(self.ws)['issues']))
        (self.root / 'campaign/invalid.md').write_text('---\n{"id": "bad"}\n---\nbody')
        self.assertTrue(any(i['path'] == 'invalid.md' for i in k.sync(self.ws)['issues']))
    def test_duplicate_raw_content_grouped(self):
        for repo in ['campaign', 'related']:
            (self.root / repo / 'copy.md').write_text('# Identical\nexact copied account')
        k.sync(self.ws)
        h = k.search(self.ws, 'exact copied account')['hits'][0]
        self.assertEqual(len(h['also_at']), 1)

    def database(self):
        root = self.root / 'database'
        (root / 'objects').mkdir(parents=True)
        (root / 'facts').mkdir()
        self.data['sources'].append({'id': 'db', 'path': 'database', 'type': 'json-records',
            'subjects': ['math'], 'authority': 'Owns definitions and structured facts.',
            'collections': [
                {'id': 'objects', 'glob': 'objects/*.json', 'kind': 'definition', 'alias_fields': ['short_name']},
                {'id': 'facts', 'glob': 'facts/*.json', 'kind': 'relationship', 'schema': 'facts/schema.json',
                 'references': {'object': {'collection': 'objects', 'key': 'short_name',
                                          'prefix': '#objects/', 'fields': ['name', 'definition']}}}]})
        self.config.write_text(json.dumps(self.data))
        self.ws = k.Workspace(self.config)
        obj = root / 'objects/first.json'
        obj.write_text(json.dumps({'id': 7, 'name': 'Finite structures', 'short_name': 'finite',
                                  'definition': 'Acyclic structures only.'}))
        fact = root / 'facts/bound.json'
        fact.write_text(json.dumps({'id': 12, 'name': 'Scoped bound', 'object': '#objects/finite',
                                   'status': 'refuted', 'strength': 'strict', 'value': 0,
                                   'monotonic': False, 'new_field': {'caveat': 'finite nonempty'}}))
        schema = root / 'facts/schema.json'
        schema.write_text(json.dumps({'columns': [{'name': 'strength', 'description': 'Scope of witness',
            'enum': [{'value': 'strict', 'display_name': 'Finite gap only; not an unbounded ratio.'}]}]}))
        return obj, fact, schema

    def test_structured_status_scope_identity_and_ownership(self):
        obj, fact, schema = self.database()
        self.assertFalse(k.sync(self.ws)['issues'])
        hit = k.inspect(self.ws, 'db:facts:12')[0]
        self.assertEqual(hit['status'], 'refuted')
        self.assertEqual(hit['kind'], 'relationship')
        self.assertEqual(hit['origin_kind'], 'structured')
        self.assertIn('not independently verified', hit['review'])
        self.assertIn('not an unbounded ratio', hit['body'])
        self.assertIn('"monotonic": false', hit['body'])
        self.assertIn('"value": 0', hit['body'])
        self.assertIn('finite nonempty', hit['body'])
        self.assertIn('Acyclic structures only', hit['body'])
        self.assertEqual(hit['relations']['references'], ['db:objects:7'])
        self.assertEqual(len(hit['sources']), 3)
        self.assertEqual(k.inspect(self.ws, 'db:objects:7')[0]['status'], 'unreviewed')
        self.assertEqual(k.search(self.ws, 'db:facts:12')['hits'][0]['id'], 'db:facts:12')
        self.assertEqual(k.sync(self.ws)['changed'], 0)
        fact.rename(fact.with_name('renamed.json'))
        k.sync(self.ws)
        self.assertEqual(k.inspect(self.ws, 'db:facts:12')[0]['path'], 'facts/renamed.json')
        registry = k.source_registry(self.ws)
        self.assertEqual(registry['sources'][-1]['type'], 'json-records')

    def test_structured_reference_and_schema_changes_invalidate(self):
        obj, fact, schema = self.database()
        k.sync(self.ws)
        obj.write_text(obj.read_text().replace('Acyclic', 'Connected'))
        self.assertTrue(k.inspect(self.ws, 'db:facts:12')[0]['freshness_issues'])
        k.sync(self.ws)
        hit = k.inspect(self.ws, 'db:facts:12')[0]
        self.assertIn('Connected structures', hit['body'])
        self.assertFalse(hit['freshness_issues'])
        schema.write_text(schema.read_text().replace('Finite gap only', 'Strict finite gap only'))
        k.sync(self.ws)
        self.assertIn('Strict finite gap only', k.inspect(self.ws, 'db:facts:12')[0]['body'])

    def test_structured_missing_reference_and_invalid_file_remove_stale_results(self):
        obj, fact, schema = self.database()
        k.sync(self.ws)
        obj.unlink()
        report = k.sync(self.ws)
        self.assertTrue(any(i['issue'] == 'unresolved-reference' for i in report['issues']))
        self.assertIn('UNRESOLVED REFERENCE', k.inspect(self.ws, 'db:facts:12')[0]['body'])
        fact.write_text('{ invalid')
        self.assertTrue(k.sync(self.ws)['issues'])
        with self.assertRaises(ValueError):
            k.inspect(self.ws, 'db:facts:12')
        self.assertTrue(k.sync(self.ws)['issues'])

    def test_structured_duplicate_ids_fail_source_and_config_changes_refresh(self):
        obj, fact, schema = self.database()
        k.sync(self.ws)
        self.data['sources'][-1]['collections'][1]['kind'] = 'value'
        self.config.write_text(json.dumps(self.data))
        self.ws = k.Workspace(self.config)
        k.sync(self.ws)
        self.assertEqual(k.inspect(self.ws, 'db:facts:12')[0]['kind'], 'value')
        fact.with_name('duplicate.json').write_text(fact.read_text())
        self.assertTrue(any('Duplicate record ID' in i['issue'] for i in k.sync(self.ws)['issues']))
        with self.assertRaises(ValueError):
            k.inspect(self.ws, 'db:facts:12')

    def test_structured_context_is_complete_or_omitted(self):
        obj, fact, schema = self.database()
        record = json.loads(fact.read_text())
        record['proof'] = 'Long proof. ' * 1000
        fact.write_text(json.dumps(record))
        k.sync(self.ws)
        out = k.context(self.ws, 'db:facts:12', 'test', 1500)
        self.assertIn('db:facts:12', out['omitted'])
        self.assertNotIn('Long proof.', out['text'])
        out = k.context(self.ws, 'db:facts:12', 'test', 25000)
        self.assertIn(record['proof'], out['text'])
        self.assertIn('not independently verified', out['text'])

    def test_profile_changes_do_not_rebuild_content(self):
        self.card('A', 'A reusable result.')
        k.sync(self.ws)
        self.data['campaigns']['test']['summary'] = 'An updated campaign status. ' * 2000
        self.config.write_text(json.dumps(self.data))
        self.ws = k.Workspace(self.config)
        self.assertFalse(k.status(self.ws)['registry_current'])
        report = k.sync(self.ws)
        self.assertEqual(report['changed'], 0)
        self.assertTrue(k.status(self.ws)['registry_current'])
        packet = k.context(self.ws, 'A reusable result', 'test', 2000)
        self.assertTrue(packet['profile_omitted'])
        self.assertIn('A reusable result.', packet['text'])
        self.assertIn('profile --campaign test', packet['text'])
        self.assertLessEqual(k.units(packet['text']), 2000)

    def test_source_configuration_still_invalidates_content(self):
        p = self.root / 'campaign/excluded.md'
        p.write_text('unique excluded result')
        k.sync(self.ws)
        self.data['sources'][0]['exclude'] = ['excluded.md']
        self.config.write_text(json.dumps(self.data))
        k.sync(k.Workspace(self.config))
        self.assertFalse(k.search(self.ws, 'unique excluded result')['hits'])

    def test_discovery_skips_file_and_directory_compatibility_links(self):
        (self.root / 'campaign/copy.md').symlink_to(self.root / 'campaign/lemma.tex')
        (self.root / 'campaign/view').symlink_to(self.root / 'related', target_is_directory=True)
        (self.root / 'related/result.md').write_text('one canonical owner')
        report = k.sync(self.ws)
        self.assertFalse(report['issues'])
        self.assertFalse(k.search(self.ws, 'one canonical owner')['hits'][0]['also_at'])
        conn = self.ws.connect()
        self.assertFalse(conn.execute("SELECT key FROM files WHERE path='copy.md' OR path LIKE 'view/%'").fetchall())
        conn.close()

    def test_queries_remain_consistent_while_writer_commits(self):
        self.card('A', 'Before the correction.')
        k.sync(self.ws)
        reader = self.ws.connect()
        before = reader.execute("SELECT body FROM chunks WHERE json_extract(meta,'$.id')='A'").fetchone()[0]
        self.card('A', 'After the correction.')
        k.sync(self.ws)  # A WAL reader must not block this commit.
        self.assertEqual(reader.execute("SELECT body FROM chunks WHERE json_extract(meta,'$.id')='A'").fetchone()[0], before)
        reader.close()
        self.assertEqual(k.inspect(self.ws, 'A')[0]['body'], 'After the correction.')

    def test_writer_wait_is_bounded_and_preserves_existing_index(self):
        k.sync(self.ws)
        lockpath = self.ws.dbpath.with_suffix('.lock')
        with lockpath.open('a+') as owner:
            fcntl.flock(owner, fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.assertTrue(k.status(self.ws)['sync_in_progress'])
            self.ws.lock_timeout = .02
            with self.assertRaisesRegex(ValueError, 'Index writer busy'):
                k.sync(self.ws)
            self.assertTrue(k.search(self.ws, 'finite')['hits'])
        self.assertFalse(k.status(self.ws)['sync_in_progress'])

    def test_query_migration_and_legacy_chunk_writes_preserve_corrections(self):
        self.card('A', 'Main result.')
        correction = self.card('B', 'Unrelated vocabulary.', kind='correction',
                               relations={'corrects': ['A']})
        k.sync(self.ws)
        # Simulate a pre-upgrade database containing real indexed cards.
        conn = self.ws.connect(True)
        for trigger in ('chunks_query_insert', 'chunks_query_update', 'chunks_query_delete'):
            conn.execute('DROP TRIGGER ' + trigger)
        conn.execute('DROP TABLE card_search')
        conn.execute('DROP TABLE correction_links')
        conn.execute("DELETE FROM state WHERE key='query_schema'")
        conn.commit(); conn.close()
        self.assertEqual(k.sync(self.ws)['changed'], 0)
        self.assertEqual(k.inspect(self.ws, 'A')[0]['corrections'][0]['id'], 'B')
        # Old distributed writers update chunks without knowing the new tables.
        conn = self.ws.connect(True)
        row = conn.execute("SELECT key,meta FROM chunks WHERE json_extract(meta,'$.id')='B'").fetchone()
        meta = json.loads(row['meta']); meta['relations'] = {'refutes': ['different-target']}
        conn.execute('UPDATE chunks SET meta=? WHERE key=?', (json.dumps(meta), row['key']))
        conn.commit(); conn.close()
        self.assertFalse(k.inspect(self.ws, 'A')[0]['corrections'])
        correction.unlink()
        k.sync(self.ws)
        self.assertFalse(k.search(self.ws, 'Unrelated vocabulary')['hits'])

    def test_card_file_changes_are_reported_even_if_proof_source_is_unchanged(self):
        p = self.card('A', 'Old extracted statement.')
        k.sync(self.ws)
        p.write_text(p.read_text().replace('Old extracted', 'New corrected'))
        self.assertTrue(any('library:math/A.md' in issue
                            for issue in k.inspect(self.ws, 'A')[0]['freshness_issues']))

    def test_established_source_status_is_preserved_without_promoting_review(self):
        self.card('published-result', 'An imported theorem.', status='established',
                  review='Source statement read; not independently reproved')
        self.assertFalse(k.sync(self.ws)['issues'])
        hit = k.search(self.ws, 'published-result')['hits'][0]
        self.assertEqual(hit['status'], 'established')
        self.assertIn('not independently reproved', hit['review'])

    def test_full_sync_detects_content_with_unchanged_stat_and_avoids_unneeded_rewrites(self):
        import os
        p = self.root / 'campaign/hidden.md'
        p.write_text('alpha'); k.sync(self.ws)
        stat = p.stat(); p.write_text('bravo')
        os.utime(p, ns=(stat.st_atime_ns, stat.st_mtime_ns))
        self.assertEqual(k.sync(self.ws)['changed'], 0)
        self.assertEqual(k.sync(self.ws, full=True)['changed'], 1)
        self.assertTrue(k.search(self.ws, 'bravo')['hits'])
        self.assertEqual(k.sync(self.ws, full=True)['changed'], 0)

if __name__ == '__main__':
    unittest.main()
