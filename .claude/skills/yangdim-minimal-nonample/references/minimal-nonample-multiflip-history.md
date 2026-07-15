# Single-flip, multiflip, and unit-defect history

This file was split out of the former monolithic `minimal-nonample-vcr-history.md`. Load it only when the task specifically touches this historical route.

The first-failure version is now proved (`lem:single_flip_first_failure_lift`): if a
minimal `W subset V` is not shattered by one single-flip fibre, then that fibre projects to the
punctured cube `2^W\\{alpha}`, and every ambient extenture contained in the missing trace
`phi^u union alpha` contains all of `W`.  Such a lift has support `A union W`, `A subset D`, size at
least `m=|D|`; if it has size `m`, maximality of the original overlap forces it to replace exactly
`|W|` old coordinates from `R=D cap K` and keep all of `U=D\\K`.  The live obstruction is therefore
overlap-deleting first-failure lifts.  The secondary weighted tie-breaker is proved
(`cor:weighted_first_failure_exchange`): if `D` also maximizes a chosen weight sum on `D cap K`,
then any minimum-size first-failure lift replacing `W subset V` has support `(D\\B) union W` with
`B subset R`, `|B|=|W|`, and `weight(W)<=weight(B)`.  Thus weight-increasing exchanges are excluded
and must instead be higher-support graded-replacement failures.  The operational pairwise form is
`cor:pairwise_single_flip_failure_dichotomy`: if a single-flip fibre fails to shatter `{x,y} subset
V`, then the projection is a punctured square and every ambient extenture below its missing label is
either higher-support or a minimum-size two-coordinate exchange `(D\\B) union {x,y}` with
`B subset R`, `|B|=2`, and `weight(x)+weight(y)<=weight(B)`.  The higher-support branch is
finite-height (`cor:pairwise_lift_bounded_height`): every lift has one of exactly three profiles,
`(D\\B) union {x,y}` of size `m`, `(D\\{r}) union {x,y}` of size `m+1`, or `D union {x,y}` of size
`m+2`.  Thus the unresolved pairwise graded branch is only the one-deletion and no-deletion cases.
The exact overlap accounting is proved in `cor:pairwise_higher_lift_overlap_gain`: a pairwise lift
of size `m+j`, `j in {1,2}`, has `K`-overlap at least `|R|+j`; more precisely the `m+1` profile has
overlap `|R|+1` if the deleted coordinate lies in `R` and `|R|+2` if it lies in `U`, while the
`m+2` profile has overlap `|R|+2`.  Equivalently, the off-`K` defect
`delta_K(S)=|S\\K|` never increases under pairwise lifts (`cor:pairwise_lift_defect_monotonicity`);
it strictly drops only in the `m+1` profile deleting a coordinate of `U`, and all other pairwise
profiles preserve `delta_K=|U|`.  Since `K` is shattered, no extenture support is contained in `K`;
hence pairwise lifts satisfy `1<=delta_K(S)<=|U|` (`cor:pairwise_lift_positive_defect`).  In
particular, if `|U|=1`, the pairwise branch is actually closed: `cor:unit_defect_full_v_fiber`
shows that `F_u=H_{D=phi^u}` projects onto the full cube `2^V`, because `K=R union V` is shattered
and any realization of `R=phi|R` cannot take `u=phi(u)` without realizing the missing `D`-trace.
Thus `F_u` shatters all of `V` and no pairwise single-flip failure occurs in unit defect
(`cor:unit_defect_pairwise_profiles`).  Pairwise graded-replacement obstructions start only when
`|U|>=2`.
The side-fibre split is also proved
(`lem:side_extenture_or_overlap_exchange`): for each `x in V` and side value `b`, either some
`r in R` gives a same-size extenture on `D-r+x`, or the side fibre `H_{x=b}` has `phi` as an
extenture on `D` and therefore projects to `2^D\\{phi}`.  In the second branch, the side realizes
every non-empty multi-flip `phi^T`, `T subset U`; if both sides are in this branch then each
non-empty multi-flip fibre strongly shatters `{x}`.  The packaged consequence
`cor:outside_coordinate_exchange_or_flip_visibility` says that each `x in V` either already gives a
same-size one-coordinate overlap exchange `D-r+x`, or every non-empty flip fibre `H_{D=phi^T}`
strongly shatters `{x}`.  Thus, after excluding one-coordinate exchanges for `x`, all remaining
failures involving `x` are genuinely multi-coordinate coupling failures; singleton edge visibility
is no longer an open issue.  Multi-flip first failures are now packaged by
`lem:multiflip_first_failure_lift`: if one-coordinate exchanges are excluded for all `x in V`,
`F_T=H_{D=phi^T}` is any nonempty flip fibre, and `W subset V` is inclusion-minimal not shattered by
`F_T`, then `|W|>=2`, `F_T|W=2^W\\{alpha}`, and every ambient extenture below
`phi^T union alpha` contains all of `W`.  A minimum-size lift keeps all of `U=D\\K` and deletes
exactly `|W|` old overlap coordinates from `R=D cap K`.  Therefore the first-failure lift
structure is no longer special to single flips.  The weighted version is also proved
(`cor:weighted_multiflip_first_failure_exchange`): after the secondary weight tie-breaker, any
minimum-size lift of a multi-flip first failure has support `(D\\B) union W`, `B subset R`,
`|B|=|W|`, and `weight(W)<=weight(B)`.  Thus weight-increasing multi-flip failures are forced into
the higher-support graded branch; the exchange-frontier mechanism does not depend on choosing a
single-flip fibre.  The higher branch is finite-height (`cor:multiflip_first_failure_profiles`):
for `q=|W|`, every lift support is `(D\\B) union W` with `B subset D`, `|B|<=q`, and height
`j=q-|B| in {0,...,q}`; its `K`-overlap is at least `|R|+j`, and its off-`K` defect is
`|U|-|B cap U|`, so the defect never increases and remains positive.  Height `0` is exactly the
weighted exchange branch.  Unit-defect strict-drop endpoints are terminal away from the top boundary
(`cor:multiflip_unit_defect_endpoint`): if a lift support `S` has `delta_K(S)=1`, unique off-`K`
coordinate `z`, and `K\\S` is nonempty, then the flipped fibre `H_{S=psi^z}` projects onto the
full cube on `K\\S`.  The exact height accounting is now proved
(`cor:unit_defect_height_accounting`): in the genuine coupling range `|U|>=2`, for
`S=(D\\B) union W` of height `j`, unit defect means
`B cap U=U\\{z}`, `|S cap K|=m+j-1`, and `|K\\S|=k-m-j+1`; non-top endpoints are exactly
`j<=k-m`, while top endpoints are exactly `j=k-m+1`.  The top unit-defect branch is conditionally routed
(`cor:multiflip_top_boundary_conditional`): if a lift support is `K union {z}` and the projection
shatters every proper subset, then the existing one-coordinate top-skeleton trichotomy gives either
the unique-puncture/Claim-X branch or the antipodal co-pair branch.  The missing input is exactly
this proper-skeleton hypothesis; it is automatic in the old pairwise top branch.  Its failure now
descends under the normalized minimum-support, maximum-overlap choice (`cor:multiflip_top_boundary_descent`):
for `|U|>=2`, a missing proper trace inside `K union {z}` gives a unit-defect extenture `E` with
`m<|E|<=VC(H)`, and the flipped fibre is full on `K\\E`; by height accounting this is strict
positive-height descent from the top height.  Thus the top unit-defect branch is reduced
to proper-skeleton puncture/co-pair or a positive-height low-degree terminal unit-defect support.
The packaged endpoint trichotomy (`cor:complete_unit_defect_endpoint_trichotomy`) is now: non-top
unit-defect endpoints are terminal full-fibre endpoints, top proper-skeleton endpoints are
unique-puncture/Claim-X or antipodal co-pair, and top proper-skeleton failures descend to strictly
lower-height non-top terminal endpoints.  Unit defect therefore has no independent topological
residual; the remaining obstruction must use the old failed set `W` or exchange/better-overlap data.
The residual block of a terminal non-top endpoint is identified exactly
(`cor:unit_defect_residual_block`): if `S=(D\\B) union W`, then
`K\\S=(B cap R) sqcup (V\\W)`.  The full flipped fibre therefore kills every obstruction internal
only to the deleted old-overlap coordinates and the outside coordinates not in the original failed
set; any surviving obstruction must involve `W`, the off-`K` coordinates, or the exchange/comparison
data that produced the endpoint.  The arity budget is explicit (`cor:unit_defect_arity_budget`):
if `p=|U|`, `q=|W|`, and `B_R=B cap R`, then every unit-defect endpoint of height `j` satisfies
`q=p+j-1+|B_R|`; hence `q>=p`.  Thus pairwise first failures can reach unit defect only for
`|U|<=2`, while for `|U|>=3` they remain in the higher-defect/graded-replacement branch.
The unit-defect base case is closed (`cor:unit_defect_multiflip_failures`):
if `U={u}`, the only non-empty flip fibre is `F_u` and `F_u|V=2^V`, so no multi-flip first failure
occurs; genuine coupling starts only at `|U|>=2`.  Computational audit through exhaustive `n<=4`
plus antipodal/co-pair/cycle/complement families in `n=5,6` found no maximal-overlap configuration
with `|V|>=2`; relaxed individual-fibre near-misses in the `10`- and `12`-cycles are punctured
squares, and their missing labels contain same-size extentures with strictly larger `K`-overlap.
