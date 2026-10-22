# Methodological Failure Modes And Pivots

Load this when a campaign has many cases but little theorem movement, when an imported theorem or
proxy keeps failing, when local data cannot distinguish examples, or when the route needs a genuine
change of perspective.

Use the progress definitions and cumulative route review in `state-compression.md`. The checks here
diagnose a proposed method; passing a check or discovering another limitation does not itself renew
the route. Distinguish a mathematical implication from a conjecture about which method will be useful.

## Native-Structure Audit

Run this before adopting a generic theorem, proxy, local criterion, or compressed invariant.

```text
Target statement:
Proposed proxy/import/reformulation:
Direction: equivalent / necessary / sufficient / special-case / heuristic
Native data in the target:
Data preserved:
Data forgotten:
Known witnesses that differ only in forgotten data:
Why the forgotten data is harmless, or why the route is quarantined:
Replacement exact formulation:
```

Typical native data: signs, colors, paired layers, endpoint provenance, labels/owners, rank or
dimension, quotient/gauge choices, boundary orientation, admissibility, cancellation, global
compatibility, and passive parameters.

If two objects have the same proxy value or local data but different target status, that data alone
cannot characterize the target. Record the precise scope. This does not exclude useful one-sided
bounds, a different encoding, or the whole mathematical method. Do not claim a feature was proved
indispensable to every proof merely because one encoding omitted it.

## Census-To-Principle Rule

A census aimed at a structural goal should inform a decision through one of:

- a theorem statement;
- a counterexample or discriminating falsifier profile;
- a canonical normal form;
- an exact symbolic criterion;
- a structural invariant;
- a regression test for a named lemma.

If the next step is merely "increase the size/radius/order" after the last census found no failure,
freeze the census as evidence and write the conceptual replacement target. Valid replacements
include a colored transfer lemma, exact boundary map, obstruction class, descent theorem,
universality/wildness statement, or dual certificate.

Finite coverage explicitly requested by the user, or needed to close a proved finite reduction, is
a separate legitimate objective. Do not apply the structural-goal stop rule to forbid that work.

## Local-To-Global Gate

For a construction, first separate input existence from assembly. If the target is
\(H(X)\Rightarrow\exists w\,W(X,w)\) and the construction proves
\(H(X)\land A(X,d)\Rightarrow W(X,F(X,d))\), the missing implication is
\(H(X)\Rightarrow\exists d\,A(X,d)\). Name the theorem that supplies the admissible data, with its
exact quantifiers. Separately available local witnesses need not form a compatible tuple:
\(x=0\) and \(x=1\) are each satisfiable, but not jointly. A conditional assembly theorem remains useful at its
stated scope; it does not prove input existence. Test the least-supported indispensable input
before extending the assembly calculus.

Before promoting a local route, answer:

```text
Local datum being used:
Global theorem it should imply:
Compatibility/transport/gluing mechanism:
Holonomy, boundary, ancestry, or provenance data retained:
Smallest pair with same local data but different global status:
Exact extra hypothesis needed:
```

If compatibility is unproved, retain the conditional result and mark that implication open. Identify
what could supply compatibility before treating the construction as a sufficient proof route.
In an induction, also check strict descent, closure of hypotheses, and the exact conclusion supplied
on smaller objects. Existence of some smaller witness does not provide prescribed boundary values.

## Stronger-Statement Quarantine

Many stalled routes silently replace the target by a stronger sufficient claim. Quarantine the
stronger claim instead of letting it govern the campaign.

For a selection problem, compare the choices allowed by the target with those frozen by the method:
a reference witness, partial assignment, boundary values, positivity, monotonicity, or a fixed bank
of operations. Explain why each restriction is needed for the method and whether the target needs
it. A fixed-choice failure does not exclude global reselection. Before declaring nonexistence,
exclude every choice the target permits; signed or averaged identities conversely do not supply
positive or integral witnesses without proof.

```text
Original target:
Stronger statement being pursued:
Why it would imply the target:
Evidence that it may be false or overpowered:
Status of the original target without it:
Condition for reopening the stronger statement:
```

Use `stronger open problem`, `false proxy`, `calibration only`, or `superseded` explicitly. These
statuses are different and prevent false restarts.

## Exact-Layer Split

Separate proof debt into layers before adding lemmas:

- feasibility or nonemptiness;
- positivity;
- integrality or purification;
- equivalence versus sufficient condition;
- local-to-global compatibility;
- extremal/minimal-counterexample reduction;
- publication-level exposition.

Do not merge these into one vague "remaining obstruction". The next round should change one named
layer.

## Perspective-Pivot Trigger

At a strategy review or repeated failure of the same mechanism, consider a change at the level of
the original target, not just a translation of the latest auxiliary lemma. After a bounded discovery
pass, select a promising approach or report that no credible replacement emerged:

- **Solved analogue:** reconstruct the proof of the closest solved problem and isolate the step
  that supplied its decisive structure. Test that step's transfer before surveying more analogies.

- **Alon-style import:** locate a theorem or technique from probability, algebra, topology,
  geometry, spectral theory, entropy, coding theory, or additive combinatorics, and require a native
  lemma or counterexample as output.
- **Grothendieck-style abstraction:** define the objects, morphisms, invariants, universal property,
  exact sequence, or functorial operation that makes the current cases shadows of one structure.
- **Dual formulation:** restate the target as a kernel/cokernel, separation, obstruction class,
  certificate, homology/cohomology statement, LP dual, or universal property.
- **Invariant search:** ask which quantity is unchanged by the allowed operations and distinguishes
  the smallest known positive and negative examples.

State the proposed consequence for the conjecture or general theory, and the evidence of improved
tractability, a new capability, or structural understanding. Use the theory criteria in
`state-compression.md` when a framework merits its own branch or paper without a known return to the
conjecture. An equivalent formulation that simply relocates the same difficulty is not yet a
strategic improvement. A creative pass may honestly be inconclusive.

For an encoding, name the gained capability: a theorem whose hypotheses can now be checked, an
operation producing new witnesses, a distinguishing obstruction, or a genuinely smaller residual
problem. Check both translation directions and identify where the target's defining hypothesis
enters. If the remaining transfer is the old existence statement under another name, record a
reformulation rather than an easier problem; useful independent theory may still result.

## Dashboard Method Role

When updating a dashboard, mark a branch's methodological role when it clarifies state. Suggested
values include `exact reformulation`, `native invariant`, `census`, `proxy`, `local test`,
`global compatibility`, `side import`, `counterexample search`, `tombstone`, and `publication
consolidation`.

Use method roles as warnings: active `census`, `proxy`, and `local test` leaves should have explicit
stop rules or compatibility gates in the ledger.
