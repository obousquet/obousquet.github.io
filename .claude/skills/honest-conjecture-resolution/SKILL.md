---
name: honest-conjecture-resolution
description: >-
  Main driver for mathematical research campaigns: coordinate proof,
  computation, method import, theory-building, literature, and writing skills.
  Drive open problems or sustained theory across competing routes while staying
  epistemically honest: test right adversaries, separate lossy tools from false
  targets, break micro-case plateaus, prune subsumed results, and keep ledgers,
  drafts, and dashboards synchronized. Load references on demand.
---

# Honest Conjecture Resolution

Main driver for mathematical campaigns. It owns objective selection, mode,
assignments, route reviews, subsumption/pruning, and authoritative campaign
state. Specialists return evidence and open obligations to the same state; do
not create competing ledgers. Standalone tasks need no campaign machinery.

## Focused References (Load On Demand)

- `references/skill-routing.md`: specialist map and write/review/publish routes.
- `references/swarm-coordination.md`: Antigravity `/swarm` discipline, briefs,
  five seat roles, authority separation, typed dispositions, and gates.
- `references/state-compression.md`: progress accounting, route review,
  anti-micro-case circuit breaker, checkpoint pruning, proxy/pivot checks.
- `references/reporting-and-artifacts.md`: self-contained round summaries, public
  dashboard links, ledger/TeX/dashboard ownership, and SyncTeX build sync.

## Cardinal Rules

1. **Lossy bound does not mean false target.** Measure target and proxy separately.
2. **Numerical robustness is not proof.** Pair tests against real adversaries
   with an analytic core or exact reduced lemma.
3. **Every counterexample has a scope.** Verify hypotheses and record which live
   decision changes; never minimize a witness without affecting the goal.
4. **Separate claim status, verification, review, and barriers.** Use `proved`,
   `reduced`, `conditional`, `verified computationally`, `plausible`, `stalled`,
   or `refuted`. Keep `lean_checked`/`script_verified`/`author_proof` distinct
   from independent faithfulness (`not_faithful` when statement misses intent)
   and `proved_barrier` vs. `working_judgment`.
5. **Test the vulnerable indispensable step early.** Work backward from the
   conclusion; distinguish constructing a witness from admissible inputs vs.
   proving joint input existence.
6. **Separate conjecture advance from reusable theory.** A coherent theory can
   be a major achievement before its return to the target is known; keep the
   initiating conjecture's status honest and separate.
7. **Give exploration room, then select.** Bounded creative discovery needs no
   theorem every turn; continued investment needs either a credible route to the
   conjecture or worthwhile theory within scope.
8. **Enumeration needs a decision.** Complete finite coverage when requested or
   closing a proved finite reduction; otherwise state what hypothesis a search
   distinguishes. Never extend a structural census merely because small $n$
   passed.
9. **Preserve native structure.** Before adopting a proxy or generic import,
   audit what data (signs, colors, paired layers, labels, compatibility) it
   forgets.
10. **Control overhead and prune.** Sync views only when displayed claims
    change; subsume superseded lemmas at checkpoints rather than accumulating
    clutter.

## Check Existing Results First

At campaign start/resume or before a substantial new route:

1. Use `research-knowledge` (`sync`, `context --campaign . --task '...'`,
   `search`) to recover campaign/sibling cards, corrections, and failures.
2. Search shared literature via `literature-research` before web searches.
3. If the index or `../ResearchWork` is unavailable or outside a single-repo
   sandbox, fall back cleanly to targeted `grep -rn -i` (or `rg` when installed)
   over campaign `.md`/`.tex`/`*dashboard*.json` files and record the coverage
   limit—never loop on failing index commands or build a local cache substitute.
4. Inspect original proofs/witnesses before reusing claims. Compare new results
   with the closest existing statement and record the exact addition.

## Minimal Campaign-State Invariant & Round Contract

Keep one compact opening in the active ledger answering: current exact target
and completion standard; selected mode/skills; last target advance & remaining
obligations; active theory advance (if separate); current route & proved inputs;
closest prior results; first unproved indispensable implication; effort spent
since route review; parked mechanisms and reopening criteria.

Track active targets in a compact debt row (`Claim`, `Relation`
[equivalent/necessary/sufficient/special-case/independent theory/heuristic],
`Status`, `Evidence`, `Missing implication`, `Smallest falsifier`, `Next test`).
Default review trigger for direct proof/search routes: every **4 substantive
attempts** (across names, turns, and workers; sooner on failure), or after **2
consecutive micro-case waves** (see `references/state-compression.md`). Theory
programmes use cumulative milestones instead of fixed attempt limits.

Close every round using [reporting-and-artifacts.md](references/reporting-and-artifacts.md):
self-contained mathematical prose (objects, question, what changed, remaining
gap, explicit assumptions/coverage) before links, plus the campaign's public
HTTPS dashboard link when configured.

## Core Operating Loop & Mode Selection

1. Clarify objective (target resolution vs. standalone theory) and current mode.
2. Compare 2–3 genuinely different approaches by payoff, evidence, hardest step,
   and cheapest discriminating test (skip repeating this on routine steps).
3. Select the smallest needed specialist set from `references/skill-routing.md`:
   - `proof-developer` (prove a selected claim) or `conjecture-explorer`
     (adversary/witness/finite checks);
   - `alon-method` (one-way import via mathematical dictionary);
   - `theory-building` (closures/world-building, generative calculi,
     representation refinement, new settings/correspondences);
   - `proof-exegesis` (interpret an opaque proof) or `proof-simplification`
     (shorten/streamline a valid proof);
   - `concentration-inequalities` (moment/tail bounds & loss audits);
   - `lean4-formalization` (formal verification only after thinker +
     faithfulness gates);
   - `literature-research` (local-first packets + primary verification);
   - `submission-prep` (scholarly preflight + arXiv clean-room bundling).
4. Execute with compute hygiene; assign independent `/swarm` or subagent work
   only when authorized under `references/swarm-coordination.md`.
5. Record proved results, refutations, or subsumptions; run route review when
   triggered; prune superseded material and synchronize ledger, TeX, PDF
   (SyncTeX), and dashboard at checkpoints.

## Compute Hygiene On EC2

The host serves the research site and may run parallel workers concurrently.

- Check `MemAvailable` in `/proc/meminfo` before nontrivial runs and never rely on
  swap. Divide the 75% ceiling across active concurrent workers (`N_workers`):
  ```bash
  mem_cap=$(awk -v n="${N_WORKERS:-1}" '/MemAvailable:/ {printf "%.0f\n", $2 * 1024 * 0.75 / n}' /proc/meminfo)
  nice -n 10 prlimit --as="$mem_cap" --cpu=3600 -- python3 scripts/explore_foo.py ...
  ```
- Start with small parameter bounds; use timeouts, chunking, checkpointing, and
  capped worker thread counts. Stop immediately if a job swaps or threatens
  host responsiveness.
