# Local-CM radius and Buchsbaum status

Use this packet for `CM_t`, `t^*`, `hd-VC` bounds, and Buchsbaum base-gap status.

## Local-CM hierarchy

- `Delta_H` is Buchsbaum iff every non-empty one-literal conditioning has ample Yang complex.
- More generally, `CM_t` means every realized partial assignment of size at least `t` has ample version class.
- The best learning-theoretic interpretation of the optimal `t` remains open.
- `cor:cmt_radius_calibration`: `0<=t^*(H)<=|X|`, and `t^*(H)=0` iff `H` is ample.

## Gap bounds

- `thm:local_cm_gap_bound`: if `Delta_H` is `CM_t`, then `hd(H)<=VC(H)+t`, so `hd(H)-VC(H)<=t^*(H)`.
- The proof uses `lem:hochster_link_descent`: high-dimensional induced homology descends through chosen vertices to a link; a `t`-trace link is ample under `CM_t`.
- `cor:recursive_trace_link_hd`: for every depth `s`, `hd(H)<=s+max_{|sigma|=s} hd(H_sigma)`.
- `cor:one_step_trace_profile_optimal`: positive-depth trace-link profiles are optimized at depth one.
- `cor:profiled_local_cm_bound` gives trace-dependent refinements; the uniform `t^*(H)` specialization overpays off the ample stratum.

## Buchsbaum base-gap status

- `cor:local_cm_sharpness_buchsbaum_base`: equality examples in the global radius bound descend to Buchsbaum non-ample base-gap examples.
- Historical reductions converted such a base gap into a VC-preserving one-literal fiber, a cross-realized extenture, and then a common-trace Mayer-Vietoris obstruction.
- The relative phantom/common-trace branches are now closed: `lem:buchsbaum_split_no_phantom_faces` and related corollaries remove the old phantom-trace obstruction.
- `thm:buchsbaum_hd_equals_vc` supersedes the earlier base-gap campaign: Buchsbaum classes now satisfy `hd=VC` in every VC dimension.
- `prop:buchsbaum_vc_one_vc_drop` and `cor:buchsbaum_vc_one_no_base_gap` remain useful low-dimensional calibrations.

## Guardrails

- Do not claim small `CM_t` controls RTD by `RTD<=VC+t`: Hall's `C_H` is ample/`CM_0` with `RTD=4>VC=3` (`cor:cmt_not_rtd_bound`).
- Constant coordinates create artificial profile slack; strip essential cores when running diagnostics.
- `scripts/explore_local_cm_gap.py` is regression/proof-history support, not the source of current theorem status.
