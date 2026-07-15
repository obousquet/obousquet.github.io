# Derived complexes, teaching, h-vectors, and Hall guardrails

- **Δ_H shellable ⟺ teachable-by-attachment** (unconditional, `thm:shellable_characterization`):
  an ordering where each new concept's restriction-face sample has every coordinate a Hamming-1 flip
  to an earlier concept. Shellable ⟹ ample+dismantlable (CCMW), conditional on CM⟺ample.
- **Sequentially shellable `Delta_H` ⟺ shellable `Delta_H`** because Yang complexes are pure
  (`cor:sequential_shellable_yang_iff_shellable`).
  Sequential shellability remains meaningful for non-pure derived complexes such as `sh(H)`, the
  Scarf/irredundant set-teaching complex, refined teaching-derived complexes, and other derived
  complexes, but it is not a separate class for `Delta_H` itself.  Do not propose the naive downward
  closure of set-teaching as a target; it is the full simplex.
- **`sh(H)` is unrestricted even inside ample classes** (`prop:shattering_complex_unrestricted`,
  `cor:no_ampleness_only_shattering_topology`).  For any finite simplicial complex `Gamma`
  on `X`, take the downward-closed concept class `H=Gamma`.  Then `sh(H)=st(H)=Gamma`, so `H` is
  ample.  Therefore no ampleness-only theorem can force shellability, SCM, approximate CM,
  constructibility, vertex-decomposability, collapsibility, Buchsbaum-ness, etc. of `sh(H)` unless it
  holds for every finite simplicial complex.  Derived topology targets should focus instead on the
  Scarf/irredundant set-teaching complex, explicitly defined downward-closed teaching complexes,
  Alexander-dual complexes, or mixed-degree Yang ideals.
- **Approximate CM is not a raw-`Delta_H` stratum under the paper's current definition**
  (`prop:raw_yang_not_approxcm`).  The definition used in `main.tex` is
  non-pure/two-adjacent-dimensional, while every non-empty Yang complex is pure of dimension `n-1`.
  Treat approximate-CM questions as targets for derived complexes
  (`sh(H)`, the Scarf/irredundant set-teaching complex, refined teaching-derived complexes),
  Alexander-dual complexes, or componentwise pieces of `I_{Delta_H}` / `I^*_{Delta_H}`, and ask
  whether those derived conditions bound the VC--hd gap.
- **Global contractibility/acyclicity of `Delta_H` is too coarse.**  T4 gives
  `proper ample non-full => nonevasive => contractible`; the full cube is the ample spherical
  exception.  The converse fails in an infinite two-concept family
  (`prop:two_concept_collapsible_nonample`): if `H={h,h'}` and the Hamming-difference set `D` is a
  nonempty proper subset of `X`, then `Delta_H` is two `(n-1)`-simplices meeting in the simplex on
  `X\\D`, hence collapsible.  If `2<=|D|<n`, then `|sh(H)|=1+|D|>|H|=2`, so `H` is non-ample.  The
  `n=3`, `|D|=2` case is two triangles meeting in a vertex.
- **h-vector of Δ_H**: for shellable, `h_i = #{concepts taught with sample size i}` (teaching
  histogram); for ample, `h_i = |sh_i(H)|` (shattering histogram); for maximum classes `h_i=C(n,i)`,
  `deg(h)=VC`. **RTD is NOT an h-vector/f-vector invariant** (C_H vs dismantlable max class).
  Outside the ample case, the shattered-set histogram alone does **not** determine the `h`-vector:
  the full projection profile `f_{k-1}=sum_{|S|=k}|H|_S|` does, or equivalently the complement
  cube-face vector via `lem:hvector_cubefaces`.
- **Conditioning = link**: `lk_{(x,b)}(Δ_H) = Δ_{H_{x=b}}` where `H_{x=b}={h|_{[n]∖x}: h(x)=b}`.
  hd is monotone under conditioning and projection; `hd ≤ AID` (adaptive identification depth).
- **h-vector coordinate recursion** (proved): `h_H(t) = (1-t)h_{H|_{[n]∖x}}(t)+t(h_{H_{x=0}}+h_{H_{x=1}})`.
- **Pajor (CORRECT form).** `|sh(H)| = |sh(H|∖x)| + |sh(H_{x=0}) ∩ sh(H_{x=1})|`. ⚠️ The tempting
  exact deficit identity `deficit(H)=deficit(H|∖x)+deficit(H^x)` is **FALSE** (176k violations at n=4;
  e.g. H={∅,1,23,13,123} along x=3): `sh(H_{x=0})∩sh(H_{x=1})` can strictly exceed `sh(H^x)=sh(H_0∩H_1)`.
  What IS true and all we use: `deficit(H) ≥ deficit(H|∖x)` (so **projection of ample is ample**),
  and **H ample ⟹ H|∖x and H^x both ample** (FORWARD only; the converse is false). `H^x=H_{x=0}∩H_{x=1}`
  is the *x-reduction*, NOT a link of Δ_H (the obstruction in CM⟹ample). See `lem:pajor_recursion`.
- **Tracy Hall's `C_H`** (`CH.txt`): ample, n=12, |H|=299, VC=hd=3, **RTD=4** — the counterexample to
  "CM⟹shellable", "RTD=VC for maximum classes", "OCN=VC". The canonical hard test case.
  New T2 status: `Delta_{C_H}` is constructible by the general constructible=ample theorem, and the
  explicit recursive coordinate-splitting certificate remains as verification support
  (`scripts/explore_constructible_hall.py --recursive`: 532 states, 430 clean constructible splits,
  no failures).  Thus `C_H` separates constructible from shellable.  This is now recorded as
  `cor:hall_ccmw_topological_separation`: `Delta_{C_H}` is CM, constructible, nonevasive, and
  collapsible, but not shellable and not vertex-decomposable; `C_H` is ample but has no corner and is
  not dismantlable.
  `sh(C_H)` = exactly the 299 sets of size ≤3. ⚠️ C_H **separates** the addition/deletion forms of the
  Litman–Moran/Rónyai–Mészáros **extension conjecture** (`explore_CH_extension.py`, `rem:CH_extension`):
  C_H has 0 ample single-element DELETIONS (no corner; every C_H∖{c} still shatters all 299 size-≤3 sets
  ⟹ |sh|=299≠298). By complementation (`lem:complement_ample`: ample⟺complement-ample) and H^c∪{c}=(H∖{c})^c,
  adding to C_H^c = deleting from C_H, so **C_H^c (ample, proper, |·|=3797) has 0 ample extensions = a
  MAXIMAL ample class ≠ full cube, REFUTING the extension conjecture**. Addition & deletion forms are
  EQUIVALENT under complementation (both false). [EARLIER ERROR I made: checked only additions to C_H
  (16 exist) and wrongly said "addition survives" — must check the COMPLEMENT.] Verified n=12.
  ⟹ no ample-completion induction (Claim X needs a global/topological argument).
- **No general corner theorem.**  Do not trust claims that every lopsided/ample class has a corner.
  For the CCMW/isometric-ordering notion of corner, Hall's `C_H` is an internal counterexample:
  ample, no corner, not dismantlable, and `Delta_{C_H}` not shellable.  Corner peeling is only a
  sufficient structure for special ample subclasses, not a general induction principle.  Cite
  `cor:hall_ccmw_topological_separation` and `rem:no_general_corner_theorem`.
