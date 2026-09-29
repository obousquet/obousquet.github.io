# Research workspace

## Shared Literature

Before any web search for prior work, search the common extracted literature
with `python3 scripts/research_library.py search 'terms'`. It searches titles,
identifiers, succinct result extractions, merged summaries, and project notes;
add `--sources` for full extracted text, or `--limit 0` for every hit.
Local result statements may be more useful than abstracts or web snippets.
Browse for gaps, verification, or updates after checking the local results.

Resolve the shared location from `.research-library.json`; all subjects share
one library. Use the `shared-literature` skill to reuse or reserve a canonical
packet before downloading or extracting. Never start another repo-local cache.
Keep different source versions and project interpretations, and link to common
results. Existing `literature/` and `references/` links are compatibility views.
Commit source packets and refreshed indexes in the library's owning repository;
project symlinks do not stage their target files. Preserve restricted views.

## Existing Results Before New Work
- Before a substantial proof attempt, computation, or new route, check what is already known in the
  current campaign and related repositories. Recover this context after handoffs or compaction;
  the latest round and dashboard alone are not a complete account of earlier results.
- Search current and archived ledgers, theorem/proof files, result inventories, and relevant
  experiments by mathematical statement, equivalent formulations, and old terminology. Use project
  guides and cross-references to identify related repos; search their authoritative artifacts too.
  Also search the shared literature library, but do not assume it indexes campaign results.
- Inspect matching statements and proofs, including hypotheses, quantifiers, conventions, and later
  corrections. Reuse established results with a source path and theorem/round reference. Reopen a
  failed route only when a changed assumption or new ingredient escapes the recorded failure.
- Before calling a result new or reporting progress, state what it adds to the closest existing
  result. Rediscovery is reuse or verification; a stronger statement, new proof, or new application
  needs its precise difference recorded. An unsuccessful keyword search does not establish novelty.
- Keep a compact, searchable result map in the existing ledger or inventory: statements and aliases,
  status, proof/source links, known failures, and relevant related-repo links. Preserve these links in
  handoffs. Reuse recent checks for unchanged work; search again when the target or evidence changes.
