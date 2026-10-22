# Shared research knowledge

## Objective and ownership

Make prior results, ideas, examples, counterexamples, failed approaches, and corrections
retrievable across research campaigns and literature. Sources remain authoritative in their
owning repositories. The artifact workspace owns the registry, campaign profiles, curated
packets, and evaluation cases. This repository owns generic tools, schemas, and skills.
No project names, local paths, or campaign state belong in reusable code or guidance.

## Architecture

1. A configured registry selects source roots and campaign relationships. Index original
   Markdown, TeX, and selected JSON/text sources, including uncommitted research. Exclude
   generated pages, build outputs, vendored code, skill copies, caches, and symlink duplicates.
2. An incremental SQLite FTS5 index stores source fingerprints and section-level chunks.
   It is a disposable local cache, not the authoritative result database. Updates are
   transactional and serialized; readers see a complete index generation. Missing roots
   and unreadable/oversized files appear in coverage reports.
3. Curated result cards carry stable IDs, precise statements and assumptions, evidence
   status, source anchors and fingerprints, aliases, and typed relationships. A status
   reported by an author is separate from extraction review and source freshness.
4. Internal writeups receive library packets with source manifests and deterministic TeX/
   Markdown extraction candidates. Semantic summaries and review remain agent work.
   Refresh candidates without overwriting reviewed cards. Follow TeX input dependencies;
   a changed dependency makes the packet stale. Never infer proof correctness from a parser.
5. Search combines lexical ranking, exact identifiers, scoped synonym expansion, campaign
   affinity, and related-repo retrieval with global fallback. Group identical content and
   repeated presentations of a stable card. Always accompany a result with indexed
   correction/supersession records. Semantic similarity is not mathematical equivalence.
6. A context builder combines the campaign profile, selected results, known failures and
   corrections within an explicit budget. Keep assumptions and qualifications intact;
   omit an oversized record with a pointer rather than silently truncating its statement.
7. Optional specialist briefs support historian, literature, and transfer-checking roles.
   They are reproducible task packets, not hidden persistent agent memory. Actual spawning
   remains a decision of the calling agent under the session's delegation permissions.

## Data contracts

### Structured source extension

The registry also declares source `type` (`text`, the default, or `json-records`),
`subjects`, and an `authority` description. A structured source declares collections,
file globs, identity/title/alias fields, optional schemas, and reference mappings.
These mappings belong to the consuming workspace; generic code contains no database names.

Import one JSON object per file as one complete searchable record. Namespace its stable
identity by source and collection. Preserve every field, including source status, scope,
witness strength, citations, proof pointers, and unknown future fields. Add schema meanings
and configured one-hop reference labels/definitions without inventing new mathematical claims.
Missing status remains unreviewed; importing an established record is not a new proof review.
Fingerprint the record, schemas and resolved references. Report invalid records, duplicate
identities, missing references and empty collections. Rebuild a structured source when any
of its inputs change; registry changes invalidate cached mappings as well.

The database remains editable only in its owning repository. The index stores derived views,
not independent packets for every existing structured record. Curated packets can cite these
records. Exclude generated manuscript catalogues when their database owners are indexed,
while retaining authored proofs and narrative. Context includes a complete structured record
or omits it with an inspectable ID. Source registration is discoverable through `sources`.

Initial support is for version-controlled JSON databases. Other formats require an explicit
adapter or a maintained JSON export; indexing a binary database as text is not supported.

The registry has a schema version, a cache path, source roots with stable IDs, and campaign
profiles. Paths resolve relative to the registry. Profiles specify source IDs, related source
IDs, a short objective/conventions summary, pinned source files, and scoped synonym groups.
Private source roots require explicit inclusion in retrieval; indexing does not publish them.

A result card is Markdown with a JSON object between frontmatter delimiters (also valid YAML).
Required fields are `id`, `kind`, `status`, `title`, and `sources`. Source entries identify
`repo`, `path`, optional `anchor`, and the source `sha256`; revision is provenance, not identity.
Optional fields include `aliases`, `review`, `assumptions`, and `relations` mapping relation
names to stable result IDs. The Markdown body preserves the substantive statement, uses,
limitations, and proof/witness pointers. IDs survive renaming and source movement; unresolved
anchors or changed source fingerprints are reported, never silently blessed.

An internal packet has `metadata.json`, `source-manifest.json`, `extraction-candidates.md`,
and optionally `results/*.md` cards plus a generated `key-results.md`. It uses an explicit
work ID and `origin_kind: internal`; identifiers such as DOI remain optional. Multiple
writeups may point to one result ID without becoming independent discoveries.

## Maintenance and context lifecycle

- Register a writeup once it contains reusable mathematics. Update the packet after a
  meaningful source or dependency change, or after changing a claim's status.
- The authoring agent checks extraction candidates, writes precise cards, and links older
  results and corrections. Automation detects drift; it does not endorse the mathematics.
- At campaign start/resume, sync and read a context bundle. Before a substantial new attempt,
  search the proposed claim and failure mechanism, then inspect the closest original sources.
- Before reporting an advance, compare hypotheses and conclusions with existing results.
  Persist useful findings and relationships; update profiles only when current state changes.
- After compaction or delegation, reconstruct from the same profile and IDs. Specialist
  returns must include source-backed applicability and search limitations.
- Audits report stale packets/cards, broken sources/relations, duplicate IDs, uncovered roots,
  and registered writeups missing packets. Raw search remains available for uncurated material.

## Delivery and validation

Deliver a standard-library CLI with `sync`, `search`, `inspect`, `context`, `packet`, and `audit`.
Preserve existing literature commands. No network service, paid embedding dependency, renderer
change, or automatic publication is required. A later semantic backend can reuse these records.

Test against temporary repositories: incremental edits/deletions, changed TeX dependencies,
aliases, exact IDs, correction attachment, duplicate content and IDs, scope restrictions,
budget handling, uncommitted files, missing roots, and safe packet refresh. Replay real
rediscovery cases in the artifact workspace and record retrieval ranks, timings, coverage,
and context sizes. Pilot curation uses an active campaign and its related repositories;
the full configured corpus is searchable immediately. Broad retrospective curation is a
maintenance queue, not a prerequisite for search.

## Acceptance criteria

- Every configured root is indexed or explicitly reported as unavailable; no silent omission.
- Search returns source locations and distinguishes raw text from curated evidence.
- Corrections accompany known result IDs; stale evidence is visible in search and context.
- Context budgets are honored without presenting truncated claims as complete statements.
- Internal packets can be created, refreshed, and audited without overwriting curated work.
- A real pilot recovers earlier same-campaign and related-repo results, with durable evaluation.
- Generic instructions and entry points are available from sibling workspaces.
