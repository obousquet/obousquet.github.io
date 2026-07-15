# First-middle signatures and bridge-pair classification

This file was split out of the former monolithic `m6d2-finite-signatures.md`. Load it only when the task specifically touches this finite-signature route.

`(m,d)=(5,2)`.  This first middle case is nonempty and not unique:
`scripts/explore_antipodal_side_m5d2.py` enumerates `192` labelled
antipodal `10`-cycle bridges, `5952` ordered disjoint bridge pairs,
`380928` frontier orientations, and `11904` compatible labelled maximum
VC-two sides across four one-inclusion degree profiles.  These form six
cube-automorphism orbits of sizes `384,1920,1920,1920,1920,3840`; after
also identifying side-complement `A -> A^c`, there are five orbits, with
cube orbits `4` and `5` paired and the others self-complementary up to cube
automorphism.  One representative is promoted to `main.tex` as
`ex:first_middle_antipodal_side`, and the orbit census is recorded as
`rem:first_middle_antipodal_census`, giving explicit minimal non-ample
VC-three antipodal suspensions on six coordinates.  A first diagnostic shows
that coarse one-inclusion graph data is not the classifier: in all six
orbits `Q(A)` has `16` vertices, `25` edges, balanced edge-label multiset
`(5,5,5,5,5)`, one connected component, diameter `5`, and `10` four-cycles.
Bridge-pair distance data separates orbit `1`, orbit `2`, and the block
`3-6`; `K`--`K^vee` edge-label data separates orbit `3` from `4-6`; the
remaining distinctions live in the asymmetric frontier orientation
`P=A setminus bar(A)` (attachment profiles and missing-label signatures on
three-coordinate projections).  The general signature encoding is now proved
as `prop:maximum_missing_signature`: if `A` is maximum VC `d`, then the
unique missing labels `mu_T` on all `(d+1)`-coordinate projections determine
`A` by `A={a:a|T != mu_T for every |T|=d+1}`.  Therefore the compatible
side problem can be phrased as a global consistency problem for choosing one
hole `mu_T in {alpha_T,bar(alpha_T)}` on every bridge co-pair projection,
plus the dual bridge condition for `K^vee`.  This is now formalized as
`prop:antipodal_sign_system_parameterization`: for fixed bridges
`K,D`, admissible signatures are exactly those for which every antipodal
pair in `D` hits chosen missing labels on both endpoints, while every
antipodal pair outside `K union D` hits on exactly one endpoint; admissible
signatures are in bijection with compatible maximum sides having bridges
`(K,D)`.  Thus the remaining higher-rank problem is existence and orbit
structure of admissible signatures for bridge pairs, not the
definition of the frontier object.  In the `(5,2)` census, the
script confirms `11904` distinct missing-triple signatures, each
reconstructing its side exactly.  The general fixed-bridge Boolean form is
now proved as `prop:antipodal_sign_system_affine_form`: after choosing base
holes for the primal bridge, the pairs outside `K union K^vee` impose affine
`F_2` equality constraints on the missing-label signs, while the dual bridge
imposes not-all-equal constraints on the same active sign sets.
