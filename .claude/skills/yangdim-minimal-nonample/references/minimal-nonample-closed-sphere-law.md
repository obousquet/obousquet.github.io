# Closed minimal-nonample sphere-law package

Use this packet for current theorem status and guardrails around minimal non-ample classes.

## Main theorem status

- CM iff ample is proved; do not list it as conjectural.
- Claim-X is proved. Remaining bridge work should be phrased as reaching the hypotheses of this tool, not as proving Claim-X.
- `lem:complement_ample` and `prop:minimal_duality`: `H` ample iff the set complement `H^c` is ample, hence `H` minimal non-ample iff `H^c` is minimal non-ample.
- `thm:minimal_nonample_vcr_purity`: for minimal non-ample `H`, `VC_r(H)=VC(H)` and global extenture supports are pure of size `VC(H)+1`.
- `cor:minimal_nonample_sphere_law`: `X_{H^c}` is a homology sphere in dimension `n-VC(H)-1`.
- `thm:maximum_fiber`: every one-coordinate fiber of a minimal non-ample class is a maximum VC `VC(H)-1` class.

## Dimension bookkeeping

- Use `X_{H^c}` as a complement-normalized way to track missing traces/extentures of the named class, not as a distinct asymmetric target.
- Since `H^c` is also minimal non-ample, universal statements about `X_{H^c}` are equivalent to the same theorem schema about `X_H` after replacing `H` by `H^c`.
- Recompute the dimension for the class being complemented. Example: if `H=C_6 subset Q_3`, then `VC(H)=2` and `X_{H^c}=S^0`; applying the theorem to `H^c` gives `VC(H^c)=1` and `X_H=S^1`.

## Guardrails

- Pure topology alone is not enough to characterize minimality: non-minimal non-ample classes can realize the same acyclic/facet-slice/projection-complement profiles. The kernel required cardinality/ample-closure information.
- Ample implies `X_{H^c}` collapsible when the complement is nonempty, but the converse is false.
- Do not describe the historical connected-middle gap as open. It is closed by the VC-radius/sphere-law/maximum-fiber package.
- The remaining cubical questions are stronger structure questions: shellability, polytopality, vertex-decomposability, or fixed-convention cubical refinements.
