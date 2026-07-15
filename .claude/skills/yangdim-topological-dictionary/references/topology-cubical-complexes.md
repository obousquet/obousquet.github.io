# Cubical complexes packet

Use this packet for `X_H`, `X_{H^c}`, cubical collapsibility, CAT(0), median, shellability conventions, and VC-one graph strata.

## Cubical collapsibility

- For a nonempty ample class, `X_H` is collapsible (CCMW Proposition 4.12), with one-skeleton `Q(H)`.
- If `H` is proper ample, complement-ampleness gives nonempty ample `H^c`, so `X_{H^c}` is collapsible (`prop:ample_cubical_collapsible`).
- This is not a corner/dismantling theorem: Hall's `C_H` has collapsible `Q(C_H)` but no corner and no dismantling.
- Converse is false: non-ample classes can have collapsible `X_H` or `X_{H^c}`.

## Dimension and purity

- Cells of `X_H` are positioned strongly shattered cubes `(S,tau)` whose full extension cube lies in `H`.
- `dim X_H=max{|S|: S in st(H)}`; for ample classes this equals `VC(H)` because `st(H)=sh(H)` (`cor:ample_cubical_dimension_vc`).
- Cubical purity means every inclusion-maximal contained subcube has the same free-coordinate size. It is stronger than purity of the abstract family `st(H)`.
- Ampleness does not imply cubical purity (`ex:ample_cubical_nonpure`). Cubical shellability/constructibility results that assume purity need an explicit purity hypothesis or non-pure convention.

## CAT(0), median, and graph stratum

- `X_H` is CAT(0) iff `Q(H)` is a median graph in its intrinsic graph metric (`prop:cubical_cat0_median`).
- Connected coordinatewise-majority closure is a stronger ambient sufficient condition and implies an ample/dismantlable CCMW median class; the converse is false (`ex:intrinsic_cat0_not_majority`).
- For nonempty `VC(H)<=1`, `X_H` is a graph. In this stratum, `H` ample iff `Q(H)` connected iff `Q(H)` is a tree iff `X_H` collapsible iff `X_H` CAT(0)/median (`prop:vc_one_cubical_tree`).
- Under standard graph conventions, graph shellability/constructibility are weaker than tree-ness; outside `VC<=1`, even tree-ness of `X_H` need not imply ampleness because shattering can be non-positioned.
