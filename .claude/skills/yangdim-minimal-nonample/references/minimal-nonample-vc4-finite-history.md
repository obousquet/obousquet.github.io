# VC-four and two-by-two finite-core history

This file was split out of the former monolithic `minimal-nonample-vcr-history.md`. Load it only when the task specifically touches this historical route.

Basic normalization now appears as `lem:low_extenture_overlap_blocks`: for a minimum extenture
support `D` with `|D|<=k=VC(H)` and a shattered `k`-set `K` maximizing overlap, the blocks
`U=D\K` and `V=K\D` are non-empty and `|U|<=|V|`; any smaller support or same-size support with
larger `K`-overlap closes the normalized counterexample.  Use this as the closure criterion for
graded replacement-tower branches.  First higher-VC specialization now appears as
`cor:vc_four_low_extenture_profile`: in a hypothetical `VC=4` low-extenture obstruction, the
normalized minimum support has size `3` or `4`, the overlap `R=D cap K` is non-empty, the anchored
normalized slice `G=H_{R=f_R}` is ample (`cor:anchored_normalized_slice_ample`), and in the
two-by-two case `|U|=|V|=2` the projection `G|_{U union V}` misses at most two labels from the
twelve-point punctured cylinder (`cor:two_by_two_ample_slice_two_holes`), with exact hole list in
`cor:two_by_two_ample_slice_classification`: empty, one singleton-`U` hole, two holes in one
`V`-fiber, or two holes in distinct `V`-fibers using the two singleton `U` labels.  The ambient
bridge `cor:two_by_two_singleton_holes_top_endpoint` proves that every singleton-`U` hole lifts to
a size-`m+1` extenture on `(D-u_i) union V`; in the `VC=4,m=4,|U|=2` branch this support is
`K union {z}` and its projection shatters every proper subset.  The same corollary routes the
projection to the punctured Claim-X branch or the antipodal co-pair branch, so after the proved
Claim-X exclusion every non-full two-by-two residual can only survive as a co-pair endpoint.  The
local two-by-two simultaneous-failure mechanism is now closed by
`cor:two_by_two_residual_dichotomy`: if the projection is the full punctured cylinder, then there
is no non-trivial simultaneous failure in the anchored slice `G`, and every non-empty anchored
flip fibre `H_{D=f^T}` projects onto the full cube `2^V`; if it is not full, it enters the routed
top endpoint branch.  The full-cylinder branch is now sharpened by two actual-cube reductions.
`cor:full_cylinder_anchored_flip_cubes` turns every projected-full anchored flip fibre
`H_{D=f^T}` into an actual full `V`-cube with all outside coordinates fixed.  Also
`cor:full_cylinder_overlap_half_collars` says that, for each `r in R`, the one-coordinate side
`H_{r=f(r)}` contains an actual full cube over `(R\\{r}) union V` at a fixed nonzero `U`-label
`tau_r`, again with all outside coordinates fixed.  The core reduction
`cor:full_cylinder_six_coordinate_core` removes the outside coordinates from the essential
obstruction: projecting to `Q=R union U union V` either gives a six-coordinate minimal non-ample
full-cylinder residual with the same data, or routes to the Claim-X projection-minor obstruction
through a first proper ample one-coordinate projection.  The exact finite verifier
`scripts/check_vc4_full_cylinder_core.py` now eliminates the six-coordinate full-cylinder
cube-package: among `4,792,763` `R`-swap side-pair orbits surviving the forced `R`-conditioning
filters, `4,195,356` have a bad `U`/`V` conditioning, `580,708` are ample, `16,699` have
`VC != 4`, and `0` non-ample residuals survive.  After the proved Claim-X exclusion, the
remaining two-by-two endpoint is therefore the co-pair endpoint.  The off-`K`
defect is only `1`, `2`, or the top profile `(m,|R|,|D\K|,|K\D|)=(4,1,3,3)`, defect one has no
multi-flip first-failure residual, and a canonical tight defect-two branch reaches a unit-defect
strict descendant (so it is impossible when `m=4`).  Non-ample local full-star survivors are
therefore fake residuals once `R` is anchored; the first open higher-VC purity layer no longer
includes the finite six-coordinate full punctured-cylinder cube-package, and the remaining
two-by-two endpoint is the routed co-pair endpoint.
