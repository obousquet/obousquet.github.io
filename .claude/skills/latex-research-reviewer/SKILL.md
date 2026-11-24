---
name: latex-research-reviewer
description: >-
  Comprehensive expert peer review, focused terminology/jargon auditing, and
  conservative Skim-annotation editing for mathematical and ML LaTeX papers.
  Checks mathematical correctness, conventions, compressed calculations,
  imported-theorem contracts, jargon/terminology precision, structural
  navigability, citation support, provenance, and rendered SyncTeX PDF quality.
---

# LaTeX Research Paper Reviewer

Deliver thorough expert referee reviews, focused terminology audits, or
review-and-implement revision passes for single papers or companion series.

## Step 1: Parse In True Reading Order

1. Read the root `.tex` file and every `\input`/`\include` in reading order.
2. If a compiled PDF exists, map sections to rendered pages (and if given a
   `scripts/skim_notes_to_review.py` file, treat each SyncTeX-mapped note as an
   explicit edit item: verify PDF quote against TeX source, edit conservatively,
   and flag stale/ambiguous annotations instead of guessing).
3. For companion-paper series, build a 1-page dependency/handoff map across parts
   first and verify consistent notation, terminology, and non-duplication.

## Step 2: Technical, Structural & Presentation Checks

### Mathematical Rigor & Imported Contracts
- Verify theorem statements, quantifier order, edge cases (empty set/complex,
  zero denominators, indexing/grading shifts), and logical completeness of every
  proof branch.
- Reconstruct compressed calculations (indexing, truncations, parity, sums).
- Audit **imported-theorem contracts**: verify exact hypotheses, conventions,
  and theorem numbers against primary sources via `literature-research`; never
  hide hypothesis translations under "by standard results."
- **Novelty & provenance calibration:** distinguish new theorems, new proofs of
  known results, translations/dictionaries, syntheses, and corollaries; match
  verbs (`prove`, `deduce`, `translate`, `assemble`, `recall`) to evidence.

### Terminology & Jargon Audit
Run this systematically across abstracts, intros, tables, headings, and proofs
(both `.tex` source and extracted PDF text):
- Enforce **first-use & definition adequacy**: no undefined symbols or acronyms
  in abstracts/intro/tables; pair informal glosses with exact formulas, domains,
  and normalizations matching the later proof.
- Flag **AI-like / internal campaign jargon** (`proof spine`, `pipeline`, `gate`,
  `assay`, `proof debt`, `package`, generic `mechanism`/`obstruction`/`sector`)
  unless formally standard and defined; replace with concrete math (`reduction`,
  `induction step`, `remaining lemma`).
- **Classify recurring technical labels:** (1) *standard & exact* (keep; gloss if
  cross-field), (2) *ordinary English* (keep), (3) *nonstandard shorthand*
  (replace with standard term or explicit data), (4) *overloaded false friend*
  (e.g., `slice`, `locus`, `endpoint`, `transport`, `lift`, `fiber`, `profile`,
  `scale`, `regime` used outside standard meaning—fix immediately), (5)
  *justified new term* (define formally without apologetic phrasing). Apply the
  **data-vs-name test**: if deleting a coined label and stating its short
  property list loses zero information, delete the label.

### Structural Navigability & Simplification Handoff
- Flag long flat walls of theorems lacking `\subsection` signposting, and check
  that the table of contents reflects conceptual structure.
- Flag linear chains of one-use lemmas ("would anyone cite this standalone?");
  recommend collapsing them into named proof steps (`ledger-to-journal-writeup`).
- When a valid proof carries over-engineered machinery, avoidable case splits,
  leaked proof-internal lemma interfaces, or tangled constants, recommend
  `proof-simplification`. Keep `\label` keys safe when moving text and verify
  before/after cross-reference integrity.

### Rendered Presentation
- Compile with SyncTeX (`latexmk -pdf -synctex=1 main.tex`), scan logs for
  undefined citations/references, multiply defined labels, and overfull boxes,
  and inspect materially changed PDF pages visually (orphaned headings, table
  overflow, bad breaks, caption separation). Treat incomplete sections
  constructively with concrete completion suggestions.

## Step 3: Deliverable Mode

- **Review only:** return concise Overall Summary, Issues Fixed/To Fix grouped
  by Mathematical (`critical`/`major`/`minor` with location + fix), Clarity/
  Terminology, Structure, Citations, plus General Suggestions and Line Comments.
- **Review and implement / focused jargon or Skim pass:** fix well-supported
  issues directly, rebuild with SyncTeX, inspect rendered changes and diff, and
  summarize edits, validation, and any items left for author judgment.
