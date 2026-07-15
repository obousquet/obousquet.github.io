# Computational pitfalls and diagnostics

## Homology and projective dimension

- Reduced `Htilde_{-1}` convention: `reduced_homology_dim_simple(faces, -1)` returns `1` iff `faces` is empty, but the topologically correct `Htilde_{-1}=k` case is the irrelevant complex `{emptyset}`.
- The old convention drops Koszul/maximal-ideal contributions and can silently give `pd=0` for `T_h=<v_1,...,v_n>` when the truth is `n-1`.
- When computing projective dimension of an arbitrary squarefree ideal, use the fixed `j=-1` rule: `Htilde_{-1}=1` iff `faces=={emptyset}`.
- `compute_hd` needs `n_vars = 2n`, the literal count.
- The Hochster index is `dim+1`, so `hd = max(dim+1 : Htilde_dim(Delta_H[W]) != 0)`.

## Data and command traps

- Parsing `CH.txt`: skip prose lines containing letters, otherwise header digits such as "VC-dimension 3" and "299 concepts" are read as concepts.
- Sanity check for `CH.txt`: `|C_H|=299` and `h=(1,12,66,220)`.
- Background jobs buffer stdout under `> file`; for early results, run a small unbuffered slice with `python3 -u -c "..."` or split the sweep.

## Expensive routines and adversaries

- `yang_dim` and `is_CM` are expensive at `n>=4`; `is_CM` iterates all faces times link homology, and `yang_dim` sweeps `2^{2n}` literal subsets.
- Filter with cheap necessary conditions first, such as ampleness, connectivity, and `hd=VC`, before heavy checks.
- At `n>=5`, sample rather than enumerate unless the finite universe is deliberately bounded.
- Random non-ample classes are often tiny and disconnected, hence trivially non-CM.
- Informative adversaries are near-misses: non-ample but connected with `hd=VC`, often obtained by deleting or swapping one concept of a maximum class such as `ball(n,d)`.
- `is_extremal` is legacy code terminology for ample/extremum; there is no separate `is_ample`.
- Use `shatter_deficit = |sh|-|H| >= 0`, with equality iff ample.
