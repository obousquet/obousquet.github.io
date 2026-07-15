# Terminology guardrails

## Extentures and non-ampleness

- **Extenture** means a minimal missing trace, not a synonym for non-ampleness.
- Ample classes can have extentures, for example simplex/down-set examples that miss a top trace.
- Non-ampleness means failure of the shattering-extremum equality, equivalently a mismatch between shattered and strongly shattered sets.
- In the VC-radius/sphere-law route, the relevant obstruction is a low-support or purity-violating extenture, not the mere existence of an extenture.

## Maximal / maximum / extremum / extremal

- **Maximum VC-d** means Sauer equality: `|H|=sum_{i<=d} binom(n,i)`.
- **Maximal VC-d** means inclusion-maximal among classes of VC dimension at most `d`; adding any outside concept increases VC dimension.
- Maximum implies maximal, but maximal need not imply maximum.
- **Ample / shattering-extremum** means Pajor equality: `|H|=|sh(H)|`, equivalently `sh(H)=st(H)`.
- **Extremal** should be reserved for inclusion-maximality with respect to increasing `|sh(H)|`.
- Ample/extremum implies extremal, but the equality and maximality notions are different.

## Teaching and compression language

- Never say "compression" for a concept-level map `H -> T(H)`.
- Use **representation map** (`mfw`, injective teaching map), **fully-identifying teaching map** (each `tau(h)` a teaching set iff indicator basis of `k[v]/I^0_H`), or **OCS** (acyclic teaching graph `G_tau`).
- Reserve **compression map** for `kappa:T(H)->T(H)` acting on all traces.
- Measures: `mfw <= NCTD <= RTD <= OCN`, `NCTD <= VC`.
- `mfw`, `VC`, and `hd` are numerical/homological; `RTD`, `OCN`, and `NCTD` are order-dependent and provably not captured by numerical invariants.
