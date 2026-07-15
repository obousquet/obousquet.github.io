# Split-lift row-nerve diagnostics

Use this packet for row-nerve gap-chain diagnostics and cycle-lowering tools adjacent to the split-lift route.

## Dominated-row diagnostics

- `scripts/explore_row_nerve_gap_chains.py` rules out raw incidence domination, single-facet swallowing, star-at-most-two domination, and greedy-star-minimality as general local claims.
- In canonical `(8,4)` batches, reachable deletion states often have a dominated row with maximal star at most `3`, and star-`3` cases have singleton minimum-star cores.
- The honest theorem target is a recursive edge-core three-star/singleton-core maximal-swallowing theorem, not an active-size greedy deletion rule.

## Scope guardrail

- Do not strengthen diagnostics to arbitrary induced row subsets. The induced-core mode finds nondominated arbitrary five-row induced subsets with row-nerve `H_1=1`.
- Reachability from prescribed-bridge survivor dynamics is a real hypothesis unless the proof switches to direct cycle lowering for the actual row nerve.

## Cycle-lowering tools

- `lem:cycle_specific_link_coning` removes a vertex from a row-nerve cycle whenever its incident cycle-neighbor chain bounds in that vertex link.
- `cor:usable_row_h1_criterion` reduces row-nerve `H_1=0` to finding a usable row in every nonzero cycle.
- Remaining direct crux: `target:reachable_cycle_usable_row`, i.e. prove actual recursive row-nerve cycles always have such a usable row after triangle replacements or recursive witness lowering.
- Private-edge witnessed cycles refute the lower-link pivot as a local incidence-only claim; any proof must use prescribed-pair provenance or provide a provenance-lower two-filling.
