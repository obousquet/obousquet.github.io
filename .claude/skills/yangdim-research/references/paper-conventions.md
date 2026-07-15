# Paper and LaTeX conventions

## Notation macros

- Use the project macros `\hd`, `\VC`, `\mfw`, `\NCTD`, `\RTD`, `\OCN`, `\STD`, `\hs`, `\T`, `\H`, `\X`, `\k`, `\bv`, and `\bx`.
- Introduce notation before first use and keep names aligned with `main.tex` and `prescribed_dual_bridge_realization.tex`.
- Avoid adding packages or redefining macros unless the paper needs it.

## References and labels

- Use `\autoref` for references unless the surrounding section already uses a different local convention consistently.
- Label every theorem, lemma, proposition, definition, equation, or target that is referenced later.
- Rename labels when terminology changes, especially `extremal` labels that actually mean `ample` or `extremum`.

## Build hygiene

- For significant `main.tex` or `prescribed_dual_bridge_realization.tex` edits, compile and commit the generated top-level PDF with the source when the standing project rule applies.
- Check for fatal TeX errors and undefined-reference warnings after requested compiles.
- Do not commit transient auxiliary files such as `.paux`.
- Keep generated PDFs at the repository top level when they correspond to top-level TeX entrypoints; build-directory copies are transient unless deliberately tracked.
