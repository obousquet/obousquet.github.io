# Theory-Building Constructions And Checks

Selective checks for `theory-building`. Pick only the section matching the
current mathematical bottleneck.

## 1. Closure & Construction Cycle

1. Specify the object class, retained data, equivalences, and ordinary/singular
   examples (reusing known theory from `research-knowledge` / `literature-research`).
2. Test natural operations (restrictions, products, quotients, extensions,
   gluing, duals, completions) and record types, admissibility, and witnesses
   where an operation leaves the class.
3. Compare enlargements (enriched data, latent parameters, formal expressions,
   ambient classes) and verify existence, well-definedness of quotients, and
   preservation/loss of properties from the smaller class.

## 2. Calculus Construction & Soundness Pattern

Choose sorts $s$, typed operations $o: (s_1,\dots,s_k)\to s$, model sets
$V_s$, certificate/annotation sets $A_s$, and validity predicates $P_s(x, c)$.
Define partial interpretations $\operatorname{val}_o$, update maps
$\Phi_o$, and admissibility predicates $\operatorname{Adm}_o$. Prove on actual
domains:
$$\Big(\bigwedge_{j=1}^k P_{s_j}(x_j, c_j) \land \operatorname{Adm}_o(\mathbf{x}; \mathbf{c})\Big) \implies \operatorname{val}_o(\mathbf{x})\text{ defined and } P_s(\operatorname{val}_o(\mathbf{x}), \Phi_o(\mathbf{c})).$$
Pair structural induction over finite expressions with explicit **leaf
theorems** and a **root readout theorem** returning the target conclusion (plus
continuity/convergence arguments if passing to limits).

| Observed behavior | Candidate algebra | Obligation still required |
|---|---|---|
| Linear combination & cancellation | Vector/graded space with bilinear form | Linearity and actual norm/variance control |
| Repeated coordinate or scale changes | Group/semigroup action | Composition and transformation of bounds |
| Nested substitutions | Typed trees / operadic composition | Units, domains, associativity, overlap |
| Order sensitivity | Operators and commutators | Exact identities plus analytic control |
| Local-to-global gluing | Transition data / descent | Cocycle compatibility and assembled existence |
| Divergent cutoffs | Counterterms / completion | Uniform estimates and limit realization |

## 3. Finite Partition & Observable-Space Refinement

When finite nonempty $X$, total operations $U$, and decidable finite-image
observable $Q: X \to Y$ are explicitly given (for partial operations, add a
distinct absorbing failure state):

- **Partition refinement:** initialize blocks by $Q$; iterate grouping by
  signature $(\text{block}(x), (\text{block}(u(x)))_{u\in U})$ until stable
  (at most $|X|-b_0$ splits). Record the distinguishing composition word on each
  split. Two states coincide iff $Q(w(x)) = Q(w(y))$ for all words $w$ over $U$.
- **Linear observable space** (real $Q$): initialize $W_0 = \operatorname{span}\{1, Q\}$
  in $\mathbb{R}^X$ and iterate $W_{r+1} = W_r + \operatorname{span}\{f \circ u : f \in W_r, u \in U\}$
  in exact arithmetic until invariant (at most $|X| - \dim W_0$ steps). Induced
  pullbacks $u^*: W \to W$ suggest operator matrices and commutators.

Both procedures are finite diagnostics only: they can stabilize at all of $X$,
and infinite generalizations still require uniform proofs.

## 4. Comparison Obligations For Enlargements & Correspondences

- **Completions / embeddings ($J: C \to D$):** specify the exact test class for
  any universal property, which limits/exactness/estimates survive, and which
  counterexamples fail once hypotheses (e.g., uniform continuity or completeness)
  are relaxed.
- **Correspondences ($F: C \to D$, $G: D \to C$):** state categories, variance,
  and whether the claim is equivalence, adjunction, restricted-image inversion, or
  partial heuristic dictionary; prove preservation and reflection explicitly.
- **Internal / quantitative recovery:** distinguish syntactic soundness from
  conservativity, and separate qualitative existence from constructive bounds or
  effective witnesses under limits/quotients.
