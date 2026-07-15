# Adversaries, Proxies, And Compute Hygiene

Load this when a route depends on computational evidence, a bound looks lossy, a proxy may be false,
or a crux lemma needs stress testing.

## Adversary Design

- Test the axes the claim is sensitive to: degree/scale, rank, sign pattern, cancellation, support,
  component spread, coherence, boundary cases, and mixed regimes.
- Build adversaries that stress several axes simultaneously. Pure/symmetric families are often
  benign.
- For `P => Q`, test near-misses of `P`: start from genuine `P`-instances and minimally perturb them
  while preserving cheap necessary conditions.
- Random dense samples miss sparse structured extremizers. Always test matchings, blocks, towers,
  dictators, uniform/symmetric cases, and recursive constructions where relevant.
- Random weights inside the right structured family can miss the extremizer; seed uniform/symmetric
  members explicitly.
- Optimize candidate inequalities to break them before promoting them to theorem statements.

## Numerical Evidence

- Robust numerics are necessary, not sufficient.
- Prefer “proved core + numerics for remainder” to “numerics for everything.”
- Cross-check evaluation methods at overlap points.
- Use symmetry reduction for exact large-parameter computations when possible.
- If a construction depends on a summary statistic, compute over the statistic’s exact law rather
  than enumerating the full space.

## Proxy Traps

### Lossy Bound Versus False Target

When `bound / truth` grows, ask separately:

- Is there an adversary making the target itself fail?
- Is the tool or proxy merely loose while the target stays bounded?

Measure the actual quantity, not only the bound.

### Assembly Trap

A sharp per-piece bound is not a proof if assembly uses `sum |piece|`. Signed cancellation across
pieces may be essential. Before assuming assembly is bookkeeping, measure `sum |piece| / truth`.

### Intermediate Target Trap

An intermediate proxy `B` can grow while the final target `A` stays bounded. If `B/budget` grows,
retarget closer to `A` instead of proving a false proxy bound.

### Proxy Ladder

Several increasingly faithful proxies can fail one rung at a time. When a rung fails, name what
structure it discarded: signs, weights, cancellations, orthogonality, geometry, degree, topology, or
admissibility. The next crux should preserve that structure.

### Exact Dual Before Sufficient Proxy

Before introducing local witnesses, cuts, certificates, or normal forms, state the exact target as a
membership/non-membership, kernel/cokernel, separator, extension, obstruction class, or universal
property. Then label every tractable route as `equivalent`, `necessary`, `sufficient`, `special
case`, or `heuristic`.

## Structural Reduction Patterns

- **Minimal counterexample via hereditary operation:** if restrictions preserve the target property,
  reduce to minimal bad objects.
- **Kill cheap-invariant characterizations early:** find witnesses showing cheap necessary
  invariants are not sufficient.
- **Exact recursion:** derive how the invariant transforms under deletion, restriction, link, minor,
  product, or quotient.
- **Saturation shortcut:** before local casework, ask whether Sauer, Helly, Kruskal-Katona,
  Euler characteristic, rank-nullity, dimension, matroid rank, or LP duality already forbids adding
  another object.

## Special Cases

Use special cases as axis tests, not reassurance.

- Map which axes the special case varies and which it freezes.
- If single-axis cases are harmless, test the first mixed-axis case.
- Do not assemble separable/product cases by triangle inequality without a new lemma.
- Preserve faithful weights and hypotheses from the live target.
- Record the mechanism that made the case work and the interaction still untested.

## Hidden Structure Dossier

When direct estimates fail, build a dossier for each object:

- exact definition;
- equivalent representations: sums, traces, matrices, generating functions, recursions, spectra,
  measures, homology/cohomology, duals;
- invariances and natural operations;
- known bounds, extremizers, and first variation;
- identities, positivity, convexity, majorization, or moment-sequence structure.

The goal is to isolate one missing structural fact, often positivity or an identity, and promote it
to the crux lemma.

## Compute Hygiene On EC2

- Treat the EC2 instance as shared infrastructure, not a batch cluster.
- Start small and estimate memory growth before scaling.
- Use `nice -n 10 uv run python scripts/explore_foo.py ...` for heavy diagnostics.
- Limit workers and avoid multiple high-memory/all-core jobs.
- Prefer chunking, checkpointing, sample limits, staged output, timeouts, and symmetry reduction.
- Stop and redesign if a run swaps, pegs all cores too long, or threatens the web service.
