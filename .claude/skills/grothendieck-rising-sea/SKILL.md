---
name: grothendieck-rising-sea
description: >-
  Attack a mathematical problem by progressively abstracting it in the spirit of
  Grothendieck's rising sea: invent the right objects, morphisms, functorial
  operations, invariants, universal properties, and structural theorems until
  the original problem becomes a special case or shadow of a broader theory. Use
  this skill when direct estimates or casework keep reproducing the same
  obstruction, when many examples suggest a missing category/geometry/invariant,
  or when the problem should dissolve into a better conceptual framework rather
  than be solved by a single imported theorem.
---

# Grothendieck Rising Sea

Use this skill when the direct route is too cramped: the objects are named in the wrong language, the
same diagrams recur without a unifying invariant, or a proof would become clear if the problem lived
in a more natural category.

This complements `alon-method`: Alon-style work imports an external theorem; Grothendieck-style work
builds a new ambient theory in which the theorem becomes natural.

## Core Principle

Do not only strengthen the lemma. Raise the level of abstraction until:

- the current objects are instances of a more natural class;
- the operations become functorial rather than ad hoc;
- examples and counterexamples are explained by universal properties or invariants;
- the original conjecture becomes a corollary of a structural theorem.

The goal is not abstraction for style. The abstraction must reduce proof debt by making invisible
structure explicit.

## Rising-Sea Workflow

1. **Collect recurring structure.** List the operations, diagrams, restrictions, dualities,
   equivalences, examples, and failed case splits that keep appearing.
2. **Name the objects and morphisms.** Define the category, class, geometry, algebra, or invariant
   that treats those recurring features as primitive.
3. **State functorial laws.** Write how the new objects behave under restriction, quotient,
   product, gluing, duality, localization, completion, limits, or base change.
4. **Find universal properties.** Ask whether the construction is initial, terminal, free,
   cofree, adjoint, representable, a sheafification, a completion, or a localization.
5. **Lift the conjecture.** Reformulate the original target in the new language. Mark whether the
   lift is equivalent, stronger, weaker, or only a sufficient condition.
6. **Prove structural theorems first.** Before attacking the original statement, prove the ambient
   theory's natural lemmas: exactness, descent, gluing, invariance, classification of basic objects,
   representability, positivity, or comparison theorems.
7. **Descend carefully.** Translate the abstract theorem back and check that no hypothesis,
   finiteness condition, or equivalence direction was silently lost.

## Abstraction Moves

- **Categorify the data.** Replace objects by a category where maps, products, quotients, and
  restrictions are visible.
- **Sheafify local information.** When local conditions fail to assemble, encode compatible local
  data and descent as a sheaf-like object.
- **Add the missing morphisms.** If the class is not stable under natural operations, enlarge it
  until closure becomes a theorem rather than an exception.
- **Replace points by functors.** Study an object through all probes into it, especially when
  ordinary points miss nilpotent, infinitesimal, generic, or boundary behavior.
- **Build moduli or parameter objects.** If many examples differ by the same hidden choices, make
  those choices coordinates on a classifying object.
- **Localize or complete.** Invert harmless maps, complete along the relevant filtration, or pass to
  a limit where the obstruction becomes structural.
- **Search for comparison theorems.** Relate the new invariant to older invariants so the new
  language is not isolated from known facts.

## Discipline Against Empty Abstraction

- Every new definition must explain at least two old phenomena: a proof step, counterexample, exact
  operation, family of examples, or obstruction.
- Track the lift direction. A beautiful stronger statement that no longer implies the target is a
  side theory, not a solution.
- Keep a small stock of test examples and counterexamples and reinterpret each new definition on
  them immediately.
- Avoid introducing a category when a named invariant or normal form would suffice.
- If abstraction only changes terminology and does not create new lemmas, stop and return to a more
  concrete route.
- Do not let the framework become the campaign. If the abstraction produces a useful companion
  theory but no movement on the active conjecture, record the theory as a side deliverable and
  return to the exact obstruction.

## Descent and ROI Checks

Rising-sea work should make repeated local structure primitive, then descend quickly. In a congested
campaign, abstraction is justified only when it compresses active state.

### Methodology lesson from overgrown abstractions

When a campaign has many definitions, notes, and route branches, use abstraction to compress the
frontier rather than to organize the archive.

- **Abstract the recurring obstruction, not the historical document.**  The input is the repeated
  compatibility failure, survivor profile, or duplicated proof-debt row, not every object introduced
  during the campaign.
- **Name the deletion target first.**  Before defining a new category, invariant, complex, or
  universal property, list the local cases, labels, diagrams, or dashboard leaves it is meant to
  replace.
- **Demand first descent before second language.**  After one abstraction layer, the next output must
  be a native comparison theorem, obstruction criterion, descent criterion, normal form, or blindness
  statement.  Do not add a second abstraction layer first.
- **Track lift direction immediately.**  Mark the abstract statement as equivalent, necessary,
  sufficient, stronger, weaker, or heuristic.  Do not refine a sufficient-only framework without a
  kill/promote test.
- **Park non-descending theory.**  If the framework explains examples but does not change a native
  proof-debt row, keep it as companion structure and remove it from the active dashboard.

### Fast abstraction protocol

Use this when a mature campaign is producing many cases, definitions, or local certificates without
closing the main proof debt.

```text
Native crux:
Repeated failures:
State to delete:
New invariant/object:
Lift direction:
First native theorem:
Descent result:
Delete / merge / park:
```

- **Delete before enriching.**  Name the labels, cases, diagrams, or proof-debt rows the abstraction
  is meant to replace before introducing the new object.  If nothing will be deleted, the framework
  is exposition.
- **First theorem before second layer.**  After one abstraction layer, prove or refute one native
  comparison theorem, obstruction criterion, descent criterion, normal form, or blindness statement
  before adding more terminology.
- **Track lift direction immediately.**  Mark whether the abstract statement is equivalent,
  necessary, sufficient, stronger, weaker, or heuristic at the point where it is introduced.
- **Park non-descending theory.**  A coherent framework that does not change a proof-debt row should
  become a companion viewpoint, not an active dashboard branch.

### Lessons from abstraction detours

Use these constraints when a campaign has already accumulated many definitions, route notes, and
case labels.

- **Abstract the obstruction, not the archive.** The input to a rising-sea pass is the smallest
  current falsifier profile or repeated compatibility failure, not everything remembered by the
  campaign. A framework for the whole archive is usually too large to descend.
- **Name the deletion target before the object.** Before introducing a category, invariant, complex,
  or universal property, list the cases, labels, proof-debt rows, or diagrams it is supposed to
  replace. If no old state can be deleted, the abstraction is exposition rather than proof progress.
- **Demand a first native theorem.** After one new abstraction layer, the next mergeable result must
  be a comparison theorem, descent criterion, obstruction criterion, normal form, or blindness
  statement in the original language. Do not add a second layer of terminology first.
- **Track lift direction explicitly.** Mark the abstract target as equivalent, necessary,
  sufficient, stronger, weaker, or heuristic. Refining a sufficient-only lift without a kill/promote
  test is a standard way to create nonconvergent proof debt.
- **Treat failed descent as information.** If the framework cannot descend, identify the native
  feature it forgot: endpoints, signs, support, orientation, rank, boundary data, deletion behavior,
  or cycle compatibility. That feature becomes the next native invariant or proof target.
- **Park companion theory quickly.** A coherent framework that explains examples but does not change
  a proof-debt row should be written as a parked companion viewpoint, not kept as an active dashboard
  branch.

### Mature-campaign abstraction gate

- **Abstract from repeated obstruction forms.** Start with the local gadgets, compatibility failures,
  certificate types, or falsifier profiles that keep reappearing. Do not abstract from the whole
  historical draft.
- **Name the failure mode before naming objects.** State which labels, cases, or diagrams the new
  framework is meant to replace. If no old state will be deleted, the abstraction is probably
  exposition.
- **Record the before-state as a deletion target.** Before introducing a new object, list the active
  labels, cases, or proof-debt rows the abstraction is supposed to merge or remove. If this list is
  empty, the move is background theory rather than a campaign route.
- **First theorem before second layer.** After introducing one object, invariant, or category, prove
  or refute one comparison theorem, descent criterion, obstruction criterion, exactness statement, or
  normal form before adding more terminology.
- **Classify the lift direction.** Mark the abstract formulation as equivalent, necessary,
  sufficient, stronger, weaker, or heuristic. Do not iterate inside a sufficient-only lift without a
  kill/promote test.
- **Require native descent.** The first structural theorem must yield a statement in the original
  language and identify the proof-debt row it changes. Without that native corollary, park the
  framework as background.
- **Demand a deletion dividend.** A successful abstraction deletes local labels, merges proof-debt
  rows, or replaces several cases by one invariant, functorial law, obstruction class, or descent
  criterion. Cleaner vocabulary with the same blockers is not proof progress.
- **Keep the first abstraction layer accountable.** If the new framework needs a second layer of
  definitions before proving any comparison theorem, pause and ask whether a single invariant,
  exact sequence, or normal form would have captured the same structure with less debt.
- **Use failed descent as invariant discovery.** If the framework is blind, record exactly which
  native structure it forgot: signs, endpoints, support, rank, boundary orientation, deletion
  behavior, or cycle compatibility. That forgotten feature is the next invariant to seek, not a
  license for another abstraction layer.

### Fast descent audit

Before preserving a framework as active, write:

```text
Original crux:
Repeated structures being replaced:
New object/invariant:
First structural theorem:
Lift direction:
Native corollary:
Proof debt changed:
State deleted or merged:
First-theorem deadline:
Promote / park / retire:
```

If `State deleted or merged` is empty, the default decision is `park` or `retire`, not `continue`.

### Merge discipline after abstraction

- **First theorem before second framework.** After introducing a new object, category, invariant, or
  functorial viewpoint, the next mergeable output must be a native comparison theorem, descent
  criterion, obstruction class, normal form, or blindness statement. Do not add a second abstraction
  layer before this first theorem exists.
- **Delete the old taxonomy.** A successful rising-sea pass should replace several local labels,
  cases, or proof-debt rows by one invariant or structural theorem. If the old taxonomy remains
  active unchanged, the abstraction is exposition, not campaign progress.
- **Park useful theory that does not descend.** If the new framework is coherent but does not change
  the original proof contract, record it as a companion viewpoint and return to the exact crux. Do
  not keep it in the active tree because it feels conceptually promising.

### Learned ROI rules for mature campaigns

- **Abstraction must pay rent quickly.** In a mature campaign, a new object, category, complex,
  sheaf, or invariant should produce a first comparison theorem, descent criterion, obstruction
  class, or normal form before any second abstraction layer is introduced.
- **Abstract to delete local state, not to rename it.** Before introducing a framework, list the
  cases, labels, dashboard leaves, or proof-debt rows it is meant to replace. If the abstraction only
  organizes the same obligations under better names, park it as exposition instead of treating it as
  an active route.
- **Start from repeated failures.** The right rising-sea object usually comes from the structure that
  several failed routes could not control--for example endpoint compatibility, support minimality,
  cycle holonomy, boundary orientation, or quotient exactness. Do not abstract from the accumulated
  prose of the campaign; abstract from the recurring obstruction.
- **Demand native descent after the first theorem.** The first comparison theorem, obstruction class,
  or normal form must immediately imply a statement in the original problem language and change a
  proof-debt row. If descent requires another layer of terminology, stop and look for a smaller
  invariant.
- **Abstract from repeated failures, not from accumulated prose.** The input to a rising-sea pass is
  the recurring obstruction pattern or duplicated proof-debt rows, not the full historical draft. If
  no old labels, cases, or leaves will be deleted, the abstraction is likely exposition rather than
  proof progress.
- **Record lost structure when descent fails.** A failed framework is useful when it identifies the
  native feature it cannot see--signs, endpoints, support, rank, orientation, deletion behavior,
  boundary data, or cycle compatibility. That blindness statement should replace the framework as the
  active output unless a repair lemma is immediately available.
- **Park useful theories that do not descend.** A framework may be mathematically valuable and still
  not close the current campaign. Preserve it as background or a companion note, but do not keep it
  as an active leaf unless it changes a proof-debt row in the original language.
- **Use a first-theorem deadline.** In a mature campaign, the first abstraction layer must quickly
  produce one comparison theorem, obstruction class, descent criterion, or normal form in the native
  language. If it needs a second layer of terminology before any such theorem appears, stop and ask
  for a smaller invariant.
- **Make the deletion target explicit.** Before preserving a new framework, name the old cases,
  labels, or proof-debt rows it eliminates. If the abstraction explains the same material while
  leaving all obligations active, it is expository background rather than campaign progress.
- **Separate companion theory from active route.** A useful framework that does not descend should
  be written as a parked companion note or terminology guide. It should not remain in the dashboard
  unless it has a native proof-debt row and a kill/promote criterion.
- **Abstract the recurring obstruction, not the accumulated document.** Long ledgers and repeated
  cleanups tempt one to build a framework for everything that has been said. Instead, choose the
  smallest obstruction that survived the latest exact reduction and make only the structure needed
  for that obstruction primitive.
- **Use the first abstraction as a compression test.** The new language should replace several
  active labels, cases, or diagrams by one invariant, exact sequence, descent criterion, or universal
  property. If the old labels still have to remain active, the abstraction has not compressed the
  campaign.
- **Treat non-descending theory as a side result, not a live proof route.** A framework can be
  mathematically interesting and still fail to close the current conjecture. If it does not produce a
  native corollary or sharper obstruction after its first comparison theorem, park it as companion
  structure and return to the exact target.
- **Use abstraction to compress the live frontier.** Before introducing a new object or category,
  name the duplicated labels, cases, diagrams, or proof-debt rows it is meant to replace. If the old
  local taxonomy remains active after the abstraction, the framework is exposition rather than
  progress on the campaign.
- **Run descent before enrichment.** The first abstraction layer must produce a native comparison,
  obstruction, or blindness statement before adding a second layer of terminology. If descent fails,
  record the native feature that the framework forgot and return to the exact crux rather than
  enriching the framework.
- **Separate companion theory from active proof state.** A useful conceptual framework may deserve a
  side note, but it should stay off the active dashboard unless it changes a proof-debt row in the
  original language and has a clear kill/promote criterion.

### Retrospective lessons for abstraction detours

Use these when repeated local reductions suggest a missing framework but previous abstraction
attempts did not close the campaign.

- **Abstract the recurring obstruction, not the archive.**  The input should be the smallest current
  falsifier profile or repeated compatibility failure, not the accumulated historical document.  A
  framework for everything remembered by the campaign is usually too large to descend.
- **State the deletion target before defining the object.**  Name the local labels, cases, diagrams,
  or proof-debt rows that the new invariant or category is supposed to replace.  If no state can be
  deleted, the framework is exposition.
- **Demand a first native theorem.**  After one new object or invariant, the next output must be a
  comparison theorem, descent criterion, obstruction criterion, normal form, or blindness statement
  in the original language.  Do not add a second abstraction layer first.
- **Track lift direction on the first page.**  Mark the abstract statement as equivalent,
  necessary, sufficient, stronger, weaker, or heuristic.  Refining a beautiful but sufficient-only
  lift is a common way to generate nonconvergent proof debt.
- **Treat failed descent as information.**  If the framework cannot descend, identify the native
  feature it forgot: endpoints, signs, support, orientation, rank, boundary data, deletion behavior,
  or cycle compatibility.  That feature becomes the next invariant or native proof target.
- **Park companion theory quickly.**  A coherent theory that explains examples but does not change
  the current proof contract should be written as a parked companion viewpoint, not kept as an active
  dashboard branch.
- **Compress before enriching.**  A rising-sea pass succeeds when one invariant replaces several
  active cases.  If the old taxonomy remains active, stop enriching the framework and return to the
  exact crux.

### Plateau abstraction discipline

Use this stricter mode when the campaign is producing many definitions, notes, and route branches
without closing the central proof debt.

- **Abstract from the obstruction, not from the archive.**  The input is the current recurring
  compatibility failure or smallest falsifier profile, not the full historical document.
- **Name the deletion target first.**  Before introducing a new object, invariant, category, or
  complex, list the local labels, cases, dashboard leaves, or proof-debt rows it is supposed to
  replace.
- **First theorem before second language layer.**  After one abstraction layer, the next output must
  be a native comparison theorem, descent criterion, obstruction criterion, normal form, or
  blindness statement.  Do not add more terminology first.
- **Track lift direction at the point of definition.**  Mark whether the abstract formulation is
  equivalent, necessary, sufficient, stronger, weaker, or heuristic.  A beautiful sufficient-only
  framework should not become the active route unless it has a kill/promote test.
- **Park non-descending frameworks quickly.**  If the abstraction explains examples but does not
  change a proof-debt row in the original language, keep it as companion structure and return to the
  exact crux.

### Post-abstraction accounting

After a rising-sea detour in a mature campaign, merge the framework only through native descent.

```text
Native row attacked:
Repeated local structures replaced:
New object or invariant:
First comparison/descent theorem:
Lift direction:
Native corollary:
Rows deleted/merged/parked:
Decision: promote / park / retire
```

- If the abstraction does not replace named local structures, it is exposition, not frontier
  progress.
- If the first theorem does not descend to a native corollary, park the framework as companion
  theory before adding more terminology.
- If the lift direction is only sufficient or heuristic, keep a kill/promote test next to it; do not
  let a beautiful abstraction become the default active route by inertia.
- If the old taxonomy remains active unchanged, the framework has not compressed the campaign and
  should be retired or reduced to one invariant/blindness statement.

### When abstraction did not compress the state

Use this after a framework-building pass that produced cleaner language but left the same proof debts
active.

- **Treat unchanged debt as failed descent.**  If the same rows remain active after the abstraction,
  the framework is explanatory background unless it immediately yields a native comparison theorem,
  obstruction criterion, normal form, or counterexample template.
- **Extract the invariant or blindness sentence.**  Keep the smallest reusable object: one invariant
  replacing several cases, or one statement naming the native feature the framework cannot see.
  Retire the rest from the active proof state.
- **Do not build a framework for the archive.**  Repeated consolidation often tempts a global theory
  for every historical branch.  Instead, abstract only the recurring obstruction that survives the
  last exact reduction.
- **Require compression before enrichment.**  A second abstraction layer is allowed only after the
  first one deletes local labels, merges proof-debt rows, or descends to a native theorem.  Otherwise
  return to the original crux.

## Deliverables

When using this skill, produce a rising-sea packet:

```text
Original target:
Recurring structures:
New objects:
Morphisms/operations:
Universal property or functorial law:
Lifted target and direction:
First structural theorems to prove:
Test examples/counterexamples:
Descent back to original problem:
Net simplification gained:
Deleted/merged active debt:
Promote / park / retire decision:
Status: equivalent lift / stronger lift / useful framework / stalled
```

The first useful output is often not a proof but a cleaned-up framework: definitions, functorial
lemmas, examples, and a comparison theorem showing why the original problem was poorly phrased.

## Historical Examples

For analogy patterns and source links, read `references/examples.md` when deciding what kind of
abstraction may be missing.
