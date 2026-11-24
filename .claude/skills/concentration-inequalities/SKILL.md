---
name: concentration-inequalities
description: Choose and audit moment or tail bounds for dependent sums, stable functionals, and Rademacher or Walsh chaos. Use when comparing martingale, decoupling, hypercontractive, bounded-difference, Stein, transport, or coefficient methods and checking their hypotheses and losses.
---

# Concentration inequalities

State the random object, probability space, centering, moment range, and target
norm before selecting a theorem. Keep campaign state, unpublished results,
route labels, and numerical certificates in the project that owns them.

## Preserve the hypothesis

- Distinguish a bound on a function or replacement difference from a bound on
  the absolute sum of its Fourier coefficients. The latter may be much stronger.
- Distinguish independent replacement, full coordinate flip, conditional
  centering, and derivatives; write their normalization explicitly.
- Keep pointwise bounds, finite-moment bounds, variance bounds, and conditional
  bounds separate. Do not exchange a supremum with an expectation without a
  justified inequality in the needed direction.
- For quotient or infimum formulations, retain simultaneous compatibility.
  Separately optimized components need not assemble into a feasible optimizer.
- Audit every exchange of a norm with a sum, integral, expectation, or infimum.
  Name the inequality and record the dimension, degree, and moment dependence.

## Select the mechanism

| Method | Useful structure | What to check |
|---|---|---|
| Martingale inequalities | Filtration and controlled increments or bracket | Predictable versus realized bracket; maximal increments; loss from the chosen reveal order |
| Bounded differences and Efron–Stein | Coordinate sensitivity and variance estimates | Almost-sure versus averaged sensitivity; a variance bound alone does not give an exponential tail |
| Bernstein-type bounds | Variance plus a size or moment-growth control | Both budgets are needed; rare spikes can defeat variance-only reasoning |
| Hypercontractivity | Fixed-degree polynomial or spectral support | Degree dependence; cancellation lost by decomposing and summing levels |
| Decoupling and random selectors | A valid independent-copy representation | Independence, centering, reconstruction multipliers, and dependence on degree |
| Coefficient estimates for chaos | Explicit coefficient tensor and relevant tensor norms | The exact tensor norms required by the theorem, rather than a convenient stronger proxy |
| Stein and exchangeable pairs | An exchangeable construction with regression control | Conditional variance and regression remainder; preserve the original probability model |
| Transport or duality | An exact primal/dual formulation | An exact representation still needs a quantitative bound; inspect feasible-set constraints |
| Cumulants | Controlled joint dependence and cumulant growth | Range of orders and constants sufficient for the desired moment or tail regime |

## Test losses before extending a proof

Use examples that separate the candidate method from the original claim:
independent sums, a complete quadratic chaos, high-degree parity, disjoint
blocks, a common shared component, rare-event spikes, and signed mixtures with
cancellation. Choose only the families relevant to the proposed inequality.

Compute the target quantity and each intermediate proxy on the same example.
A proxy that diverges while the target remains bounded rules out that proof
step, not the target theorem. Search for a scalable family when small cases
suggest a loss. Mark finite enumeration, floating-point evidence, and an exact
symbolic certificate separately.

## Literature and proof audit

Use primary sources for imported inequalities. Record the exact theorem,
normalizations, independence or dependence assumptions, norm order, and valid
parameter range. Derive the specialization before calling it applicable.

For the final proof, track constants or their allowed dependencies, handle
zero denominators and boundary parameter cases, and justify any conversion
from moments to tails. Report the proved statement, assumptions, unavoidable
losses, and remaining gap. Do not import a project's closure status as a
universally established theorem.
