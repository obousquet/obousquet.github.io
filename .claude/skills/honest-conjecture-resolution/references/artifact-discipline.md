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
- **Inventory:** where artifacts live and what role/status they have.
- **Skills:** reusable process lessons only, not campaign chronology or local route names.

## Ledger Rules

- Start with the current target and proof-debt table before history.
- Update by replacement, not sedimentation; avoid stacked “Update/Earlier/Now” layers.
- Remove closed material from active-open lists.
- Record false shortcuts once: false claim, witness/mechanism, replacement rule.
- Prefer named debts and success/failure criteria over “continue” or “needs work.”
- Chat is not storage; write status-changing claims to ledger or draft before relying on them.

## Draft / TeX Rules

- Convert route ledgers into readable mathematics when the ledger becomes fragmented or after a
  route status changes.
- Start with definitions, notation, standing hypotheses, and target statement.
- Promote durable facts as `Definition`, `Lemma`, `Proposition`, `Conjecture`, `Question`,
  `Example`, `Counterexample`, or `Remark`, with status labels.
- Write killed routes as real mathematics: construction, failed claim, mechanism, growth rate or
  smallest witness.
- Move raw logs, tables, and scratch scripts out of the narrative; cite the stable script or
  inventory entry.
- Add dependency maps: “Target follows from A+B; A proved; B reduces to C; D refuted by W.”

## Dashboard Rules

Use the `conjecture-dashboard` skill for format and rendering details.

- The authored manifest (`dashboard.json` or another `*dashboard*.json`) is the route-tree source of
  truth for the dashboard.
- Update the manifest when ledger/TeX route status changes.
- Show theorem-level routes and smallest active cruxes; avoid local atom clutter.
- Link every node to the relevant ledger, draft, script, or theorem.
- Active/proved/refuted/stalled/parked status should be visible at a glance.
- If the dashboard grows without reducing uncertainty, consolidate before adding leaves.

## Inventory And Script Sync

- Maintain a root inventory such as `EXPLORATION_INVENTORY.md` when a repo has many route artifacts.
- Every reusable finite certificate or diagnostic should have three things: script command,
  human-readable statement/table, and inventory entry.
- When a script becomes evidence, label it as active diagnostic, verifier, regression check, finite
  certificate, or historical scratch.
- Preserve runnable entry points when moving scripts.

## Round Update Order

Before:

- ensure ledger opens with current target, definitions, current crux, and statuses;
- if the map is stale, clean it before new mathematics.

During:

- keep scratch computations in scripts or temporary notes;
- record only reusable mechanisms, counterexamples, finite certificates, and named reductions.

After proof:

- promote theorem-level material to TeX/side draft;
- update ledger and dashboard;
- demote scripts to verifier/regression if appropriate;
- remove closed active debt.

After failure:

- record smallest witness, failed claim, and mechanism once;
- stop reopening the exact route unless new evidence changes the claim.

After plateau:

- freeze current state and choose consolidation, subagent packet, located literature search,
  adversarial diagnostic, or side-route assay.

## Generated Outputs

- For key `.tex` files, periodically generate PDF artifacts only.
- Do not generate HTML from `.tex` files as a standing artifact; these builds are slow and brittle
  in the current research repos.
- When generated PDF artifacts are tracked, commit and push them with the source changes that
  produced them.
- Keep dashboard HTML generated from the manifest and committed with it when the dashboard is part
  of repo state. Regenerate it whenever `dashboard.json` or another `*dashboard*.json` manifest
  changes.
