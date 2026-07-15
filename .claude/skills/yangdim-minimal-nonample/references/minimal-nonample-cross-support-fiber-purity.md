# Cross-support fibre-purity route

Load this packet when a task touches cross-realized fibre extentures, support purity, co-pair projections, or exchange reductions in the closed VC-radius proof history.

## Core reductions

- `lem:extenture_conditioning`: an extenture of `H` restricts to an extenture of the matching non-empty conditioning after deleting the conditioned coordinate.
- `lem:fiber_extenture_decomposition`: global extentures containing `(x,b)` are exactly extentures of `H_{x=b}` realized by the opposite fibre `H_{x=1-b}`, with `(x,b)` added back.
- `lem:ample_extenture_punctured_cube`: an extenture of an ample class is a punctured cube on its support.
- `lem:cross_realized_shattered`: a cross-realized fibre extenture of a minimal non-ample class has support shattered by `H`, while adding the split coordinate gives a non-shattered set; hence cross-realized size is at most `VC(H)`.

## Co-pair and circuit reductions

- `lem:full_facet_minimal_copair` and `cor:cross_support_copair_reduction` reduce the co-pair pattern to proving the projection `H|S union {y}` is non-ample.
- `lem:full_base_proper_slices_nonample` and `cor:cross_support_proper_slice_reduction` show that if neither `y`-slice over `S` shatters `S`, then `H|S union {y}` is non-ample and hence a co-pair.
- `lem:full_slice_descent` and `cor:proper_ample_cross_projection_descent` reduce the proper-ample projection branch to either a smaller cross-realized support or a punctured cube.
- `lem:punctured_projection_exchange` and `cor:punctured_projection_circuit` identify punctured boundaries as minimal non-shattered circuits of `sh(H)`, whose codimension-one faces are cross-realized supports.
- `lem:punctured_lift_descent`, `cor:full_cross_projection_descent`, `lem:punctured_slice_opposite_full`, and `cor:product_boundary_vc_cost` reduce the full-projection branch to smaller/exchanged supports or to a VC-cost branch in the opposite split fibre.

## Uniformity and purity endpoint

- `cor:vc_drop_cross_support_copair` excludes rigid product/circuit boundaries under cross-support-size purity and VC-drop of non-empty coordinate conditionings.
- `cor:vc_preserving_conditioning_circuit` and `cor:vc_drop_failure_top_circuit` identify VC-preserving conditioning with a top punctured projection whose codimension-one faces are cross-realized.
- `lem:proper_projection_first_obstruction` and `cor:top_circuit_claimx_minor` route proper ample projections and top punctured circuits to Claim-X projection-minor obstructions.
- `cor:cross_support_split_boundary` normalizes a small-support branch to an antipodal split-boundary form, modulo Claim-X and minimal descent.
- `lem:copair_projection_exchange` and `cor:no_claimx_minimal_cross_enlargement` give outside-coordinate exchange for minimum cross supports.
- `cor:nonfull_minimum_cross_uniform` and `cor:pure_cross_support_uniform_layer` show that once the minimum cross-support size reaches `VC(H)`, Johnson-graph connectivity forces every `VC(H)`-set to be cross-realized.
- `cor:global_cross_purity_equiv` identifies minimum cross-support purity with minimum global extenture-support purity: cross-support sizes are global extenture sizes shifted down by one.

## Pitfall

Do not prove purity from local fibre ampleness alone. The historical obstruction was the possible existence of low-degree global extentures; that branch is routed through `minimal-nonample-low-degree-star-normalization.md` and is now closed only by the full VC-radius/extenture-purity theorem.
