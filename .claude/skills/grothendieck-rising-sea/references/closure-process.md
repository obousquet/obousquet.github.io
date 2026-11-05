# Closure-Driven Theory Development

Use when a class of objects cannot support a mathematically useful construction,
or when systematically exploring its surrounding theory. The aim is a coherent
setting and its structural mathematics, not merely an expanded list of cases.

## A Repeatable Construction Cycle

1. **Specify the current objects and examples.** Record retained data, hypotheses,
   equivalences, boundary examples, and the questions the setting should support.
   Recover known constructions and earlier failures before replacing them.
2. **Generate meaningful neighboring constructions.** Vary assumptions and test
   restrictions, products, quotients, extensions, gluing, duals, or completions as
   appropriate. For each operation record input/output types, admissibility,
   intended interpretation, and why it matters. This is a menu, not a requirement
   to introduce all these constructions.
3. **Inspect closure.** Produce an object witnessing departure from the class, an
   unavailable operation, or a failed comparison. Distinguish missing objects
   from lost representation data, false laws, and unproved analytic estimates.
   A successful construction can also suggest new structural questions.
4. **Construct an enlargement.** Compare enriched objects, latent presentations,
   formal expressions, changed maps, and existing ambient theories. Specify the
   embedding or interpretation of original objects and the new constructions.
   There need not be a smallest or uniquely natural enlargement.
5. **Prove the foundations.** Establish existence, domains, composition, and
   comparisons; show what is retained, identified, or newly added. Check models
   and singular examples. Universal properties require their existence and
   uniqueness proofs; a desirable axiom list does not supply a model.
6. **Develop and consolidate.** Investigate invariants, realization, classification,
   decomposition, and connections suggested by the enlarged setting. Revisit old
   examples and the initiating question at natural milestones. Record independent
   theory value separately from any proved implication to that question.

These steps recur and can overlap. Definitions and existence theorems can require
substantial work, and an unknown return to the conjecture does not invalidate it.

## What Can Be Enumerated

Given a class C0 and typed, possibly partial constructions O, define successive
stages by adjoining O(c1,...,ck) for admissible inputs from the previous stage.
Bounded expression generation is an effective search when generators, parameters,
and admissibility tests have effective bounded descriptions. Keep three claims
separate:

- an expression is syntactically well formed;
- an object realizing it exists and its interpretation is well defined;
- the object supports the desired structural or quantitative conclusions.

Formal closure does not prove the latter two. Quotienting presentations needs
well-definedness; completion needs a topology and convergence results; gluing needs
compatibility and an assembly theorem. Infinite closure needs additional arguments
beyond validity for each finite expression. A larger class can also destroy a
useful property, so record the tradeoff rather than silently extending old claims.

## Example: Hiding Coordinates

A positive law on five signs can have density proportional to
exp(t x0(x1+x2+x3+x4)), t != 0. Its log density is quadratic. Summing over x0
produces 2 cosh(t(x1+x2+x3+x4)); its log density has a nonzero fourth-order term.
Thus quadratic log densities are not closed under hiding coordinates.

Two different enlargements deserve comparison: allow higher-order potentials,
or retain the full law together with a marked set of visible coordinates. In the
second presentation, hiding removes visible coordinates, and successive hiding
is governed by union of the removed sets. The interpretation is the marginal law,
with the composition identity proved by finite summation. A representation of a
marginal in this larger class does not itself supply concentration or mixing bounds.

The reusable lesson is to distinguish closure of concrete objects, closure of
presentations, and estimates on their interpretations. The formulas are a small
classical illustration, not a general solution method or a novelty claim.

## Working Output

Integrate the construction table, witnesses, definitions, proved laws, comparison
maps, and open structural questions into the existing theory document. Do not
create a parallel ledger merely to follow this procedure. At consolidation, state
what new objects or questions are accessible and which comparisons remain open.
