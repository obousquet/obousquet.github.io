# Readable Campaign Reporting And Artifact Discipline

Use this reference for round summaries, dashboard overviews, and synchronizing
ledgers, drafts, scripts, literature packets, and PDF builds.

## Source-Of-Truth Roles

- **TeX / side draft:** durable definitions, examples, theorems, proofs, and
  counterexamples.
- **Ledger:** active target, debt table, parked mechanisms with reopening rules,
  and next decisive tests. Update by replacement, never append-only `Update/Now`
  sedimentation; remove closed debt from open lists.
- **Dashboard (`*dashboard*.json` -> HTML):** theorem/crux-level navigation view;
  link to authoritative proofs rather than duplicating the ledger.
- **Scripts:** reproducible verifiers/diagnostics (label role: verifier vs.
  scratch; preserve entry points).
- **Literature packets:** canonical shared packets via `literature-research`
  plus internal packets via `research-knowledge`.
- **Skills:** generic reusable methods only—no project names or campaign state.

## Self-Contained Round Reports & Dashboard Overviews

Every round summary and dashboard executive overview (`goal`, `honest_assessment`,
`latest_progress`) must be intelligible to a mathematician who has not read
earlier rounds:

1. **Explain the math before naming it.** State the objects, question, and
   essential hypotheses plainly first; define campaign-specific symbols/terms at
   first use or replace private process labels (`gate`, `package`, `odometer`)
   with their mathematical meaning.
2. **State what changed and its limits.** Distinguish proof, conditional
   reduction, finite computation (exact range/exhaustive vs. sampled), and
   refutation. If the main problem did not advance, say so cleanly; explain
   independent theory value on its own merits.
3. **Put prose before links.** Links verify provenance; readers should grasp the
   result and remaining gap without opening another file.
4. **Link the public dashboard.** Include a descriptive HTTPS link (e.g.
   `[Campaign dashboard](https://...)`) resolved from the site's inventory or
   deployment config (never guessed or replaced by a `file://` path when a
   public URL is configured; state clearly if local updates are not yet
   published).

*Contrast — opaque:* "R18 closes the forest gate; C3 kills extension package."  
*Readable:* "We ask which finite graphs are 2-colorable. Beyond paths, we
proved every acyclic graph is 2-colorable (2-coloring each component by distance
parity from a root), while a triangle needs 3 colors; the open question is
whether excluding all odd cycles characterizes 2-colorability [proof link]."

## Consolidation, Subsumption & Hygiene

- Rewrite summaries in place and replace superseded results rather than stacking
  round-by-round history.
- When a general theorem subsumes special cases, prune or archive the old leaves
  (retaining aliases in the ledger's result map so nothing is rediscovered) and
  strip per-iteration chronological tallies from dashboards and writeups.
- Keep research artifacts and builds synchronized only when claims change:
  - Compile key `.tex` files with SyncTeX (`latexmk -pdf -synctex=1 main.tex`),
    keeping `.synctex.gz` untracked; do **not** generate standing `.tex`-to-HTML
    pages.
  - Regenerate `dashboard.html` whenever `*dashboard*.json` changes; check
    integrity with `render_conjecture_dashboard.py --check`.
  - When committing and pushing checkpoints, include updated tracked PDFs and
    regenerated dashboard HTML together with the source edits. Commit shared
    literature packets and index updates in the library's owning repository.
