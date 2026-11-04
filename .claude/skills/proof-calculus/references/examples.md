# Designing And Checking A Calculus

## Regularity Structures: An Architectural Analogy

Hairer's *Introduction to Regularity Structures* separates a graded model space
and reexpansion group from concrete model maps satisfying consistency identities
and analytic bounds. Reconstruction connects modelled distributions to actual
distributions; products and integration require further hypotheses and estimates.
See Definitions 2.1 and 2.4, Theorem 2.8, and Sections 4–5 in the linked July 2013
notes. Later versions have different numbering. The introduction simplifies some
statements; consult the full theory before importing a theorem.

Design lesson: develop formal operations, concrete interpretations, and a theorem
connecting them. Transferring this architecture to another field is an analogy
until that field's models and validity theorem are constructed. It does not make
analytic estimates consequences of algebra alone.

Source: [Hairer's introduction](https://www.hairer.org/papers/Regularity.pdf).

Bruned–Hairer–Zambotti organize renormalisation using decorated coloured forests
and two Hopf algebras in cointeraction. Their compatible coactions describe how
transformations interact; this is more than assigning an invariant to each tree.
Use the example to ask which substitutions and compatibility laws a new setting
needs. Copying the terminology does not provide the necessary analytic theory.

Source: [Algebraic renormalisation of regularity structures,
version 4](https://arxiv.org/abs/1610.08468v4).

## A Small Calculus That Can Be Verified Directly

Consider centred real random variables with certificates

\[
  \mathbb E e^{\lambda X}\le e^{v\lambda^2/2}
  \quad\text{for every }\lambda\in\mathbb R,\qquad v\ge0.
\]

Scaling by a real number a sends v to a²v: substitute aλ into the certificate.
Adding independent certified variables sends (v,w) to v+w: independence factors
the moment generating function, after which the two bounds multiply. To iterate,
attach base randomness to expressions and require disjoint independent sources
at each addition; marginal certificates alone cannot check this condition.

Induction on such expressions proves their certificates. For v>0 and t>0,
exponential Markov followed by λ=t/v gives
P(X≥t)≤exp(−t²/(2v)). For v=0, letting λ grow gives P(X≥t)=0.
The bound is one-sided; applying it to −X yields the other tail.

This is an elementary example, not a novelty claim. It illustrates how the
algebra of expressions, model assumptions, parameter propagation, and a
conclusion-extraction theorem fit together.

An immediate adversary is reuse of the same Rademacher sign ε twice. Each copy
has v=1, but 2ε does not have v=2: cosh(2λ)=1+2λ²+O(λ⁴) exceeds
exp(λ²)=1+λ²+O(λ⁴) near zero. Dependency information cannot be discarded.
Nor does closure under addition establish closure under products or suprema.
Those operations require new rules with their own hypotheses and proofs.

## Proposals That Still Owe Mathematics

- A graded decomposition does not itself define a cochain complex: specify the
  differential and prove d²=0. Identifying graded pieces with cohomology needs
  another argument, as does extracting a quantitative estimate from vanishing.
- Calling entropy tensorization a monoidal law can organize its use, but concrete
  models still require a tensorization proof. A variance decomposition alone does
  not imply exponential concentration; finite-variance variables can have heavy tails.
- A framework with function objects does not by that fact make every external
  supremum measurable, attained, or integrable. State and prove the comparison.
- A perturbation or commutator identity does not itself imply a spectral gap,
  mixing estimate, or stable inverse. Identify the analytic control required.
- An asymptotic limit that removes error terms does not automatically recover
  explicit finite rates. A quantitative transfer theorem must supply them.

These checks locate the remaining work. They do not rule out developing the
proposed theory or prove that a different construction cannot succeed.
