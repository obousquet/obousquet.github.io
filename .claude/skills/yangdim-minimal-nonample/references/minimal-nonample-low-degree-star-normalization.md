# Low-degree extenture star normalization

Load this packet when a task uses the old low-degree extenture obstruction: a minimum extenture support `D` of size at most `VC(H)` compared against a shattered `VC(H)`-set `K` chosen to maximize overlap.

## Normalized setup

- `cor:minimum_extenture_support_exchange`: modulo Claim-X, a hypothetical minimum low-degree extenture support admits outside-coordinate insertion exchange, with prescribed deletion whenever the replacement projection is non-full.
- `cor:low_extenture_full_replacement_star`: if `D` is a minimum support maximizing overlap with a shattered `K`, then `D` is not contained in `K`, and every replacement `(D-x) union {y}` with `x in D\K` and `y in K\D` has full projection.
- `cor:normalized_full_star_obstruction`: after conditioning on `R=D cap K`, the remainder `U=D\K` supports an extenture, `V=K\D` is shattered, and every swap projection `U-x+y` is full.

## Slice and cylinder consequences

- `cor:normalized_extenture_slice_persistence`: every one-coordinate slice in `V` is non-empty and keeps the same extenture on `U`.
- `cor:normalized_single_coordinate_cylinders`: minimal non-ampleness forces one-coordinate cylinder normal forms `G_{y=c}|U=2^U\{f|U}` and `G|U union {y}=(2^U\{f|U}) x 2^{ {y} }`.
- One-coordinate cylinder data do not imply the full simultaneous product; the historical counterexample was `((2^U\{00}) x 2^V)\{(01,00)}` for `|U|=|V|=2`.
- `cor:normalized_multislice_lower_skeleton`: for nonempty `W subset V`, every `W`-slice realizes all `f|T` with `|T|+|W| <= |U|`; failures can only occur in top layers near the missing `U`-vertex.

## Failure accounting

- `cor:normalized_top_layer_failure_extenture`: a top-layer failure with `|T|+|W|=|U|+1` gives a global extenture of size `m+1`.
- `lem:normalized_graded_failure_accounting`: a failure with excess `s=|T|+|W|-|U| >= 1` contains a global extenture of size `m+j`, `0 <= j <= s`, obtained by deleting exactly `s-j` coordinates; if `|W|>s` then `j>=1`.
- `lem:normalized_first_failure_overlap_deletion`: in a first nontrivial failure, every minimal subfailure keeps all visible coordinates of `T` and `W` and may delete only coordinates from the conditioned overlap `R`.
- `lem:normalized_first_failure_g_extenture`: the visible failed label is itself an extenture of the normalized class `G`.
- `lem:normalized_overlap_deletion_interval`: any overlap-deletion extenture persists through every partial restoration of the deleted overlap block.
- `lem:normalized_overlap_deletion_numerical_ample`, `lem:normalized_overlap_one_step_restoration`, `cor:normalized_nonproduct_restoration_descent`, and `cor:normalized_restoration_descend_or_branch` convert restoration steps into either product-boundary persistence or visible-support descent.
- `lem:punctured_visibility_propagation` and `cor:normalized_no_descent_hamming_persistence` package the historical residual as full anchored partial-cube persistence unless visible-support descent occurs.

## Status

This packet records the route that led to the graded replacement tower. The low-degree obstruction is closed globally by `thm:minimal_nonample_vcr_purity`; use these lemmas only as reusable local mechanisms or as cautionary examples for current bridge-realization descent arguments.
