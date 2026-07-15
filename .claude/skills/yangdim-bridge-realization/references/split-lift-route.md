# Split-lift repair-component route overview

This is the overview for the active split-lift route. For current proof state, read this with `prescribed_dual_bridge_realization.tex` and `ledgers/proof_route_topological_dictionary.md`; the ledger is authoritative for active reduced targets.

## Current route shape

- `prop:exact_common_coordinate_split_reduction` rewrites a common coordinate split as a split-lift problem with candidate side `A=0*U union 1*bar(V)` and repair variable `W=V\F=T\U`.
- Validity is controlled by a top-projection VC test and a cross test. The cross test contracts to primal/dual repair components; the top test becomes a component-assignment constraint system.
- Endpoint separation is closed in the handoff-free route, so local top constraints reduce to complementary binary choices, hence a signed graph.
- The remaining existence/classification proof debt is signed balance of this graph, equivalently vanishing row-torsor holonomy. Signed connectedness is the separate refinement giving exactly two repairs modulo the antipodal repair involution.

## Child references

- `split-lift-exact-formulation.md`: exact variables, cross-test component contraction, top alternatives, and signed-graph reduction.
- `split-lift-endpoint-separation.md`: closed missing-path endpoint separation, selected co-pair no-gap guardrails, and diagnostics.
- `split-lift-wall-provenance.md`: backed boundary handoffs, singleton collars, dual-clean projected collars, anchored swallowing, wall-collar closure, and current reduced descent alternatives.
- `split-lift-row-nerve-diagnostics.md`: row-nerve gap-chain diagnostics and cycle-lowering tools.
