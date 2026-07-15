# Raw Yang core dictionary

Use this packet for stable facts about the raw simplicial Yang complex `Delta_H`.

## Numerical and CM facts

- `VC(H) <= hd(H)`, `hs(H) <= hd(H)`, and `STD(H)-1 <= hd(H)` via Scarf faces.
- `CM(Delta_H) <=> H ample` is proved in `main.tex`. Hence CM Yang complexes have `hd=VC`.
- The converse `hd=VC => CM` is false.
- For nonempty Yang complexes, `constructible(Delta_H) <=> ample <=> CM(Delta_H)`.
- For nonempty Yang complexes, `SCM(Delta_H) <=> ample <=> CM(Delta_H)`, because raw Yang complexes are pure.

## Structural facts

- Every nonempty raw Yang complex is pure and balanced (`prop:yang_pure_balanced_crosspolytope`). Facets choose one literal over each coordinate.
- The facet-ridge graph of `Delta_H` is canonically the one-inclusion graph `Q(H)` (`prop:yang_facet_ridge_connectivity`). This is not an ampleness criterion in general.
- Ordinary connectedness is literal co-occurrence: if `R(H)` joins two realized literals when some concept realizes both, then `Delta_H` is connected iff `R(H)` is connected (`prop:yang_ordinary_connectedness`). Keep `R(H)` separate from `Q(H)`.

## Teaching and Scarf guardrails

- The unrestricted set-taught subsets form a hypergraph, not generally a simplicial complex.
- The canonical simplicial teaching object is the irredundant set-teaching complex, equivalently the Scarf complex of `I^*_{Delta_H}`.
- Ordinary teaching is the singleton version-space case of set-teaching; irredundancy is the Scarf/algebraic essentiality condition, while minimal sample size is a separate optimization layer.
- Do not require a teaching sample to contain all fixed coordinates of the canonical agreement cube; smaller samples may exist.
- Universal topology for the Scarf/irredundant teaching complex is false: `prop:scarf_cone_realization` realizes arbitrary finite complexes as links, and `cor:scarf_not_universally_shellable` gives nonshellable examples.
- The naive downward closure of the set-teaching hypergraph is trivial because `H` itself is set-taught by the empty sample (`prop:downward_set_teaching_trivial`).
