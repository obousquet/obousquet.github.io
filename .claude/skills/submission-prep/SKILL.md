---
name: submission-prep
description: >-
  Prepare and validate LaTeX manuscripts for arXiv or journal submission in two
  gates: (1) scholarly preflight for citation verification, provenance,
  conversation residue, promotional/defensive prose, and AI disclosure; and
  (2) minimal reproducible source bundling, bundle audit, clean-room
  compilation, and metadata preparation.
---

# Submission Prep

Run this before arXiv upload, journal submission, or public release. Keep
**scholarly preflight** (claims, citations, prose, disclosure) and **source
bundling** (reproducible compilation from a minimal archive) strictly distinct:
a bundle that compiles cleanly never establishes that its citations or claims are
ready.

## Gate 1: Scholarly & AI-Artifact Preflight

Load [publisher AI policies](references/publisher-ai-policies.md) and, when
submission is imminent, verify current venue/arXiv moderation rules online.

1. **Run the static scanner** (outputs leads, not clearance):
   ```bash
   python3 .claude/skills/submission-prep/scripts/ai_slop_preflight.py main.tex
   ```
2. **Audit every citation and reference.** Check every `\cite`, bibliography
   entry, DOI/arXiv ID, and theorem attribution against external primary
   records (never trust an AI-recalled citation). Confirm the cited source
   actually supports the local claim; substantiate or remove unverified
   "standard", "classical", "optimal", or "best known" assertions.
3. **Verify provenance.** Confirm every theorem, proof, computation, figure, and
   dataset traces to a durable derivation, cited source, script, or proof
   assistant rather than an AI transcript alone.
4. **Strip AI artifacts & framing bloat:**
   - Remove conversation residue, assistant phrasing, TODO/TBD markers, and
     agent-facing comments.
   - Replace undefined process/AI jargon (`proof spine`, `gate`, `pipeline`,
     `seamless`, `pivotal`, `delve`, etc.) with exact mathematics.
   - Delete defensive assurances (`all details are proved here`, `for
     completeness`, `not counted as a contribution`) and promotional framing
     (`important in its own right`, `reusable tool`, `merits emphasis`) in favor
     of explicit mathematical statements and sourced comparisons.
   - Introduce necessary notation directly (`We refer to ... as ...`) without
     apologetic commentary, or use `latex-research-reviewer` if full terminology
     cleanup is still needed.
5. **Prepare disclosure.** AI systems are never authors or cited authorities.
   Where AI use was substantive, draft a clear disclosure naming tools/models,
   tasks performed, affected material, and human/formal verification performed.
   Verify rendered PDF text (not `.tex` alone) to ensure macro expansions or
   comments leak no residue.

## Gate 2: Minimal Archive & Clean-Room Verification

Load [the submission checklist](references/submission-checklist.md) and confirm
current arXiv file, TeX engine, metadata, and abstract length rules online
before upload.

1. **Trace the authoritative source graph.** Identify the root `.tex`, compiler,
   included `.tex` files (`.fls` plus `\input`/`\include`), `.bib`/`.bbl`,
   figures, local styles/classes, and exact case-sensitive filenames.
2. **Build and inspect the repo PDF.** Compile with SyncTeX (`latexmk -pdf
   -synctex=1 main.tex`, using `nice` for heavy builds). Resolve errors,
   undefined references/citations, rerun warnings, and new overfull boxes.
   Inspect the rendered title page, abstract, equations, references, and final
   page; do not generate standing `.tex`-to-HTML builds.
3. **Build a minimal allowlisted archive.** Include only files required to
   compile (`.tex`, bib/required `.bbl`, local `.cls`/`.sty`/`.bst`, figures,
   essential data). Exclude ledgers, dashboards, literature caches, scratch
   scripts, `.git`, logs/aux/`.synctex.gz`, and the compiled paper PDF (unless
   genuinely used as an `\includegraphics` input). Emit a sorted manifest and
   SHA-256 checksum.
4. **Audit and clean-room compile:**
   ```bash
   python3 .claude/skills/submission-prep/scripts/audit_arxiv_bundle.py archive.tar.gz --root main.tex
   ```
   Extract the archive into a fresh temporary directory and compile using only
   the extracted files. Compare the clean-room PDF (page count, extracted text,
   visual pages) with the repository PDF; recreate and retest the archive after
   every source edit.
5. **Prepare metadata & hand off author attestations.** Record exact title,
   author order, abstract checked against arXiv's current character limit,
   comments (page/figure count without hype), proposed primary/cross-list
   categories, compiler, and license options (leave journal ref/DOI blank unless
   published). Require explicit human confirmation for authorship/consent,
   rights, category, license, disclosure wording, and the final preview PDF.

## Decision Standard

Report `blocking` / `revisions needed` / `ready` with exact citation audit status,
clean-build PDF check, archive checksum, and open author confirmations. Never
call a submission ready while any citation is unverified, conversation/AI residue
persists, required disclosure is missing, or the clean-room build fails.
