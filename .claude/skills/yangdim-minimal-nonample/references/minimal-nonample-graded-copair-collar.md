# Graded co-pair and outside-collar packet

Load this packet for fibre-skew co-pair endpoints, split-fibre witnesses, and inherited outside-collar alignment obstructions in the old graded replacement route.

## Co-pair endpoint structure

- `lem:common_profile_top_extenture`: a common tight extension with all one-coordinate deletions shattered gives a top extenture support of size `VC(H)+1`.
- `cor:common_profile_top_puncture_or_copair`: ambient minimal non-ampleness leaves only a punctured cube, triggering the Claim-X projection-minor criterion, or an antipodal co-pair.
- `lem:top_missing_fiber_source` and punctured-fibre corollaries: non-antipodality cannot come from complete lifts of local co-pair holes; it must come from a realized base label whose outside fibre is a punctured cube.
- `cor:copair_completed_top_paired_fibers`: in the positive-completion branch the base projection is full, exactly two antipodal base labels have punctured outside fibres at antipodal labels, and all other base fibres are full.
- `cor:paired_completed_copair_reduction_tower`: every nonempty common reduction of a paired completed co-pair is again a co-pair, ending at the base co-pair.

## Split-fibre witness tools

- `lem:split_fiber_witness_criterion`: if both side fibres shatter `S` while their common fibre does not strongly shatter `S`, then the split class shatters `{x} union S` but does not strongly shatter it.
- `cor:missing_common_trace_split_witness`: it is enough to exhibit a single missing labeling of `S` in the common fibre.
- `lem:missing_trace_common_fiber_collar`: an inherited missing `D` labeling can be located in a conditioned common fibre after fixing the complementary collar.
- `lem:copair_slice_side_fiber_visibility`: one-coordinate slices of antipodal co-pairs give side-fibre visibility on every proper post-split subset.
- `cor:collared_missing_trace_split_witness`: a missing inherited trace plus side-fibre shattering after fixing the complementary collar gives a non-ample collared conditioning, forbidden in a minimal non-ample ambient class when the collar is nonempty.

## Outside-collar alignment obstruction

- `lem:missing_trace_no_internal_split_visibility`: the split coordinate cannot lie inside the inherited missing support `D`; use an outside co-pair/path coordinate with a nonempty collar inside `D`.
- `cor:outside_collar_visibility_forbidden`: for minimal non-ample `H`, any outside split `x notin D` and nonempty proper collar `M subset D` forces at least one side fibre to fail shattering `D\M`.
- `lem:outside_collar_missing_side_label`: each outside side fibre individually misses the inherited remaining label `phi|_{D\M}`.
- `cor:outside_collar_full_punctured_alignment`: any full-or-one-punctured side projection on a set containing `D\M` must have exactly `R=D\M`, be punctured, and have unique puncture `phi|_{D\M}`.
- `cor:outside_collar_no_antipodal_copair_alignment`: a literal antipodal co-pair on the inherited outside split is impossible because both side projections are forced to omit the same inherited label.
- `cor:outside_collar_proper_skeleton_descent`: the collared projection to `(D\M) union {x}` cannot shatter all proper subsets; some minimal missing trace lies on a proper subset.
- `cor:minimum_outside_collar_descent_dichotomy`: for minimum-size `D`, every proper missing trace in the collared projection has support exactly `|D\M|` and lifts to a global size-`|D|` extenture.
- `cor:max_overlap_outside_collar_residual`: with maximal-overlap `(D,K)`, the replacement branch `D-u+x` is impossible for `x in K\D` and visible collar remainder in `D\K`.
- `lem:same_support_extenture_not_adjacent`, `cor:singleton_offk_collar_forced_cylinder`, and `cor:two_offk_collar_antipodal_residual` sharpen singleton and two-coordinate off-`K` collars.

## Status

The collar packet is a reusable warning for current bridge work: local co-pair visibility must be aligned with inherited missing traces before it yields a contradiction or descent.
