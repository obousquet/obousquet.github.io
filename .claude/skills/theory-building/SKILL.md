---
name: theory-building
description: >-
  Develop coherent mathematical theory beyond single-route proof attempts:
  explore closures and invariants around objects (Grothendieck rising sea),
  discover generative operations and calculi with concrete models and validity
  theorems, diagnose and refine lossy representations, or construct new
  settings and two-way correspondences with explicit comparison theorems.
---

# Theory Building

When local proof tactics stall—or when objects, operations, or analogies
deserve structure of their own—develop the mathematical world directly. Build
definitions, examples, constructions, invariants, and theorems together.

Inside a campaign, `honest-conjecture-resolution` retains status authority;
return established laws, models, witnesses, and open obligations to the
existing campaign state rather than starting a parallel ledger. Keep progress
on the developed theory visibly distinct from progress on any initiating
conjecture: a coherent theory can be a standalone contribution even when its
return to an open problem remains unknown.

Choose among the four interacting directions below by what the mathematics needs
now; they are complementary lenses, not sequential gates. For concrete
checklists and construction patterns, load
[constructions and checks](references/constructions-and-checks.md).

## 1. Territory, Closure, And Foundations

Start from actual mathematical objects, neighboring phenomena, and ordinary,
extremal, and boundary examples (check `research-knowledge` and
`literature-research` first so known theory is reused).

- **Vary and enlarge.** Test restrictions, products, quotients, extensions,
  gluing, duals, limits, or completions. Identify which distinctions are
  essential and which properties break under an enlargement.
- **Close under constructions.** Record input/output types, admissibility, and
  interpretation for each construction; produce explicit witnesses when a class
  fails closure and compare candidate enlargements (enriched objects, latent
  presentations, formal expressions, or ambient spaces).
- **Separate three distinct claims:** (1) syntactic well-formedness,
  (2) existence and well-defined realization of the object, and (3) structural or
  quantitative theorems about it. Formal closure never proves an analytic
  estimate or a universal property without an existence/uniqueness argument.
- **Assess cumulatively.** Judge foundations by what can now be constructed,
  compared, or explained—not by whether every turn yields an immediate lemma for
  the initiating conjecture. Redirect only for mathematical reasons: artificial
  elaboration, unsupported laws, or circularity.

## 2. Generative Operations And Calculi

When recurring constructions suggest hidden algebra, build syntax, semantics,
and estimates together:

- **Capture the mechanism, not prose.** Record each primitive operation's
  domains, admissibility conditions, conserved data (signs, source provenance,
  degrees, regularity, scales), and error propagation.
- **Inspect composites and defects.** Compute small well-typed composites; prove
  identities where they hold and compute commutators or remainders where they
  fail. Let observed algebraic behavior suggest the structure (vector/graded
  space, action, tree substitution, descent data) rather than prescribing an
  elaborate label in advance.
- **Prove reliability via concrete models.** Establish leaf certificates,
  primitive admissibility, compatibility under quotienting, and structural
  induction for finite expressions plus a readout theorem translating the root
  certificate back to the target claim. Infinite or limiting expressions require
  separate convergence/continuity proofs.
- **Keep hard inputs exposed.** Never absorb the essential bound or conclusion
  into an interface assumption or leaf certificate without proving it on actual
  models. Track completeness and optimality separately from soundness.

## 3. Representation Refinement

When an invariant, summary, or quotient loses data needed by intended
observations $Q: X \to Y$ or operations $u$:

| Observed failure | Diagnosis and action |
|---|---|
| Concrete object violates the claimed target | Correct or refute the target itself |
| Proposed auxiliary identity fails | Revise the algebraic law; target may still hold |
| Equal retained summaries give different required values $Q$ | Refine the representation $\alpha$ or weaken exact recovery |
| Operation leaves the object class | Enlarge the objects/presentations and prove comparison |
| Identity holds, quantitative control is absent | Prove the missing analytic or combinatorial estimate |

- **Exact recovery vs. bounds.** An exact readout $Q(x) = q(\alpha(x))$ exists
  iff $Q$ is constant on every $\alpha$-fiber; a single pair with
  $\alpha(x)=\alpha(y)$ and $Q(x)\ne Q(y)$ refutes exact recovery, whereas
  refuting a common upper bound requires violating the bound itself. Deterministic
  induced operations also require $\alpha(x)=\alpha(y)\Rightarrow\alpha(u(x))=\alpha(u(y))$
  and matching definedness domains.
- **Meaningful repairs.** Adjoin the missing datum suggested by the failed law
  (sign, source labels, transition data, or remainder), prove separation and
  the repaired laws globally, and verify that computing the extra data does not
  hide the original problem. When $X$, $U$, and $Q$ are explicitly finite, use
  partition refinement or observable-space pullback iteration as a diagnostic.

## 4. Settings And Two-Way Correspondences

When existing morphisms or foundations obstruct constructions, design the setting
or dictionary itself with explicit comparison obligations:

- **Enlargements and completions.** Specify the embedding $J: C \to D$, test
  objects/morphisms, what information is retained or identified, and any
  limits/exactness lost in passage.
- **Functors and dualities.** Specify categories, variance, and exact strength
  (equivalence, adjunction, isomorphism-class bijection, or partial image
  correspondence). Matching numerical invariants never proves equivalence.
- **Preservation vs. reflection.** A theorem proved in the image or completion
  only settles the original object once reflected back with explicit quantifiers,
  domains, and effective bounds (qualitative compactness does not grant uniform
  finite bounds). For formal/internal languages, keep conservativity over the
  base theory distinct from model existence and avoid silently altering trusted
  axioms.

## Boundaries And Handoff

Use `alon-method` when a one-way encoding into an existing external theorem
suffices; `proof-exegesis` to extract the mechanism from an existing solved
argument; `proof-simplification` to shorten an already-valid proof; and
`proof-developer` for proving a selected standalone claim. Keep durable
definitions, examples, comparison maps, and open structural questions in the
owning project's documents with exact proof status separated from analogies or
conjectural extensions.
