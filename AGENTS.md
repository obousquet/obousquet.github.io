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
