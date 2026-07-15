---
name: alon-method
description: >-
  Attack a mathematical problem by importing powerful techniques from adjacent
  fields in the spirit of Noga Alon: probabilistic method, polynomial method,
  algebraic encodings, topological theorems, spectral tools, entropy,
  combinatorial geometry, coding theory, additive combinatorics, and related
  transfer principles. Use this skill when a direct proof route is stale, when
  the problem has a combinatorial surface but may be encoded into algebra,
  topology, probability, geometry, or linear algebra, or when the goal is to
  develop a new proof technique by adapting a theorem from another domain.
---

# Alon Method

Use this skill when the right move is not another local reduction but a method import: find a
powerful theorem or technique from another area, encode the problem so that the theorem can see it,
and refine the encoding until the original obstruction becomes accessible.

This complements `honest-conjecture-resolution`: that skill manages route status and evidence; this
skill deliberately broadens the proof toolkit.

## Core Principle

Do not ask "how do we prove this in the native language?" first. Ask:

- What hidden structure would make this problem look probabilistic, polynomial, topological,
  spectral, geometric, algebraic, entropic, or algorithmic?
- Which famous theorem would solve a neighboring problem if only the hypotheses matched?
- What encoding, auxiliary object, or relaxation makes those hypotheses almost true?
- If the theorem does not apply, what new lemma is the smallest missing transfer principle?

## Method-Import Workflow

1. **Name the native obstruction.** State the exact local difficulty in the problem's own language.
   Avoid vague labels such as "need a clever argument."
2. **Generate a transfer menu.** Try several external languages before committing:
   probability/random choice, polynomial vanishing, linear algebra rank, topology/compactness,
   spectral expansion, entropy/information, finite fields, convexity/duality, geometry, additive
   combinatorics, coding theory, or algorithmic amplification.
3. **Build the dictionary.** For each candidate language, map objects, constraints, witnesses,
   extremizers, and failure modes. Record what structure is preserved and what is lost.
4. **Match theorem hypotheses.** Pick one or two major theorems whose assumptions almost match the
   encoded problem. The useful work is often the gap between the true hypotheses and the desired
   hypotheses.
5. **Stress the encoding.** Test whether the encoding sees the known hard examples, counterexamples,
   and equality cases. If it makes them invisible, the import is probably a false proxy.
6. **Extract the missing lemma.** If no theorem applies directly, formulate the smallest transfer
   lemma that would make it apply. This lemma is now the route target.
7. **Return to the native problem.** Translate the imported conclusion back into the original
   statement and check constants, quantifiers, boundary cases, and whether the result is equivalent,
   sufficient, or only heuristic.

## Useful Import Patterns

- **Probabilistic existence.** Replace explicit construction by a random object plus expectation,
  alteration, local lemma, concentration, or entropy compression.
- **Polynomial encoding.** Turn forbidden configurations into polynomial vanishing/non-vanishing,
  degree constraints, finite-field identities, or rank conditions.
- **Topological obstruction.** Encode colorings, partitions, intersections, or equivariant maps so a
  fixed-point/Borsuk-Ulam/Tucker/Tverberg-type theorem forces a witness.
- **Linear algebra and rank.** Represent incidence, independence, or set systems by vectors,
  matrices, exterior algebra, eigenvalues, or low-rank factorizations.
- **Spectral or expansion transfer.** Replace local combinatorics by an operator, Laplacian,
  adjacency matrix, Markov chain, or high-dimensional expansion statement.
- **Entropy and information.** Prove counting, concentration, or extremal statements via entropy,
  mutual information, Shearer's lemma, compression, or information monotonicity.
- **Geometry and convexity.** Translate discrete data into convex bodies, separating hyperplanes,
  polytopes, LP duals, Helly/Radon/Caratheodory phenomena, or geometric inequalities.
- **Algorithmic viewpoint.** If a randomized or algebraic algorithm detects the object, its analysis
  may contain the proof technique.

## Anti-Patterns

- Importing a theorem by analogy without writing the exact dictionary.
- Applying a powerful theorem to a proxy that discards the structure making the target true.
- Treating a theorem's conclusion as useful before translating it back to the original quantifiers.
- Trying only one external field and calling the side quest complete.
- Letting the imported technique become a broad literature survey rather than a named route.
- Producing many plausible method imports without choosing one operational crux.
- Keeping an imported method alive after it has only generated vocabulary and no theorem,
  counterexample, exact reformulation, or sharper diagnostic.

## Side-Quest ROI Discipline

Alon-style side routes are valuable when they change the proof geometry quickly. In a mature
campaign they must be short, obstruction-centered, and contractive.

### Methodology lesson from low-yield method imports

When an Alon-style detour follows many failed local attempts, run it as an assay rather than as a
survey.

- **Start with the current normalized obstruction.**  Translate the smallest survivor, falsifier
  profile, or proof-debt row before listing theorem families.
- **Check visibility before strength.**  If the encoding forgets the decisive native feature, a
  stronger theorem in that encoding is unlikely to help.  Record the forgotten feature and retire or
  repair the encoding once.
- **Cap repair attempts.**  Try the first encoding and at most one repaired encoding that preserves
  the lost feature.  If neither changes proof debt, stop the detour rather than broadening the menu.
- **Return one native export.**  The mergeable output is one native lemma, theorem citation,
  diagnostic, counterexample, exact reformulation, transfer lemma, proxy kill, or blindness
  statement.  A list of possible techniques is background.
- **Score by deletion.**  The detour remains active only if it deletes, merges, sharpens, or
  relabels an existing proof-debt row.  Otherwise keep the blindness statement and park the method.

### Fast side-route protocol

Use this when an Alon-style detour is launched from an already mature campaign.

```text
Native row:
Normalized obstruction:
External encoding:
Visibility test:
One theorem family:
Missing transfer lemma:
Native export:
Delete / merge / park:
```

- **Visibility before power.**  Test whether the encoding sees the current normalized obstruction
  before surveying strong theorems.  A powerful method that forgets the obstruction is a blindness
  result, not a route.
- **One theorem family per pass.**  After a short menu, choose one external theorem family and state
  the exact native transfer lemma it would require.  Do not preserve a list of possible imports as
  active proof state.
- **Export or retire.**  The pass must return one native lemma, counterexample, theorem citation,
  diagnostic, exact reformulation, transfer lemma, proxy kill, or blindness statement.  If it cannot,
  retire or park the detour.
- **Deletion dividend.**  A successful import deletes, merges, sharpens, or demotes an existing
  proof-debt row.  If the dashboard frontier is larger after the pass, the merge failed.

### Lessons from low-yield creative detours

Use these constraints when an Alon-style pass is launched from a mature conjecture campaign rather
than from an early brainstorming phase.

- **Run the visibility assay first.** Encode the current smallest falsifier or normalized
  obstruction before surveying theorem families. If the encoding cannot distinguish that obstruction
  from benign examples, the output is a blindness statement, not a new active route.
- **Attack one proof-debt row, not the whole conjecture.** The pass starts with a named native row
  and ends by saying whether that row was proved, refuted, sharpened, killed as a proxy, or left
  unchanged. A broad method menu is not a mergeable result.
- **Export one native object.** The useful deliverable is one native lemma, transfer principle,
  theorem citation, diagnostic, counterexample, exact reformulation, or blindness statement. Keep
  additional analogies as background unless they delete or merge active state.
- **Cap repair attempts.** Try one encoding and, if it fails by forgetting a named native feature,
  one repaired encoding that preserves that feature. If neither changes proof debt, retire or park
  the side quest instead of widening the toolbox.
- **Require a deletion dividend.** An imported method remains active only if it deletes, merges, or
  relabels an existing leaf. Otherwise it may be useful context, but it should not increase the
  dashboard frontier.
- **Let failed imports guide the native route.** A failed polynomial, spectral, probabilistic,
  entropy, topological, or algebraic encoding should leave a sentence of the form: "this encoding
  forgets X, so the native proof must keep X visible." That sentence is often the real progress.

### Mature-campaign import gate

- **Start from the normalized obstruction.** Do not import a method against the broad theorem. Pick
  the current smallest falsifier, atom, quotient, certificate, or proof-debt row and translate that
  object first.
- **Record the before-state in native terms.** Before opening the external toolbox, write the active
  proof-debt row, the smallest known falsifier profile, and the exact native feature that current
  methods fail to control. This prevents the import from optimizing a different problem.
- **Run the obstruction-visibility test before the method menu.** If the encoding cannot distinguish
  the current obstruction or near-miss from benign examples, record the lost native feature and retire
  or repair the encoding before surveying more theorem families.
- **Collapse to one theorem family and one transfer lemma.** A menu of probabilistic, polynomial,
  spectral, topological, and algebraic analogies is brainstorming. The mergeable output is one chosen
  theorem/technique, one hypothesis mismatch, and one native transfer lemma or diagnostic.
- **Return in native objects.** The deliverable must be a lemma, counterexample, exact reformulation,
  diagnostic, theorem citation, proxy-kill, or non-transfer statement about the original objects.
- **Demand a deletion dividend.** The import remains active only if it proves, refutes, sharpens,
  demotes, deletes, or merges an existing proof-debt row. If the before/after native frontier is the
  same, park the side route as background.
- **Prefer a killed proxy to an unconstrained toolbox.** It is a successful Alon pass to discover
  that a polynomial, spectral, probabilistic, or topological encoding forgets the decisive native
  feature. Record that blindness and remove the proxy from the active tree instead of trying more
  theorems in the same encoding.
- **Do not let breadth replace descent.** After one failed theorem family and one repaired encoding,
  either produce a native transfer lemma or stop. A long menu of possible imports is useful only
  during initial brainstorming, not in a mature campaign.
- **Keep failed imports low-fidelity.** A failed polynomial, spectral, probabilistic, topological, or
  algebraic encoding should leave one precise blindness statement naming the native structure it lost,
  not a new dashboard subtree.

### Fast import audit

Before merging an Alon pass, write:

```text
Native obstruction:
Chosen encoding/theorem family:
Obstruction-visibility result:
Hypothesis mismatch:
Native export:
Proof debt changed:
Before/after frontier delta:
Promote / park / retire:
```

If `Proof debt changed` is empty, the default decision is `park` or `retire`, not `continue`.

### Merge discipline after a side route

- **Export one native object.** The side route should merge back as exactly one native lemma,
  obstruction, counterexample, theorem citation, transfer lemma, diagnostic, or blindness statement.
  If several possible exports appear, choose the one that most directly changes the active proof-debt
  row and park the rest.
- **No active menu after merge.** A list of candidate external tools is useful during the pass, but
  should not remain as active dashboard state. After merging, the active state should contain either
  one chosen transfer lemma or one reason the import is blind.
- **Use failed imports to narrow the native target.** When an encoding forgets the decisive feature,
  record the forgotten feature as a native constraint on the next proof/disproof attempt. Do not keep
  trying nearby theorem families unless the repaired encoding explicitly preserves that feature.

### Learned ROI rules for mature campaigns

- **One import pass should shrink the native problem.** A successful Alon pass does not merely list
  probabilistic, polynomial, spectral, or topological analogies. It returns one native lemma,
  counterexample, theorem citation, diagnostic, exact reformulation, or blindness statement that
  changes the proof-debt table.
- **Import against the current falsifier, not the whole conjecture.** In a mature campaign, the
  useful object to encode is the normalized obstruction currently surviving the native proof route.
  If the external language cannot distinguish that obstruction from accepted examples, the route has
  probably found a blindness statement, not a new active branch.
- **Score the pass by deletion.** Before preserving an imported method as active, name the exact
  dashboard leaf, proof-debt row, proxy, or case taxonomy it deletes or merges. If nothing is
  deleted, the output is parked background even if the analogy is conceptually useful.
- **Use side-route failure to identify the missing native feature.** A failed polynomial, spectral,
  probabilistic, or topological encoding is useful when it says precisely which feature it forgot:
  endpoint data, signs, support, orientation, boundary incidence, admissibility, cycle holonomy, or
  cancellation. That forgotten feature should guide the next native crux.
- **Use failed visibility as a result.** If an encoding cannot distinguish the current normalized
  obstruction from benign examples, record exactly which native feature it forgot--signs, endpoints,
  support, orientation, boundary data, admissibility, or cycle compatibility--and retire that encoding.
- **Do not promote a toolbox without a transfer lemma.** A promising external theorem family remains
  parked until the missing transfer lemma is stated in the original problem language with its
  direction marked as equivalent, sufficient, necessary, or heuristic.
- **Merge by deletion.** When an import works, it should delete or merge an existing leaf. When it
  fails, it should leave one compact warning. It should not create a subtree of adjacent theorem
  families unless one of them has already changed the native proof contract.
- **Use a two-pass cap in mature campaigns.** Try one encoding and, if it fails by forgetting a
  native feature, one repaired encoding that explicitly preserves that feature. If the repaired
  encoding still gives no native lemma, diagnostic, theorem citation, or proxy-kill, retire the
  import instead of surveying more adjacent theorem families.
- **Export the blindness as the result when no theorem transfers.** A side route that proves
  "polynomial methods cannot see endpoint compatibility" or "spectral data forgets signs" has
  succeeded if that statement deletes a proxy. Preserve that sentence, not the whole attempted
  toolbox.
- **Do not let an import increase the active frontier.** The default Alon merge should replace an
  existing proof-debt row by a sharper row. If it instead creates several new rows, keep only the
  strongest transfer lemma active and park the rest.
- **Use method imports to test visibility before strength.** A powerful theorem family is irrelevant
  if its encoding cannot see the decisive native feature of the current obstruction. First test
  whether the encoding distinguishes the smallest survivor, near-miss, or known counterexample from
  benign instances; only then ask whether the theorem is strong enough.
- **Retire failed imports with a native blindness sentence.** The valuable output of a failed
  polynomial, spectral, probabilistic, entropy, or topological pass is often a sentence of the form:
  "this encoding forgets X, so it cannot control Y." Keep that sentence and delete the active method
  branch unless a repaired encoding preserving X is immediately available.
- **Cap breadth after a mature-campaign detour.** In an early brainstorming phase, a long transfer
  menu is useful. In a mature campaign, after one chosen encoding and one repaired encoding fail to
  change native proof debt, stop the import and return to the proof contract. More adjacent theorem
  families usually add vocabulary faster than they add descent.
- **Run the side route as a visibility assay before a toolbox survey.** First test whether the
  encoding distinguishes the current normalized obstruction, smallest survivor, or known near-miss
  from benign instances. If it does not, record exactly which native feature was lost and retire or
  repair the encoding before naming more theorems.
- **Export one object, then delete or park.** The mergeable result of an Alon pass is one native
  transfer lemma, theorem citation, diagnostic, counterexample, exact reformulation, or blindness
  statement. If that object does not delete, merge, or relabel an active proof-debt row, keep it as
  background and do not leave the method as an active branch.
- **Do not let creative breadth become proof-state growth.** A mature campaign uses Alon-style
  breadth to change proof geometry, not to expand the dashboard. After the pass, the active frontier
  should be no larger than before unless the new leaf has an explicit kill/promote test and replaces
  older debt.

### Retrospective lessons for side quests

Use these when an Alon-style detour was launched after a campaign plateau.

- **Run a visibility assay before surveying tools.**  Encode the current smallest falsifier or
  normalized obstruction first.  If the encoding cannot distinguish it from benign instances, the
  result is a blindness statement, not an invitation to list more theorem families.
- **Import against one proof-debt row.**  The side route should name the exact row it tries to prove,
  refute, sharpen, or kill.  If the row is unchanged after the pass, park the method even if it gave
  useful intuition.
- **Make failed imports pay by naming the lost feature.**  A failed polynomial, spectral,
  probabilistic, entropy, topological, or algebraic encoding should leave a sentence of the form:
  "this encoding forgets X, so it cannot control Y."  Preserve that sentence and delete the active
  method branch unless a repaired encoding preserving X is immediate.
- **Prefer one transfer lemma to a technique menu.**  After brainstorming, choose one theorem family
  and state the smallest native transfer lemma needed.  A list of five plausible imports is not a
  mergeable result in a mature campaign.
- **Use side-route failure to accelerate the native route.**  The failed import should constrain the
  next native proof/disproof move by identifying which feature must remain visible.  If it does not
  change the next native move, record it as background only.
- **Stop after one repair attempt.**  Try the initial encoding and, if it fails by losing a named
  feature, one repaired encoding.  If neither changes proof debt, retire the side quest rather than
  broadening the toolbox.

### Plateau side-quest discipline

Use this stricter mode when the main campaign has already gone through several false routes and
cleanup cycles.

- **Start from one normalized obstruction.**  Do not launch an Alon pass against the whole theorem.
  Choose the current smallest survivor, falsifier profile, certificate, atom, or proof-debt row.
- **Score visibility before strength.**  A powerful theorem family is irrelevant if the encoding
  cannot distinguish the normalized obstruction from benign instances.  First ask what the encoding
  forgets.
- **Return exactly one native export.**  The mergeable output is one native lemma, counterexample,
  theorem citation, transfer lemma, exact reformulation, diagnostic, proxy-kill, or blindness
  statement.  A menu of methods is not an active result.
- **Do not increase the dashboard frontier.**  If the import works, it should delete or merge an
  existing proof-debt row.  If it fails, preserve one sentence naming the lost feature and retire or
  park the method.
- **Use side-route failure to accelerate the native route.**  The important product of a failed
  polynomial, spectral, probabilistic, entropy, or topological encoding is often the feature it
  forgot--signs, endpoints, support, orientation, admissibility, boundary incidence, or cycle
  compatibility.

### Post-detour accounting

After an Alon-style detour in a mature campaign, do not merge the detour as prose.  Merge it as a
native proof-contract diff.

```text
Native row attacked:
Encoding tried:
Current obstruction visible? yes / no / partially
Feature lost, if any:
Native export:
Rows deleted/merged/parked:
Decision: promote / park / retire
```

- If the detour did not attack a named native row, retroactively classify it as background.
- If the encoding did not see the current obstruction, keep only the blindness sentence and retire
  the encoding unless a repaired encoding is immediate.
- If the export is a menu of possible techniques rather than one native lemma, diagnostic, theorem
  citation, transfer lemma, exact reformulation, or counterexample, choose one and park the rest.
- If no row is deleted, merged, parked, or relabeled, the side route may be intellectually useful but
  should not remain on the active dashboard.

### When an Alon detour was not useful enough

Use this after a creative-method pass that produced ideas but did not move the theorem.

- **Diagnose the failed import by visibility, not by strength.**  Ask which native feature the
  encoding failed to preserve: signs, endpoints, support, rank, orientation, boundary incidence,
  admissibility, cycle compatibility, or deletion behavior.  Record that feature as the output.
- **Do not compensate by widening the menu.**  If the first encoding and one repaired encoding do
  not see the active obstruction, retire the method for this row.  More theorem families usually add
  proof-state noise rather than speed.
- **Convert the detour into one native constraint.**  The useful residue of a failed import is a
  sentence of the form: "Any proof of row X must keep feature Y visible."  Use that constraint to
  design the next native proof or counterexample search.
- **Keep the dashboard unchanged unless debt changed.**  A side route that only changed intuition is
  background.  It should not create a new active leaf.

## Deliverables

When using this skill, produce a short method-import packet:

```text
Native obstruction:
Candidate external languages:
Chosen theorem/technique:
Dictionary:
Hypothesis mismatch:
Known adversaries/equality cases under the encoding:
Missing transfer lemma:
Native conclusion if successful:
Before/after crux movement:
Deleted/merged active debt:
Promote / park / retire decision:
Status: imported / reduced / stalled / refuted
```

If the import works, write the result as a theorem or lemma in the native problem language. If it
fails, record the precise mismatch and whether it suggests a different imported method.

## Historical Examples

For concrete examples and source links, read `references/examples.md` when the task needs inspiration
or a broader method menu.
