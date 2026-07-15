# Computational toolkit

## Reusable helper map

- **`lib_boundary_drop.py`** provides: `all_subsets(n)`, `vc_dim(H,n)`, `shattered_sets(H,n)`,
  `is_extremal(H,n)` (legacy name for ample/extremum), `compute_hd(faces, n_vars)` [n_vars = **2n**, not n!],
  `reduced_homology_dim_simple(faces, dim)`, `yang_complex_faces(H,n)`.
- **`explore_trace_compression.py`** provides reusable helpers actually imported across explorations:
  `trace_class(H,n)`, `face_of(h,n)`, **`yang_dim(H,n)`** (correct hd, any H), `find_best_shelling`,
  `restriction_face`, `teaching_set`.
- **`explore_hvector_compression.py`**: `f_vector(H,n)`, `h_vector(fvec,n)` (the h-vector transform).
- **`explore_shellable_characterization.py`**: `is_CM(H,n)` (Reisner over Q), `yang_faces`.
- Concepts are `frozenset`s of coordinates `1..n` (so `x∈h` means `h(x)=1`). Conditioning/projection
  helpers relabel `[n]∖{x}` to `1..(n-1)`.

## Command and compatibility guardrails

- Default to the repo convention `uv run python <script>` for exploration scripts unless the script header or current `AGENTS.md` says otherwise.
- Write `explore_*.py` for working scripts: quick-and-dirty is acceptable, but the mathematical logic and printed patterns must be clear.
- Keep route findings in the active ledger or a focused `drafts/` report; do not append chronological script notes to overview references.
- For old quick diagnostics that may run under older Python, prefer `bin(x).count("1")` or a local `popcount` helper over `int.bit_count()`.
- Diagnostic output for active proof routes should print compact route-level profiles by default and put long per-record tables behind explicit flags such as `--records` or `--show-*`.
- For group-action diagnostics, precompute orbit or stabilizer maps once per canonical representative instead of recomputing side alignments for every presentation.
