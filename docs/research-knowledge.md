# Research knowledge CLI

Implementation: `scripts/research_knowledge.py` (Python standard library, SQLite FTS5).
Design and progress: [design](research-knowledge-design.md), [work plan](research-knowledge-work-plan.md).

## Commands

Run from a configured campaign directory, or place `--config PATH` before the subcommand.

```bash
python3 scripts/research_knowledge.py sync
python3 scripts/research_knowledge.py status
python3 scripts/research_knowledge.py search 'relative module linear resolution' --campaign . --limit 5
python3 scripts/research_knowledge.py inspect 'internal:stable-result-id'
python3 scripts/research_knowledge.py context --campaign . --task 'current research question' --budget 12000
python3 scripts/research_knowledge.py context --campaign . --task 'compare these hypotheses' --role transfer
python3 scripts/research_knowledge.py profile --campaign .
python3 scripts/research_knowledge.py packet internal-writeup
python3 scripts/research_knowledge.py packet internal-writeup --refresh
python3 scripts/research_knowledge.py audit
python3 scripts/research_knowledge.py sources
```

Search/inspect/audit return JSON; context returns readable Markdown (`--json` includes omissions
and coverage). `--kind` is repeatable on search. Private roots require `--include-private` on
retrieval commands; this is a local visibility convention, not an authentication boundary. Do not
publish the database or expose the CLI as an unauthenticated service.

`sync` records edits/deletions and uncommitted files. Unchanged size/mtime skips re-reading;
`sync --full` hashes every selected file without rewriting unchanged content. Changes to indexing
configuration invalidate the affected sources; profile, pin and writeup-registration edits do not
force a content rebuild. Index transactions are serialized using a file lock.
The first build can take minutes; later runs only replace changed chunks. The coverage report
lists missing roots, unreadable/oversized files and counts per source. Text/TeX/Markdown and
metadata/dashboard JSON are indexed by default; root-specific include/exclude globs customize this.
Directory symlinks are not traversed. Configure their canonical owners as sources instead.
SQLite temporary sorts use the cache directory unless `SQLITE_TMPDIR` is explicitly set.
`sources` lists registered roots, types, subjects, ownership and collection mappings without
requiring an index. Private sources are omitted unless `--include-private` is given.

Queries use SQLite WAL snapshots: a sync can commit while readers use the previous complete
generation. Curated cards have their own full-text index, and reverse correction links are indexed;
retrieval does not load the whole card collection. These derived structures migrate transactionally
at the next sync. SQLite triggers maintain them even for older writers, although all campaign helper
copies should be updated to avoid old indexer versions causing full rebuilds.

`status` is a cheap health check; it reports index age, registry and indexer compatibility, coverage
issue count, whether a sync is running, and the journal mode. Search responses include the same
snapshot metadata. Freshness checks hash the returned records' original sources and the indexed
files themselves, so an edited extraction cannot silently appear current just because its cited
proof is unchanged. Age and sync status do not certify a proof or prove that no file has changed.

Allow sync to finish: a first build or migration can take minutes. CLI progress goes to stderr;
stdout remains JSON. The default writer/SQLite lock wait is 300 seconds, configurable before the
subcommand, for example `--lock-timeout 600 sync`. A short tool yield is fine; a six-second process
timeout is not a suitable sync allowance. Continue polling the running process instead of launching
duplicate syncs. On lock expiry, inspect `status` and the running job; do not remove a shared lock
or terminate another campaign's job. Scope and resource limits still govern execution.

Context preserves full curated cards and attached corrections, or omits the whole group if it
does not fit. Raw excerpts may be partial and are labeled as such. The budget is a conservative
UTF-8-byte upper bound for byte-based tokenizers, not an exact tokenizer count. Campaign profiles
that are too large are omitted as a whole with an explicit notice, reserving room for evidence;
`profile --campaign ID` returns the complete profile. An oversized task still requires a shorter
task or larger budget. Context also reports coverage issues and raw-candidate limits. Use inspect
for omitted evidence. No automatic context injection or agent spawning is installed: skills
explicitly invoke and read the command.

## Registry

Store campaign-specific configuration in the artifact workspace. Relative paths resolve from the
registry's directory. A consuming repo may have `.research-knowledge.json` containing
`{"config":"../artifact-workspace/knowledge/workspace.json"}`. The existing shared-library binding
also discovers `knowledge/workspace.json` beside the library. Environment override:
`RESEARCH_KNOWLEDGE_CONFIG`. The registry format is:

```json
{
  "version": 1,
  "cache": ".cache/knowledge.sqlite",
  "library": "../literature",
  "sources": [
    {"id": "project", "path": "../../project", "exclude": ["literature", "references"]},
    {"id": "related", "path": "../../related"},
    {"id": "literature", "path": "../literature"}
  ],
  "campaigns": {
    "project": {
      "sources": ["project"], "related": ["related", "literature"],
      "summary": "Current objects and conventions; link the live goal in the owning ledger.",
      "synonyms": [["older term", "current term"]],
      "pins": ["internal:stable-result-id"]
    }
  },
  "writeups": [
    {"id": "internal-writeup", "domain": "math", "repo": "project",
     "entry": "main.tex", "extra_sources": ["macros.sty"], "title": "Writeup title"}
  ]
}
```

Pins may also be `{ "repo": "project", "path": "CURRENT_STATE.md" }` for live text. Use short
profiles and pins so retrieved mathematics fits. The `.` campaign selector identifies the profile
from the current working directory. Registry changes require another sync. Unknown profiles fail
explicitly. Default exclusions cover skill copies, Git/build environments, caches and submission
bundles. `include`/`exclude` use pathlib path-match globs; names such as `literature` prune a directory.

### Structured databases

Add a `json-records` source for a database stored as one JSON object per file. The default
source type remains `text`. Keep actual repo names, subject assignments and field mappings
in the artifact workspace's registry:

```json
{
  "id": "catalogue",
  "path": "../../../code/catalogue",
  "type": "json-records",
  "subjects": ["mathematics"],
  "authority": "Owns definitions and structured facts; proof links identify external owners.",
  "collections": [
    {"id": "objects", "glob": "data/objects/*.json", "kind": "definition",
     "id_field": "id", "title_field": "name", "alias_fields": ["short_name"]},
    {"id": "facts", "glob": "data/facts/*.json", "kind": "relationship",
     "schema": "data/facts/schema.json", "status_field": "status",
     "references": {
       "object_id": {"collection": "objects", "key": "short_name", "prefix": "#objects/",
                     "fields": ["name", "definition"]}
     }}
  ]
}
```

Identity defaults to `id`, title to `name`, status to `status`, and kind to `record`.
The stable search ID is `SOURCE:COLLECTION:ID`; renaming its file does not change identity.
Use `inspect` on this ID, or search with `--kind relationship`, `--kind value`, etc.
Every field is preserved, including unknown fields, false Booleans and zero values. Missing
status is `unreviewed`; existing statuses such as `established` or `refuted` are preserved
verbatim. Importing a record does not certify its proof. A record is kept whole in context
or omitted for budget, with its ID available through `context --json` and `inspect`.

Optional schemas use a `columns` list with `name`, `description`, and optional `enum` entries
(`value`, `display_name`). Their descriptions make codes and scope readable; this is not
JSON Schema validation. Run the database owner's validators for semantic/schema validation.
Registered schema files are excluded from record globs automatically. Each record must match
exactly one collection. Reference mappings expand selected fields one hop, retain target IDs,
and fingerprint the referenced files. Full proof and citation pointers stay in the original
record; the importer does not fetch or certify external proofs or infer correction relations.

`sync` rereads structured records to detect changes and rebuilds that source when a record,
referenced definition, or schema changes. Registry changes invalidate mappings. Malformed
records and broken references appear in coverage; ambiguous IDs/lookup keys fail the source
rather than selecting an arbitrary record. Deleted or invalid records are removed from search.
Subjects and ownership are descriptive metadata; campaign `sources`/`related` control affinity.

Keep structured facts in the database owner and authored prose/proofs in their owner. Exclude
generated catalogue directories from the text source once their originals are indexed. Do not
create independent editable packets for every imported database row. Agent-written synthesis
cards may cite the underlying JSON files with source fingerprints. Other database formats
need an adapter or a maintained object-per-file JSON export; binary SQL databases and JSON
arrays are not supported by this adapter.

## Result cards

Cards live in `<library>/<domain>/<work-id>/results/*.md`. Frontmatter is a JSON object enclosed
in Markdown frontmatter delimiters; JSON is also valid YAML. One editable card owns each stable ID.

```markdown
---
{
  "id": "internal:stable-result-id",
  "title": "A precise reusable result",
  "kind": "theorem",
  "status": "proved",
  "review": "statement checked; proof audit pending",
  "assumptions": ["Finite objects", "Specified field convention"],
  "aliases": ["older theorem name"],
  "sources": [{"repo":"project", "path":"main.tex", "anchor":"thm:main", "sha256":"FULL_SOURCE_HASH"}],
  "relations": {"uses": ["internal:earlier-result"]}
}
---
Full mathematical statement, interpretation, limitations, and proof or witness pointers.
```

Kinds: theorem, lemma, definition, example, counterexample, conjecture, idea, failed-approach,
correction. Statuses: proved, established, conditional, computational, conjectural, refuted, withdrawn, open,
unreviewed. Status records mathematical evidence as reported by the source; `review` describes
what was checked during extraction. Never equate those fields. A packet manifest supplies source
fingerprints; include dependency sources when an extracted claim depends on separate definitions.

Incoming `corrects`, `refutes`, and `supersedes` relationships attach evidence to a retrieved ID.
Other relations are displayed and checked for missing targets. Automatic equivalence merging is
not performed. Exact duplicated raw text is grouped; different cards retain distinct IDs.

## Internal packets and maintenance

Register the work, then create the packet. Deterministic extraction captures theorem-like TeX
environments and Markdown sources as unreviewed candidates. It is not a full TeX interpreter.
Literal input/include/bibliography dependencies are followed; register local macro files and
other implicit sources in `extra_sources`. Dynamic or missing dependencies are errors. Manuscript
sources remain in their owning repo, identified by revision and content hash.

Refresh regenerates source manifests and candidates. It never edits cards. When cards exist,
`key-results.md` is generated only if absent or already marked as managed by this tool; hand-written
overviews are preserved. Refreshing a packet does not make stale card fingerprints current.

Audit provides a maintenance queue, including unregistered standalone TeX candidates. Not every
standalone scratch file deserves a packet: promote reusable writeups deliberately. Review changed
statements/corrections, update cards and relations, then sync. Do not move research sources or copy
campaign-specific vocabulary into reusable code. Embeddings, automatic launcher hooks and broad
historical curation are follow-up work rather than hidden dependencies of the initial system.

## Explicit legacy-source decoding and exclusions

Text is read strictly as UTF-8 unless the source owner records an exact-path
`text_policies` entry on its registry source. A policy requires `action`, the
SHA256 of the retained raw bytes, and a provenance `reason`. `decode` additionally
requires a supported explicit `encoding` (`cp1251`, `cp1252`, `iso8859-2`, or
`iso8859-15`). Approve a codec only from source/version evidence, such as an active
TeX encoding declaration; do not guess from successful decoding. The reader checks
strict decoding and byte-for-byte re-encoding and never rewrites the source.

An `exclude` policy records an unresolved source-access limitation. Sync reports
it in `text_dispositions`, removes any old indexed content for that path and does
not count it as indexed. Other packet files remain eligible. Exclusion is not
successful full-source recovery. Both actions are checked on every sync; raw hash
drift, unsupported codecs and undiscovered policy paths are errors requiring
review. `audit` retains the sync dispositions in its `coverage` field.

Update distributed helper copies before using a registry with these policies.
After an owner-approved change, run `sync` and `audit` and report decoded files,
explicit exclusions and actual errors separately. Registry edits must preserve
unrelated concurrent fields; the ignored search cache is not source authority.
