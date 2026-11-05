# Develop Abstractions Through Three Interacting Processes

Use when the objective is to develop objects, higher abstractions, or a calculus
around a hard problem. This specializes the driver's operating loop; it is not a
second campaign workflow or a universal solver. Direct proofs and known-method
imports remain available whenever they serve the objective.

## One Evolving Mathematical Account

Recover the precise problem or theory question, previous results and corrections,
and representative examples. Reuse the existing theory document and result map.
Keep the following information as compact as the work permits:

- **Objects and examples:** definitions, retained data, equivalences, boundary and
  singular examples, and the current class of objects or presentations.
- **Operations:** input/output types, admissibility, mathematical purpose, and
  what data each construction must preserve.
- **Laws and witnesses:** proposed identities, inequalities, or controlled errors;
  proof status, counterexamples, and the exact scope of each failure.
- **Models and controls:** concrete interpretations, existence, analytic bounds,
  quantitative constants, dependence, domains, and compatibility assumptions.
- **Comparisons and questions:** what can be recovered in the original mathematics,
  the evolving structural questions, and any proved or unknown return to the target.

These are mathematical data, not five mandatory new files. A small investigation
may need only an example, an operation, and a proposed law to begin. Do not fill
unknown fields with assumptions of the desired conclusion.

## Choose Work By The Mathematical Question

| Current question | Process and specialist | Concrete work to undertake |
|---|---|---|
| What objects should exist to support natural constructions? | Closure-driven theory building: `grothendieck-rising-sea` | Generate neighboring objects, compare enlargements, and prove existence, composition, or comparison laws |
| What operations could generate a family of arguments reliably? | Operation-driven calculus construction: `proof-calculus` | Define typed operations and models, prove primitive/compatibility laws, and develop a validity or reconstruction theorem |
| What information must a representation retain? | Failure-driven representation refinement: `representation-refinement` | Find a discriminating witness, select operation-motivated extra data, and prove the repaired recovery or composition law |

These questions can be chosen at the outset and can evolve together. Failure is
not a prerequisite for theory building or calculus invention. A known obstruction
can select the next task without requiring all three processes. When constructing
a new setting or a substantial two-way correspondence is the main work, use
`mathematical-framework-design`; it can support either closure or refinement.

## Execute, Compare, And Feed Back

1. **Choose a concrete portion of work.** Specify the construction, comparison,
   operation law, representation question, or model theorem to develop next, and
   why it contributes to the chosen objective. In early exploration this can be
   an open structural question; a finished master theorem is not an entry gate.
2. **Develop actual mathematics.** Construct examples and models, propose definitions,
   derive laws, search for discriminating counterexamples where informative, and
   prove the part that can be established. Keep formal syntax, realization of
   objects, and quantitative validity distinct. A list of candidate algebras is
   an agenda until its mathematical laws and models are constructed.
3. **Use the result to choose the next work.** A new class from closure may need
   invariants and their operation laws; those suggest a calculus. A failed calculus
   rule may expose forgotten provenance; refinement can supply it. The refined
   objects may then need an enlargement or comparison theorem. A successful
   construction can also open independent classification or realization questions.
   Follow these implications when useful rather than switching modes by schedule.
4. **Classify failure precisely.** A false target calls for correction or refutation;
   a false auxiliary law calls for a changed law; lost data calls for refinement;
   departure from the class calls for enlargement; an uncontrolled norm calls for
   an estimate. These can coexist. Retain the witness and the claim it refutes.
5. **Consolidate at natural milestones.** Integrate the definitions, dependencies,
   proofs, models, and comparisons. Re-examine earlier examples and try a different
   composition or model where appropriate. Compare against the closest existing
   result and account for construction/model costs when assessing reuse. Additional
   examples test scope, not a universal claim.
6. **Revisit objectives and continue within scope.** Prove a specialization back to
   the original problem if available. Otherwise record its connection as unknown
   and assess the cumulative theory on its merits. Choose the next meaningful
   construction, proof, or question; redirect formalism that has become artificial
   or circular. Respect user budgets without imposing a generic short expiry on
   sustained theory development.

A compact implementation of the loop is:

    recover sources, examples, objectives, and current mathematics
    repeat within the user's research scope:
        choose an object, operation, representation, or model question
        use the relevant process; generate, compare, test, and prove
        classify the result and any failure at its actual scope
        update objects, retained data, laws, models, and comparisons
        at a milestone: consolidate, revisit objectives, choose next work
    report established mathematics, open obligations, and target status

The driver selects and integrates work. Specialists own its mathematical details;
this loop does not authorize subagents or require invoking the driver recursively.

## Two Short Feedback Paths

**A calculus fails because it forgot shared sources.** Adding two marginal
sub-Gaussian parameters suggests an invalid certificate for twice the same sign.
Refinement retains signed source coefficients. Scaling and addition now act
linearly on those coefficients; independent source certificates prove a quadratic
control for every finite expression. The repaired representation has led back to
a calculus and a model theorem. Nonlinear products still need new rules.

**A construction leaves the object class.** Hiding a coordinate in a positive law
with quadratic log density can create higher-order log interactions. Compare a
larger potential class with latent presentations retaining the full law and visible
coordinates. Prove that hiding composes and the interpretation is the intended
marginal. Further laws or estimates can then be studied in the new setting.
Representational closure alone supplies no probabilistic estimate.

These paths illustrate interaction, not a requirement to complete a three-step
cycle. The specialized skills contain the detailed construction procedures.

## Mechanical Components And Research Judgments

With effective bounded inputs, tools can generate typed expressions, enumerate
finite models, compare exact observations, find counterexamples, and check supplied
proofs. For an explicit finite action system, `representation-refinement` provides
a terminating sufficient-quotient construction and a linear observable-space
construction yielding candidate operators. Such a quotient is relative to supplied
operations and observations and may retain the entire original state.

Choosing fruitful objects and operations, discovering uniform laws, proving
existence and analytic validity, and extending finite patterns to an infinite class
remain research tasks. Soundness is distinct from completeness and optimality.
Recording the unknown answer, assuming the target in an interface, or making
syntax formally closed does not complete the missing mathematics.

At review, keep two accounts: what the theory now constructs or explains, and what
is actually proved about the initiating problem. Coherent foundations and independent
structural questions can justify further theory work while the latter is unchanged.
No guarantee of useful compression, eventual termination, or resolution of every
hard problem follows from the process.
