# Split-lift exact formulation

Use this packet for variables and finite constraint reductions in the split-lift route.

## Exact split-lift setup

- `prop:exact_common_coordinate_split_reduction` rewrites a common coordinate split
  `K=0*F union 1*bar(F)`, `K^vee=0*D union 1*bar(D)`, `T=Q_Y\D`
  as the split-lift problem `U union V=T`, `U cap V=F`, with candidate side `A=0*U union 1*bar(V)`.
- Under bridge sizes, every split has Sauer-tight size.
- Validity is exactly the two VC tests: `VC(U union bar(V))<=d` and no `d`-set shattered by both `U` and `bar(V)`.
- Repair-variable form: `W=V\F=T\U`, so `U=T\W` and `V=F union W`.

## Cross-test component contraction

- If `lambda_R` is the unique label missed by maximum bridge fiber `F` on a `d`-set `R`, the cross test is equivalent to `W` being all-or-none on each block `{z in T\F : z|R=lambda_R}`.
- The side-complement gives dual blocks from missing labels of `D` on codimension-`d` sets.
- Every valid split is therefore a union of components of the combined primal/dual repair hypergraph.

## Top test

For each `(d+1)`-set `S`, with `tau_S` the unique label missed by `T` on `S`, either:

- `bar(tau_S)` is not realized by `F union W`, so the original hole remains missing; or
- some `a != tau_S` is removed from `T\W` and not reintroduced by `bar(F union W)`.

After component contraction this is an explicit selected/unselected component system.

## Signed graph reduction

- When each top-support constraint is a complementary binary choice after component contraction, the component system is a signed graph.
- Existence and affine classification are controlled by signed consistency/balance; exactly two repairs are equivalent to signed consistency plus connectedness, modulo the antipodal repair involution (`cor:split_repair_antipodal_pair`).
- Complementary-binary top constraints are equivalent to exactly one missing and separated antipodal label pair in `F|S` for each top support `S`.
- Current connectedness target: `NO-ABSORBED-COMPONENT-CUT`.  For each top-support clause with alternatives `(P_S,Q_S)`, put `B_S=P_S union Q_S`.  The unsigned signed-component graph is connected iff no nonempty proper subset of repair components contains every `B_S` wholly on one side of the cut.  An absorbed cut would allow flipping that side and would create extra repairs beyond global antipodal complement.
- Current comparison status: the split component graph and the fixed-pair equality graph are equivalent at the solution-system level, not by a proved literal graph isomorphism.  Satisfying component labelings, valid repairs, maximum sides, and admissible fixed-pair signatures are canonically in bijection.
