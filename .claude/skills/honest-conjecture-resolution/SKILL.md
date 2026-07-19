---
name: honest-conjecture-resolution
description: >-
  Drive a hard mathematical conjecture toward resolution across competing proof
  routes while staying epistemically honest: test the right adversaries,
  distinguish false claims from lossy tools, reduce to named crux lemmas,
  calibrate evidence, avoid route proliferation, and keep ledgers/drafts/
  dashboards synchronized. Use for multi-round open-problem campaigns,
  plateau audits, proof/disproof alternation, side-route decisions, subagent
  packet design, and converting route state into readable mathematical drafts.
  Load targeted references only when needed.
---

# Honest Conjecture Resolution

This is the orchestration layer for hard conjecture campaigns. It is not the script-writing layer
(`conjecture-explorer`) and not the final proof-writing layer (`proof-developer`). Its job is to keep
the proof state honest, small, falsifiable, and synchronized while several routes compete.

## Load References On Demand

Use this main file for every campaign round. Load only the relevant reference file when the task
needs detail:

- `references/adversaries-and-proxies.md`: adversary design, proxy failures, assembly traps, exact
  dual targets, and compute hygiene.
- `references/state-compression.md`: proof-contract accounting, plateau gates, route walkback,
  consolidation, side quests, and subagent discipline.
- `references/artifact-discipline.md`: ledgers, side drafts, dashboards, inventories, generated
  outputs, and source-of-truth synchronization.
- `references/full-playbook.md`: archival full pre-compression playbook. Read only if a needed
  historical lesson is missing from the distilled references.

## When To Use

- A conjecture has several candidate routes, live subclaims, or possible counterexample families.
- A route looks numerically robust but lacks a proof.
- A bound or proxy is growing and you need to decide whether the target is false or the tool is lossy.
- The campaign is plateauing, looping through reductions, or expanding the dashboard without closing
  proof debt.
- Subagents or side quests may help, but only if their contracts are precise and mergeable.
- The ledger has become chronological clutter and needs conversion into a current-state proof map.

## Cardinal Rules

1. **Lossy bound does not mean false target.** Measure the actual target and the proxy separately.
   A proxy can grow while the theorem remains true.
2. **Numerical robustness is not proof.** Robust tests count only against the right adversaries and
   should be paired with a proved analytic core or a precise reduced lemma.
3. **A counterexample is a result.** Record the witness, failed claim, mechanism, and smallest known
   instance. Then stop reopening that exact route.
4. **Every active claim needs a status.** Use `proved`, `reduced`, `conditional`, `verified
   computationally`, `plausible`, `stalled`, or `refuted`. Avoid “morally” or “essentially” proved.
5. **Proof and disproof alternate.** A proof reduction must name the smallest falsifier profile; a
   failed counterexample search must name the structure it failed to realize.
6. **Progress shrinks state.** A round that adds definitions, leaves, pages, or terminology without
   proving/refuting/merging/parking debt is probably negative progress.
7. **Methods must change the proof contract.** Alon-style imports, Grothendieck-style abstractions,
   literature searches, computations, and subagent batches are active only if they return a native
   lemma, theorem citation, counterexample, exact reformulation, proxy kill, diagnostic, or blindness
   statement.
8. **Consolidation is mathematical work.** It should reduce active leaves, expose the current crux,
   remove closed debt, and install a gate that prevents the same clutter from returning.

## Minimal Campaign-State Invariant

Before another serious round, the active ledger opening should answer:

```text
Current exact target:
Last equivalent reduction:
Current smallest falsifier profile:
Proved inputs being reused:
Active proof-debt rows:
Parked routes and why:
Next decisive move:
What will be deleted/merged if the move succeeds or fails:
```

If this does not fit in one screen, consolidate before proving more lemmas.

## Round Contract

Use a before/after packet for every significant round:

```text
Before:
Exact target:
Current crux:
Smallest falsifier profile:
Rows allowed to change this round:
Artifacts allowed to change this round:

After:
Proof-contract delta:
Rows proved/refuted/merged/parked:
State deleted:
New smallest falsifier profile:
Next decisive move:
```

Valid deltas are: proved row, refuted row, equivalent reformulation, sharper falsifier, imported
theorem, proxy killed, leaves merged, route parked, or explicit blindness statement. If no delta
exists, record at most one compact diagnostic and do not expand the dashboard, ledger, or proof
spine.

## Proof-Debt Table

For each active theorem-level target, maintain rows like:

```text
Claim:
Direction needed: equivalent / necessary / sufficient / special-case / heuristic
Status: proved / refuted / reduced / computational / plausible / stalled / open
Evidence:
Missing implication:
Smallest falsifier profile:
Next decisive test:
```

Most rabbit holes start when a sufficient condition is refined as if it were equivalent. Track the
direction on every arrow.

## Core Operating Loop

1. State the exact target and last equivalent reduction.
2. Identify the current smallest crux and its falsifier profile.
3. Choose one mode: proof attempt, adversarial diagnostic, exact literature match, side-method assay,
   subagent batch, or consolidation.
4. Run the round with bounded scope and compute hygiene.
5. Merge by proof-contract delta: prove, refute, merge, park, demote, or sharpen.
6. Update the source-of-truth artifacts in the same pass: TeX/side draft, ledger, dashboard,
   inventory/scripts, and durable literature packets where relevant.

## Mode Selection

- **Need to test a lemma or search for witnesses:** use `conjecture-explorer`; read
  `references/adversaries-and-proxies.md` for adversary patterns.
- **Proxy or bound looks wrong:** read `references/adversaries-and-proxies.md`; measure proxy and
  target separately.
- **Dashboard/ledger is growing faster than theorem progress:** read `references/state-compression.md`.
- **Need subagents:** read `references/state-compression.md` and spawn only from orthogonal evidence
  contracts.
- **Need an exact literature match or theorem import:** use the `literature-reviewer` skill and
  `references/artifact-discipline.md`; store downloaded, converted, or extracted sources under
  `literature/<citation-key>/`, write precise reusable statements in `key-results.md`, refresh the
  literature index when present, and link route-relevant results from the ledger/dashboard.
- **Need to clean route records or write a readable synthesis:** read
  `references/artifact-discipline.md`.
- **Need dashboard format/rendering details:** use the `conjecture-dashboard` skill.

## Compute Hygiene On EC2

The EC2 instance also serves the research site and may host other work.

- Start small, estimate memory/CPU growth, and scale gradually.
- Prefer `nice -n 10 uv run python ...` for heavy diagnostics.
- Limit worker counts; do not launch several all-core or high-memory jobs at once.
- Use timeouts, sample limits, chunking, checkpointing, or symmetry reduction.
- Stop jobs that start swapping, peg all cores for too long, or threaten server responsiveness.

## Exit Criteria

A round is closed only after one of these is true:

- `promote`: a proof or stable statement moves to TeX/side draft.
- `continue on named crux`: exactly one next proof-debt row is active.
- `spawn next packet`: subagent routes are orthogonal and have success/failure criteria.
- `park/stall`: the blocker is precise and the route is not active.
- `refuted`: the witness/mechanism is recorded and the route is closed.

Do not end a round with “continue” as the status.
