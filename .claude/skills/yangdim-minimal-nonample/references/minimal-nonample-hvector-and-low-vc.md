# h/g-vectors and low-VC strata

Use this packet for h-vector formulas, endpoint calibrations, and low-VC minimal non-ample classifications.

## Cubical h/g vector formulas

- `lem:hvector_cubefaces`: `h_{Delta_H}(t) = (1+t)^n - sum_j g_j(1-t)^j t^{n-j}`, where `g_j` counts `j`-subcubes of `H^c`.
- `thm:sphere_gvector`: if `X_{H^c}` is a homology `d`-sphere, then `g_j(H^c)=2 binom(n,j) sum_{i<=d-j} binom(n-j-1,i)`, and `|h_i|=binom(n,i)` with signs determined by `d`.
- The generating function proof is the stable route for the signed binomial h-vector; do not rederive it from ad hoc endpoint counts unless the task is expository.

## Endpoints and small dimensions

- Endpoint `d=0`: minimal non-ample plus hypercube-independent complement gives an antipodal pair; equivalently the named class is a co-pair.
- Endpoint `d=n-2`: antipodal-pair class.
- The `d=1` stratum has `g(H^c)=(2n,2n,0,...)` and follows from suspension/projection complements.
- `VC=2` is classified: `Q(H)` is an isometric `2n`-cycle, each coordinate labels two opposite edges, and `X_H` is a cubical `1`-sphere (`thm:vc_two_cycle_classification`).

## Low-VC calibrations

- `cor:minimal_nonample_no_binary_extentures`: minimal non-ample classes with `VC>=2` have no extentures of support size `1` or `2`.
- The VC-three low-extenture route is closed: common-puncture and singleton-cover branches reduce to finite local gluing lemmas certified by scripts and promoted to `main.tex`.
- `cor:low_vc_vcr_calibration`: the homology-sphere base extends through `VC<=3`.
- `cor:vc_three_maximum_fibers`: in the `VC=3` stratum, every one-coordinate fiber is an ample maximum VC-two class and `|H|=n^2-n+2`.
- The first remaining connected-middle problem after these results is structural gluing of maximum VC-two fibers, not radius, sphere-law, or maximum-fiber cardinality.
