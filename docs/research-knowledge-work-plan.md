# Research knowledge implementation progress

Design: [research-knowledge-design.md](research-knowledge-design.md).
This checklist tracks software delivery only. Campaign-specific configuration, packets,
evaluation inputs, and results belong in the artifact workspace.

- [x] 1. Write the design, ownership rules, data contracts, and acceptance criteria.
- [x] 2. Implement configuration, source discovery, incremental indexing, and coverage reports.
- [x] 3. Implement ranked search, aliases, stable record inspection, corrections, and freshness.
- [x] 4. Implement internal-writeup packet creation, dependency tracking, safe refresh, and audits.
- [x] 5. Implement bounded campaign context and optional specialist task briefs.
- [x] 6. Add meaningful regression tests and user-facing CLI documentation.
- [x] 7. Configure the full workspace and curate/evaluate a representative campaign pilot.
- [x] 8. Update generic workflow skills and propagate entry points/guidance to sibling repos.
- [x] 9. Commit/push scoped changes and verify installation and remote delivery.

## Structured source extension

- [x] Inspect existing database/manuscript ownership and record contracts; write the extension design.
- [x] Add configurable JSON record ingestion, source listing, provenance and invalidation.
- [x] Test status/scope preservation, references, changed schemas, deletion and malformed input.
- [x] Register the database and ownership in the artifact workspace; evaluate real retrieval.
- [x] Update maintenance guidance and propagate compatible tools; commit and push scoped changes.

The extension passes twenty-four combined knowledge/library tests. The artifact workspace records
structured import coverage and five retrieval checks against the full index. These verify retrieval
and preservation of source qualifications, not independent mathematical correctness.

## Deferred extensions

Semantic embeddings, automatic session-launch hooks, and exhaustive historical card curation
are subsequent enhancements. The initial implementation supplies lexical search, explicit
context loading, specialist briefs, and a visible maintenance queue.

## Delivery evidence

- Nineteen knowledge/library regression checks pass.
- CLI copies and skill discovery validated throughout the sibling workspace.
- The artifact workspace contains index coverage, maintenance, retrieval evaluation and context reports.
- The pilot recovers all seven expected prior results at rank one; this is not a global recall guarantee.
- Encoding failures and unregistered writeups remain visible in the maintenance/coverage reports.
