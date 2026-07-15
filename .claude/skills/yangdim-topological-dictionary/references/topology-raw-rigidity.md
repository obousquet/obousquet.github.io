# Raw-Yang rigidity packet

Use this packet for standard topological adjectives applied directly to the raw Yang complex `Delta_H`.

## Deletion-robust CM and Buchsbaum

- Standard same-dimension deletion-robust `k`-CM raw Yang complexes are classified: `k=1` is ordinary CM/ample; `k=2` iff `H=2^X`; `k>=3` is impossible for nonempty classes on nonempty ground sets.
- The `k=2` proof uses `lem:yang_literal_deletion_dominated`: deleting a realized literal forces the matching projected fiber to be contained in the opposite fiber; applying both literals forces closure under coordinate flips.
- The direct same-dimensional deletion-Buchsbaum weakening is also rigid: every one-literal deletion pure Buchsbaum of original dimension forces `H=2^X` (`cor:deletion_buchsbaum_yang_full_cube`).
- Buchsbaum* is not fixed in the paper. Do not state Buchsbaum* classifications until a convention is defined.

## Sphere and pseudomanifold rigidity

- Gorenstein* raw Yang complexes are only full cubes: CM gives ampleness, and proper ample Yang complexes are nonevasive/collapsible/contractible, not spheres.
- Closed pseudomanifold/no-boundary raw Yang complexes are only full cubes: every missing Hamming neighbor creates a free ridge (`prop:yang_codim_one_boundary`).
- Under the common pseudomanifold-with-boundary convention, `Delta_H` has the property iff `Q(H)` is connected (`prop:yang_pseudomanifold_boundary`). This is not an ampleness criterion in general.

## Dominated literals and raw vertex-decomposability

- Pure literal deletions are exactly dominated literals: `del_{Delta_H}(x,b)` is pure of original dimension iff `H_{x=b} subseteq H_{x=1-b}`, and then the deletion is `(x,1-b)*Delta_{H_{x=1-b}}`.
- Vertex-decomposable `Delta_H` is exactly dominated-literal eliminability.
- This is stronger than shellability and stronger than ampleness in general, but in the `VC(H)<=1` stratum the raw-Yang hierarchy collapses to ampleness (`cor:vc_one_raw_hierarchy`).
- Do not confuse dominated-literal eliminations with cubical corner peeling/dismantlability.

## T4 nonevasiveness/collapsibility

- `thm:proper_ample_nonevasive`: for the simplicial Yang complex, proper ample implies nonevasive, hence collapsible. The full cube is excluded because `Delta_H` is the cross-polytope sphere.
- Converse is false: non-ample collapsible/nonevasive Yang complexes already occur at `n=3`.
- The proof uses an ambient cross-polytope ball lemma, fixed-shadow complement reduction, and the full-shadow projection observation.
- The single-missing-facet strengthening is dead in dimension `5`; T4 does not assert that one missing facet supplies the whole certificate.
