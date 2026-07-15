# Antipodal bridge classification and recursive criteria

First gluing compatibility is now formalized as
  `cor:maximum_fiber_split_compatibility`: after splitting a minimal non-ample
  class over coordinate `x` as `H=0*A union 1*B`, the side fibers are maximum
  VC `VC(H)-1` classes and every non-split sliced re-gluing
  `0*A_{y=c} union 1*B_{y=c}` is ample.  The remaining structural target is
  therefore a multi-slice local-ampleness compatibility classification, not a
  free gluing problem for two maximum classes.  The projected union is also
  constrained by `cor:maximum_fiber_projection_union_obstruction`: `A union B`
  is either the full cube or is non-ample; the proper-ample union case is
  exactly the forbidden Claim-X projection.  The full-projection branch is now
  closed by `cor:maximum_fiber_projection_dichotomy`: it is the antipodal
  co-pair endpoint.  In the remaining branch, `A union B` is a smaller minimal
  non-ample class with the same VC dimension, and the common reduction has
  forced size `2*sum_{i<=VC(H)-2} binom(n-2,i)`.  Iterating this gives
  `cor:minimal_nonample_projection_spine`: every projection onto more than
  `VC(H)+1` coordinates remains minimal non-ample with the same VC dimension,
  every projection onto exactly `VC(H)+1` coordinates is an antipodal co-pair,
  and every projection onto at most `VC(H)` coordinates is full.  Thus every
  `VC(H)`-set is shattered in a minimal non-ample class.  The intersection side
  is also recursive (`cor:maximum_fiber_common_reduction_descent`): for a split
  `H=0*A union 1*B`, the common reduction `A cap B` is empty when `VC(H)=1`,
  and is minimal non-ample with VC `VC(H)-1` when `VC(H)>=2`; every
  `VC(H)`-projection of `A cap B` is an antipodal co-pair.  The split is in
  fact antipodal (`cor:minimal_nonample_antipodal_split_normal_form`): for
  every coordinate split, the side fibres satisfy `B=bar A`, so
  `H=0*A union 1*bar(A)` for a maximum VC `VC(H)-1` class `A`.  Equivalently,
  every minimal non-ample class is antipodally closed.  The remaining gluing
  problem is therefore the classification of maximum classes `A` whose
  antipodal suspension is minimal non-ample.  The graph/cubical translation is
  explicit (`prop:antipodal_split_graph_cubical_normal_form`): with
  `K=A cap bar(A)`, `Q(H)` is two copies of `Q(A)` bridged by vertical matching
  edges indexed by `K`, and
  `X_H=(0*X_A) union (1*X_barA) union ([0,1]_x times X_K)`.  The bridge `K`
  is empty in rank `1` and minimal non-ample of VC `VC(H)-1` in higher rank.
  The exact reduced target is now formalized by
  `def:antipodal_suspension_cross_slices`,
  `prop:antipodal_suspension_minimality_criterion`, and
  `q:antipodal_suspension_classification`: if `A` is maximum VC `d<|Y|`, then
  `Susp_x(A)=0*A union 1*bar(A)` is automatically non-ample, and it is minimal
  non-ample iff every cross-slice
  `0*A_{y=c} union 1*bar(A_{y=1-c})` is ample.  The complement has the dual
  normal form (`cor:antipodal_split_dual_normal_form`)
  `H^c=0*A^c union 1*bar(A^c)`, where `A^c` is maximum of VC `|Y|-VC(H)` and
  the dual bridge is `K^vee=2^Y\(A union bar(A))`.  The remaining reduced
  target is to characterize these maximum side classes in graph/cubical or
  partial-cube-minor language.  The side-VC-dimension-one case is closed by
  `thm:vc_one_antipodal_suspension_classification`: for maximum VC-one `A`,
  `Susp_x(A)` is minimal non-ample iff `Q(A)` is a path; then
  `Q(Susp_x(A))` is the `2(|Y|+1)`-cycle, recovering the VC-two minimal
  non-ample model from the side-fiber viewpoint.  The classification is
  self-dual by `prop:antipodal_suspension_side_duality`:
  `Susp_x(A)^c=Susp_x(A^c)`, so compatibility of a maximum VC `d` side is
  equivalent to compatibility of its maximum VC `|Y|-d-1` side-complement.
  Consequently the dual one-dimensional side case is also closed
  (`cor:corank_one_antipodal_suspension_classification`): maximum VC `|Y|-2`
  sides work iff their complements are rank-one path sides.  The recursive
  bridge obstruction is formalized by `cor:antipodal_bridge_recursion`: if
  `A` is maximum VC `d` on `m=|Y|` coordinates and compatible, then
  `K=A cap bar(A)` is empty for `d=0` and otherwise minimal non-ample VC `d`
  of size `2*sum_{i<=d-1} binom(m-1,i)`; dually
  `K^vee=2^Y\(A union bar(A))` is empty for `m-d-1=0` and otherwise minimal
  non-ample VC `m-d-1` with the analogous size.  This is a necessary
  bridge constraint, not a converse.  The remaining side data is
  isolated by `cor:antipodal_four_piece_side_decomposition`: writing
  `P=A setminus bar(A)`, one has `2^Y=K sqcup K^vee sqcup P sqcup bar(P)`,
  `A=K sqcup P`, and `|P|=binom(m-1,d)`.  Thus the live middle-rank target is
  an asymmetric-frontier transversal problem between two bridges,
  subject to maximumity and all cross-slice ampleness tests.  The twisted
  cross-slices are directly controlled by bridge fibres
  (`cor:antipodal_twisted_bridge_fibres`): for
  `U=A_{y=c}`, `V=bar(A_{y=1-c})`, `T=U union V`, and `L=U cap V`, one has
  `L=K_{y=c}` and `2^(Y\\{y})\\T=K^vee_{y=c}`.  Hence, once the dual bridge
  has its recursive minimal-non-ample form, the twisted projection obstruction
  is automatic; the remaining local compatibility obstruction is simultaneous
  `d`-shattering by the two twisted fibres.  The frontier form of this
  obstruction is `cor:antipodal_twisted_phantom_frontier`: since each
  `K_{y=c}` is maximum VC `d-1`, for every `d`-set `S` it misses a unique
  label `lambda_{y,c,S}`; compatibility is equivalent to forbidding this same
  missing label from appearing in both `P_{y=c}|S` and `(bar P)_{y=c}|S`.
  These double fillings are the twisted phantom top traces isolated by the
  intermediate bridge-phantom criterion.  They are now known to be automatic
  non-obstructions: `cor:antipodal_phantom_automatic` proves that if `A` is
  maximum VC `d` and `K=A cap bar(A)` is minimal non-ample VC `d`, then no
  twisted phantom top trace can occur.  On `T=S union {y}`, the bridge has the
  antipodal co-pair holes `(c,lambda)` and `(1-c,bar(lambda))`, while
  maximumity of `A` makes `A|T` a one-punctured cube; hence the frontier
  `P=A \setminus bar(A)` fills exactly one hole and cannot double-fill both.
  The consolidated intermediate criterion is
  `thm:antipodal_bridge_phantom_criterion`: for `1<=d<|Y|`,
  `Susp_x(A)` is minimal non-ample iff the primal bridge is minimal non-ample
  VC `d`, the dual bridge is empty when `|Y|-d-1=0` and otherwise minimal
  non-ample of VC `|Y|-d-1`, and the frontier has no twisted phantom top
  traces.  The active exact criterion is the cleaner
  `thm:antipodal_bridge_criterion`: for `1<=d<|Y|`,
  `Susp_x(A)` is minimal non-ample iff `K=A cap bar(A)` is minimal non-ample
  VC `d` and `K^vee=2^Y\(A union bar(A))` is empty in dual dimension zero or
  minimal non-ample of VC `|Y|-d-1` otherwise.  There is no additional
  twisted-phantom obstruction.  The remaining middle-rank problem is therefore
  a bridge-realization problem: characterize maximum sides `A` for
  which both antipodal bridges have the prescribed recursive minimal-non-ample
  form.  The bridge criterion is self-dual by
  `cor:antipodal_bridge_self_dual`: under `A -> A^c`, the side VC dimension
  `d` is replaced by `e=|Y|-d-1` and the two bridges swap,
  `K_{A^c}=K_A^vee` and `K_{A^c}^vee=K_A`.  Since side-VC-dimension one and dual dimension
  one are already classified, the open side VC dimensions may be restricted to
  `2 <= d <= floor((|Y|-1)/2)`; the first genuinely self-dual middle case is
