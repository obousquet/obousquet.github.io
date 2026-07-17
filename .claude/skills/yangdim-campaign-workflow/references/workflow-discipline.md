# Workflow and campaign discipline

Use this reference with `honest-conjecture-resolution` for long YangDim proof campaigns.  The goal is to keep mathematical state recoverable from repository artifacts, not from chat history.

## Source-of-truth roles

- `main.tex`: theorem-level results and polished exposition.
- `prescribed_dual_bridge_realization.tex`: self-contained active open-problem formulation and proof-route draft material.
- `drafts/`: route syntheses, finite certificates, and arguments not ready for the paper.
- `ledgers/`: active-only targets, reduced cruxes, blockers, and next actions.
- `scripts/`: diagnostics, verifiers, and regression checks.
- `EXPLORATION_INVENTORY.md`: navigation map.
- Skills: reusable methodology and stable project memory, not route diaries.

## Clean-ledger invariant

Every active ledger should begin with the current theorem/question, definitions, assumptions, route IDs, status labels, and the next one to three concrete actions.  Closed proofs are removed from the active list once promoted to `main.tex`, `prescribed_dual_bridge_realization.tex`, or a stable side draft.  Historical chronology stays in git unless it records a reusable obstruction or counterexample.

## Evidence and promotion

- Any durable computational certificate needs a documented command in `scripts/`, a human-readable statement in a ledger or side draft, and an inventory entry.
- Do not silently promote finite evidence or subagent claims to `main.tex`.
- Promotion requires a proof-level statement, explicit hypotheses, dependency labels, and removal or demotion of the corresponding active-ledger debt.
- Once a lemma is proved in `main.tex`, mark supporting scripts as `regression`, `calibration`, or `verification` unless they remain part of a finite certificate.

## Proof/disproof alternation

Run counterexample search and proof development as a feedback loop, not as separate phases.

- A counterexample-search round should not end only with "no witness found."  Record what structure survived the search: a forced local pattern, a saturation phenomenon, a conserved label, a descent mechanism, or a common obstruction to constructing a bad example.  Turn that structure into a candidate lemma, proof-route branch, or sharper diagnostic.
- A proof-reduction round should not end only with a new crux.  Name the smallest configuration that could falsify the crux, the invariant such a counterexample would have to preserve, and the script, finite family, or hand-built near-miss that should be tested next.
- If proof branches keep multiplying without disproof pressure, pause branch expansion and attack the strongest new crux from the counterexample side.  If searches keep passing without yielding a structural lesson, stop widening the search and extract the mechanism behind the passes.
- Ledger updates should record both sides: `proof-facing lesson from search` and `disproof-facing diagnostic from proof`.  This keeps computations from becoming standalone scans and keeps proofs from becoming unchecked reduction treadmills.

## Subagent discipline

Use subagents only after the active target has been frozen in the ledger.  Split by route ID, not by duplicate brainstorming.  Each packet should state definitions, allowed artifacts, success/failure criteria, known false shortcuts, and required calibration language.  After they return, audit and merge by route ID before starting another batch: proved, refuted, computational only, reduced, stalled, or blocked.

## Pause and side-quest discipline

After several iterations without a new lemma, counterexample, verifier, or sharper reduction, stop and consolidate.  The pause note should name the current reduced target, what has actually been proved, what is finite/conditional, which routes are dead, and the next diagnostics that would change the status.  Do not push one proof corridor indefinitely; periodically run a bounded alternate-route packet from algebraic, topological/cubical, finite-certificate, or literature representations.

## Status synchronization

A status-changing result should be reflected in the same pass across the relevant sources of truth: theorem-level mathematics in `main.tex` or a side draft, live status in `ledgers/proof_route_topological_dictionary.md`, navigation in `EXPLORATION_INVENTORY.md`, and reusable verifier commands in scripts.  Chat-only conclusions are not project state.  When cleaning up, replace stale blocks rather than appending another chronological layer.

## Paper artifact rule

After a significant `main.tex` or `prescribed_dual_bridge_realization.tex` edit, compile with
SyncTeX enabled, regenerate the top-level PDF artifact, commit, and push the source plus generated
artifact.  Generated side PDFs from draft compiles should not be committed unless explicitly
requested.
