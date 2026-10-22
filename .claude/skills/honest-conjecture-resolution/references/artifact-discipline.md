# Artifact Discipline

Load this when updating ledgers, drafts, dashboards, inventories, generated outputs, or source-of-
truth records after a research round.

## Source-Of-Truth Roles

- **TeX / side draft:** durable definitions, examples, theorem statements, proofs, counterexamples,
  proof sketches, and compact warnings a reader should cite.
- **Ledger:** current exact target, proved inputs, active proof debt, parked routes, blockers,
  falsifier profiles, and next decisive moves.
- **Dashboard:** scan-level navigation for active/proved/refuted/parked route status with links to
  source artifacts.
- **Scripts:** reproducible diagnostics, verifiers, finite certificates, and regression checks.
- **Literature packets:** durable source conversions, extraction metadata, and compact key-result
  files for papers that influence route status, terminology, or proof inputs.
- **Inventory:** where artifacts live and what role/status they have.
- **Skills:** reusable process lessons only, not campaign chronology or local route names.

## Ledger Rules

- Start with the current target and proof-debt table before history.
- Update by replacement, not sedimentation; avoid stacked “Update/Earlier/Now” layers.
- Remove closed material from active-open lists.
- Record false shortcuts once: false claim, witness/mechanism, replacement rule.
- Prefer named debts and success/failure criteria over “continue” or “needs work.”
- Chat is not storage; write status-changing claims to ledger or draft before relying on them.
- Keep a compact searchable map of reusable results and failed mechanisms in the existing ledger
  or inventory, with statements/aliases, current status, originating proof locations, and links to
  relevant related-repo results. Preserve it through consolidation and handoffs; see
  `existing-results.md`. An archive entry stays discoverable even after leaving the active tree.

## Draft / TeX Rules

- Preserve sufficient reasoning and evidence to audit a result. A scratch attempt needs a compact
  record; a verified reusable result may need a research note; the curated manuscript needs selected
  results that serve its argument or an explicitly chosen standalone contribution.
- Mathematical correctness does not automatically justify manuscript promotion. Explain the
  result's role before expanding the paper. Keep a full proof available when relying on a result,
  even when it is not promoted to the main narrative.
- A coherent general theory can warrant its own active branch and full journal paper while the
  initiating conjecture remains open. Give the paper its own central question, general statements,
  substantive proofs, examples, and relation to existing literature. Its independent mathematical
  contribution can justify promotion without a known implication back to the conjecture. Use the
  appropriate research-writing and review skills; preserve the original conjecture's separate status.
- Consolidate research notes into readable mathematics at a meaningful milestone, or when the user
  requests a writeup. A route status change alone need not trigger a new manuscript section.
- Start with definitions, notation, standing hypotheses, and target statement.
- When promoting material, use `Definition`, `Lemma`, `Proposition`, `Conjecture`, `Question`,
  `Example`, `Counterexample`, or `Remark` as appropriate, with status labels.
- For a failed route, record the precise claim, verified witness, and failure mechanism. Develop a
  full expository section only if its significance warrants one; minimization is not mandatory.
- Move raw logs, tables, and scratch scripts out of the narrative; cite the stable script or
  inventory entry.
- Add dependency maps: “Target follows from A+B; A proved; B reduces to C; D refuted by W.”

## Dashboard Rules

Use the `conjecture-dashboard` skill for format and rendering details.

- The authored manifest (`dashboard.json` or another `*dashboard*.json`) is the route-tree source of
  truth for the dashboard.
- Update the manifest when a displayed route status or claim changes. A local record update that
  does not alter the dashboard's claims does not require rewriting its summaries.
- Show theorem-level routes and smallest active cruxes; avoid local atom clutter.
- Link every node to the relevant ledger, draft, script, or theorem.
- Active/proved/refuted/stalled/parked status should be visible at a glance.
- If the dashboard grows without reducing uncertainty, consolidate before adding leaves.

## Inventory And Script Sync

- Maintain a root inventory such as `EXPLORATION_INVENTORY.md` when a repo has many route artifacts.
- Track durable literature packets in the inventory when a paper contributes a proof input, route
  obstruction, terminology choice, or exact comparison theorem.
- A certificate used as evidence needs a reproducible command and a human-readable statement of
  exactly what was checked. Index reusable evidence at consolidation; exploratory scratch output
  does not need an inventory row for every attempt.
- When a script becomes evidence, label it as active diagnostic, verifier, regression check, finite
  certificate, or historical scratch.
- Preserve runnable entry points when moving scripts.

## Literature Artifact Rules

Use `shared-literature` to locate and search the common library before close reading.
Reuse or reserve `<library>/<domain>/<citation-key>/`; do not create a separate project cache.
A useful packet contains:

- `metadata.json` with citation, source URL/DOI/arXiv ID, access date, extraction command, and
  license/repo-policy note when relevant.
- `source.txt` converted from arXiv TeX, official HTML, or PDF text extraction.
- `source.tex`, `source-html.html`, or a PDF checksum/URL when useful for provenance.
- `key-results.md` listing the theorem/lemma/proposition statements that matter, with exact
  paper numbering, hypotheses, conclusion, location, notation translation, and route relevance.

Prefer arXiv source TeX or official HTML over PDF text when they preserve theorem structure. Do not
re-download or reconvert a paper if an adequate packet already exists. If a paper changes a route
status, cite the `key-results.md` entry from the ledger/dashboard rather than leaving the result only
in chat.

When packets change, run `python3 scripts/research_library.py index` and
`python3 scripts/render_literature_index.py` against the configured shared library.
Commit packet changes and indexes in the library's owning repository; links in
project views do not stage their targets. Link the shared index or packet from the
relevant dashboard. Keep project-specific interpretation separate from reusable results.

## Update Only The Affected Records

Keep one authoritative current-state record and link to it. Avoid copying the same detailed update
into multiple ledgers, route notes, and dashboard nodes. Derived summaries must remain accurate, but
need not mention every new local lemma. Batch archival indexing and presentation work at milestones;
record changed mathematical claims, invalidated evidence, and active status promptly.

Before:

- ensure ledger opens with current target, definitions, current crux, and statuses;
- if the map is stale, clean it before new mathematics.

During:

- keep scratch computations in scripts or temporary notes;
- record only reusable mechanisms, counterexamples, finite certificates, and named reductions.

After proof:

- preserve the proof and decide whether it merits manuscript promotion;
- update the authoritative ledger and any views whose claims changed;
- demote scripts to verifier/regression if appropriate;
- remove closed active debt.

After failure:

- record a verified witness, failed claim, and mechanism once;
- stop reopening the exact route unless new evidence changes the claim.

After plateau:

- freeze current state and choose consolidation, subagent packet, located literature search,
  adversarial diagnostic, or side-route assay.

## Generated Outputs

- For key `.tex` files, periodically generate PDF artifacts only.
- Compile LaTeX with SyncTeX enabled, for example `latexmk -pdf -synctex=1 main.tex`, so PDF
  review annotations can later be mapped back to source lines. Treat `.synctex.gz` as a local build
  artifact unless explicitly asked to preserve or share it.
- Do not generate HTML from `.tex` files as a standing artifact; these builds are slow and brittle
  in the current research repos.
- When committing/pushing source changes is authorized and generated PDF artifacts are tracked,
  include the corresponding PDFs. Artifact upkeep does not independently authorize publication.
- Keep dashboard HTML generated from the manifest and committed with it when the dashboard is part
  of repo state. Regenerate it whenever `dashboard.json` or another `*dashboard*.json` manifest
  changes.
