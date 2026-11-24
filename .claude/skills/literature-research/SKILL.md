---
name: literature-research
description: >-
  Search existing shared literature packets first, verify primary sources
  verbatim, reserve and maintain canonical source packets and shared indexes,
  and produce cited mathematical literature reviews comparing hypotheses,
  terminology, and prior results.
---

# Literature Research

Combine local shared-library reuse with targeted external searches and strict
primary-source verification. Durable papers belong in the common library
configured by `.research-library.json` (with `root` and `default_domain`, or
overridden via `RESEARCH_LIBRARY_ROOT` / `--root`), never in a separate
per-project download cache. If that checkout is unavailable or blocked outside
the sandbox, report the missing access and coverage limit rather than creating
a local substitute.

## 1. Local Library First

Before any web search for prior work, check what is already extracted locally:

1. Locate and search across all domains (`math`, `biomed`, `physics`):
   ```bash
   python3 scripts/research_library.py locate
   python3 scripts/research_library.py search 'query terms'
   python3 scripts/research_library.py search 'query terms' --sources --limit 10
   ```
2. Search by DOI, versionless arXiv ID, PMID, title, authors, and old citation
   keys; inspect `merged-results.md`, `key-results.md`, `metadata.json`,
   `library-record.json`, and `variants/`. Never re-download or reconvert a
   source when an adequate local extraction already exists.
3. For internal campaign writeups and sibling-repo results, pair this with
   `research-knowledge`, which indexes project cards and freshness.

## 2. Targeted Search & Verbatim Verification

When web search is needed to fill gaps, compare against newer preprints, or
situate results across fields:

- **Query variations:** search core mathematical objects, equivalent or dual
  formulations, and alternative community terminology (not only the current
  paper's wording).
- **Check primary sources verbatim:** never cite a theorem from memory, an
  abstract, or a secondary reference. Verify exact theorem numbering, quantifier
  order, assumptions, normalizations, constants, domain conventions, and
  publication metadata in the original text.
- **Calibrate exact comparison:** classify each related paper relative to the
  current work (implies / generalizes / special case / orthogonal / sharper
  bound / different hypothesis / counterexampled or superseded). Flag known
  errata or restricted validity explicitly.

## 3. Canonical Packets & Ownership

Before acquiring or extracting a paper absent from the shared library, reserve
its packet under the shared lock:

```bash
python3 scripts/research_library.py reserve --domain math --key author2024topic \
  --title 'Paper title' --doi '10.1234/example'
```

- Interpret `reuse-or-review` as "inspect and reuse the existing packet"; wait or
  coordinate if another task holds an incomplete reservation.
- Populate the returned canonical directory cleanly:
  ```text
  <library>/<domain>/<citation-key>/
    metadata.json              # URL/DOI/arXiv ID, access date, version, status
    library-record.json        # aliases and import provenance
    original.pdf               # immutable binary evidence (when policy permits)
    source.txt                 # extracted text, source TeX, or official HTML
    key-results.md             # exact theorems/hypotheses/conclusions from source
    project-notes/<project>.md # local relevance, notation map, caveats
    variants/<origin>/         # retained alternative versions
  ```
- **Preserve separation & immutability:** keep universal extracted statements
  separate from project-specific interpretation. Treat source PDFs/archives as
  immutable (add a new versioned file rather than overwriting symlink targets).
- **Commit in the owning repo:** project `literature/` or `references/` symlinks
  are compatibility views only—adding files through them does not stage them in
  Git. Commit canonical packet and index changes in the shared library's owning
  repository; commit only links or project notes in the consuming repo. Keep
  restricted notes out of shared public indexes.

## 4. Index Refresh & Output

After adding or updating packets, refresh the shared search and HTML indexes:

```bash
python3 scripts/research_library.py index
python3 scripts/render_literature_index.py
```

Return verified citations (title, authors, year, venue/arXiv/DOI, verified source
location), exact theorem hypotheses/conclusions matching the target question,
terminology alignment notes, and any remaining search coverage gaps.
