# Swarm Coordination And Antigravity Execution

Load this before launching `/swarm` or multiple subagents on a campaign. Extends
[state-compression.md](state-compression.md) and
[reporting-and-artifacts.md](reporting-and-artifacts.md).

## Single Authoritative State

- All workers share the campaign's existing ledger, `dashboard.json`,
  manuscripts, and `research_knowledge` records. Never create per-worker
  ledgers or private status files.
- Workers return concise findings, reproducible artifacts, and one typed
  disposition to the coordinator, who updates the authoritative state once.

## Antigravity Swarm Execution Discipline

1. **Know when NOT to swarm.** Run solo (or at most 1 helper) for tightly coupled
   sequential proofs, final proof polishing (`proof-simplification`), single-file
   editing, or when recent waves have fragmented. Use `/swarm` when fronts are
   genuinely decoupled (e.g., main proof vs. red-team falsification vs.
   literature/computation).
2. **Self-contained worker briefs.** Workers almost never open repo `SKILL.md`
   files on their own—inline everything needed in the `swarm add` brief:
   - exact target, allowed assumptions, and source file links;
   - workspace mode: `workspace:"share"` whenever a worker creates or edits files
     or runs scripts that write outputs; keep `inherit` only for strictly
     read-only auditors/reviewers;
   - per-worker compute cap: `nice -n 10`, `python3` (not `uv`), and
     `prlimit --as` ≤ `0.75 * MemAvailable / N_workers`;
   - stop rule (no micro-case grinding; exit after named obstruction or budget)
     and exact typed return contract.
3. **Zero `manage_task` polling loops.** When launching background scripts,
   always set `NotificationTimeoutSeconds` and end the turn to wake reactively.
   Never call `manage_task(Action="status")` in a loop.
4. **No silent `swarm_wait` deadlocks.** Instruct every worker to `@coordinator`
   when finished, blocked, or parking. When the coordinator calls `swarm_wait`,
   also arm a bounded `schedule` check-in timer so the coordinator checks
   `swarm status`, nudges idle workers, or cancels stalled tracks cleanly.

## Five Standard Campaign Roles

Assign workers by **distinct epistemic function**, never redundant guessing:

| Role ("Seat") | Mandate | Required output |
|---|---|---|
| **Front Owner** | Advances one decoupled front in bounded steps. | Typed disposition, 1-line finding, artifact links |
| **Red Team / Faithfulness Auditor** | Audits definitions/statements for vacuity or quantifier drift *before* proof work; hunts counterexamples against active cruxes. | Verified counterexample witness OR `not_faithful` ruling with exact mismatch |
| **Obstruction / Barrier Desk** | Maintains `barriers` registry; screens proposals against known impossibility/proxy walls. | `proved_barrier` or `working_judgment` ruling naming the wall |
| **Strategy / Critical-Path Owner** | Maintains ranked `critical_path` & single `hard_link`, runs route reviews, stops micro-case inflation. | Bottleneck rank, pivot decision, or subsumption/consolidation patch |
| **Independent Editor / Reviewer** | Audits round summaries, dashboard overviews, and claims against proofs (`author != reviewer`). | Approval or explicit `corrections` entry |

## Authority Separation & Typed Dispositions

Keep three dashboard axes distinct: (1) `verification` (`unverified`,
`author_proof`, `script_verified`, `lean_checked`), (2) `review` (`unreviewed`,
`independent_audit`, `human_reviewed`, `not_faithful`, `judgment`), and
(3) `authority` (`proved_barrier` vs. `working_judgment`). A `lean_checked`
vacuous claim must be marked `not_faithful`, never solved.

Every delegated task terminates with one typed disposition: `proved`, `refuted`,
`reduced`, `exhausted` (script path, exact range, SHA-256),
`hypothesis_too_weak`, `missing_lemma`, `statement_seems_false`,
`vacuous_or_misstated`, `does_not_elaborate`, or `out_of_budget`.

## Reduction, Twin, Formalization & Cancellation Gates

- **Non-trivial reduction gate:** splitting $S$ into $A_1 \land \dots \land A_k \Rightarrow S$
  must verify the implication first, reject sterile "$H$ holds vs. $\neg H$"
  splits unless one side closes, and make every $A_i$ structurally distinct;
  credit vests only when essential children close.
- **Crux-only negated twins:** pair only the **1–3 active `hard_link` cruxes**
  with explicit $\neg P$ red-team targets; never auto-generate micro-lemma twins.
- **Thinker -> Builder formalization gate:** (1) paper + `literature-research`/
  `conjecture-explorer` check, (2) non-author faithfulness check, (3) only then
  heavy `lean4-formalization` compute.
- **Staggered concurrency & prompt cancellation:** start one mechanism owner on a
  hard claim before adding a second *different* mechanism; cancel or reallocate
  obsolete workers immediately when a claim closes, recording `death_cause` and
  `killed_by` in the ledger/graveyard.
