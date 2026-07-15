# Split-lift endpoint separation

Use this packet for the local missing-path endpoint-separation part of the split-lift route.

## Local path status

- The local missing VC-one tree `M_S=2^S\F|S` is forced to be an antipodal geodesic path for bridges: project to `S union {x}` and use the projection spine plus dual one-dimensional/side-complement classification.
- The local Route D endpoint-separation crux is closed modulo the named handoff receivers.
- Endpoint calibration was framed as two subclaims: primal repair blocks preserve the `tau_S`-cut of each local missing path, and dual repair blocks do not merge the two endpoint sides. The current active target is the downstream signed component graph.

## Selected co-pair boundary formulation

- Boundary endpoint separation is equivalently selected co-pair no-gap: for `z_i=(v_i,lambda_O)`, the indices with some selected dual top-hole hit `z_i|B=theta_B` should form an interval.
- Maximumity/local path geometry alone does not prove this.
- Gap-shadow correction: for maximum `D`, the deletion shadow equals the ordinary projection `pi_s(D)`, so projection membership along a gap is tautological. The useful content is that selected top-hole supports at gap endpoints must contain the entering and exiting path coordinates.
- Current sharper crux: downstream signed consistency and signed connectedness for the split-lift component graph. `BOUNDARY-SELECTED-SUPPORT-TRANSFER` is now a parked stronger boundary formulation, not an active endpoint-separation debt.
- Reduced subtargets: the non-singleton fan/core-escape branch is closed in the handoff-free endpoint route by nearest-realization handoff; the singleton branch is closed by the cross-corner nearest-realization handoff, which gives projected `F/D` overlap or an actual `F/Omega` boundary edge. `SELECTED-SPINE-PREFIX-EXCHANGE` is therefore superseded for the active route.
- Closed singleton guardrail: `NO-RECURSIVE-SELECTED-V-FORK-MINOR` is proved in `prescribed_dual_bridge_realization.tex` as `prop:no_recursive_selected_v_fork_minor`, using the side-VC-dimension-one classification to rule out the forced maximum VC-one side whose one-inclusion graph is a 3-star rather than a path. It remains useful only if the stronger selected-spine formulation is revived.
- Refuted contraction shortcuts: deleting the entering/exiting coordinate swallows a boundary endpoint; endpoint conditioning leaves a one-sided gap; `R_s(D)` does not preserve the full `D`-run; projecting `F` can fill missing labels.
- Endpoint survival under contraction is exactly certificate-core escape: the deleted internal coordinate must avoid both endpoint selected-support cores. Equivalently, it must avoid being a `D`-spike direction from either bounding `T`-endpoint. Because `D` is maximum/ample, every endpoint spike completes a one-punctured square adjacent to the first or last `D`-vertex of the gap, so the non-singleton blocker is a square-fan cover rather than a bare spike cover. The nearest-realization lemma `lem:square_fan_nearest_realization_handoff` closes this blocker after handoffs are removed: for any square-fan arm, a closest `F`-realization of its off-path trace steps toward `lambda_O` either into `D`, producing projected `F/D` overlap, or into `Omega`, producing an actual `F/Omega` boundary edge. Therefore endpoint square-fan covers and endpoint-spike covers cannot occur in a handoff-free residual. The weak `(m,d)=(5,2)` outside-distant fan witness remains only as a guardrail for the older distance-from-`lambda_O` formulation; it has a projected-overlap handoff at the nearest-realization step.

## Diagnostics

- `scripts/diagnose_split_lift_endpoint_separation.py --seeds 25` checks the canonical `(8,4)` layer.
- The maintained calibration has no primal endpoint failures, no dual endpoint merges, complementary-binary constraints on every top support, no signed graph conflicts, one signed component, and two signed-graph solutions per instance.
- Treat these diagnostics as calibration, not proof.
