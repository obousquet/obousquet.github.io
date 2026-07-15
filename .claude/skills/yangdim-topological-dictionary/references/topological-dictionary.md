# Topological and algebraic dictionary overview

Load this file as the entry point for Yang-complex/topological dictionary questions. Then load exactly one or two topical child packets.

## Stable headline facts

- `CM(Delta_H) <=> ample` is proved in `main.tex`; hence CM Yang complexes have `hd=VC`, but `hd=VC` alone is not a CM criterion.
- Constructible and SCM raw Yang complexes coincide with ample/CM for nonempty classes.
- Many raw `Delta_H` topological adjectives are rigid: they collapse to full cubes, one-inclusion connectivity, or dominated-literal elimination.
- Derived, teaching, Alexander-dual, and cubical objects have separate conventions; do not transfer raw-Yang classifications without checking the object.
- Cubical properties of `X_H` and `X_{H^c}` require separate hypotheses. Ampleness gives some collapsibility statements but is not characterized by them in general.

## Child references

- `topology-raw-and-alexander-dual.md`: compatibility router for the two raw/algebraic packets below.
- `topology-raw-yang-core.md`: raw Yang facts through CM/constructible/SCM, purity/balancing, connectivity dictionaries, and teaching/Scarf guardrails.
- `topology-alexander-dual-vc1.md`: Alexander-dual componentwise-linear, shellable, linear-quotient, and vertex-decomposable strata; exact VC-one classification.
- `topology-local-cm.md`: overview for local-CM/Buchsbaum profile packets.
- `topology-local-cm-radius-and-buchsbaum.md`: `CM_t`, `t^*`, `hd-VC` bounds, Buchsbaum base-gap closure, and strictness/status guardrails.
- `topology-local-cm-profile-kernels.md`: one-step trace-link kernels, Mayer-Vietoris/projected-bridge criteria, and remaining higher-profile interpretation targets.
- `topology-rigidity-and-cubical.md`: overview for raw-rigidity and cubical packets.
- `topology-raw-rigidity.md`: deletion-robust CM/Buchsbaum, Gorenstein*, pseudomanifold conventions, dominated literals, raw VD, and T4 nonevasiveness.
- `topology-cubical-complexes.md`: cubical collapsibility, dimension/purity, CAT(0)/median, and VC-one graph/tree facts.
- `topology-derived-teaching-hvector.md`: derived complexes, `sh(H)`, teaching/Scarf refinements, h-vectors, Pajor recursion, Tracy Hall's class, and no-general-corner guardrails.
