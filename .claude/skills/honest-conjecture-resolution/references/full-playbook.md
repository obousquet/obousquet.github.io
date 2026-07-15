---
name: honest-conjecture-resolution
description: >-
  Drive a hard mathematical conjecture toward resolution across many competing
  proof routes while staying epistemically honest — testing computationally,
  distinguishing a lossy bound from a false claim, choosing adversarial test
  cases that actually reveal obstructions, reducing to crux lemmas without
  over-trusting them, documenting dead ends, and calibrating claims to evidence.
  Use this skill for the multi-week lifecycle of attacking an open problem: when
  you are juggling several candidate routes, deciding whether a route is alive or
  dead, converting route ledgers into readable mathematical drafts, stepping
  back after a plateau to broaden the search for proof angles, or at risk of
  declaring victory from numerics alone. Complements conjecture-explorer (which
  writes the test scripts), proof-developer (which writes a proof once the
  statement is sharp), literature-reviewer (which searches after the obstruction
  is named), and latex-paper-completer (which can polish a consolidated draft).
---

# Honest Conjecture Resolution

The meta-process of attacking a hard open problem over many iterations: forming routes, testing them
honestly, killing the dead ones with evidence, reducing live ones to crux lemmas, and never claiming
more than the evidence supports. This is the orchestration layer above "write a test script" and
"write a proof." It exists because the expensive failures in research are *epistemic*: trusting a
bound that was actually lossy, or a lemma that was only tested on benign cases.

## When to use

- You are running a long campaign on one conjecture with several candidate proof routes in flight.
- You need to decide whether a route is alive, dead, or merely stalled.
- You have a "numerically robust" lemma and are tempted to treat it as proved.
- You're writing up status and must phrase claims at the right confidence.
- A route ledger has become too chronological or fragmented, and needs to be converted into a
  structured mathematical note.
- The campaign is looping or plateauing, and you need to step back, find special cases, locate
  applications, search adjacent literature, or generate new proof vectors.

## The cardinal rules

1. **A numerical bound being lossy ≠ the claim being false.** Separate the *tool* from the *target*.
   When `bound / truth` grows, ask both: "is there an adversary making the target itself fail?" and
   "is the tool just loose — does the *actual* quantity stay bounded?" Measure the actual quantity,
   not only the bound. (A whole route was revived this way: McDiarmid allowed `sqrt(n)`, the truth
   didn't.)
2. **Numerical robustness is necessary, not sufficient.** A lemma can pass every test you wrote and
   still be false — because you tested the wrong family. Robustness counts only against the *right*
   adversaries, and ideally alongside a proved analytic core.
3. **Get an analytic foothold before trusting.** Prefer "proved `L_2` core + numerics for the
   remainder" over "numerics for everything." A route with a rigorously proved sub-case is in a
   different trust class than one resting on simulation alone.
4. **Calibrate language to evidence.** Use a fixed vocabulary: *proved* (rigorous, gap-free),
   *reduced to X* (conditional on a stated lemma), *robust numerically* (passes adversaries, no
   proof), *plausible*, *open*, *excluded* (disproved by a specific counterexample). Never let
   "robust numerically" drift into "essentially proved."
5. **A counterexample is a result.** Killing a route honestly is progress: it removes a direction and
   usually names the obstruction. Document it as carefully as a theorem.
6. **Alternate proof and disproof on purpose.** Do not let a campaign become only a counterexample
   search or only a proof grind. Each proof reduction should state the exact obstruction profile a
   counterexample must satisfy after the reduction; each disproof search should report the structural
   features it repeatedly fails to realize, because those failures are proof-side information. Use the
   loop "prove a restriction, search for a survivor, read the survivor or absence structurally, then
   refine the next lemma."
   A search packet is incomplete if it only says "no counterexample found"; it must also name the
   structural constraint suggested by the failed search. A proof packet is incomplete if it only adds a
   new lemma; it must also name the smallest survivor family that would refute or bypass that lemma.
   If the two outputs stop informing each other, pause and walk back the route before expanding the
   active leaf set.
7. **Progress must shrink the state, not only move it.** A round that creates three new definitions,
   two new branches, and no smaller exact crux has probably increased proof debt even if every step
   was mathematically sensible. Count progress by net compression: a theorem proved, a route refuted,
   a proxy demoted, a repeated obstruction named once, or several leaves collapsed to one sharper
   target. If the dashboard grows without a corresponding decrease in uncertainty, stop and
   consolidate before continuing.
8. **A method is useful only if it changes the proof contract.** A side route, imported technique,
   framework, or subagent batch should end by saying exactly what changed in the current theorem
   contract: an equivalence was found, a sufficient condition was demoted, a counterexample profile
   was sharpened, a lemma was proved, or a branch was retired. If the output is only new vocabulary,
   analogies, or more possible leaves, record it as background and do not keep it active.
9. **Consolidation is a research move, not clerical cleanup.** A consolidation pass should reduce
   the live state: fewer active leaves, clearer definitions, closed items removed from the open
   list, and one current crux visible from the ledger and dashboard. If a consolidation only makes a
   long historical note prettier while preserving the same ambiguity, it has not done its job.

## Operational lessons from repeated route churn

Use these rules when a campaign has produced many partial reductions, side routes, subagents, and
cleanup passes but the headline theorem still has not moved.

- **Treat repeated consolidation as a theorem-state alarm.** If the same branch repeatedly needs
  cleanup, the issue is usually not prose but a non-contracting proof state: too many active leaves,
  a proxy that is not known to be exact, inherited debt recorded as new debt, or side material kept
  at proof-spine fidelity. Before continuing, recover the last exact or equivalent statement and
  rebuild the frontier from there.
- **Force every round to declare a delta.** At the end of a round, write one sentence of the form:
  "This round changed the proof contract by ...". Valid completions are: proved a row, refuted a
  row, imported an exact theorem, found an equivalent reformulation, sharpened the smallest
  falsifier, killed a proxy, merged leaves, parked a branch, or produced a blindness statement. If
  none apply, do not expand the dashboard, ledger, proof note, or terminology.
- **Distinguish frontier work from framework work.** Frontier work attacks the current smallest
  obstruction directly. Framework work builds language or a companion theory. Both are useful, but a
  framework pass remains background unless it exports a native lemma, invariant, obstruction
  criterion, or theorem citation that changes a named proof-debt row.
- **Use page count and leaf count as quantitative diagnostics.** A long PDF or large dashboard is
  healthy only if most added pages/leaves are closed results. If the active crux is unchanged while
  pages, labels, or leaves grow, stop local refinement and choose one of: disprove the current crux,
  walk back to the last exact target, import a located theorem, or switch proof geometry.
- **Merge subagents by deletion, not anthology.** A subagent batch is successful only if the merge
  deletes, merges, proves, refutes, or relabels active debt. Reports that return overlapping
  vocabulary, adjacent cases, or plausible but unmerged ideas indicate a failed decomposition; the
  next move is consolidation, not another batch.
- **Keep proof spine, ledger, and archive at different fidelities.** The proof spine contains only
  durable definitions, examples, lemmas, proofs, and compact warnings. The ledger contains current
  target, exact reductions, proof debts, and parked routes. Chronological attempts and false starts
  belong to git history or a very short archive note, not the active state.
- **Alternate proof and disproof after every exact reduction.** A proof reduction should produce a
  smallest falsifier profile; a counterexample search should report the structural feature it failed
  to realize. If proof and disproof no longer feed each other, the route is probably refining a
  proxy rather than the original theorem.
- **End every methodological pause with one irreversible action.** The pause must delete a leaf,
  merge rows, park a route, demote a proxy, install a gate, or select one decisive next test. If the
  active tree is unchanged, the pause was reflection rather than state compression.

### Minimal campaign-state invariant

At all times, the active ledger opening should fit the following contract. If it cannot, consolidate
before doing more exploration.

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

Do not open a new route unless the final line has a concrete answer.

## Lean campaign operating protocol

Use this protocol after a campaign has already produced several false starts, side routes, subagent
batches, and consolidation passes.  Its purpose is to turn accumulated experience into faster
convergence rather than a larger archive.

### Round contract

Every active round should have a before/after contract.

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

- **One round, one contract.**  Do not mix frontier proof, exposition cleanup, side-route
  brainstorming, and dashboard restructuring unless the round explicitly says which proof-debt rows
  may change.
- **No delta, no expansion.**  If the after-state cannot name a proof-contract delta, do not add new
  leaves, terminology, proof-spine pages, or subagent packets.  Preserve at most one compact
  diagnostic or blindness statement.
- **Delete something before preserving something.**  A new definition, route, or note earns its
  place only if it deletes a stale row, merges siblings, replaces a proxy by an exact target, or
  records a durable theorem/counterexample.

### Active-state budget

Keep the live state small enough that a fresh reader can recover it without chat history.

- **Dashboard budget.**  The dashboard should expose theorem-level routes and the smallest active
  cruxes, not every local atom.  If it needs scrolling to understand what is active, merge or park
  leaves before continuing.
- **Ledger budget.**  The first ledger block should fit on one screen: definitions, proved inputs,
  active proof-debt rows, ruled-out shortcuts, and the next decisive move.  Historical chronology is
  archive material.
- **Proof-spine budget.**  TeX grows only for durable definitions, examples, lemmas, proofs, or
  compact warnings.  Repeated "same crux, more pages" is negative evidence for the current proof
  geometry.
- **Conditional-lemma wall gate.**  A long chain of individually correct conditional lemmas is not
  progress unless the theorem contract gets smaller.  Before adding another conditional lemma, write
  the current closure formula in the form "Target follows from rows A+B+C" and the reverse-dependency
  formula "This new lemma would close/delete/merge row X by mechanism Y." If the new lemma neither
  proves a row, deletes a row, merges rows, turns a sufficient proxy into an equivalent target, nor
  replaces the closure formula by a strictly shorter equivalent one, quarantine it outside the proof
  spine. Record at most one compact background sentence, and do not add a dashboard leaf for it.
- **Conditional-stack triage.**  When a proof route has more than three unproved conditional rows, do
  not add a fourth layer before triaging the stack.  Compress the route into a table with one row per
  unproved condition, and for each row record: exact statement, direction relative to the target
  (`equivalent`, `sufficient`, `necessary`, or `diagnostic`), why it is needed, smallest falsifier
  profile, available evidence, and what would close or kill it.  After triage, exactly one row may
  remain active; the others must be proved, merged, parked as background, or converted into explicit
  counterexample searches.  If no row can be selected as decisive, walk back to the last equivalent
  reduction instead of continuing local lemma production.
- **No hidden proof debt.**  A lemma whose proof assumes another local "regularity", "compatibility",
  "faithfulness", or "genericity" condition counts as conditional unless that condition is already a
  named proved input.  Do not bury these assumptions inside prose.  Promote them to proof-debt rows or
  remove the lemma from the proof spine.
- **One-screen theorem contract.**  The current theorem contract must remain readable in one screen:
  target, last exact reduction, proved inputs, active rows, smallest falsifier, and next decisive
  move.  If explaining the live proof state requires a dependency graph, the graph is already too
  large for frontier work; consolidate before proving more conditional lemmas.
- **Jargon budget.**  A local name is allowed only if it replaces repeated prose or supports a
  theorem statement.  If the branch keeps producing names, stop and look for an invariant, exact
  sequence, dual certificate, or counterexample template.

### Plateau response

After two consecutive zero-delta rounds, or after the same obstruction reappears under a third name,
do not do another local refinement.  Choose exactly one of:

- walk back to the last equivalent reduction and restart from that target;
- search for a counterexample satisfying the current smallest falsifier profile;
- import one located theorem or one bounded side route with a required native export;
- compress the branch into a proof-debt table and park it;
- change proof geometry by seeking an invariant, dual certificate, topological obstruction,
  algebraic encoding, or exactness statement.

### Subagent discipline

Parallelism helps only when the contracts are orthogonal.

- **Split by evidence type, not by enthusiasm.**  Good packets are proof attempt, counterexample
  search, finite diagnostic, literature match, and abstraction descent.  Bad packets ask several
  agents to elaborate the same taxonomy.
- **Merge by state change.**  The main agent must turn reports into proved/refuted/merged/parked
  rows.  If a batch returns overlapping vocabulary and no row changes, the failed object is the
  decomposition, not the theorem.
- **Do not spawn to postpone consolidation.**  If the active state is already too large, compress it
  before asking subagents to explore more.

### Source-of-truth separation

- **TeX is for durable mathematics.**  Definitions, examples, theorem statements, and proof details
  that a reader should cite belong in the paper or focused note.
- **Ledger is for current proof state.**  It should say what remains open and why, not narrate every
  attempt.
- **Dashboard is for navigation.**  It should make active/proved/parked status visually obvious and
  link to the source of truth.
- **Skills are for reusable process.**  Add only rules that change future behavior.  Do not store
  local route names or campaign-specific chronology in skills.

## Methodology retrospectives after long campaigns

When a campaign has gone through false routes, subagent batches, side quests, and repeated
re-consolidations, pause to improve the operating system before doing more mathematics. The output
should be a smaller active state and a sharper next move, not a postmortem.

### Retrospective protocol

- **Classify recent rounds by frontier delta.** For each round, record whether it produced a proof,
  counterexample, exact reformulation, smaller falsifier, killed proxy, imported theorem, diagnostic,
  background, or no movement. Only the first seven may change active state.
- **Check whether the campaign is remembering more than it is proving.** Long PDFs, verbose
  dashboards, many named local cases, and repeated cleanup requests are not merely exposition
  problems. Treat them as evidence that the proof state may be preserving chronology instead of
  converging. Before adding mathematics, identify which active rows can be deleted, merged, parked,
  or replaced by one invariant.
- **Audit the artifact delta before the mathematical delta.** If the paper draft, side note, ledger,
  dashboard, and scripts no longer tell the same story, the next mathematical move is likely to be
  based on stale state. First rewrite the smallest source-of-truth block so it states the current
  target, proved inputs, active debts, and parked routes without chronology.
- **Name at most three failure modes.** Common failures are stale state, hidden proxy, inherited debt
  duplicated as independent debt, sufficient condition treated as exact, side route without native
  descent, subagents with overlapping contracts, terminology accretion, and proof-spine page growth
  without proof-contract shrinkage.
- **Convert each failure into a gate.** A useful lesson changes allowed future moves: no new leaf
  without deleting or merging an old one, no side route without a native export, no subagent batch
  without orthogonal evidence contracts, no local refinement after two zero-delta rounds, and no
  proof-spine growth unless a proof-debt row changes status.
- **Separate symptom from cause.** Long PDFs, verbose dashboards, many active leaves, and repeated
  cleanup requests are symptoms. The cause is usually a non-exact frontier, a lossy proxy, a missing
  invariant, or side material being preserved at proof-spine fidelity.

### Campaign compression audit

Use this audit before another exploration round when the campaign feels busy but not closer to
resolution.  The audit is successful only if it reduces the live proof state.

```text
Top theorem:
Last exact/equivalent reduction:
Current active crux:
Rows that are genuinely independent:
Rows that are inherited consequences:
Rows that are only sufficient proxies:
Rows to delete/merge/park now:
One next decisive move:
Success/failure effect on the live state:
```

- **Separate independent debt from inherited debt.**  A repeated obstruction should appear once in
  the ledger.  If several leaves all depend on the same hidden lemma, merge them into one row with a
  list of consequences rather than treating each consequence as an active target.
- **Do not polish stale branches.**  If a branch is no longer on the proof spine, compress it to one
  theorem, counterexample, or blindness sentence.  The goal of cleanup is to make the next proof move
  safer, not to preserve the full campaign archaeology.
- **Promote only exact statements.**  A new focused note or dashboard branch is justified when the
  target is equivalent to the parent problem, gives a sharp falsifier profile, or has a concrete
  kill/promote test.  Otherwise keep it as background until it exports a native result.
- **Use side-route ROI as a routing signal.**  If Alon-style or Grothendieck-style detours repeatedly
  return only vocabulary, analogies, or non-descending frameworks, stop launching broader detours and
  instead identify the native feature all of them failed to see.
- **Make the next move falsifiable.**  The next round should have an observable outcome: a row is
  proved, a counterexample is found, a proxy is killed, a theorem is imported, or the branch is
  parked.  If success and failure would both leave the dashboard unchanged, the move is not sharp
  enough.

### Artifact hygiene gates

Long campaigns produce several artifacts.  Keep each artifact at the right fidelity.

- **Proof note gate.**  Add to TeX only durable definitions, examples, theorem statements, proofs,
  and concise warnings that a reader needs.  Do not add chronological attempts or speculative route
  logs.
- **Ledger gate.**  The ledger starts with the current exact target, proved inputs, active debt,
  parked routes, and next decisive move.  Closed rows are removed or compressed into a proved-input
  list.
- **Dashboard gate.**  The dashboard is a navigation summary.  It should show theorem-level routes
  and active cruxes; if local atoms dominate the view, merge them into one proof-debt row.
- **Skill gate.**  Skills receive only reusable process rules.  Do not record campaign-specific
  labels, examples, or chronology in skills.
- **Subagent gate.**  A subagent report is not an artifact until the main agent converts it into a
  proof-contract delta.  Otherwise it is scratch evidence and should not enlarge the dashboard.
- **Resume with one named move.** End the pause with exactly one next mathematical action: prove a
  named crux, search for a named falsifier profile, import a located theorem, run a bounded side
  route, rewrite the proof spine, or park the branch.

### Progress-speed gates

Use these gates when a campaign has gone through several attempts, side routes, subagents, and
re-consolidations without closing the main theorem. They are meant to make progress faster by
preventing state growth from masquerading as proof progress.

- **One-screen state gate.** Before another exploration round, the active state must fit in one
  dashboard screen and one opening ledger block: current target, exact reduction, smallest falsifier,
  active proof-debt rows, parked routes, and next decisive move. If it does not fit, consolidate
  first.
- **Deletion-before-expansion gate.** Opening a new route, local case, side file, or subagent batch
  requires naming what it may delete or merge. If success or failure of the route cannot shrink the
  active state, keep it as background rather than a dashboard leaf.
- **Two zero-delta rounds gate.** After two consecutive rounds with no proof-debt status change,
  stop local refinement. Either search for a counterexample to the current crux, walk back to the
  last exact/equivalent target, import a located theorem, or switch proof geometry.
- **Proof-spine growth gate.** Do not add proof-spine pages unless a theorem, definition, example,
  or proof is durable and changes the contract. Historical attempts, failed proxies, and subagent
  narratives belong only as compact warnings or archived notes.
- **Invariant-before-taxonomy gate.** If the active branch is producing many local labels, atom
  types, certificate subclasses, or endpoint cases, pause and ask for the common invariant, exact
  sequence, obstruction class, potential, or dual certificate before naming another subclass.
- **Side-route ROI gate.** Alon-style, Grothendieck-style, literature, and computational detours
  must return a native theorem, lemma, counterexample, exact reformulation, diagnostic, theorem
  citation, proxy-kill, or precise blindness statement. Otherwise they are parked background.
- **Subagent merge gate.** Subagents are useful only after the main agent writes orthogonal evidence
  contracts and commits to a merge action. If the reports return overlapping vocabulary or adjacent
  cases, treat the batch as failed decomposition and merge/delete before spawning again.

### Retrospective output packet

After a long sequence of attempts, false starts, side quests, subagents, and cleanups, write a short
methodology packet before doing more mathematics.  This packet should be small enough to fit at the
top of a ledger and should change future behavior, not merely summarize history.

```text
Current exact target:
Last exact/equivalent reduction:
Current smallest falsifier profile:
What grew: pages / leaves / terminology / scripts / subagent reports
What actually moved: proof / counterexample / exact reformulation / theorem import / proxy killed
Main failure mode:
Gate added:
Next decisive move:
```

- **Use the packet to delete or demote state.** If the packet does not retire a branch, merge leaves,
  demote a side route, or replace a proxy by an exact target, the pause has not yet paid for itself.
- **Separate lessons by scope.** A campaign-specific lesson goes in the ledger; a reusable operating
  rule goes in a skill; a mathematical theorem goes in TeX; a failed route goes into one compact
  warning or counterexample.
- **Prefer gates over advice.** Convert each lesson into a future constraint: no new leaf without a
  deleted or merged leaf, no side route without native export, no subagent batch without orthogonal
  contracts, no proof-spine growth without a proof-debt status change, and no third local taxonomy
  before a walkback to the last exact target.

### Repeated-campaign lessons

These are the methodological lessons that repeatedly paid for themselves in long YangDim-style
campaigns with several false routes, side quests, subagents, and consolidation passes.

- **Treat reconsolidation frequency as evidence.** If the same campaign repeatedly needs cleanup,
  the problem is usually not prose quality. It means the active frontier is too wide, non-exact, or
  mixed with historical memory. Pause to recover the last equivalent target before continuing.
- **Require a one-line proof-contract delta after every round.** The merge note must say exactly
  which proof-debt row changed and how: proved, refuted, equivalent reformulation, sharper falsifier,
  imported theorem, proxy killed, or route parked. If no row changed, do not add leaves, terminology,
  or proof-spine pages.
- **Side routes must export a native object, not an atmosphere.** Alon-style and Grothendieck-style
  explorations are useful when they return a native lemma, obstruction criterion, exact sequence,
  invariant, counterexample, or precise blindness statement. A better analogy with no native export is
  background, not an active route.
- **Subagents are for orthogonal evidence, not parallel enthusiasm.** A productive batch assigns
  distinct evidence contracts: proof, disproof, finite diagnostic, literature match, or abstraction
  descent. If reports return overlapping vocabulary or many nearby cases, the decomposition failed
  and the next step is merge/delete, not another batch.
- **Use page count, leaf count, and jargon count as smoke alarms.** A long PDF or verbose dashboard
  can be healthy only when it records many closed theorems. If the smallest live obstruction is
  unchanged while the document grows, stop adding local refinements and either compress, disprove, or
  switch proof geometry.
- **Do not preserve failed routes at proof fidelity.** Once the reusable lesson is extracted, keep a
  compact warning or counterexample and let git history preserve chronology. The reader-facing proof
  spine should contain durable definitions, statements, examples, and proofs.
- **Alternate frontier attack with framework building deliberately.** A framework side quest is worth
  keeping only if it changes the current frontier or supplies reusable tools for the next attack. If
  the framework is promising but not closing the route, park it as a separate result and return to the
  named crux.
- **Measure method ROI explicitly.** After an Alon-style, Grothendieck-style, literature, or
  computational detour, assign exactly one status: `promoted` if it changed a proof-debt row,
  `parked` if it produced useful background but no native descent, or `retired` if it lost the
  obstruction. Do not leave a detour in the active tree because it felt conceptually promising.
- **Treat repeated cleanup requests as proof-state feedback.** If the user repeatedly asks for
  cleanup, compactness, or dashboard readability, assume the source-of-truth structure is failing.
  Before further proof work, restore a one-screen dashboard, a current-state ledger opening, and one
  visible crux; otherwise the next proof step is likely to be based on stale or duplicated debt.
- **Use a frontier budget.** Before opening a new branch, record which active branch will be closed,
  merged, parked, or demoted if the new branch succeeds or fails. If no existing state can be
  deleted by the new branch, the branch is probably background rather than active proof work.
- **Make consolidation irreversible.** A cleanup pass should not merely reorganize old material so
  it can expand again in the next round. It should install a gate: a maximum active-leaf count, one
  current crux, a proof-debt table, or an explicit rule that failed proxies cannot be reopened
  without a new witness, theorem, or exact reformulation.
- **Treat "same reduced target, more pages" as negative evidence.** If a draft grows substantially
  while the reduced target and falsifier profile are unchanged, assume the local language is
  overfitting the obstruction. Stop refining names and either attack the exact target directly,
  search for a counterexample to the current crux, or switch proof geometry.
- **Audit by proof-contract shrinkage, not effort.** A week of reductions, side quests, and
  re-consolidations can still leave the theorem exactly where it started. The honest question is:
  did the current proof contract get smaller? Count only durable outputs: a proved implication, a
  refuted proxy, an equivalent reformulation, a sharper smallest falsifier, an imported theorem, or a
  deletion/merge of active debt.
- **Prefer route walkback over another local refinement once the same crux recurs.** When several
  rounds keep returning to the same obstruction under new names, stop before adding another label.
  Walk back from the original problem to the present crux, mark each arrow as equivalent,
  sufficient, necessary, special-case, or heuristic, and restart from the last exact/equivalent
  layer unless the current proxy has a decisive kill/promote test.
- **Consolidation must install a future constraint.** A cleanup pass should leave behind an
  operational rule such as a live-leaf budget, a single current crux, a proof-debt table, a
  no-new-leaf-without-deletion rule, or a side-route ROI gate. If the same material can immediately
  accrete again, the consolidation was transcription rather than state compression.
- **Use side routes as bounded visibility tests.** Alon-style imports and Grothendieck-style
  abstractions should first ask whether the new language sees the current normalized obstruction. If
  it forgets the decisive native feature, the useful output is the blindness statement and a killed
  proxy, not another menu of related techniques.
- **Merge subagents by deletion, not by anthology.** Parallel agents are high-value only when their
  reports let the main agent prove, refute, merge, or retire active rows. If the merge produces a
  collection of plausible but overlapping perspectives, treat the decomposition itself as failed and
  shrink the frontier before spawning again.
- **Keep the proof spine and campaign state at different fidelities.** Durable definitions,
  examples, lemmas, and proofs belong in TeX. Current blockers and exact next tests belong in the
  ledger/dashboard. Failed attempts, false routes, and side-route narratives should survive only as
  compact warnings or counterexamples unless they are pedagogically essential.
- **End a methodological pause with one decisive mathematical move.** The pause has not improved
  speed unless it chooses the next proof attempt, counterexample search, theorem import, or route
  retirement with a clear success/failure criterion.

### Systematicity upgrades from long YangDim campaigns

Use these rules when a campaign starts alternating between proof attempts, false routes,
re-consolidations, side-method detours, and subagent batches.  The point is to convert accumulated
experience into a faster operating loop.

- **Run scheduled retrospectives, not emergency cleanups.**  After any two zero-delta rounds, any
  side-route batch, any subagent batch, or any major proof-spine growth, pause for a methodological
  packet before more mathematics.  The packet must classify what moved, what grew, what is stale,
  and which single proof-debt row is next.
- **Score rounds by frontier movement.**  Each round receives exactly one score: `proved`,
  `refuted`, `equivalent-reformulation`, `smaller-falsifier`, `theorem-import`, `proxy-killed`,
  `diagnostic-only`, `background-only`, or `zero-delta`.  Only the first six may add active state.
  A `diagnostic-only` round may add one compact warning; `background-only` and `zero-delta` rounds
  should not expand the ledger or dashboard.
- **Use a stale-state triage before proving.**  When the next move is unclear, first identify stale
  state: closed claims still listed as open, inherited debt duplicated under multiple names,
  sufficient conditions treated as exact targets, side-route vocabulary without native descent, or
  proof-spine material that belongs in the archive.  Delete or demote stale state before adding a
  lemma.
- **Make branch walkback routine.**  If the same crux reappears under a new name, write the chain
  from the original theorem to the current target and mark every arrow as equivalent, necessary,
  sufficient, special-case, or heuristic.  Restart from the last exact/equivalent layer unless the
  current proxy has a decisive kill/promote test.
- **Prefer one invariant to another taxonomy.**  When local labels proliferate, the next task is not
  another case split.  Ask for the invariant, exact sequence, dual certificate, boundary map,
  obstruction class, potential function, or normal form that would make several labels disappear.
- **Merge side routes as native exports.**  A creative detour has succeeded only if its output can
  be written in the native proof contract as one lemma, theorem citation, obstruction criterion,
  counterexample, exact reformulation, or blindness statement.  Otherwise park it as background and
  do not keep its vocabulary active.
- **Merge subagents as a proof-debt diff.**  A subagent merge should say which rows were proved,
  refuted, merged, parked, or relabeled.  If the reports mainly add adjacent terminology or
  overlapping partial arguments, the decomposition was bad; consolidate before spawning again.
- **Keep source-of-truth roles rigid.**  The proof note should read like durable mathematics, the
  ledger should show current proof debt, the dashboard should navigate active/proved/parked state,
  and skills should store reusable process.  If the same information appears in all four, it is
  probably too verbose or not assigned to the right artifact.
- **Install an irreversible constraint after every consolidation.**  A cleanup pass should leave a
  new gate: a maximum live-leaf count, one visible current crux, a proof-debt table, a no-new-leaf
  without deletion rule, a side-route ROI gate, or a proof-spine growth gate.  If no future move is
  constrained, the cleanup was only transcription.
- **Translate false routes into accelerators.**  A false route is useful when it leaves a named
  obstruction, forgotten feature, killed proxy, or counterexample profile that speeds up the next
  proof/disproof attempt.  If it only leaves a long story, compress it to one warning and let git
  history preserve the rest.

### Round scoreboard

Maintain a small scoreboard for mature campaigns.  It can live at the top of the ledger or in the
campaign dashboard summary.

```text
Last 3 rounds:
1. Score:
   Proof-contract delta:
   State deleted/merged:
2. Score:
   Proof-contract delta:
   State deleted/merged:
3. Score:
   Proof-contract delta:
   State deleted/merged:

Current crux:
Next decisive move:
Stop/retrospective trigger:
```

- If two of the last three scores are `diagnostic-only`, `background-only`, or `zero-delta`, do not
  open a new local branch.  Walk back, search for a falsifier, import one located theorem, or switch
  proof geometry.
- If no row was deleted or merged in the last three rounds, do a consolidation pass before further
  exposition.
- If the current crux has not changed while pages or dashboard leaves grew, treat the growth as
  negative evidence for the present proof geometry.

### Lessons from false routes and reconsolidation loops

Use this checklist when a campaign has produced many reasonable attempts but the top-level theorem
has not visibly moved.  The goal is to convert experience into speed, not to preserve more history.

- **Treat false routes as compression opportunities.**  A failed route should leave exactly one of:
  a counterexample, a blindness statement, a killed proxy, a sharper falsifier profile, or a warning
  about a non-equivalent reduction.  If it leaves a long active subtree, the failure has not yet been
  digested.
- **Ask what the failed route could not see.**  Repeated failures usually point to a missing native
  feature: endpoint data, signs, support, orientation, rank, boundary incidence, admissibility, or
  cycle compatibility.  Name that feature explicitly and make it the next proof/disproof target.
- **Promote only exact frontiers.**  Before continuing from a reduced problem, mark the arrow from
  the original target as equivalent, necessary, sufficient, special-case, or heuristic.  Do not spend
  another round refining a sufficient-only or heuristic frontier unless it has a decisive
  kill/promote test.
- **Use cleanup requests as convergence diagnostics.**  If the user repeatedly asks for cleanup,
  compactness, or a clearer dashboard, assume the research state is too diffuse.  The next action is
  to merge, delete, park, or replace active debt before proving another local lemma.
- **Convert reconsolidation into an irreversible rule.**  After a cleanup pass, install a concrete
  constraint: one current crux, a maximum active-leaf budget, a no-new-leaf-without-deletion rule, a
  side-route ROI gate, or a proof-spine growth gate.  Otherwise the same clutter will return.
- **Separate proof spine from campaign memory immediately.**  Durable definitions, examples,
  lemmas, and proofs belong in TeX.  Current blockers belong in the ledger/dashboard.  Failed
  attempts and side-route narratives survive only as compact warnings unless pedagogically essential.
- **Prefer a smaller exact obstruction to a richer taxonomy.**  If a branch keeps producing local
  labels, certificate types, or case families, stop naming cases and search for the invariant,
  exact sequence, dual certificate, obstruction class, or counterexample template common to the
  survivors.
- **Make every round close with a deletion question.**  Ask: what can now be removed from the active
  state?  If the answer is "nothing," record at most one compact background note and do not expand
  the dashboard, ledger, or proof spine.

### Subagent and side-route speed rules

Subagents and creative side routes are useful only when they create orthogonal evidence and shrink
the live proof contract.

- **Spawn agents from evidence contracts, not topic labels.**  Assign distinct roles such as proof
  route, disproof route, finite diagnostic, exact literature match, and abstraction descent.  If two
  agents could plausibly write the same definitions, the split is not orthogonal enough.
- **Merge subagents by deletion.**  A subagent batch is successful only if the main agent can prove,
  refute, merge, park, or relabel active proof-debt rows.  An anthology of plausible perspectives is
  a failed decomposition until it is compressed.
- **Cap parallelism after low-yield batches.**  If one batch returns overlapping vocabulary or no
  proof-contract delta, do not spawn another larger batch.  Walk back to the last exact target and
  redesign the decomposition.
- **Demand native exports from side routes.**  An Alon-style or Grothendieck-style detour must
  return a native lemma, counterexample, theorem citation, exact reformulation, diagnostic,
  blindness statement, or proxy kill.  A conceptual analogy without a native export is background.
- **Alternate side routes with frontier attacks.**  Framework building can improve the campaign, but
  it must be interleaved with direct proof/disproof attempts against the current crux.  If a
  framework does not change the current falsifier profile, park it and attack the frontier again.
- **Retrospectives should end in an executable move.**  A methodology pause is complete only after
  choosing one next action with a success/failure criterion: prove a named row, search for a named
  falsifier, import a located theorem, retire a proxy, or rewrite the proof spine.

### Proof-contract accounting

Maintain a proof-debt table for every active theorem-level target. Each row should contain:

```text
Claim:
Direction needed: equivalent / necessary / sufficient / special-case / heuristic
Status: proved / refuted / reduced / computational / plausible / stalled / open
Evidence:
Missing implication:
Smallest falsifier profile:
Next decisive test:
```

- **Track direction on every arrow.** Most rabbit holes start when a sufficient condition is refined
  as if it were equivalent to the original target.
- **Keep inherited and expository debt out of the active blockers.** If one lemma would close several
  leaves, merge them under that lemma.
- **Close rounds by deleting or relabeling debt.** If no row changes status, record at most one
  compact warning, diagnostic, or background note, and do not expand the dashboard.
- **Promote normal forms only when stricter.** A new obstruction profile is progress only if every
  remaining counterexample must satisfy it and it is visibly smaller, more rigid, or more checkable
  than the previous crux.
- **Every debt needs a retirement test.** A row without a condition under which it will be proved,
  refuted, merged into another row, or parked tends to become permanent clutter. Add a kill/promote
  criterion before spending another round on it.

### Conditional-lemma wall protocol

Use this protocol when a proof route starts producing many statements of the form "assuming A, it
remains to prove B."  This is a common failure mode: each lemma may be correct, but the stack can
grow into a wall of unclosed obligations while the theorem contract stays unchanged.

- **Classify new lemmas as bridge or debt.** A bridge lemma proves, refutes, merges, or strictly
  shortens an existing proof-debt row. A debt lemma introduces a new unproved hypothesis, regularity
  condition, compatibility condition, or normal-form assumption. Debt lemmas do not belong in the
  proof spine unless they replace several older debts by one sharper equivalent debt.
- **Write the closure formula before adding the lemma.** Keep the current route in the form
  `Target follows from rows A+B+C`. A proposed lemma must say whether it proves a row, replaces
  `A+B` by a single equivalent row, or merely adds `D`. If it merely adds `D`, do not add it to the
  active proof note.
- **Set a conversion deadline for debt lemmas.** A conditional lemma can stay active for at most one
  round without either being proved, refuted, merged into another row, or demoted to background. Do
  not let provisional conditions become permanent theorem state.
- **Cap visible conditional depth at three.** If closing the theorem requires more than three
  unproved rows, stop proving local implications and replace the branch by a proof-debt table. Pick
  exactly one decisive row to attack; park or merge the others.
- **Prefer discharge over refinement.** Once a row is named, the next round should try to prove it
  directly, find a counterexample to it, or show it is not equivalent enough to be worth keeping.
  Refining the row into subrows is allowed only if the new formulation is strictly closer to the
  original exact target or gives a sharper smallest falsifier.
- **Use a debt burn-down note.** After a round, record the number of unproved rows before and after.
  A round that changes `3 open rows` into `4 open rows` is negative progress unless it also proves an
  equivalence or kills a proxy.

### State-compression discipline

- **Separate proof spine, current state, and archive.** The proof spine contains definitions,
  theorem statements, and durable proofs. The ledger contains only active proof debt, ruled-out
  shortcuts, smallest falsifiers, and next moves. The archive contains historical attempts after their
  reusable lesson has been extracted. Never let the archive become the proof spine.
- **Consolidation must choose, not summarize.** Keep durable facts, current debts, and compact
  warnings. Delete duplicate labels, demote historical derivations, and leave one visible current
  crux. Rewriting every attempt in cleaner prose preserves the same cognitive load.
- **Use page count and leaf count as smoke alarms.** A large proof note or dashboard is fine only if
  it records many closed results. If the active crux is unchanged while pages or leaves grow, the next
  action is compression, exact-target recovery, adversarial disproof, or a different proof geometry.
- **Keep active state below the reader threshold.** A future reader should recover the campaign from
  one self-contained route draft or paper section, one proof-debt ledger, and one dashboard screen. If
  chat history or a long historical PDF is required, stop and reset the state.
- **Use consolidation as merge, not polish.** A successful cleanup removes closed claims from the
  ledger, merges sibling leaves, demotes stale routes, or replaces several local targets by one
  theorem-level contract.

### Branch walkback and plateau gates

Use this after two consecutive zero-delta mathematical rounds, after a third non-closing local split,
or whenever the same obstruction reappears under new names.

- **Walk back to the last exact target.** Write the chain
  `original target -> reduced target -> current crux -> smallest falsifier profile`, marking each
  arrow as equivalent, necessary, sufficient, special-case, or heuristic.
- **Audit lost structure.** For each arrow, record what structure was preserved and what was
  discarded: signs, endpoint data, support, rank, topology, boundary orientation, admissibility,
  cycle compatibility, or cancellation.
- **Extract an invariant before another split.** If leaves proliferate into local gadgets, atom
  types, or certificate subclasses, stop naming subcases and ask for the common invariant, exact
  sequence, obstruction class, potential, boundary map, or dual certificate.
- **Switch proof geometry deliberately.** If the current split is non-exact or purely sufficient,
  either retreat to the exact parent, attempt a counterexample satisfying the current profile, or run
  a bounded side route with a required native export.

### Side routes and imported methods

Alon-style, Grothendieck-style, literature, and computational side routes are useful only when they
change the native proof contract.

- **Start from the normalized obstruction, not the whole theorem.** Translate the current smallest
  falsifier, atom, quotient, certificate, or proof-debt row into the side language before surveying
  methods.
- **Run an obstruction-visibility test first.** If the encoding cannot distinguish the current
  obstruction from benign examples, record the lost native feature and retire or repair the encoding.
- **Return exactly one native export.** The mergeable outputs are: theorem, lemma, counterexample,
  diagnostic, exact reformulation, theorem citation, obstruction criterion, or precise non-transfer
  statement.
- **Demand a deletion dividend.** The side route remains active only if it proves, refutes, sharpens,
  demotes, deletes, or merges an existing proof-debt row. Otherwise it is background.
- **Score side routes by contract movement, not insight density.** A side route that explains why an
  approach is blind can be high value if it kills a proxy. A side route with many interesting
  analogies is low value if the active theorem statement, falsifier profile, and proof-debt table are
  unchanged.
- **Keep failed side routes low-fidelity.** Preserve one sentence naming the lost structure or proxy
  killed. Do not turn each external theorem family or abstraction layer into a new dashboard leaf.

### Subagent protocol

Use subagents for independent evidence, not momentum.

- **Spawn only from a written packet.** Include the exact target, definitions, allowed artifacts,
  route ID, known false shortcuts, deliverable type, calibration vocabulary, and success/failure/stall
  criteria.
- **Make contracts orthogonal.** A productive batch splits by evidence type: proof attempt,
  counterexample search, finite diagnostic, exact reformulation, or literature match. Do not ask
  several agents to enumerate variants of the same local taxonomy.
- **Merge before the next batch.** Subagent reports are raw inputs. The main agent must audit them,
  extract proved claims or blockers, update the source of truth, and delete or relabel active debt.
- **Treat low-yield batches as decomposition failures.** If a batch returns overlapping vocabulary,
  plausible local reductions, or no audited theorem/counterexample/diagnostic, consolidate or change
  methodology before spawning again.

Route packet template:

```text
Round:
Target:
Definitions/hypotheses:
Allowed proved tools:
Known false shortcuts:
Routes and route IDs:
Deliverable format:
Success / failure / stall criteria:
Merge destination:
```

### Ledger, dashboard, and draft hygiene

- **Use one source-of-truth quartet.** Durable mathematics lives in `main.tex` or a self-contained
  side draft. Current blockers live in the ledger. The dashboard is scan-level navigation. Scripts
  are reproducible diagnostics. The inventory records where artifacts are, not branch-by-branch
  mathematics.
- **Update ledgers by replacement, not sedimentation.** Rewrite the relevant status block to state
  the current truth directly. Avoid stacked dated comments unless chronology itself is evidence.
- **Start active ledgers with current targets.** The first section should give definitions,
  hypotheses, proved inputs, ruled-out shortcuts, live cruxes, and next decisive tests before any
  historical notes.
- **Keep the dashboard two-tier.** Show theorem-level routes and the smallest current active crux.
  Fine subcases belong in the ledger or proof note until they require genuinely different evidence.
- **Refresh artifacts in one pass.** A status-changing result should update the draft or paper,
  ledger, dashboard, scripts/inventory if relevant, and skill only if the process lesson generalizes.
- **Skills store process, not chronology.** Add or replace rules that change future behavior. Do not
  store local theorem names, route history, or campaign notation in a skill.

### Consolidation exit checklist

A consolidation pass is complete only when the following are true:

- one current theorem or reduced target is stated self-containedly;
- one proof-debt table separates proved inputs, independent debts, inherited debts, sufficient-only
  routes, and ruled-out shortcuts;
- the ledger and dashboard agree on the smallest live obstruction;
- closed material has been removed from the active-open list;
- failed routes survive only as compact counterexamples, warnings, or diagnostics;
- the next action has a named success/failure criterion.

## Choosing adversaries — the highest-leverage skill

The single most common failure is testing only **benign** cases: small, symmetric, pure, low-rank,
single-scale. They almost always satisfy a candidate bound and tell you nothing. Before trusting any
bound:

- **Enumerate the structural axes** the bound might be sensitive to (degree/scale, rank, sign
  pattern, how mass spreads across components, coherence vs. cancellation).
- **Build an adversary that stresses each axis simultaneously** — especially *mixed* (low + high
  scale together) and *opposite-sign* constructions, which expose cancellation and coherence that
  pure families hide.
- **Ask "what would this bound need to be false?"** and try to build exactly that, then check it
  numerically. If you cannot build it, that itself is weak evidence the bound holds.
- When a route dies, record *which adversary* killed it and *why* (the mechanism), so the next route
  can be checked against the same stress immediately.
- **For an implication `P ⟹ Q`, the deadly adversaries are the near-misses of `P`.** Random instances
  that lack `P` usually lack it *grossly* (and trivially satisfy `Q`'s negation or are obviously fine)
  — they are benign. Build the dangerous cases by **taking a genuine `P`-instance and minimally
  perturbing it to break `P` while preserving every cheap *necessary* condition for `P`.** War story:
  testing "Cohen-Macaulay ⟹ ample," random non-ample classes were small and disconnected — useless.
  The real test was "non-ample but passes the cheap CM-necessary conditions (connected, `hd=VC`),"
  produced by deleting/swapping one element of a maximum class. Hundreds of these existed and *all*
  failed CM — strong evidence precisely because they were near-misses.
- **Random *dense* samples miss *structured sparse* extremisers.** Sampling random dense instances
  (e.g. a full random symmetric matrix) is a weak adversary: the worst case is often a sparse,
  highly structured object (a perfect matching, a single block, a recursive construction) that random
  dense sampling has vanishing probability of realising. A bound that looks "flat to `n=18`" under
  random search can be *false*, broken by a one-line structured kernel. Always hand-build the
  structured extremes (matchings, disjoint blocks, towers, dictators) in addition to sampling.

War story: `||G_R||_op/B` looked bounded (`~1.2`, flat to `n=18`) under *random dense* degree-2
kernels. The *matching* `R = sum_b z_{2b} z_{2b+1}` — sparse, structured, `B=1` — makes it grow like
`sqrt(log n)`, refuting the conjecture. Random search never came near it.

- **Random misses the extremiser even *inside* a structured family.** Sampling *random-weighted*
  members of the right family is still a weak adversary: the extremiser is usually the **uniform /
  fully-symmetric** member, and random weights only *decrease* the quantity. War story: searching for
  the max of `w(G_R|K)/iota` over "matching-lift" kernels with *random* vertex/pair weights returned
  `0.83 < 1` after a 10000-second optimization — yet the *uniform* matching lift gives `1.31`. The
  random seeds polished into weak local maxima and never climbed to the symmetric peak. Always seed an
  adversarial search with the **uniform/symmetric** family members explicitly, not just random draws
  from the family.
- **Optimize the candidate inequality to *break* it before you commit a theorem.** A "scale condition"
  or proxy bound you intend to assume should first be *adversarially maximized* (gradient-free
  optimization over the kernel), not merely spot-checked. Two would-be theorems were caught this way in
  one session: a clean "overlapping rank-`k` products satisfy the rate iff `B^{k-2}sigma^2 <= iota^k`"
  was retracted when optimization drove the ratio past `25` (the maximiser exploited coordinate
  collisions that broke double-degeneracy); and the same condition for single forms was found to hold
  for polynomials but fail for `|L|^3`. Spot-checking said "holds"; optimization said "false."

War story to internalize: a self-referential lemma passed every *pure-degree* test (parity, rank-2,
BKZ are all pure-degree) and looked like the frontrunner. A single *mixed* degree-2 + parity
construction showed its ratio grows like `sqrt(n)`. The lesson is permanent: **pure/symmetric
families are benign; test a genuinely mixed adversary before believing anything.**

## Compute hygiene on the EC2 instance

The EC2 box also serves the research site and may host other active work. Treat compute resources as
shared infrastructure, not as an unlimited batch cluster.

- **Scale searches deliberately.** Start with small parameters, estimate CPU and memory growth, and
  only then move to larger runs. Prefer chunked or checkpointed searches over one large all-or-nothing
  process.
- **Use lower priority for heavy jobs.** For expensive diagnostics, use `nice`, e.g.
  `nice -n 10 uv run python scripts/explore_foo.py ...`, so interactive work and the web service stay
  responsive.
- **Limit parallelism.** Do not launch multiple high-memory or all-core jobs at once. If a script has
  worker/thread/process options, set them conservatively unless the user explicitly asks for a
  saturation run.
- **Bound exploratory runs.** Use timeouts, max-parameter flags, sample limits, or staged output for
  first passes. A diagnostic that can be stopped and resumed is better than one that risks exhausting
  memory.
- **Stop on resource distress.** If a run starts swapping, pegs all cores for too long, or threatens
  other services, terminate it and redesign the computation with smaller cases, streaming output,
  symmetry reduction, or a targeted adversary family.

## Pushing evaluation past the toy regime

Small cases can be misleading precisely where it matters (an effect that only appears for many
components, or large `n`). Escalate evaluation:

- **Exploit symmetry for exact large-`n` evaluation.** If the construction is a function of a single
  summary statistic, compute exact moments over that statistic's law for enormous `n`. This turns a
  suggestive `n<=20` trend into a decisive `n=4000` verdict.
- **Symmetry reduction also buys *reliability*, not just size — a naive iteration can pollute to
  numerical noise.** A Krylov / power iteration in the full `2^n` space accumulates floating-point
  error and keeps manufacturing spurious "new" directions: the reported subspace dimension blew up to
  `401` when the true invariant subspace had dimension `28`, and the quantity computed on the polluted
  basis is untrustworthy. If the kernel has a symmetry group, the relevant subspace lives in the
  **invariants** (here `~m^2/2`-dimensional), where the operator restricts to a small *exact* matrix —
  compute there. The pollution masquerades as a real high-dimensional object; cross-check the iterate's
  dimension against the symmetry-predicted one.
- **Linearity in the kernel makes adversarial search cheap.** If the object of study is *linear* in the
  kernel `R` (e.g. the carré-du-champ `G_R`), then over a finite family `R = sum_O c_O B_O` you have
  `G_R = sum_O c_O G_{B_O}`: precompute the basis-operators `G_{B_O}` once, then optimizing your
  quantity over the whole family is just cheap linear-combination-plus-small-eigensolve per evaluation.
  This converted an intractable per-eval-`2^n` optimization into a fast one over the symmetric family.
- **Monte-Carlo what can't be done exactly**, at `n` an order of magnitude past enumeration, enough
  to distinguish "bounded" from "slow growth."
- **Cross-check two methods** at an overlap point (e.g., exact-via-symmetry vs. brute force at a
  shared `n`) to catch evaluation bugs before they mislead a verdict.
- **Design the adversary to grow the suspected-bad axis with `n`** (e.g., number of active
  scales `~ sqrt(n)`), not just `n` itself — otherwise you never enter the regime where the route
  would fail.

## Reduction to crux lemmas (and its trap)

Progress usually means reducing the full problem to ONE clean inequality, then attacking that. This
is powerful but carries a trap: the crux lemma can be *false* while looking robust. Mitigations:

- Once reduced, immediately **stress the crux lemma on the full adversary suite**, not just the
  cases that motivated it.
- Try to **prove a sub-case of the crux** (e.g., the `L_2` part, a fixed-scale case). A proved
  sub-case both raises trust and often reveals the right tool for the rest.
- State the reduction explicitly as "conjecture ⇐ Lemma A + Lemma B," with each lemma's status
  labeled, so the remaining gap is unambiguous.

### Structural reduction patterns that recur

- **Minimal-counterexample via a hereditary operation.** If the object has a structure-preserving
  "restriction" (link, minor, sub-instance, deletion) under which the *target property is hereditary*
  (`Q` of the whole ⟹ `Q` of each restriction), then a clean induction kills every non-minimal case
  for free: a bad object either has the defect already in a restriction (induction applies) or is
  *minimal-bad* (defect in no restriction). This isolates the entire problem to **minimal-bad
  objects**, usually a small, rigid, analyzable family — that is where the real lemma lives.
- **Kill the cheap-invariant characterizations on purpose.** Before grinding a hard topological/
  analytic proof, explicitly check whether some *cheap necessary condition* for `Q` already
  characterizes the target (e.g. "is `h ≥ 0` equivalent to ample?", "does a numerical invariant
  decide it?"). Usually it does **not**, and *proving the non-equivalence with an explicit witness*
  is high-value: it forecloses a whole family of doomed "just bound the cheap invariant" attempts and
  proves the obstruction is genuinely deep — which justifies (and points to) the harder route, often
  a case split. A necessary-but-insufficient condition that *looks* characterizing is a classic time
  sink; spend ten minutes refuting it early.
- **Look for an exact recursion the invariant obeys under the basic operation.** When stuck, derive
  and *computationally verify* an identity relating the invariant of the whole to those of its
  restrictions (here: an `h`-vector coordinate recursion via the Hilbert series). A verified exact
  recursion becomes the engine of the reduction and is itself a citable lemma, even before the crux
  is closed.

## The assembly trap: a sharp per-piece bound is not a proof

A recurring and expensive trap, distinct from a false crux lemma. You prove a *tight* bound on each
piece (each term, diagram, configuration, scale) — verified, sharp, genuinely correct — and then
assemble by the triangle inequality `|sum| <= sum |piece|`. **The absolute-value assembly can diverge
even when the true (signed) sum is bounded**, because cancellation *across* pieces was doing the work.
Symptoms and discipline:

- Before assuming the assembly is routine, **measure `sum |piece|` (or its closed form) against the
  truth**, scanning the order parameter (here `q`/`p`/`n`). If `sum|piece| / truth` grows without
  bound, the absolute-value route is *dead* no matter how sharp each piece is.
- Name the cancellation you are discarding. (In our campaign: `sum_configs |Val|` equals `kappa_q` of
  an explicit scalar that grows past target while the true `kappa_q` decays — the Wick signs were
  essential; the analogue is "`tr(M^q)` not `tr(|M|^q)`".)
- Beware the words **"just bookkeeping"** in your own notes. We mislabeled a hard assembly as
  "combinatorial bookkeeping," then as "an energy-decay estimate," before the honest measurement
  showed it was *cross-piece cancellation*. If you catch yourself deferring the assembly as trivial,
  that is exactly where to point an adversary.

## The intermediate target can be lossier than the final target

A trap one level up from the assembly trap. To prove the real goal `A` you bound it by an
intermediate `A <= F(B)` and chase `B` (an operator norm, an injective/tensor norm, a square-function
norm, a relaxation). **`B` can have a defect that `A` does not** — it can grow with `n` (or `p`, or
degree) while `A` stays bounded. Then *no* bound on `B` of the form you want exists, and the whole
sub-campaign to prove "`B <= C·(budget)`" is chasing a false statement, even though `A` is true.

- **Before investing in bounding the intermediate, measure `B` itself against the budget** on the
  structured adversaries — not just `A`. If `B/budget` grows, the intermediate is the wrong target;
  retarget at the scale that *is* faithful to `A` (often a larger, variance-type scale).
- Symptom: every actual instance satisfies the real bound `A`, yet your chosen proxy `B` keeps
  creeping up. That gap *is* the proxy's defect, not evidence the goal is hard.
- This both kills a doomed route **and** is good news for the goal: the only "obstruction" was an
  artifact of the proxy.

War story: the moment bound `||R||_p` was being routed through the carré-du-champ operator norm
`||G_R||_op <= C·B`. The matching kernel has `||G_R||_op ~ sqrt(log n)·B` (proxy unbounded) while
`||R||_p ~ 0.45 M sqrt(pn)` is sub-Gaussian (goal trivially true). The operator norm overcounts by
`sqrt(log n)`; the goal must be proved *without* factoring through it.

## The proxy ladder can fail one rung at a time

Some campaigns do not have one false proxy; they have a ladder of increasingly faithful proxies,
each still stronger than the target until the proof reaches the target's real geometry. Do not treat
the first repaired proxy as the final crux just because it survived the adversary that killed the
previous rung.

- **Coarse support or incidence data is the first suspect.** If a route replaces magnitudes, weights,
  signs, multiplicities, or geometry by a bare support pattern, test a sparse structured object plus a
  tiny dense perturbation. The coarse invariant may become huge while the target barely changes.
- **Uniform or worst-case local control rarely assembles for free.** A correct local supremum bound
  can coexist with a false global mass bound. If the next step sums all local contributions
  positively, build examples with many weak paths through a shared bottleneck or gateway. Such
  examples often make the positive mass large while the norm or invariant of interest stays small
  because the contributions spread out, collide, cancel, or are orthogonal.
- **Do not prove a quadratic/norm target through a total-mass proxy until the total-mass proxy has
  survived structured path-count adversaries.** A total-variation or positive-counting estimate may
  count every possible route, while the target only sees squared mass, signed mass, rank, dimension,
  topology, or another finer structure. A false total-mass crux is a proxy defect, not a disproof of
  the target.
- **Global square-sum shortcuts can fail for the opposite reason.** A collection of large local
  quantities may exist, but the admissible objects may be unable to charge all of them
  simultaneously. If an unconditional square-sum bound fails, test an object aligned with the large
  local quantities and normalized by the true hypothesis before deciding whether the real pairing is
  false.
- **When a rung fails, move one level closer to the target.** Record the failed proxy as excluded,
  name the mechanism, and restate the next crux in a norm or invariant that preserves the structure
  the failed proxy discarded: signs, weights, cancellations, orthogonality, geometry, degree, or
  admissibility constraints.

Generic lesson: a failed proxy ladder often means the proof is being routed through quantities that
discard exactly the structure making the target true. The correct response is not "the conjecture is
probably false"; it is "which structure did this proxy erase, and how do we formulate the next crux
so that structure is still visible?"

## Exact dual target before sufficient proxy

A common productive pattern is to reduce the current obstruction to an exact linear, dual,
quotient, separation, or homological criterion. A common slowdown is then to replace that exact
criterion by a more combinatorial sufficient condition and accidentally treat the sufficient
condition as if it were equivalent. This creates a new proxy ladder and can make a live route look
stalled for the wrong reason.

- **Name the exact object first.** Before introducing cuts, witnesses, certificates, normal forms,
  or local patterns, write the exact target as a membership/non-membership, kernel/cokernel,
  separator, extension, obstruction class, or universal property. State explicitly whether it is
  equivalent to the original crux.
- **Then label every tractable route by direction.** A cut criterion, local witness, finite
  certificate, or special normal form should be marked `sufficient`, `necessary`, `equivalent`,
  `special case`, or `heuristic`. Do not let the route title hide the direction.
- **Keep the exact target on the dashboard.** If the active practical route is sufficient, the
  dashboard and ledger should still show the exact parent crux and say "current sufficient route:
  X." This prevents later readers from thinking failure of X refutes the parent.
- **Use duality to produce falsifier profiles.** The dual exact target usually says what a
  counterexample must defeat: all separators, all cuts, all functionals, all quotient tests, or all
  certificates. Record that adversary profile before adding another reduction.
- **Retreat to the exact object when a sufficient route proliferates.** If several variants of a
  sufficient condition appear, pause and ask whether the exact dual statement admits a more direct
  proof, a different separator, or a counterexample. Do not stack sufficient conditions indefinitely.
- **Promote only exact or clearly directional statements.** A durable draft should say "A implies
  the crux" or "A is equivalent to the crux"; vague phrases such as "the remaining target is A" are
  allowed only when A is the exact crux.

### Compression checkpoints after route expansion

Every expansion phase should be followed by an explicit compression phase. The goal is not cosmetic
cleanup; it is to prevent the proof search from becoming a tree whose size substitutes for progress.

- **Measure route movement before adding leaves.** Ask whether the last round produced a smaller
  crux, a new exact reformulation, a killed proxy, a proof of a named lemma, a counterexample, or a
  located theorem. If not, further branching is usually premature.
- **Collapse sibling leaves aggressively.** If several leaves differ only by local terminology,
  finite cases, or a sufficient certificate variant, replace them by their common mathematical
  obstruction and keep the variants as examples or diagnostics.
- **Promote the strongest invariant, demote the rest.** A consolidation pass should end with one
  current invariant/reduction/adversary profile in front, not a ranked list of plausible directions.
  Park weaker ideas explicitly as `parked` or `evidence only`.
- **Make the next action decisive.** After compression, the next task should have a kill/promote
  criterion: prove the named crux, find a falsifier satisfying the current obstruction profile,
  locate an exact theorem, or show that a proxy has become too lossy.
- **Keep the dashboard smaller after consolidation.** A successful consolidation usually reduces the
  number of active leaves. If it does not, record why each surviving leaf is genuinely independent
  and what distinct evidence would close it.

### Frontier budget and stop gates

Use this when the campaign keeps producing plausible reductions but the main theorem is not visibly
closer.

- **Set a live-leaf budget.** Choose the maximum number of active leaves that can be held in working
  memory, usually one to three. Extra ideas must be parked, merged under a shared crux, or written as
  compact background.
- **Every new leaf pays rent immediately.** A new leaf is allowed only if it has a success/failure
  criterion and explains which current debt it could delete, merge, or demote. Otherwise it belongs
  in a parked-ideas section, not the dashboard.
- **After two zero-delta rounds, change scale.** If two consecutive rounds leave the same exact
  target, same falsifier profile, and same proof-debt table, do not run a third local refinement.
  Walk back, seek a counterexample, import a theorem, or replace the proof geometry.
- **After one low-yield subagent batch, merge before spawning.** If agents returned overlapping
  terminology, plausible cases, or no audited theorem/counterexample/diagnostic, the next action is
  compression and route redesign, not a larger batch.
- **Record the method ROI in the merge note.** For proof work, computation, literature, Alon-style
  import, Grothendieck-style abstraction, or subagents, write the before/after proof-debt row. If the
  row is unchanged, park or retire the method output.
- **Prefer one exact obstruction over many named symptoms.** When local labels proliferate, replace
  them by the exact kernel, cokernel, obstruction class, incompatibility condition, or minimal
  falsifier they are all trying to detect.

## After "fixing" a gap, re-verify the new pieces — a fix can introduce a worse gap

When you patch a proof, the patch introduces *new* claims (new constants, new norm inequalities, a
new rank/dimension bound). Verify *those specific claims* numerically and dimensionally before
trusting the patched proof — do not let the (correct) final result vouch for them. A full bound can
hold by *cancellation* while a per-step inequality you just wrote is individually false.

- **Beware the circuit dual-separator trap.** A support-minimal linear dependence is a circuit:
  every element is essential, but every element also lies in the span of the other circuit elements.
  Therefore one cannot get a functional separating a circuit element from all the others. The correct
  circuit-level conclusion is a unique full-support relation and independence after deleting any one
  element, not one-sided dual separators. Dual separators require an independent set plus an outside
  vector, or a rank test after deleting a different distinguished element.

War story: a "fix" for the degree-`>=3` case asserted `rank(H) <= C(d,2)` for a matrix that is
actually `(n-d+2)x(n-d+2)` (rank up to `n-d+2`) — a hidden dimension factor. The component bound was
false; only the full operator (by cancellation) stayed bounded. Per-component dimensional check would
have caught it immediately. **Rule: every "dimension-free" component claim must be tested for
dimension dependence at fixed degree, growing `n`, on a structured adversary — not just the assembled
result.**

## Resolving the named obstruction usually *relocates* it, not dissolves it

When you finally prove the one inequality everyone said was missing, the problem rarely falls. The
difficulty moves — typically from "bound each piece" to "assemble the pieces," or from a clean
sub-case to the regime it doesn't cover. This is normal and worth saying out loud in the writeup:
state precisely *where the difficulty now lives* rather than implying the proof is near. Re-run the
alive/dead/stalled call on the *relocated* obstruction.

## Use special cases as axis tests, not reassurance

After a plateau, proved special cases are most valuable when they isolate independent structural
axes of the conjecture. Do not count them as generic evidence. Ask what each case permits, what it
forbids, and which interaction remains untested.

- **Map the axes explicitly.** Examples of axes: number of active components, rank/separability,
  common vs. varying profiles, minimal vs. large core geometry, support pattern, sign pattern,
  uniform vs. skewed weights, and pointwise vs. averaged weighting. A special case proves something
  only about the axes it actually varies.
- **If every single-axis case is harmless, move to the first mixed-axis case.** A row-uniform
  many-component theorem, a rank-one/separable theorem, and a three-core arbitrary-profile theorem
  together do *not* suggest the problem is easy; they locate the obstruction in the interaction of
  many components with several genuinely different profiles. The next target should be the smallest
  family where those axes interact (e.g. two profiles, nonnegative rank two, or four cores), not the
  full generality.
- **Do not assemble separable cases by triangle inequality without a new lemma.** A rank-one or
  product proof says separability is harmless; it does not prove that sums of separable pieces are
  harmless. The cross-terms between profiles are often exactly where the original obstruction lives,
  and naive low-rank decomposition can introduce a rank factor or discard cancellation.
- **Keep the faithful weights in special cases.** If the live target is an averaged weighted
  inequality, preserve its averaging weights, support restriction, and crossed factors in every
  subcase. Proving a pointwise, supremum, or norm-factorized variant may only re-prove a false proxy.
- **Bank the mechanism, not just the statement.** After proving a special case, write down the
  structural reason it works ("residual factors," "only two ordered choices," "component energy
  sums by `ell_3 <= ell_2`") and the precise remaining interaction it does not cover. That mechanism
  determines the next attack.

## Two cheap force-multipliers

- **Locate before you search.** A literature search pays off enormously *after* you have named the
  obstruction precisely ("sign-preserving cumulant assembly for mixed-degree Rademacher chaos"), not
  before. A vague search returns surveys; a located one returns the exact named machinery (and often
  confirms your vehicle is the standard one).
- **Validate a decomposition by differential measurement, not re-implementation.** To check "piece X
  is small," prefer measuring `A - B` where `B` isolates everything *except* X (e.g. Rademacher
  truth minus the Gaussianized chaos = exactly the discrete correction), over re-coding the
  combinatorial classification that defines X — the re-code reintroduces the very subtlety
  (connectivity signs, diagonal conventions) you are trying to test, and silently produces wrong
  numbers.

## Match the bound's shape to the target's shape

If the goal is a *two-regime* moment bound (sub-Gaussian core + sub-exponential tail,
`||R||_p <= C(sigma sqrt p + b p)`), do not aim the crux at the one-parameter cumulant form
`|kappa_q| <= C^q (q-1)! b^q`: it is a factor `~ b^2/sigma^2` too lossy at the variance level and
silently drops the sub-Gaussian term. Target the **two-parameter Bernstein form**
`|kappa_q| <= C^q q! sigma^2 b^{q-2}` directly — it yields *both* regimes and often matches the
natural per-piece bound's shape ("variance proxy x scale^{q-2}"). Generic lesson: the *shape* of the
intermediate inequality should be dictated by the shape of the final bound, not by the first tool
that comes to hand.

## When the inequality resists a frontal proof: build the structural dossier

A hard inequality `A <= B` that defeats every direct estimate is usually missing *one* structural
fact about the objects in it — an identity, a positivity, a hidden monotone, or a connection to a
studied object. Once the frontal estimates and the proxy routes are exhausted, the productive move is
not another estimate but to **accumulate structure about the objects** until the missing fact
surfaces. Work these channels in parallel; each is cheap and compounding.

- **Dossier per object.** For every quantity appearing in the inequality, write down: its exact
  definition; *every* equivalent representation (sum, integral, trace, matrix entry, generating
  function, recursion, spectral/measure form); its invariances and symmetries; how it transforms
  under the natural operations (scaling, restriction, products, sums, adjoint, limits); its known
  bounds, extremizers, and first variation. The representation in which the inequality *looks*
  trivial is usually the one to prove it in. (Our tower `<R,G_R^j R>` only became tractable once
  read as the *moment sequence* of a spectral measure rather than as iterated operator applications.)

- **Hunt for identities, not just bounds.** An exact identity (`X = Y`) transfers far more than an
  estimate. Look for generating-function/transform representations, recursions, fixed-point or
  self-consistency relations (especially when one object is *built from* another), and conservation
  laws. A single identity can collapse the problem; a stack of inequalities rarely does.

- **Locate the objects in the literature — after you can name them.** Try to recognize each object as
  an instance of a studied one: a named operator, a classical measure or special function, the
  LHS/RHS of a known inequality, an object from an adjacent field. A located match imports an entire
  theory — and often the exact inequality, already proved. (Cross-references the "locate before you
  search" multiplier: name the object precisely first.)

- **Solve the simplest non-trivial case for its MECHANISM, not for reassurance.** Take the smallest
  case where the inequality is non-trivial *and true*, and identify the single structural feature
  that makes it true there — a positivity, a symmetry, an exact cancellation, an identity. Then ask:
  *which case-specific feature is doing the work, and does it survive?* The general proof is usually
  the right generalization of that one feature, not a new idea. (Degree two is true because the
  cumulant is a single trace and Schur applies; that *names* what the general case must replace.)

- **Name what each lossy bound discards.** When an estimate is lossy by a known factor, identify
  exactly which structural feature the loss corresponds to — a sign, a cancellation, a correlation, a
  positivity thrown away. The *conserved* features are the channels a sharp proof can route through;
  the discarded one is precisely what the sharp proof must keep. (The `ell_1`/triangle bound discards
  the sign and returns total variation; what it loses *is* the positivity to hunt for.)

- **Hunt for hidden positivity / convexity / majorization.** A large fraction of hard inequalities
  are shadows of a positivity one layer down: a measure is positive, an operator is PSD, a matrix is
  a Gram/Hankel matrix, a sequence is a valid moment sequence, a function is convex, one vector
  majorizes another. Find that hidden positivity and the inequality often becomes elementary — e.g.
  `integral lambda^q dmu <= (sup|supp mu|)^q integral dmu` is *trivial* once `mu >= 0`, turning a
  hard q-dependent bound into a one-line consequence of a support bound you may already have.

The output of this phase is not a proof but a **map**: a web of identities, representations, and
special-case mechanisms that either (a) matches a known theorem that transfers wholesale, or (b)
isolates the *one* missing structural fact — typically a positivity or an identity — whose proof is
now the whole problem, stated about a concrete, studied object instead of the original opaque
inequality. Promote that fact to the crux lemma and return to the adversary/reduction discipline above.

## Deciding alive / dead / stalled

- **Dead**: a specific counterexample shows the route's key inequality is false (with a growth rate).
  Record the witness and mechanism; move on. Do not keep poking a disproved route.
- **Stalled**: no counterexample, but no proof and no sharper tool in sight. Park it with a precise
  statement of what's missing; revisit when a new tool appears.
- **Alive**: passes all adversaries, has a proved core or a clear proof strategy, and the remaining
  gap is a named, standard-looking analytic statement. Promote it to frontrunner.

## Documenting honestly (persist it)

- Keep a running record (memory file / a `proof_route_*.tex`) of every route with its **status,
  the witness that killed it, and the mechanism**. This prevents re-treading and is genuinely
  valuable science.
- Frame partial results as "what we tried, why it fails, what remains" — never bury a dead end.
- In the paper, present excluded routes as evidence the obstruction is real, and the live route with
  its proved core and its precisely-stated remaining lemma.

## Distill the ledger into readable mathematics

A route ledger is optimized for memory; it is usually too chronological, local, and cluttered to
reveal the actual mathematical structure. Periodically convert it into a paper-like synthesis: a
draft that someone could read linearly and understand the problem, the known reductions, the killed
routes, and the current obstruction.

Trigger this distillation when the ledger becomes hard to navigate, after a route changes status, or
before a new major attack phase. Do not wait until the conjecture is solved.

- Create or refresh a synthesis file (`drafts/<topic>.tex`, `proof_route_<name>.tex`, or a section of
  `main.tex`) whose structure is mathematical rather than chronological.
- Start with formal definitions, notation, standing hypotheses, and the exact target statement. Then
  state the strongest proved results, conditional reductions, open crux lemmas, verified patterns,
  and excluded routes.
- Promote durable facts out of the ledger into highlighted statements: `Definition`, `Lemma`,
  `Proposition`, `Corollary`, `Conjecture`, `Question`, `Example`, `Counterexample`, and `Remark`.
  Label every statement by status: proved, conditional, verified computationally, open, or excluded.
- Write negative results as real mathematics. A killed route should become a proposition or
  counterexample with the construction, the failed claim, the mechanism of failure, and the growth
  rate or smallest witness when known.
- Include proof sketches for live results and full proofs when short; move purely exploratory logs,
  raw tables, and long scripts out of the narrative and cite the script or inventory entry.
- Add a dependency map: "Target follows from A+B"; "A is proved"; "B reduces to C"; "Route D is
  excluded by witness W." This makes the remaining work explicit and exposes hidden assumptions.
- Use the synthesis as a diagnostic, not just exposition. While rewriting, look for undefined
  objects, duplicated lemmas under different names, unjustified implications, stale conjectures, and
  places where the current crux is stronger or weaker than the original target.

## Multi-agent route protocol

Use subagents when the live obstruction naturally splits into independent routes or when a plateau
needs genuinely fresh attacks. Do not spawn agents just to parallelize reading the same file.

- **Run a subagent ROI audit before another batch.** If the previous batch produced no audited
  theorem, counterexample, finite certificate, sharper diagnostic, or strictly smaller crux, treat it
  as a failed decomposition, even if the reports contain many plausible ideas. The next step is
  consolidation or a different methodology, not a larger batch.
- **Use the fractal-frontier stop rule.** If the number of active leaves grows while the distance to
  the theorem does not shrink, freeze the tree, collapse overlapping leaves, and choose at most one
  to three decisive targets with explicit kill/promote criteria. Route proliferation is evidence that
  the problem statement or decomposition is too diffuse.
- **Require route diversity that changes the proof geometry.** Do not spawn several agents to
  "think about the same obstruction from different angles" unless the angles are operationally
  different: algebraic/topological translation, adversarial counterexample search, finite
  certificate design, located literature search, or a special-case proof with a named mechanism.
- **Prefer a clean solo synthesis after low-yield parallelism.** When agents return overlapping
  reductions or terminology, the main agent should write the strongest current theorem/debt pair,
  demote unaudited suggestions to parked evidence, and continue only from the resulting named crux.
- **Treat a subagent batch as a research round, not a brainstorm.** A batch starts from a written
  route packet, has named routes with success/failure criteria, and ends with a merge note. If those
  artifacts would feel too heavy, the target is probably too vague for subagents.
- **Do not spawn into a stale map.** Before launching a batch, freeze the current target in the
  ledger: definitions, hypotheses, reduced crux, known proved tools, killed routes, and the exact
  success/failure criteria for this round. If this cannot be stated crisply, the next action is
  consolidation, not more agents.
- **Split by proof route, not by chronology.** Give each subagent a distinct mathematical target:
  e.g. "prove the rank lemma," "search for a counterexample to the nonaddability lemma," "extract a
  finite certificate table," or "find a dual reformulation." Avoid asking several agents the same
  vague question.
- **Give each subagent a crisp contract.** State the exact object, assumptions, desired output, and
  what would count as success, failure, or a useful reduction. Ask for a theorem/lemma/counterexample
  with proof sketch or a precise blocker, not a general brainstorm.
- **Keep subagent context minimal and independent.** Pass definitions, current reduced targets, and
  raw artifacts, but not your preferred answer or hidden conclusion. This preserves independent
  error checking.
- **Require calibration language.** Each subagent should mark claims as proved, reduced, checked
  computationally, plausible, or refuted. Subagent outputs are not proofs until the main agent audits
  and integrates them.
- **Consolidate immediately.** After subagents return, write a short synthesis: which routes closed,
  which failed, which crux remains, and which artifacts should be ported to the paper, ledger, or
  scripts. Do this before launching the next batch.
- **Treat a low-yield batch as a signal to narrow, not widen.** If several subagents return only
  plausible subroutes, terminology, or overlapping reductions, do not spawn a broader follow-up
  batch. Freeze the sharpest reduced target, demote the broad outputs to `evidence only` or
  `parked`, and require any next subagent packet to ask for a decisive object: a proof of a named
  lemma, a counterexample, a finite certificate schema, or a precise blocker.
- **Audit the frontier after every batch.** Count the active leaves that survived the merge. If the
  number grew but no theorem, counterexample, certificate, or sharper crux was produced, treat the
  batch as negative evidence about the current decomposition. Collapse overlapping leaves, park weak
  analogies, and choose at most one to three high-information next targets.
- **Do not use subagents as momentum.** A fresh batch is justified only when the next routes are
  genuinely independent and have different kill/promote criteria. If the proposed prompts all say
  some version of "think about the same obstruction from another angle," pause for consolidation or
  change methodology instead: algebraic/topological translation, located literature search,
  adversarial diagnostic, or a clean special-case proof.
- **Require a decisive merge question.** Before spawning, write the question that the merge should
  answer, for example "does route A prove lemma L, refute L, or reduce L to named blocker B?" If the
  merge question cannot be stated in one sentence, the packet is not ready.
- **Route IDs prevent drift.** Give each route a stable short name in the ledger and subagent prompt
  (`rank/existence`, `sphere-law`, `finite-certificate`, etc.). Merge outputs by route ID, not by
  the order in which they returned.
- **Retire superseded branches.** If one route closes a target globally, demote local witness
  taxonomies and finite audits to calibration/regression status. Do not keep attacking a branch whose
  purpose has disappeared.
- **Use subagents to create contrast, not volume.** A productive batch should make the merge decision
  easier by returning different kinds of evidence: one proof attempt, one disproof search, one exact
  reformulation, one literature match. A batch whose reports all add more variants of the same local
  reduction should trigger compression, not another batch.

### Subagent packet and merge contract

Every subagent prompt should contain the same minimal packet:

- **Problem statement.** The exact conjecture/lemma, definitions, and parameter range.
- **Allowed artifacts.** The specific ledger, draft, script, table, or theorem labels the agent may
  use. Avoid giving unrelated history.
- **Deliverable format.** Require one of: proved lemma with proof sketch, counterexample with
  smallest witness/mechanism, conditional reduction with named missing lemma, finite certificate
  schema, or "stalled because X".
- **Calibration vocabulary.** Require `proved`, `reduced`, `verified computationally`, `plausible`,
  `refuted`, or `stalled`. Ban "essentially" or "morally" proved.
- **No silent promotion.** Subagent output is raw evidence. The main agent must audit it before
  adding claims to the paper, and must label unaudited claims as such if they are recorded.

After the batch returns, merge before further exploration:

- **Synthesize, then decide.** Write a short route synthesis listing what closed, what failed, what
  remains, and which object is now the smallest crux.
- **Update the source of truth in the same pass.** The ledger gets the live status, the side draft
  gets durable statements, scripts get verifier/regression labels, and the inventory gets navigation
  status. Do not leave a subagent report as the only record of a result.
- **Audit independence.** If two agents prove the same claim by different arguments, compare the
  assumptions. If they disagree, preserve the conflict explicitly instead of averaging the answers.
- **Close the round explicitly.** End the merge note with one of: promote to paper/draft, keep active
  with a named crux, mark stalled with a blocker, or mark refuted with a witness. Never leave the
  status as "continue".
- **Do not batch past a failed decomposition.** If a subagent batch returns many plausible
  reductions but no audited theorem, counterexample, finite certificate, or strictly smaller crux,
  the next action is not "spawn more agents." First rewrite the branch as a proof-contract table:
  original target, current crux, exact/equivalent links, sufficient-only links, lost structure, and
  one decisive next test. Only then decide whether another batch is warranted.

## Keep an inventory and structure the workspace

Long conjecture campaigns accumulate proof routes, exploratory scripts, side drafts, data files,
generated outputs, and literature PDFs. Treat repository organization as part of the research
record, not as cleanup after the fact.

- Maintain a root-level inventory file (for example `EXPLORATION_INVENTORY.md`) that lists every
  active route ledger, exploration script, verifier, side draft, data file, and reference file with a
  one-line purpose and status (`active`, `tool`, `verification`, `historical`, `draft`, `generated`,
  `literature`).
- Whenever adding a new `explore_*.py`, `verify_*.py`, proof route, or side `.tex` file, update the
  inventory in the same pass. The inventory is a navigation map; keep the detailed mathematics in
  `main.tex`, `proof_route_*.md`, or the relevant exploration note.
- Structure the repository by file role once clutter starts obscuring the campaign: keep reusable
  tools and scripts where imports still work; move standalone drafts to a `drafts/` directory,
  reference material to `references/`, and generated build products to `build/` or another explicit
  output directory.
- When moving files, preserve runnable entry points. If Python scripts are moved, update imports or
  add an explicit bootstrap so `python3 <script>` from the documented working directory still works.
- Record reorganizations briefly in the inventory so future route work can find the evidence trail.

## Ledger and draft discipline

The active ledger should be a map of current work, not a diary.

- **Update ledgers by replacement, not sedimentation.** When the state changes, rewrite the relevant
  status block so it says the current truth directly. Do not append "Update:", "Earlier:", "Now:",
  or multiple dated layers unless the chronology itself is evidence for a reusable obstruction.
- **Use one current-state story.** A clean ledger should answer, in order: what is the active target,
  what definitions/hypotheses are in force, what is proved and available, what is ruled out, what is
  the smallest live crux, and what exact next actions could close or refute it.
- **Keep closed material out of the active-open list.** Once a proof is in the paper or a stable
  side draft, mention it only as a closed input. Do not preserve the sequence of attempts that led to
  it; git history carries that archaeology.
- **Do not make the inventory a second ledger.** The inventory should say where artifacts are and
  what role they play. It should not duplicate branch-by-branch mathematical status except as a
  one-line pointer to the active ledger.
- **Use a short ruled-out section instead of repeated warnings.** Record each false shortcut once:
  the false claim, the counterexample or mechanism, and the replacement rule. Delete redundant
  reminders scattered through the active route.
- **Prefer named debts over vague continuation notes.** Replace "continue", "needs work", and
  "maybe try X" by named proof debts with success/failure criteria, such as `PCPI` or
  `PRESCRIBED-MINOR-SURVIVAL_t`.
- **Use explicit source-of-truth roles.** `main.tex` contains theorem-level results and polished
  exposition. Side drafts contain near-paper route syntheses and finite certificates. Ledgers contain
  current targets, statuses, blockers, and next actions. Scripts contain diagnostics and verifiers.
  The inventory is navigation. Skills contain reusable methodology and stable project memory, not
  chronological logs.
- **Start every active ledger with the current reduced targets and definitions.** A reader should see
  the live theorem/question, hypotheses, and exact remaining crux before any historical notes.
- **Separate active, closed, and historical material.** Closed proofs belong in `main.tex` or a clean
  draft. Historical explorations should be kept only if they document a reusable obstruction or a
  counterexample; otherwise they belong in git history, not the active ledger.
- **Promote or delete after each significant round.** When a result becomes theorem-level, port it to
  the paper or synthesis draft, update the inventory, and remove it from the active target list. When
  a route is killed, record the counterexample/mechanism once and stop reopening it.
- **Use side drafts as the bridge from ledger to paper.** For a complicated route, maintain a
  readable `drafts/<route>.tex` with formal definitions, lemmas, dependency map, and finite
  certificate status. Port to `main.tex` only after the draft has stabilized.
- **Keep scripts and docs synchronized.** Every verifier mode or exploration script that becomes part
  of the evidence trail should be named in the inventory with its status: active diagnostic,
  regression check, finite certificate, or historical scratch.
- **After a status-changing insight, update the skill memory if the lesson generalizes.** Examples:
  a new adversary pattern, a global saturation shortcut, a subagent protocol that worked, or a
  documentation convention that prevented stale-route drift.

### State-sync invariants

Use these invariants to prevent the campaign record from splitting across chat, ledgers, drafts, and
scripts.

- **One active target header.** Every active ledger should begin with the current target, definitions,
  reduced cruxes, route statuses, and next actions. Historical notes must not precede the target.
- **Three-way sync for durable evidence.** A reusable finite certificate or diagnostic has a script
  command, a human-readable statement/table in a draft or ledger, and an inventory entry. Missing one
  of the three means the evidence is not yet maintainable.
- **Promotion removes active debt.** When a proof is ported to `main.tex` or a stable side draft, the
  active ledger should stop listing it as open; keep only follow-up questions or reusable
  obstructions.
- **Chat is not storage.** If a statement affects the route status, write it to the ledger or draft
  before relying on it in the next round.

### Round protocol for long campaigns

Use this update order for each significant research round:

- **Before attacking.** Ensure the ledger begins with the active target, definitions, current reduced
  crux, and route status. If the ledger is historical or ambiguous, clean it first.
- **During the round.** Keep scratch computations in scripts or temporary notes, but record only
  reusable mechanisms, counterexamples, finite certificates, and named reductions.
- **After a result.** Promote proved material to `main.tex` or a side draft; demote supporting
  scripts to verifier/regression status; remove closed items from the active ledger.
- **After a failure.** Record the smallest witness, the failed claim, and the mechanism once. Do not
  leave repeated failed attempts in the active section.
- **After a plateau.** Freeze the current state and choose between a consolidation pass, a targeted
  subagent batch, a located literature search, or a new adversarial diagnostic. Do not continue with
  an unnamed "try harder" step.

### State compression audit

Use this audit whenever a campaign has accumulated long drafts, many dashboard leaves, or repeated
cleanup requests.

- **Count active obligations before and after.** Record the number of active theorem obligations,
  conditional lemmas, computational diagnostics, and side-route artifacts. A good consolidation
  should decrease at least one of these counts or replace several weak obligations by one sharper
  crux.
- **Audit conditional depth, not only leaf count.**  If the dashboard has few leaves but the draft
  contains a deep stack of "assuming X, it remains to prove Y" lemmas, count the unproved assumptions
  in the final closure formula.  A pass that moves debt from one conditional lemma to another without
  reducing that count is zero-delta, even if the exposition looks more organized.
- **Separate proof route from exposition route.** A readable 200-page note may still be a poor
  campaign state if it mixes proved facts, failed attempts, definitions, and open questions. Move
  durable facts to a self-contained draft, keep only live blockers in the ledger, and let historical
  attempts survive only as compact warnings or examples.
- **Write the current-state paragraph first.** The first paragraph of a ledger should let a future
  reader answer: what is being proved, what is already proved, what exactly remains, and what would
  count as success or failure in the next round.
- **Promote or park every side route.** After an Alon-style or Grothendieck-style side quest, assign
  one of three outcomes: `promoted` because it changed the proof contract, `parked` because it is
  useful background but not active, or `retired` because it lost the obstruction. Do not leave a side
  route in an ambiguous active state.
- **Prefer a proof-contract table over narrative history.** For each active route, maintain a small
  table with columns `claim`, `status`, `evidence`, `missing step`, and `next decisive test`. This
  is faster to audit than chronological prose and exposes when the campaign is splitting hairs.
- **Use page count as a smell, not a metric.** A growing PDF is not bad by itself, but a growing PDF
  with unchanged active crux usually means side material is being preserved at the wrong fidelity.
  Compress failed explorations to mechanisms, not transcripts.

## Saturation shortcuts before local casework

If a branch asks you to prove that no additional object can satisfy the same local equations
(nonaddability, NAE, incompatibility, maximality), first check whether the existing objects saturate
a sharp global theorem: Sauer, Helly, Kruskal--Katona, Euler characteristic, rank-nullity,
dimension, or a matroid/LP bound. Try the contrapositive: "if the extra object were addable, what
larger class or complex would still avoid the forbidden pattern?" A one-line saturation
contradiction is often better than a large table of local witnesses. In the YangDim
`(m,d)=(6,2)` bridge route, ten oriented outside rows plus one oriented dual row would give `23`
concepts on six coordinates shattering no triple, contradicting Sauer's bound `1+6+15=22`; this
closed the row-local NAE/nonaddability branch and made the bad-partner/no-bad witness taxonomy only
explanatory.

## Plateau protocol: step back without drifting

When work starts looping, do not keep nudging the same proof sketch. A plateau is a signal to change
the scale of the question or the source of ideas while preserving the current evidence.

Trigger a plateau reset when a route has produced no new lemma, counterexample, sharper experiment,
or structural reformulation after a few focused attempts; when the same obstruction recurs under
renaming; or when the next step has become "try harder" rather than a concrete diagnostic question.

- Freeze the current state in writing: exact target, strongest proved core, conditional reductions,
  smallest open crux, known adversaries, killed variants, and the smallest examples where the
  obstruction appears.
- Test special cases for mechanism, not reassurance: low dimension, extremal/minimal cases, boundary
  parameter regimes, equality cases, generic vs. highly symmetric examples, and projections/minors.
  Ask where the current proof becomes trivial, where it first fails, and what feature changes there.
- Revisit the statement itself. Try stronger and weaker forms, equivalent dual statements,
  contrapositive/minimal-counterexample forms, local-to-global variants, quantitative relaxations, and
  versions with extra hypotheses that isolate the missing mechanism.
- Broaden through applications. Ask what the current conjecture or crux lemma would imply in nearby
  domains, what known theorem it would reprove, and where the same object appears under a different
  name. Applications are not only motivation; they often point to the right invariant or proof tool.
- Run a located literature search after naming the obstruction precisely, then also run one broader
  analogy search using the candidate applications and translated formulations. Bring back tools,
  examples, terminology, and known obstructions, not just citations.
- Generate a fresh attack menu before choosing: induction/minimal counterexample, duality, algebraic
  translation, topological translation, probabilistic method, extremal examples, generating
  functions, compactness/limit objects, optimization/duality, or a classification of minimal bad
  instances.
- Alternate proof and testing. Each new vector should get both a proof skeleton and a cheap
  adversarial/computational test. If it fails, record the witness and mechanism immediately; if it
  survives, reduce it to a named crux and return to the normal route discipline.
- End the reset with a finite agenda: the next one to three diagnostics, what outcome would kill or
  promote each route, and what synthesis file or ledger entry must be updated afterward.

## Side quests and cadence

Long reduction trees can become self-sustaining: each step is valid, but the sequence never reaches a
new obstruction, a proof, or a clean counterexample. In that situation, do not keep extending the
same tree indefinitely. Instead, occasionally launch a bounded side quest that changes the
perspective.

- **Use side quests when the current route has become a reduction treadmill.** Signs include the same
  obstruction recurring under renaming, several rounds without a new lemma or witness, or an active
  route whose next step is only "reduce again."
- **Make the side quest genuinely different.** Bring in a different field's language, a dual
  reformulation, a structural analogue, a geometric or algebraic translation, or a fresh literature
  search. The point is not more of the same route in a new wrapper.
- **Keep the side quest bounded.** Give it a clear deliverable, a short time budget, and a success or
  failure criterion. A side quest should produce a theorem, a counterexample, a named blocker, or a
  precise reduction target.
- **Keep the parallel list tight.** At any time, maintain only a small number of live routes and side
  quests. Too many simultaneous explorations dilute attention and make the ledger unreadable. Prefer
  a few high-information branches over a wide fan-out.
- **Pick the cadence deliberately.** Side quests should be occasional, not constant. After a plateau
  or after a fixed number of low-yield rounds, pause the main route, run one or two divergent
  explorations, then consolidate before returning. The cadence should be loose enough to unblock but
  tight enough that the campaign still has a single current state story.
- **Consolidate immediately on return.** Merge the side quest result into the ledger, draft, or
  inventory before launching anything else. If it did not change the status of the main target,
  record that once and retire it.
- **Score the side quest by route movement, not conceptual interest.** A side quest is successful
  only if it yields at least one of: an exact reformulation, a theorem/lemma, a counterexample, a
  named blocker, a sharper falsifier profile, a useful literature match, or a principled reason to
  abandon a route. New vocabulary or a broad analogy is not enough unless it changes the active
  proof contract.
- **Separate "framework value" from "campaign value."** A side quest may produce a useful
  framework that belongs in a companion note, while still not moving the active conjecture. Record
  both statuses explicitly so the campaign does not keep paying for a side theory that has already
  delivered its transferable content.
- **When returning, choose one import to operationalize.** Do not merge a side quest as a list of
  many possible approaches. Pick the one deliverable that will become the next exact crux,
  sufficient route, or falsifier diagnostic; park the rest.
- **Run a before/after audit.** Before the side quest, record the exact active crux and falsifier
  profile. After the side quest, state what changed in that pair. If the answer is "nothing, but we
  have a useful framework," move the framework to a companion note and do not let it remain an
  active campaign branch.
- **Do not reward conceptual novelty without route movement.** A side quest can be intellectually
  interesting and still low-value for the current campaign. Its merge status should be based on
  whether it changes an exact target, proof contract, adversary profile, or literature attribution.

## Terminology hygiene

As a campaign develops, new terms, labels, and local conventions accumulate quickly. A ledger can
become unreadable to anyone who is not already inside the route unless the paper or route draft
periodically absorbs that terminology.

- **Do not let the ledger become a private glossary.** When a route introduces several new objects,
  renameings, or status labels, promote the durable ones into `open_problem.tex`, `main.tex`, or a
  side draft with explicit definitions.
- **Define the terminology before relying on it.** If a term appears in multiple ledger updates, it
  should have a stable definition in a readable TeX file. The ledger can reference it, but should not
  be the only place where the reader can learn what it means.
- **Add intuition and examples with the definitions.** A formal definition alone is often not enough
  once the notation load gets high. Add a short remark, toy example, or geometric/combinatorial
  picture so the term is usable by a non-expert who has not followed every intermediate reduction.
- **Refresh the narrative periodically.** When the live route has accumulated several layers of
  reductions, rewrite the TeX exposition so the current terminology is introduced in one coherent
  place rather than scattered across the ledger history.
- **Treat obscurity as technical debt.** If a route is mathematically clear to the core team but
  unreadable on the page, that is a sign the exposition is lagging behind the reduction tree. Pay
  down that debt before adding more terminology.

## Dashboard discipline

When a campaign has several live branches, maintain a small tree-shaped dashboard as a browser
surface for the current route status. The dashboard is for scanning and navigation, not for
replacement of the ledger.

- **Use the dedicated `conjecture-dashboard` skill.** It owns the tree format, rendering workflow,
  and HTML conventions for the status dashboard.
- **Keep an authored route manifest.** Store the tree in `dashboard.json` and update it in the same
  pass that changes the ledger or TeX files. The dashboard reflects the exploration tree itself, not
  the repository file layout.
- **Make the tree explicit.** Each node should carry a label, a route kind such as route, reduction,
  conjecture, counterexample, or lemma, a status, a short summary, optional links to ledgers or TeX
  sources, and nested children for subroutes.
- **Use the dashboard to show current status, not chronology.** The active/live/proved/refuted state
  should be readable at a glance. Historical branches stay as collapsed or separate nodes, not as a
  flood of update logs.
- **Link every branch to the source of truth.** The dashboard should point to the relevant ledger,
  draft, script, or theorem file. The browser page is the entry point; the linked artifact remains
  authoritative.
- **Let route titles and short descriptions carry math.** If a node label or summary needs inline
  notation, write it directly with LaTeX delimiters and let the renderer typeset it.
- **Expect inline dollar math to be normalized.** The renderer may convert source `$...$` math in
  titles and summaries to explicit inline delimiters in the generated HTML so it stays inline.
- **When a node previews a markdown source, render it as markdown.** If a route needs to show the
  content of a local `.md` file in the dashboard, keep the markdown formatting instead of dumping it
  as escaped text.
- **Let the renderer rewrite markdown links automatically.** Keep the manifest pointed at the source
  `.md` path; the dashboard renderer should generate the preview HTML page and rewrite the link
  target during rendering.
- **Write markdown previews with proper LaTeX delimiters.** If a route note or ledger is meant to be
  read through the dashboard preview, use `$...$`, `$$...$$`, `\(...\)`, or `\[...\]` for math and
  avoid fencing the math as code unless you want to show the literal source.
- **Keep it small enough to read on mobile.** If the tree becomes unwieldy, split it by route family
  or replace the leaf-level details with a link to a dedicated sub-dashboard.
- **Refresh the dashboard when the route tree changes.** A new branch, a status flip, or a promoted
  theorem should trigger the same pass that updates the ledger and the TeX source.

## Working rhythm

- **One focused sub-question at a time.** Before a big push, resolve a sharp diagnostic question
  ("does this hold pointwise?", "is the constant degree-free?") that tells you if you're on the right
  track. Cheap to test, high information.
- **Run proof and disproof as a feedback loop, not separate modes.** A productive round alternates:
  formulate the proof lemma the current route needs; search for the smallest counterexample or
  near-miss to that lemma; extract the structural feature shared by the surviving tests; then sharpen
  the proof lemma or replace it with a better one. If one side stops informing the other, pause and
  restate the active crux.
- **Alternate proof and disproof deliberately.** A counterexample search round should end by asking
  what structure made the tested instances pass and what proof lemma that suggests. A proof-reduction
  round should end by naming the next adversarial diagnostic that could falsify the new crux or show
  it is only a proxy. Do not let computation become standalone scanning, and do not let proof work
  become an unchecked reduction treadmill.
- **Pair every serious search with a proof-route reflection.** A counterexample campaign is not only
  a Boolean hunt for failure. When a search returns no witness, extract the common structural reason
  the instances survived: a conserved parity, a forced orientation, a saturation phenomenon, a
  forbidden local pattern, or a descent mechanism. Turn that observation into a candidate lemma or
  proof-route branch before widening the search.
- **Pair every serious proof step with a disproof diagnostic.** A new reduction, normal form, or
  crux lemma should immediately name the smallest configuration that could make it false, the
  invariant a counterexample would have to preserve, and the script or finite family that should
  stress it. If this cannot be stated, the proof branch is probably not yet sharp enough to be the
  active crux.
- **Make the alternation produce artifacts.** At the end of every search round, record at least one
  proof-facing structural lesson: an invariant that persisted, a local pattern that never appeared, a
  symmetry or compression that survived, or a candidate lemma suggested by the passing instances. At
  the end of every proof round, record at least one disproof-facing diagnostic: the exact implication
  still unproved, the smallest configuration that could falsify it, and the next adversarial family or
  finite case that would be most informative. If searches keep passing, stop treating that only as
  evidence and name the common mechanism behind the passes. If proof branches keep multiplying, pause
  branch expansion until the strongest new crux has been attacked from the disproof side.
- **Consolidate before attacking.** Periodically update the written status so it accurately reflects
  where things stand; an accurate map prevents wasted moves.
- **Report outcomes faithfully**: if a test refutes the plan, say so plainly with the numbers; if a
  step is conditional, label it; when something is proved and verified, state it without hedging.
- **Offer, don't assume, the next direction.** When a route resolves (either way), surface the
  natural next target and let the user steer.

## Campaign operating checklist

For long mathematical campaigns, use an explicit round structure.  This prevents a common failure
mode: the proof state exists only as a chronological chat transcript, while ledgers, drafts, scripts,
and inventory files drift out of sync.

### Round start

- **Name the round target.**  State the exact theorem, conjecture, or crux lemma being attacked, with
  definitions and hypotheses.
- **Identify the active route IDs.**  Each route should have a short stable name, a success condition,
  a failure condition, and the artifact that will receive the result.
- **Check the map before moving.**  If the ledger is stale, historical, or ambiguous, clean it before
  doing new mathematics.  Do not let new exploration accumulate on top of an unclear source of truth.
- **Choose the mode deliberately.**  Use direct proof work for a single sharp route, computation for a
  falsifiable diagnostic, subagents for genuinely independent routes, and consolidation when the
  target itself is no longer crisp.

### Subagent round

- **Spawn only from a written packet.**  A useful packet contains the problem statement, allowed
  artifacts, route-specific deliverable, calibration vocabulary, and what counts as success,
  failure, reduction, or stall.
- **Parallelize independent mathematical routes, not clerical work.**  Good splits are proof route,
  counterexample search, finite certificate design, dual reformulation, or literature/terminology
  lookup after the obstruction is named.
- **Demand auditable outputs.**  A subagent should return a lemma/proof sketch, counterexample,
  conditional reduction, finite schema, or blocker.  Vague suggestions are not mergeable.
- **Merge before the next batch.**  The main agent audits assumptions, resolves conflicts, updates
  the ledger/draft/script/inventory sources of truth, and then decides whether to promote, continue,
  stall, or refute the route.

### Documentation update pass

- **Update by role.**  Put polished results in the paper, near-paper arguments in side drafts, active
  status and blockers in ledgers, commands in scripts, navigation in the inventory, and reusable
  process lessons in skills.
- **Remove closed active debt.**  If a proof is promoted, the ledger should no longer list it as open.
  Keep only follow-up questions, dependencies, or reusable obstructions.
- **Label evidence precisely.**  Use `proved`, `conditional`, `finite certificate`, `verified
  computationally`, `plausible`, `stalled`, or `refuted`.  Avoid "morally proved" and other status
  blur.
- **Keep command provenance.**  If a verifier is part of the evidence trail, document the exact
  command and what it checks; if it becomes a regression check after a hand proof, say so.

### Pause and audit

- **Pause after repeated low-yield iterations.**  If several attempts produce no new lemma,
  counterexample, sharper diagnostic, or cleaner reduction, stop the attack and write a status audit.
- **Audit the target.**  Ask whether the active crux is still equivalent to the original goal, whether
  any route has been superseded by a global argument, and whether finite evidence is being mistaken
  for proof.
- **Walk back a long rabbit hole before adding another reduction.**  Write the current branch as a
  chain `L0 -> L1 -> ... -> Lk`, from the original theorem to the present crux.  For each link, mark
  whether it is an equivalence, a sufficient condition, a special case, or only a heuristic; record
  what structure it preserves, what structure it discards, and what would make the link worth
  continuing.
- **Audit the branch contract, not only the endpoint.**  For each arrow in the chain, state the
  direction actually needed for the theorem, the exact evidence supporting that arrow, and the first
  mathematical feature that may have been lost by passing to the next layer.  If two consecutive
  arrows are only sufficient conditions or local normal forms, treat further refinement as suspicious:
  either name a strict kill/promote test, retreat to the last exact/equivalent layer, or launch a
  bounded side quest with a genuinely different proof geometry.
- **Reopen the forks deliberately.**  At each old branching point, list the alternatives that were
  bypassed or parked: direct structural proof, dual/complement form, algebraic or topological
  translation, extremal/Sauer saturation, finite certificate route, located literature route, or a
  simpler special case.  Do not keep extending a narrow local crux until this list has been checked.
- **End the walkback with a decision packet.**  Choose one of: continue the current crux with a named
  success/failure test, retreat to an earlier layer, launch a bounded side quest with a different
  proof geometry, rewrite the source-of-truth draft, or park the branch.  Record the packet in the
  ledger or route draft; chat is not storage.
- **Audit the artifacts.**  Check that the active ledger is not chronological clutter, the side draft
  contains durable statements, scripts have clear verifier/regression status, and the inventory can
  guide a future reader to the current state.
- **Choose the next route from the audit.**  The next action should be one of: prove a named crux,
  falsify it with an adversarial diagnostic, spawn a route-specific subagent batch, run a located
  literature search, or consolidate further.  Avoid the unnamed instruction "continue trying."

### Artifact lifecycle for each research round

Use a small number of durable artifacts, each with a fixed role.  A round is not really closed until
the artifacts agree.

- **Create a route packet before parallel work.**  Put it in the active ledger or route draft before
  spawning subagents or running a broad computational sweep.  The packet should contain: round ID,
  route IDs, exact target, definitions, proved tools allowed for reuse, known false shortcuts,
  artifacts to inspect, and success/failure/stall criteria.
- **Choose side documents by stability.**  Use the active ledger for current status and blockers.  Use
  a side draft when a route has stable definitions, lemmas, certificate tables, or proof sketches that
  should be readable linearly.  Use scripts for reproducible diagnostics.  Use the inventory only for
  navigation.  Do not create a new document for chronological scratch.
- **Subagent reports are raw inputs, not state.**  Merge them by route ID.  Extract proved statements,
  counterexamples, finite certificate schemas, or precise blockers.  Do not leave the raw report as
  the only record of a claim, and do not promote a subagent claim without a main-agent audit.
- **Close with a merge packet.**  After a batch or significant result, write a short merge note:
  routes closed, routes refuted, routes reduced, routes stalled, current smallest crux, and where each
  artifact was updated.  End with one of `promote`, `continue on named crux`, `spawn next packet`,
  `park/stall`, or `refuted`.
- **Sync in one pass.**  Durable evidence should update the relevant script command, the ledger
  status, the side draft or paper statement, and the inventory entry in the same editing pass.  If one
  item cannot be updated yet, record explicit `sync debt` in the ledger instead of relying on chat.
- **Retire closed chronology.**  Once a proof is in the paper or a stable side draft, remove it from
  the active-open list.  Keep only reusable obstructions, counterexamples, or regression commands; let
  git history carry the rest.
- **Update skills only for reusable process lessons.**  Add to a skill when the lesson changes future
  behavior across rounds: a better subagent protocol, a documentation invariant, a recurring
  adversary pattern, or a stale-ledger failure mode.  Do not record round chronology in skills.

Route packet template:

```text
Round:
Target:
Definitions/hypotheses:
Allowed proved tools:
Known false shortcuts:
Routes:
Artifacts:
Success / failure / stall criteria:
Merge destination:
```

## Proof/disproof alternation discipline

When a route spends several iterations on counterexample search, alternate deliberately with proof-route reflection instead of only widening the search frontier.

- Maintain two synchronized artifacts for each active route: a proof-side invariant or reduction that would close the route, and a disproof-side adversary profile that tries to violate exactly that invariant.
- Use failed counterexample searches as structure: record the forbidden local pattern, forced witness, or narrowed residue they expose, not just that no example was found.
- Use every proof bottleneck to generate sharper counterexample tests: if the proof needs a descent, faithfulness, uniqueness, or exchange claim, search specifically for the smallest object where that claim fails while all accepted exits are blocked.
- End every serious counterexample-search report with a proof-facing sentence: "the surviving instances suggest lemma/invariant X because mechanism Y persists." If there is no such sentence, the search was too broad or too observational to guide the proof route.
- End every serious proof-reduction report with a disproof-facing sentence: "the new crux would fail first in configuration Z, so the next diagnostic should stress feature W." If no falsifier profile can be named, the crux is probably not sharp enough yet.
- When proof and disproof stop informing each other, do not create more leaves. Freeze the current pair of artifacts, walk back to the last exact/equivalent reduction, and either sharpen the active crux or switch viewpoint.
- Periodically run a route walkback: ask whether the current adversary profile still attacks the original problem, whether the proof invariant has become too technical to be illuminating, and whether a different algebraic, topological, or combinatorial viewpoint should be tried before splitting more leaves.

## Methodology lessons from multi-route campaigns

Use these constraints after a campaign has already gone through several proof attempts, false
routes, subagent batches, side quests, and consolidation passes.  They are meant to improve speed by
reducing live state, not by adding more process paperwork.

### Methodology review after repeated false starts

Use this when the user explicitly asks for a methodological pause, or when the campaign shows the
same symptoms repeatedly: long PDFs, verbose dashboards, many active leaves, repeated cleanup
requests, or a feeling that several rounds have not changed the theorem.

- **Review the process, not only the mathematics.**  Classify the last few rounds by their actual
  output: proof-contract delta, useful diagnostic, side-route blindness statement, exposition-only
  cleanup, or no movement.  If most rounds are diagnostics or cleanup, the active frontier is too
  diffuse.
- **Separate reusable process lessons from local history.**  Skills should receive only rules that
  change future behavior.  Do not copy route names, failed case trees, or campaign chronology into a
  skill.  Put durable mathematics in TeX, current state in the ledger/dashboard, and history in git
  or a compact archive note.
- **Prefer gates over advice.**  A lesson is useful only when it changes what is allowed next:
  require a before/after contract, cap side-route repair attempts, demand orthogonal subagent
  packets, prohibit dashboard expansion without a deletion dividend, or force a walkback after two
  zero-delta rounds.
- **Treat overgrown artifacts as evidence.**  A 200-page focused note or a dashboard with many live
  leaves is not just a formatting problem.  It usually means the proof spine is storing campaign
  memory, side explorations, or sufficient-only proxies at the same fidelity as proved mathematics.
- **Do not let reconsolidation become a loop.**  If the same branch needs another cleanup soon after
  being cleaned, walk back to the last exact/equivalent target and decide whether the current route
  is still exact, merely sufficient, merely diagnostic, or stalled.
- **Require method imports to be assays.**  Alon-style and Grothendieck-style side routes should test
  whether an external encoding or new abstraction sees the current normalized obstruction.  If it
  does not, the output is a blindness statement and possibly a native feature to preserve, not a new
  subtree.
- **Use subagents to diversify evidence, not vocabulary.**  Launch parallel agents only with
  incompatible contracts such as proof attempt, disproof search, finite diagnostic, literature
  exact-match, and abstraction descent.  Merge them by deleting, merging, parking, or relabeling
  active debt.
- **End the pause with one state change.**  A methodology review should install or update a gate,
  compress the active state, park a route, merge leaves, or choose one decisive next test.  If it
  only produces reflections, it has not improved speed.

Methodology review packet:

```text
Observed symptoms:
Last rounds classified by output:
State-model failure:
Rules/gates to install:
Artifacts to compress or separate:
One next mathematical move:
One state item to delete/merge/park:
```

### Plateau-response operating system

Use this when the campaign has accumulated many attempts, false starts, side routes, and
re-consolidations.  The goal is to make the next round faster by changing the research operating
system, not by adding another layer of history.

- **Treat repetition as a signal, not an annoyance.**  If the same requests recur--cleanup,
  dashboard compactness, self-contained definitions, "are we making progress?", or "what is the
  current reduced target?"--assume the source-of-truth structure is failing.  Repair the state model
  before proving another local lemma.
- **Separate four kinds of output immediately.**  Durable mathematics goes in the proof spine.
  Current proof debt goes in the ledger/dashboard.  Method lessons go in skills.  Historical route
  attempts go in git history or a compact archive warning.  Do not let any one artifact serve all
  four roles.
- **Install gates, not advice.**  A methodological lesson should become a future constraint:
  no new leaf without a deletion target, no side route without a native export, no subagent batch
  without orthogonal evidence contracts, no third refinement of a proxy before walkback, and no
  proof-spine growth without proof-debt movement.
- **Prefer exact reduced targets over impressive local structure.**  After several reductions, ask
  whether the current object is equivalent to the original target, merely sufficient, merely
  necessary, or only diagnostic.  Refining a non-exact proxy is the fastest way to produce a long
  note with little theorem progress.
- **Use proof and disproof as a closed loop.**  Every proof step should state the smallest surviving
  falsifier profile.  Every failed counterexample search should state the structural feature it
  repeatedly failed to realize.  If neither side changes the other, stop expanding and walk back.
- **Run method side quests as assays.**  Alon-style and Grothendieck-style detours should first test
  whether the method sees the current normalized obstruction.  If it does not, the output is a
  blindness statement and the route should be parked, not widened.
- **Make subagents produce incompatible evidence types.**  Parallelism helps when agents have
  orthogonal contracts: proof, disproof, finite diagnostic, literature exact-match, abstraction
  descent.  It is low-yield when agents enumerate nearby cases or invent overlapping vocabulary.
- **Compact by deleting, merging, or demoting.**  Consolidation is only successful if the active
  tree is smaller or sharper afterward.  A polished version of the same sprawling state has not
  improved the campaign.

Minimal plateau packet:

```text
Repeated symptom:
Likely state-model failure:
Last exact/equivalent target:
Current non-exact proxies:
What must be deleted/merged/parked:
One decisive next move:
Gate installed for future rounds:
```

### Recent campaign-retrospective rules

Apply these rules after several rounds have produced useful local facts but the main theorem still
feels unmoved.

- **Run a state-growth audit before another proof round.**  If the PDF length, dashboard leaf count,
  terminology count, or number of side files has grown while the exact target and smallest falsifier
  profile are unchanged, treat this as negative methodological evidence.  The next move should be
  compression, counterexample search, theorem import, or proof-geometry change--not another local
  refinement.
- **Measure every round by before/after contract delta.**  At the beginning of the round, write the
  active proof-debt row, its direction, and its smallest falsifier profile.  At the end, write what
  changed.  Valid deltas are: proved row, refuted row, equivalent reformulation, sharper falsifier,
  imported theorem, proxy killed, leaves merged, route parked, or explicit blindness statement.
  Anything else is background and should not expand the active dashboard.
- **When reconsolidation repeats, redesign the frontier.**  Repeated cleanup of the same branch means
  the working frontier is probably too wide, too local, or not equivalent to the target.  Walk back
  to the last exact/equivalent statement, name what structure was lost in each reduction, and choose
  whether to retreat, attack a counterexample, import a theorem, or replace the proof geometry.
- **Do not preserve campaign memory at proof fidelity.**  A side route, failed proxy, or subagent
  report should survive as a theorem, counterexample, diagnostic, or one compact warning.  If it is
  being kept only because it was expensive to discover, demote it; git history is the archive.
- **Make every side route pay a deletion dividend.**  Alon-style, Grothendieck-style, literature, and
  computational detours must return one native export and say which proof-debt row is proved,
  sharpened, merged, parked, or killed.  If the export is only better vocabulary or atmosphere, record
  it as background and keep it off the active tree.
- **Use subagents only after the decomposition is stated.**  Spawn agents from a packet that assigns
  orthogonal evidence contracts--proof, disproof, finite diagnostic, exact reformulation, or located
  literature.  If the merge produces overlapping terminology rather than audited evidence, treat the
  batch as a failed decomposition and consolidate before spawning again.
- **Distinguish mathematical progress from state growth.**  A long note, many dashboard leaves, or
  many named obstructions can mean the campaign is remembering work rather than converging.  Count a
  round as progress only if it changes the proof contract: proves a row, refutes a row, imports an
  exact theorem, shrinks the smallest falsifier, merges leaves, or identifies a native invariant that
  replaces cases.
- **Consolidate by compression, not by transcription.**  Do not rewrite every attempt into cleaner
  prose.  Keep durable facts, current debts, and compact warnings; demote failed routes to one-line
  diagnostics unless their counterexample or obstruction is reusable.
- **Require proof-contract deltas from side routes.**  Alon-style and Grothendieck-style passes are
  helpful only when they return a native lemma, obstruction, exact reformulation, diagnostic, or
  proxy-kill.  If they only produce a better conceptual story, record that as background and return
  to the active crux.
- **Use repeated reconsolidation as a stop signal.**  If the same cleanup is needed repeatedly, the
  issue is usually not exposition but an over-large or non-exact frontier.  Walk back to the last
  equivalence, name the current falsifier profile, and decide whether to prove, disprove, import, or
  retire the branch before adding terminology.
- **Make subagents orthogonal and merge by deletion.**  Parallel agents should seek different
  evidence types, not enumerate nearby subcases.  Their reports are raw material until the main
  proof state deletes, merges, or relabels active debt.
- **Prefer one invariant over many local labels.**  When the active leaves proliferate into local
  gadgets, atom types, or certificate subcases, stop splitting and ask for the invariant, exact
  sequence, obstruction class, potential, or dual certificate common to the survivors.
- **Keep failed methods low-fidelity.**  A failed imported method or false proof route should leave
  a precise blindness statement such as "this quotient forgets endpoint signs" or "this topology does
  not see support."  It should not leave a long active branch.
- **Resume from pauses with one decisive test.**  After a methodological pause, the next move should
  name one proof row and one success/failure condition.  Avoid restarting with broad exploration
  unless the audit shows the current frontier is not exact.

### Lessons from repeated consolidation cycles

Use these when a campaign has repeatedly produced good local mathematics but still leaves the same
top-level question open.  The goal is to accelerate by preventing the live state from becoming a
memory palace of previous attempts.

- **Treat repeated cleanup as a failed convergence signal.**  If the same note, dashboard, or route
  tree needs cleanup more than once, assume the frontier is over-wide, non-exact, or preserving
  historical debt.  The next move is not another local lemma; it is to recover the last
  exact/equivalent target and rewrite the active proof contract.
- **Separate durable facts from campaign scaffolding immediately.**  Stable definitions, examples,
  propositions, and proofs go into a proof spine.  Current blockers go into a proof-debt table.
  Failed routes, side quests, and subagent reports survive only as compact warnings, blindness
  statements, or counterexamples.  Do not keep all three at proof-level fidelity.
- **Require a deletion dividend before adding terminology.**  A new name, case family, obstruction
  class, or dashboard node is allowed only if it deletes, merges, or strictly sharpens existing
  active debt.  Otherwise it is private scratch or background, not campaign state.
- **Walk back before the third refinement of a proxy.**  After two refinements of a sufficient-only
  condition, local normal form, or diagnostic proxy, stop and mark the chain from the original
  conjecture to the current object.  Continuing is justified only if the current object is
  equivalent, gives a falsifier profile for the original theorem, or has a kill/promote test.
- **Use side routes as stress tests of the proof contract.**  An Alon-style or Grothendieck-style
  pass should answer: which native feature was invisible to the old route, and did the new method see
  it?  If the answer is no, record the lost feature and retire the side route rather than expanding
  the method menu.
- **Make subagent batches smaller but more orthogonal.**  Spawn agents only after assigning distinct
  evidence contracts such as proof, disproof, finite diagnostic, literature exact-match, or
  abstraction descent.  If two agents can plausibly write the same definitions, the split is not
  orthogonal enough.
- **Prefer one exact obstruction over many plausible mechanisms.**  When many mechanisms explain
  examples, choose the one that is checkable against the smallest survivor or counterexample profile.
  Mechanisms that do not discriminate the current survivor are explanatory background.
- **End every pause with an irreversible state change.**  A methodological pause should delete a
  leaf, merge rows, park a side theory, demote a proxy, or replace the active target by a sharper
  equivalent statement.  If the active tree is unchanged, the pause has not improved speed.

- **Treat active-state size as a mathematical signal.**  A large proof PDF, verbose dashboard, or
  repeated need for cleanup usually means the current proof contract is too diffuse.  Before doing
  another local refinement, identify whether the growth came from durable theorems, inherited debt
  being duplicated, sufficient-only proxies being treated as exact, or side routes that never
  exported a native object.
- **Require a contract delta for every round.**  A round should end by changing one row in the proof
  contract: prove it, refute it, make it equivalent to a sharper target, shrink the smallest
  falsifier, demote a proxy, import a theorem, or retire a route.  If none of these happened, record
  at most a compact warning and do not expand the dashboard or proof spine.
- **Prefer exactness over refinement.**  Once a route has drifted into a sufficient condition,
  local normal form, or special certificate, stop refining it until the relationship to the original
  target is marked as equivalent, necessary, sufficient, or heuristic.  Refining a non-exact proxy is
  the most common way to create impressive-looking but nonconvergent progress.
- **Make side quests answer a native question.**  Alon-style, Grothendieck-style, literature, and
  computational side routes should be launched against the current normalized obstruction or
  proof-debt row, not against the whole theorem.  Their merge packet must say what native object
  changed; otherwise the result is background.
- **Use consolidation to delete, not preserve, history.**  Consolidation should keep a forward proof
  spine, a current proof-debt table, compact dead-end warnings, and reproducible diagnostics.  It
  should not rewrite every historical attempt at higher polish.  Git history can preserve chronology;
  the ledger should preserve current state.
- **Spawn subagents only with orthogonal evidence contracts.**  Parallel agents are useful when one
  seeks a proof, one seeks a counterexample, one checks literature, and one tests a finite
  diagnostic.  They are low-yield when all agents enumerate nearby subcases of the same proxy.  The
  merge must collapse or relabel active debt before another batch is spawned.
- **Walk back before adding a third layer of local taxonomy.**  If a branch has generated labels
  like case families, atom profiles, bead types, or certificate subclasses without closing a row,
  write the chain back to the last exact target and decide whether a missing invariant, a disproof
  construction, or a different proof geometry is needed.
- **Distinguish durable mathematics from campaign memory.**  Durable definitions, lemmas, examples,
  and proofs belong in TeX.  Current blockers and proof-debt status belong in the ledger/dashboard.
  Raw attempts, failed branches, and subagent reports should be compressed into warnings or deleted
  from active state after their lesson is extracted.
- **Use no-progress as data.**  If multiple methods fail to see the same obstruction, name the
  native feature they forget--for example signs, endpoints, support, rank, orientation, boundary
  data, or compatibility around cycles.  That forgotten feature is often the next invariant to seek,
  not a reason to broaden the search indiscriminately.
- **Resume with one decisive move.**  After any pause or cleanup, the next action should be one
  named proof attempt, counterexample search, theorem import, or walkback decision with a visible
  success/failure criterion.  Do not resume with an unscoped instruction to continue exploring.
