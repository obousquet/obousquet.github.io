# Top-skeleton, co-pair, and homology handoff

Load this packet for one-coordinate top-skeleton projections, antipodal co-pair endpoints, and the interface between the old cross-support route and calibrated cubical homology.

## Calibrated homology handoff

- `prop:calibrated_homology_vcr`: calibrated cubical-complement homology implies `VC_r(H)=VC(H)` for minimal non-ample classes.
- `prop:no_premature_collapse_calibrated_homology`: if outside coordinates of a shattered `VC(H)`-set can be deleted while all intermediate one-literal slices stay proper, then the calibrated complement homology class exists.
- `cor:terminal_full_slice_core`: unavoidable premature collapse can be made terminal.
- `cor:terminal_full_slice_core_singleton` and `cor:singleton_terminal_low_or_top`: terminal full-slice cores reduce to a singleton core; the opposite slice either gives a low-degree extenture or a top punctured/Claim-X branch.
- For the dedicated homology closure statement, load `minimal-nonample-calibrated-homology-history.md`.

## One-coordinate top skeleton

- `cor:one_coordinate_top_skeleton_dichotomy`: for `VC(H)=k`, a shattered `k`-set `S`, and outside coordinate `y`, either there is a global extenture supported on at most `k` coordinates, or `H|S union {y}` shatters every proper subset of `S union {y}`; in the latter case all missing top labelings are top extentures.
- `cor:one_coordinate_top_skeleton_trichotomy`: for minimal non-ample `H`, the top-support branch has only two forms: a unique missing top labeling, which is the top-circuit/Claim-X-minor branch, or an antipodal co-pair endpoint.
- Multiple non-antipodal top holes are not a separate residual obstruction; local ampleness of one-literal conditionings rules them out.

## Co-pair calibration

- `ex:antipodal_copair_cubical_calibration`: for `H=2^A\{q,qbar}`, `VC(H)=|A|-1`, `VC(H^c)=1`, `X_{H^c}=S^0`, and `X_H=S^{|A|-2}`. The predicted sphere dimension belongs to the class being complemented.
- `lem:copair_one_step_behavior`: deleting any coordinate from an antipodal co-pair gives the full cube, while conditioning gives a punctured ample cube. Therefore a one-step co-pair endpoint cannot be shortcut to Claim-X by coordinate deletion.
- Partial-cube/minor calibration: `Q_m^{--}=2^A\{q,qbar}` is the canonical forbidden pc-minor obstruction for lopsided/ample partial cubes. Do not convert that into a classification of YangDim one-literal minimal non-ample classes; pc-minor minimality is stronger, `C_6=Q_3^{--}` is only the common endpoint, and longer symmetric/even-cycle geometry remains separate evidence.
