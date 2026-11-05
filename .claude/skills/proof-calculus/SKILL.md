---
name: proof-calculus
description: >-
  Discover and develop operations, algebraic structures, and calculi that generate
  mathematical constructions and families of arguments. Build their expressions,
  composition laws, concrete models, and validity, reconstruction, or stability
  theorems together. Use for hidden-algebra discovery and systematic method
  invention, including settings without a large proof corpus or a known master theorem.
---

# Proof Calculus

Ask which operations organize the mathematics, what structures their interactions
reveal, and what theorem makes their use reliable. Develop a language of
constructions with concrete models and proved laws that can generate results
beyond the arguments used to discover it.

The objective can be a new calculus, an algebra/analysis interface, a representation
of recurring constructions, or a theory of their transformations. Repeated proofs
are one starting point; a revealing operation, analogy, or mathematical phenomenon
can also suffice. A formalized corpus, a failed direct proof, and a candidate
master theorem are not prerequisites. Operations, representations, admissible
models, and the central theorem can emerge together.

## Discover Operations And The Data They Need

Recover relevant results, source constructions, and earlier corrections in the
project, nearby work, and shared literature. Identify the precise difference from
existing methods before claiming a new calculus. Inspect mathematical mechanisms
rather than repeated prose, tactic syntax, or superficial graph patterns.

Start from actions: substitution, multiplication, integration, conditioning,
gluing, changing base point, rescaling, transporting, eliminating variables,
renormalizing, completing, or reconstructing, as appropriate. For each candidate
operation record:

- the objects or expressions it consumes and produces;
- its domain, admissibility, and intended mathematical purpose;
- the information that must survive, including signs, provenance, scale, domains,
  regularity, dependence, constants, and errors where relevant;
- the concrete interpretation and the laws or estimates still to establish.

Generate and compare small composites. Examine order, parenthesization, repeated
inputs, boundary cases, cancellations, and accumulation of losses. A shared action
can conceal different independence, positivity, compactness, or analytic assumptions.
Keep these distinctions while seeking a common structure.

Read [operation-driven development](references/operation-process.md) for the
construction cycle, candidate-algebra table, finite-expression soundness pattern,
and a worked calculus retaining signed source coefficients.

## Develop Expressions, Structure, And Models Together

**Expressions and composition.** Choose sorts, generators, and operations that
represent the actual mathematical actions. Specify partial domains and side
conditions. Investigate units, associativity, substitutions, symmetries, and
relations. Trees may represent nested substitutions, graphs shared data, or linear
spaces signed combinations; choose according to the composition pattern.

**Algebra and defects.** Compare different composites in concrete examples. Prove
identities where they hold, and calculate defects or commutators where they do not.
Ask what additional data makes a law true and what quantitative control a defect
needs. This can suggest a grading, action, algebra, coaction, substitution system,
or compatibility structure. An observed pattern motivates a candidate; it does
not establish its axioms. A Hopf algebra, operad, or cohomology theory should arise
from a precise mathematical need rather than be prescribed in advance.

**Concrete models.** Interpret the expressions and transformations in the intended
mathematics. Construct examples and prove their assumptions, including existence,
regularity, positivity, dependence, bounds, and domains. Decide which information
belongs to syntax, annotations, or the model. A useful formal relation may fail
in some models and require a restricted class or a controlled remainder.

**Controls and comparisons.** Define the estimates, norms, error propagation, or
other certificates needed to use the operations. Prove how they transform.
Distinguish equality of interpretations from equality of estimates: equivalent
expressions may carry bounds of different sharpness. If expressions are quotiented
by relations, show the claimed interpretation and controls descend appropriately.

These are interacting research directions. The most useful algebra can become
visible only after model construction, and analytic failures can change the
expression language. Foundational work can be valuable before a broad application
or finished generating theorem is available.

## Establish What Makes The Calculus Reliable

Seek the theorem appropriate to the setting: finite-expression soundness,
reconstruction, realization, extension, stability, or continuity of transformations.
State its hypotheses, quantifiers, and concrete conclusion. Identify which parts
follow formally from composition and which require substantial existence or
analytic arguments.

For finite expressions, prove the certificates of the generators, the validity
of each primitive operation on its actual domain, and the required compatibility
laws. Structural induction can then establish validity of generated expressions;
a readout theorem connects their certificates to the desired mathematical result.
For infinite constructions, completed spaces, or singular limits, prove the
additional convergence, continuity, or reconstruction statements. Validity at
every finite stage does not alone establish the limiting claim.

Keep the difficult inputs visible. An interface whose field is the desired bound
organizes an assumption; it supplies a theorem for a concrete model only when the
field is proved there. The same applies to an admissibility condition or leaf
certificate encoding the original conclusion. Trace these obligations through
the calculus rather than hiding them in names or type classes.

Separate soundness from expressive completeness, and both from optimality. Search
through valid expressions need not represent every proof or attain the best
constant. In formal code, inspect the statements as well as their proofs: empty
interfaces, `True` witnesses, `sorry`, or assumed new axioms do not implement the
missing mathematics. Report the actual formalization status and assumptions.

Read [examples](references/examples.md) for the regularity-structure analogy,
an elementary composition theorem, and unsupported algebra-to-analysis transfers.
The methodological lesson is to develop algebraic operations, models, and validity
together; another field's estimates still require its own mathematics.

## Use Successes And Failures To Extend The Calculus

Recover known constructions with their exact scope, then try different composites,
models, or phenomena not used in the initial design. Seek results and structural
questions that the operations make newly accessible. A calculus can be valuable
independently of the problem that prompted it.

Use failures to select the appropriate next work. A false rule may need correction;
forgotten dependence or cancellation may need `representation-refinement`; a
construction leaving the object class may need an enlargement; a valid algebraic
identity may still need an analytic estimate. Test the particular claim: unequal
values with the same summary refute exact recovery, not every possible upper bound.

Use `grothendieck-rising-sea` to develop the surrounding objects and theory,
`mathematical-framework-design` when the setting or a substantial correspondence
must be constructed, and `alon-method` when an existing technique suffices. The
processes can develop together; no failure or fixed sequence is required. Campaign
coordination follows [the overall process](../honest-conjecture-resolution/references/abstraction-development.md).

## Consolidate The Method And Its Mathematical Value

During the available work period, develop an actual construction, model, relation,
validity argument, or informative counterexample. Keep definitions, proofs,
applications, and remaining obligations together in the existing theory documents.
A proposed diagram or axiom list is an agenda until its mathematical content is
established; it can still guide worthwhile foundational work.

At natural milestones, assess which constructions and arguments can now be
produced systematically, which examples are connected, and what new questions
have become accessible. Track the cost of building models, proving compatibility,
and establishing analytic inputs alongside any shorter application proofs. Mere
syntax compression is not the objective or a sufficient measure of value.

Assess development cumulatively. Central theorems can require substantial
foundations; neither each turn nor each definition needs an immediate application.
Redirect circular rules, artificial models, or elaboration without deeper results.
An unknown return to an initiating conjecture does not by itself discredit a
coherent calculus. Respect actual user scope and resources, and keep the original
problem's status distinct from the method's development.

Record independently useful results, unexpected applications, and opportunities
for a standalone paper or theory branch with their exact proof status and closest
prior work. At handoff, state the operations and laws established, models realized,
remaining analytic or comparison obligations, and concrete next work.

In a campaign, `honest-conjecture-resolution` owns objectives, assignments, and
integration; return these results to the existing state. A focused calculus request
can use this skill directly without starting a campaign or a second result ledger.
