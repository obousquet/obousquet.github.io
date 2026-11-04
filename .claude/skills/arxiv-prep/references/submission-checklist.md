# arXiv submission checklist

Use this checklist for the detailed final pass. Verify all policy-sensitive facts on the official arXiv pages at submission time.

## Official pages to verify

- Submission overview: <https://info.arxiv.org/help/submit/index.html>
- TeX submissions: <https://info.arxiv.org/help/submit_tex.html>
- File names and source preparation: <https://info.arxiv.org/help/submit_tex.html>
- Metadata preparation: <https://info.arxiv.org/help/prep.html>
- Licenses: <https://info.arxiv.org/help/license/index.html>
- Category taxonomy: <https://arxiv.org/category_taxonomy>
- Generative-AI moderation policy: <https://info.arxiv.org/help/moderation/index.html>

Record the access date in the preflight report. Do not encode a remembered character limit, accepted engine, or policy as timeless.

## Source inventory

- Identify every root containing `\documentclass`; select the intended top-level file.
- Record the engine and any nondefault flags.
- Build with file recording enabled and inspect `.fls` when available.
- Trace `\input`, `\include`, bibliography directives, local `\documentclass`/`\usepackage` files, `\includegraphics`, imported data, and generated tables.
- Determine whether bibliography sources or a generated `.bbl` are required by the chosen workflow.
- Confirm filename case matches every TeX reference.

## Repository build

- Compile to convergence from the repository with the intended engine.
- Check for errors, undefined references/citations, rerun warnings, missing glyphs, and overfull boxes.
- Inspect the PDF rather than relying only on the log.
- Check PDF metadata, page count and size, encryption, embedded fonts, and interactive features when relevant.
- Keep the repository PDF current if project policy tracks generated artifacts.

## Scholarly preflight

- Verify citation existence and local claim support.
- Remove chat residue, TODOs, hidden drafting instructions, defensive assurances, promotional prose, and apologetic terminology.
- Confirm that every theorem, computation, figure, and dataset has a durable source or reproducible derivation independent of an AI transcript.
- Draft the required AI-use disclosure and identify any sentence that requires personal author confirmation.
- Preserve mathematically necessary limitations and literature comparisons.

## Minimal archive

Include only compilation inputs:

- root and included TeX files;
- bibliography input or required `.bbl`;
- local `.cls`, `.sty`, `.bst`, or font files;
- figures in supported formats;
- indispensable data or generated tables.

Exclude unless genuinely required:

- compiled manuscript PDFs;
- `.aux`, `.log`, `.out`, `.toc`, `.fls`, `.fdb_latexmk`, `.synctex*`, and editor backups;
- `.git`, virtual environments, caches, operating-system metadata, and hidden files;
- ledgers, dashboards, literature downloads, reviewer notes, exploratory code, and unrelated manuscripts;
- secrets, private correspondence, local absolute paths, and unpublished source material not intended for distribution.

Prefer a project-local archive script with an explicit allowlist. Emit a manifest and SHA-256 checksum. Normalize tar metadata if deterministic output is desired.

## Bundle audit and clean build

- Reject absolute paths, `..`, duplicate members, links, device files, and unexpected enclosing directories.
- Check filenames against the current arXiv restrictions.
- Check that all direct TeX inputs are present.
- Extract into a newly created temporary directory.
- Compile using only extracted files and the standard TeX installation.
- Search the clean log for all warnings and errors.
- Compare the clean PDF with the repository PDF using page count, extracted text, and visual inspection. Byte identity is optional because PDF metadata can vary.
- Recreate and retest the archive after the last source edit.

## Metadata sheet

Record:

- title and author order exactly as in the paper;
- abstract converted to arXiv-compatible TeX/ASCII and its current character count;
- comments with page and figure counts, avoiding promotional language;
- primary category and optional cross-list as recommendations for author confirmation;
- license options without selecting one for the author;
- compiler and top-level file;
- journal reference and DOI only if publication data exist.

Ensure the metadata abstract and manuscript abstract make the same claims. Recount after every abstract edit.

## Final author actions

The author must personally confirm:

1. author names, order, consent, and contact information;
2. rights to distribute every source and figure;
3. primary category and cross-list;
4. license selection;
5. disclosure accuracy and any author-review attestation;
6. the arXiv-generated PDF, including title page, equations, references, and final page.
