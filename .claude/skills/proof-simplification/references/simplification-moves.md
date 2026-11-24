# Simplification Moves & Audit Checks

Reference catalogue for `proof-simplification`. Test moves selectively against
the proof's dependency graph and failed-shortcut table rather than applying them
mechanically.

## 1. Load-Bearing Audit & Failed-Shortcut Table

Track structural probes in a concise working table so failed shortcuts become
reusable knowledge instead of repeated dead ends:

| Candidate shortcut | Ingredient removed | Minimal obstruction or counterexample | Verdict |
|---|---|---|---|
| Example: drop auxiliary step `X` | Map or intermediate domain | Explicit instance showing direct bound fails without `X` | Keep `X` (or alter mechanism) |

Separate **genuine load-bearing ingredients** (those with a concrete failing
example when removed) from **historical residue** (scaffolding surviving from an
earlier proof attempt that no downstream estimate needs). Check transitive use:
an object defined early may only exist to support a lemma that has since been
bypassed or replaced.

## 2. Structural & Mechanism Swaps

- **Collapse two-stage constructions into the target space.** When a proof builds
  an unconstrained witness first and then projects, rounds, or snaps it into an
  admissible set (paying an approximation error), test defining the witness
  directly over the target set or empirical support so admissibility is built in.
- **Eliminate case splits and artificial thresholds.** When an argument splits
  into `defect > τ => progress` and `defect <= τ => done`, try eliminating the
  intermediate defect between two unconditional bounds to obtain a single
  case-free tradeoff inequality (`defect <= C * progress`), then close globally.
- **Compare dual closure mechanisms.** The same core progress lemma can often be
  closed in several ways:
  - *Fixed-budget iteration + telescoping:* concrete, finite-step, no compactness;
    carries loop indices.
  - *Largest achievable step / extremal instance:* drops iteration subscripts;
    may require checking attainment or ε-slack.
  - *Static penalized potential (`objective - θ * cost`):* kills loop structure
    and inverse-function algebra in one variational step; requires choosing the
    coupling weight `θ`.
  Test which closure deletes the most bookkeeping in context.
- **Replace exact optima with ε-near-optima.** If attaining an exact `max`, `min`,
  or fixed point forces compactness, continuity, or quotient arguments, test
  choosing an ε-near-extremizer (`>= sup - ε`) and carrying ε cleanly to the end.
- **Drop quotient or proxy spaces.** If the proof restricts to a finite quotient
  or inherits auxiliary bijections/orderings only to make sums finite, test
  working directly in the ambient space with finitely supported objects.

## 3. Target-First & Operator-Level Compression

- **Start from the target extremal expression.** State the desired minimax or
  supremum quantity first and massage it step by step with triangle, convexity,
  or symmetrization inequalities so every intermediate lemma visibly handles one
  piece of the decomposition.
- **Defer existential witness extraction.** Repeatedly writing "pick `x` realizing
  the expectation" or "choose `y` satisfying the event" fragments the proof with
  quantifiers and named witnesses. Keep `min`, `max`, `sup`, or a single named
  functional inside the algebra so independent variables visibly drop out, and
  convert an expectation bound to an existence claim at the last possible step.
- **Test mechanism factorization.** When hypothesis `A` seems coupled to target
  `C`, check whether `A -> B -> C` factors cleanly through a simpler intermediate
  property `B`. Keep the factorization if `B` decouples two independent arguments;
  skip it if `B` adds translation overhead without simplifying either half.

## 4. Structure First, Numbers Last & Constant Hygiene

- **Keep conceptual steps symbolic.** Write the main steps with symbolic
  parameters and record only the minimal side conditions each inequality uses
  (for example, positive slack, disjointness, or small radius).
- **Unify redundant parameters.** Multiple loosely related scaling parameters or
  thresholds often hide a single dimensionless ratio or one "price" parameter.
  Express derived quantities explicitly as functions of one primary parameter so
  the symbolic bound exposes the exact scaling before any numbers are plugged in.
- **Order the final parameter block strictly by dependency.** Fix base
  constants first, compute derived scales second, check all recorded symbolic
  side conditions third, and evaluate the final bound last—never forward-reference
  a constant defined below.
- **Normalize units and prefer elementary bounds.** Changing base (e.g., base-2
  vs. natural logs) and trading sharp calculus optimization for coarse one-line
  elementary bounds (`log z <= z - 1`, `e > 2`) clears transcendental factors
  and turns ugly decimals into small powers of `2`. Replace "for sufficiently
  large `C`" with an explicit small power or integer whenever checking it takes
  one line.

## 5. Interfaces, Ordering, Citations & Anti-Golfing Checks

- **Trim lemma interfaces.** Keep helper constructions, internal weights, and
  auxiliary maps inside the proof unless callers actually inspect them.
- **Make each mechanism contiguous.** Order independent setup steps and
  calculations by dependency so reasoning about one object stays together and
  parameter-free steps clearly hold before specific parameters are introduced.
- **Merge vs. split discipline.** Merge adjacent lemmas when their proofs share
  the same probabilistic experiment or variational step and splitting forces
  exporting clumsy hypotheses. Split when a lemma bundles two unrelated tools or
  produces an independently clean, reusable statement.
- **Consolidate conventions and base cases.** Replace repeated local caveats with
  one standing assumption; check whether the main formula handles `0` or empty
  cases directly instead of keeping separate degenerate branches. Sweep for dead
  symbols and overloaded notation.
- **Audit black-box citations strictly.** Verify exact theorem numbers, quantifier
  direction, constant factors, and domain conventions in the primary source. Drop
  a citation if explaining the mismatch costs more clarity than proving the
  special case inline.
- **Anti-golfing triage checklist.** Reject any simplification or critique that:
  1. silently strengthens hypotheses or weakens the theorem statement;
  2. hides an unproved edge case inside "clearly" or an unverified citation;
  3. introduces bespoke jargon or opaque shorthand solely to compress lines;
  4. improves constants slightly at the price of brittle case analysis; or
  5. breaks alignment between the proof, theorem summary, overview, and remarks.
