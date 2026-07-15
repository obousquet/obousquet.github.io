# Row-torsor and anchored-quotient route

This packet is the current routing memo for the signed-balance stage of the
prescribed-dual bridge realization problem. Pair it with `prescribed_dual_bridge_realization.tex` and
`ledgers/proof_route_topological_dictionary.md`; do not use older chat history
as state.

## Current target

Fixed-pair realization is reduced in `prescribed_dual_bridge_realization.tex` to signed balance of
the coherent-row equality graph, equivalently to vanishing of the row-torsor
Cech class. In the higher-middle range `m <= 2d+1`, repeated-edge sign
compatibility gives the local descent needed to define this class. The remaining
obstruction is global row-torsor holonomy.

The active target is now the exact actual-cocycle gluing statement:

```text
target:actual_coordinate_potential_gluing
```

Equivalently, for the actual row-torsor cocycle, the local coordinate
potentials

```text
rho_y(o)=o_y
```

must glue to a single row potential.  By
`prop:actual_gluing_component_balance`, this is balance of the
coordinate-component incidence graph `Gamma_comp`.  The current exact
compression is `prop:base_coordinate_constraint_balance`: for any base
coordinate `b`, `Gamma_comp` is balanced if and only if the one-coordinate
constraint graph `Lambda_b` on the components of `G_b` is balanced.  The
forest/no-conflict sufficient criterion is
`cor:base_constraint_forest_balance`.  The component-bit form is
`prop:base_balance_component_bit_form`: choose one correction bit on each base
component so that `alpha(C_b(o))+o_b+o_y` is constant on every `G_y`
component.  The split-lift interpretation is
`prop:base_row_graph_primal_repair_hypergraph`: for a split at `b`, the
components of `G_b` are exactly the components of the primal repair-block
hypergraph on `Omega`.  Thus `cor:two_component_base_balance` is the current
preferred proof shape: find a recursive split coordinate whose primal
repair-block graph has at most two components and whose correction-bit
constancy has no label-1 loop or parallel-label conflict.

The anchored quotient exactness statement

```text
target:anchored_quotient_exactness
```

remains a stronger sufficient route, not the active leaf.  It asks that the
row-cycle transgression image vanish in
`Q_anch = Z_1(G_eq)/(row-clique triangles + anchored cycles)`, formalized by
`lem:anchored_quotient_h1` as `H_1(Delta_anch; F_2)`.

The current global reduction is `prop:coordinate_anchored_transgression`.
For each coordinate `y`, let `N_y` be the row-nerve subcomplex whose faces have
a common active top-hole variable containing `y`. Row-cycle transgression gives
a map

```text
H_1(N_row; F_2) -> Q_anch,
```

and this map vanishes on every `im H_1(N_y; F_2)`. Therefore the current
non-fractal proof target is:

```text
target:coordinate_cover_homology_generation
H_1(N_row;F_2) = sum_y im H_1(N_y;F_2).
```

If this coordinate-cover quotient vanishes, anchored quotient exactness follows.
If it does not vanish abstractly, the next question is which bridge
axiom kills it, or whether transgression vanishes on the quotient anyway; do
not respond by reopening local fiber-shadow leaves.

The Cech/Mayer-Vietoris sufficient criterion is:

```text
lem:cover_generation_h1
cor:coordinate_cover_cech_reduction
warn:coordinate_cech_overstrong
```

Let `C_coord` be the nerve of the coordinate row cover `{N_y}`.  It is enough
to prove:

```text
tilde H_1(C_coord;F_2)=0,
and every nonempty finite intersection cap_{y in S} N_y is connected.
```

This remains a sufficient Cech/Mayer-Vietoris condition for coordinate-cover
homology generation, but it is not the active target.  The calibrated `(8,4)`
audit `scripts/verify_footprint_cech.py` refutes the connected-intersection
condition on realized prescribed-dual systems: the footprint complex has
`H_1=0`, but many filtered row nerves `N_{>=S}` are disconnected.

The footprint reformulation is `prop:coordinate_cech_footprint_form`.  For a
coherent row `o`, put

```text
L(o)=union_{T in U_o} T.
```

Then

```text
C_coord = union_o 2^{L(o)},
cap_{y in S} N_y = N_{>=S} = {sigma in N_row : S subset L(sigma)}.
```

The overstrong Cech target can therefore be stated as a row-footprint problem:

```text
tilde H_1(union_o 2^{L(o)};F_2)=0,
and every nonempty N_{>=S} is connected.
```

This overstrong target is refuted by the diagnostic above.  The active target
is now the direct coordinate-cover quotient:

```text
H_1(N_row;F_2) = sum_y im H_1(N_y;F_2),
or transgression vanishes on the quotient.
```

The current finite audits identify the exact Mayer-Vietoris replacement for
the false connected-intersection shortcut.  Let

```text
C^{(0)}_p = direct sum_{|S|=p+1} H_0(cap_{y in S} N_y; F_2).
```

The current non-fractal proof target is:

```text
target:coordinate_h0_cech_exactness
H_1(C^{(0)}_bullet)=0.
```

This implies coordinate-cover generation and directly incorporates
disconnected filtered row nerves.  Equivalently, by
`lem:edge_difference_cech_kernel`, let `B_bullet` be the row-edge-difference
subcomplex generated by `o+p` over coordinate subsets contained in the common
edge footprint `L({o,p})`.  The sharp algebraic form is:

```text
target:coordinate_edge_difference_injectivity
H_0(B_bullet) -> F_2{coherent rows} is injective.
```

Equivalently, by `lem:edge_difference_row_cycle_generation`, let `G_row` be
the row graph and let `G_y` keep exactly the row edges whose edge footprint
contains coordinate `y`.  The sharp cycle-space form is:

```text
target:coordinate_anchored_row_cycle_generation
Z_1(G_row;F_2) = sum_y Z_1(G_y;F_2).
```

The cycle-space form and the coordinate-cover homology form are now explicitly
identified by `prop:row_cycle_coordinate_homology_quotient`:

```text
Z_1(G_row)/sum_y Z_1(G_y)
  ~= H_1(N_row)/sum_y im H_1(N_y).
```

Thus edge-difference injectivity, component-valued Cech exactness,
coordinate-cover homology generation, and coordinate-anchored row-cycle
generation are one quotient, not parallel leaves.  The dual form
`prop:dual_local_potential_row_cycle_form` says that every edge cochain on
`G_row` whose restriction to each coordinate subgraph `G_y` is a coboundary
must be a global coboundary.

This all-cochain statement is stronger than what signed balance strictly
needs.  The exact final-problem target is now
`target:actual_coordinate_potential_gluing`.  By
`lem:row_cocycle_coordinate_local_exactness`, the actual row-torsor cocycle
`c` satisfies

```text
c_{op} = rho_y(o)+rho_y(p)
```

on every edge of `G_y`, where `rho_y(o)` is the `y`-coordinate of the chosen
endpoint representative of row `o`.  Signed balance is exactly the assertion
that these actual coordinate potentials glue to one row potential.

This exact gluing problem is reduced by `prop:actual_gluing_component_balance`
to balance of the coordinate-component incidence graph `Gamma_comp`.  Its
vertices are pairs `(y,C)` with `C` a connected component of the coordinate
edge graph `G_y`; each row `o` and coordinate pair `y,z` gives an edge from
`(y,C_y(o))` to `(z,C_z(o))` labelled `o_y+o_z`.  A balancing potential on
this labelled graph is equivalent to a global row potential for the actual
row-torsor cocycle.

The stronger sufficient target remains:

```text
target:global_row_nerve_h1_vanishing
H_1(N_row;F_2)=0.
```

The `1000`-seed realized-dual audit checks `699` distinct systems and finds
`h0_cech_h1_profile=0:699`, `row_nerve_h1_profile=0:699`, and
`coordinate_quotient_dim_profile=0:699`.  The recursive-candidate audits with
`(recursive_seed, side_seeds)=(3,0)` and `(3,50)` check `9` and `3` distinct
disjoint candidates, again with zero component-valued Cech `H_1`, zero
row-nerve `H_1`, and zero coordinate quotient.

## Single residual obstruction

The current consolidation is:

```text
prop:anchored_quotient_normal_form
cor:single_residual_anchored_obstruction
```

If anchored quotient exactness fails, then some row-cycle transgression class
has a witnessed representative that is simultaneously:

- row-chordless;
- cyclically row-private;
- witness-edge-private;
- coreless, meaning the intersection of all consecutive top-hole overlaps is
  empty.

This private coreless quotient cycle is the only active residual obstruction.
Any future local work should be judged by whether it rules out this object or
proves that it cannot lie in the row-cycle transgression image.

## What is proved and reusable

- `prop:row_torsor_descent`: coherent fixed-pair signatures exist exactly when
  the row-torsor Cech class vanishes.
- `lem:row_cycle_transgression`: evaluation on a row-nerve cycle is the sign
  sum of the associated transgressive equality closed walk.
- `cor:transgressive_cycle_criterion`: fixed-pair realization is equivalent to
  vanishing of all row-cycle transgressive holonomies.
- `lem:eq_anchored_cycles_balance`: anchored equality cycles are balanced.
- `cor:eq_anchored_generation_balance`: generation by row-clique triangles and
  anchored cycles implies signed balance.
- `lem:anchored_quotient_h1`: the anchored quotient is a first homology group.
- `prop:anchored_quotient_normal_form`: nonzero quotient classes have private
  coreless witnessed-cycle representatives.
- `prop:coordinate_anchored_transgression`: transgression factors through
  `H_1(N_row)` and kills the homology of every coordinate row subcomplex.
- `lem:cover_generation_h1` and `cor:coordinate_cover_cech_reduction`: the
  coordinate-cover generation target follows from Cech `H_1`-acyclicity of
  the coordinate cover nerve plus connected nonempty finite intersections.
- `prop:coordinate_cech_footprint_form`: the Cech target is equivalent to
  acyclicity of the footprint complex `union_o 2^{L(o)}` plus connectedness of
  all nonempty filtered row nerves `N_{>=S}`.
- `warn:coordinate_cech_overstrong` and `scripts/verify_footprint_cech.py`:
  the Cech connected-intersection criterion is false as a general target even
  in realized calibrated systems; the same audit finds zero component-valued
  Cech `H_1`, zero coordinate quotient, and zero row-nerve `H_1` in the
  realized greedy and recursive-candidate batches.
- `lem:edge_difference_cech_kernel`: the component-valued Cech target is
  equivalent to injectivity of the edge-difference map
  `H_0(B_bullet) -> F_2{coherent rows}`.
- `lem:edge_difference_row_cycle_generation`: edge-difference injectivity is
  equivalent to coordinate-anchored row-cycle generation
  `Z_1(G_row)=sum_y Z_1(G_y)`.
- `prop:row_cycle_coordinate_homology_quotient`: the row-cycle quotient is
  canonically the same as the coordinate-cover homology quotient
  `H_1(N_row)/sum_y im H_1(N_y)`.
- `prop:dual_local_potential_row_cycle_form`: the same quotient vanishes iff
  local coordinate coboundaries glue to a global row coboundary.
- `lem:row_cocycle_coordinate_local_exactness`: the actual row-torsor cocycle
  is coordinate-locally exact, with local potentials given by row coordinate
  functions.
- `target:actual_coordinate_potential_gluing`: gluing those actual coordinate
  potentials is necessary and sufficient for signed balance; the all-cochain
  quotient route is sufficient but stronger.
- `def:coordinate_component_incidence_graph`,
  `prop:actual_gluing_component_balance`, and
  `target:coordinate_component_incidence_balance`: the exact gluing problem is
  equivalent to balance of the labelled component-incidence graph `Gamma_comp`.

## Parked sufficient mechanisms

Route A, local certified-shadow/fiber-shadow descent, is stalled. It produced
useful guardrails, but the remaining pieces split into `B`-active transfer,
inactive corner provenance, and terminal deleted-source handoff without a
common descent mechanism. Reopen Route A only if a global quotient principle
explains why all these terminal cases descend.

Route B, witnessed-cycle lowering, is a sufficient mechanism for the private
coreless obstruction, not a parallel active frontier. The row-chord,
cyclic-privacy, edge-private-witness, dominated-pivot, and dominated-chain
reductions are proved. Use Route B only if the global homology route needs a
concrete descent move for the normal-form obstruction.

## Diagnostics status

Existing scripts remain calibration/regression tools, not proof obligations:

```text
scripts/explore_row_nerve_gap_chains.py --verify-row-torsor-balance
scripts/explore_row_nerve_gap_chains.py --verify-witness-edge-private-cycles
scripts/explore_m8d4_signature_system.py --verify-row-torsor-balance
scripts/verify_footprint_cech.py --seeds 1000 --max-enum-components 26
scripts/verify_footprint_cech.py --seeds 0 --recursive-samples 100000 --recursive-seed 3 --side-seeds 0 --max-enum-components 26 --stop-on-failure
scripts/verify_footprint_cech.py --seeds 0 --recursive-samples 50000 --recursive-seed 3 --side-seeds 50 --max-enum-components 26 --stop-on-failure
```

Recorded finite runs found no row-torsor conflicts and no witness-edge-private
blockers in the tested states. This is evidence that the obstruction is sharp,
not a proof for arbitrary prescribed-dual bridge pairs.

## Next proof move

Attack base-coordinate constraint balance first:

```text
Balance Lambda_b for some/every base coordinate b, equivalently balance
Gamma_comp and glue rho_y(o)=o_y to one row potential p(o).
```

A proof closes signed balance directly.  The forest/no-conflict criterion for
`Lambda_b` is the current sharp proof shape to test against bridge
structure; via `prop:base_row_graph_primal_repair_hypergraph`, this is now a
statement about the primal repair-block hypergraph in the split-lift model.
Via `prop:base_balance_component_bit_form`, the exact remaining obstruction is
failure of correction-bit constancy on coordinate components.  The
all-cochain theorem remains a clean sufficient route:

```text
Z_1(G_row;F_2) = sum_y Z_1(G_y;F_2).
```

In dual language, this stronger theorem says that any edge cochain that is a
coboundary on every `G_y` is a coboundary on `G_row`.  A proof of the stronger
`H_1(N_row;F_2)=0` also closes the route, but do not force all work through
row-nerve acyclicity or the all-cochain quotient if the actual row cocycle has
more exploitable structure.  A counterexample with nonzero row-nerve `H_1`
should be tested for whether the actual row cocycle is still globally exact
and whether `Z_1(G_row)/sum_y Z_1(G_y)`, `H_1(C^{(0)}_bullet)`, and the
coordinate quotient are still zero.  Do not
add more local leaves unless they attack this exact row-cycle/Cech
obstruction, the coordinate quotient, or the private coreless normal-form
obstruction.
