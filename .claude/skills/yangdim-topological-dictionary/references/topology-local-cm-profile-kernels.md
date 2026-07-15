# Trace-link profile kernels and projected bridges

Use this packet when the task concerns why a trace-link numerical bound is sharp or slack.

## Exact one-step kernel

- `prop:one_step_profile_kernel_exact`: for `r=M_1(H)>=1`, the one-step bound `hd(H)<=r+1` is sharp iff some induced one-literal link has a top class in `H~_{r-1}` whose image in the deletion piece is zero.
- The open part after this formal exactness is translating the kernel into concept-class or cubical data.

## Mayer-Vietoris and projection interpretations

- `lem:one_vertex_mv_component_merge` gives the abstract one-vertex Mayer-Vietoris mechanism.
- `cor:one_step_yang_witness_survival`: a Yang one-step witness survives exactly when the deletion piece kills the local top class.
- `cor:fiber_projection_witness_survival`: for `v=(x,b)`, the deletion piece is the induced Yang complex of the projected class `overline H_x`, while the link is the fiber `H_{x=b}`.
- `cor:projected_graph_witness_survival`: in the `H_0` regime, a one-step witness survives iff two components of the single-fiber realized-literal graph become connected in the projected realized-literal graph.
- `cor:two_fiber_component_incidence`: equivalently, connectivity is detected by the bipartite incidence graph between components of the two fiber realized-literal graphs.

## First-profile exactness

- `prop:first_profile_h0_exact`: if every non-empty one-literal conditioning has `hd<=1`, then `hd(H)=2` iff some induced fiber `H_0` witness is not incidence-separated.
- Diagnostics `one_step_projected_bridge_summary` and `one_step_incidence_bridge_summary` matched the exact `n<=4` frontier, but direct opposite-face bridging is too strong without extra hypotheses.

## Remaining refinement target

Higher-profile kernels and iterated bridge filling remain the conceptual target. Do not mistake failure of a numerical profile for a failure of local-CM theory; the separator is whether local witnesses survive the relevant deletion/projection piece.
