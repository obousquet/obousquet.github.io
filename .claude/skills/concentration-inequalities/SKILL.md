---
name: concentration-inequalities
description: Prove moment and tail bounds for sums of dependent random variables, polynomial chaos, and stable/algorithmic functionals. Use this skill when the task involves bounding an L_p norm or tail of a sum R = sum_i g_i (especially with degenerate/mean-zero summands, Walsh-Hoeffding/Rademacher chaos, U-statistics, or uniform-stability error terms), choosing between decoupling / Khintchine / hypercontractivity / Latała / McDiarmid / Stein, or diagnosing why a candidate moment bound is lossy. Encodes a vetted toolbox, the standard reductions, the known accuracy "walls" of each tool, and the diagnostic adversaries that reveal real obstructions.
---

# Concentration Inequalities for Dependent Sums and Chaos

A working toolbox and methodology for proving sharp moment bounds `||R||_p <= (target)` for sums
`R = sum_i g_i` of dependent, typically mean-zero ("degenerate") summands — Rademacher/Walsh chaos,
U-statistics, and uniform-stability error sums. Distilled from a campaign to prove the linear
moment rate `||R||_p <= C(p n beta + M sqrt(p n))` for doubly-degenerate sums.

## When to use

- You must bound `||sum_i g_i||_p` or a tail, and the `g_i` are dependent and/or mean-zero given the rest.
- You are choosing among decoupling, Khintchine, hypercontractivity, Latała partition norms,
  McDiarmid/bounded differences, Stein exchangeable pairs, or cumulants.
- A moment bound you derived is a constant/`sqrt`/`log` factor too large and you need to know whether
  the *tool* is lossy or the *target* is false.

## Core objects and notation

- `R = sum_i g_i`, `g_i = Z_i q_i` with `q_i = q_i(Z_{-i})` mean-zero, `Z in {-1,1}^n` Rademacher.
- **Walsh-Hoeffding decomposition**: `R = sum_D R_D`, `R_D` the degree-`D` part; `R_D = sum_i Z_i q_i^{(D-1)}`.
- **Stability / slice budget** (the structural hypothesis, "(H3)"): flipping one coordinate moves a
  summand by `<= beta`, equivalently the per-coordinate Fourier `ell_1` budget
  `sum_{S ∋ m} |qhat_i(S)| <= beta/2`. This is the analogue of a Lipschitz/bounded-difference
  constant and is almost always the quantity you must convert into an analytic bound.
- **Square function** `f = (sum_i q_i^2)^{1/2}` and per-degree `h_D = (sum_i (q_i^{(D-1)})^2)^{1/2}`,
  with the identity `sum_D h_D^2 = sum_i q_i^2 = f^2`.

## The toolbox — and each tool's WALL

Every tool buys a specific rate at a specific cost. Knowing the *wall* (where the tool stops being
sharp) saves weeks. From sharpest-where-applicable to most general:

| Tool | Gives | Constant | WALL (where it goes lossy) |
|---|---|---|---|
| **Khintchine** (single Rademacher sum) | `||sum eps_i a_i||_p <= sqrt(p) (sum a_i^2)^{1/2}` | universal `sqrt p`, **degree-free** | none — but applies only after you isolate one sign layer |
| **Single-coordinate decoupling** (front sign) | replace on-diagonal sign by independent copy | **absolute** (degree-free) | — |
| **Full tetrahedral decoupling** (all `D` coords, de la Peña–Giné) | decouple a degree-`D` chaos | `C^D` (grows with degree) | exponential in `D`; **do not** invoke if you only need to peel one coordinate |
| **Hypercontractivity** | `||f||_p <= (p-1)^{D/2} ||f||_2` for degree `D` | `(p-1)^{D/2}` | the **degree-blind `p^{D/2}` wall**; useless once `D` is large |
| **McDiarmid / bounded differences** | sub-Gaussian fluctuation of a Lipschitz functional | `sqrt(p) * (sum_m b_m^2)^{1/2}` | **lossy for `ell_2`-norms of chaos / square functions** — per-coordinate sensitivities overcount; use Talagrand convex-Lipschitz / spectral instead |
| **Talagrand convex-Lipschitz** | concentration of a convex 1-Lipschitz function of independent signs | spectral / Gaussian-width | the sharp replacement for McDiarmid on square functions |
| **Latała partition norms** | two-sided `L_p` of *Gaussian* chaos | `C_D` | only Gaussian; reaching it from Rademacher costs `(pi/2)^{D/2}` (next row) |
| **Rademacher ≤ Gaussian** | pass to Gaussian chaos (one-line Jensen) | `(pi/2)^{D/2}` | **lossy when a few coordinates carry a bounded product** (the "star" `Z_i Z_1 Z_2 Z_3`); typically caps the route at degree 3 |
| **Stein exchangeable pairs** (Chatterjee) | `||R||_p <= sqrt(p) ||v||_{p/2}^{1/2}`, `v` a proxy | — | the **proxy multiplies energy at different degrees** → fails for genuinely mixed-degree `R` |
| **Cumulant method** (see dedicated section) | `|kappa_q(R)| <= C^q q! Var (n beta)^{q-2}` (Bernstein) | — | the *assembly* (cross-config cancellation), not the per-diagram bound, is the wall |
| **Elimination-order / tensor-train contraction bound** | `|Val(G)| <= ||a||_HS^2 (max_J ||a||_J)^{q-2}` for a connected complete contraction of order-`D` tensors | absolute | per-*configuration* only; the absolute sum over configurations diverges (next section) |

## Standard reductions (the moves that work)

1. **Grade by degree, then sum (Minkowski over degrees).** `||R||_p <= sum_D ||R_D||_p`. Immune to
   cross-degree coherence (see Obstructions): aligned degrees can only make the true `||R||_p`
   *smaller* than the sum, never larger. Bound each `R_D` by its own energy. **Caveat: this is
   `sqrt(log n)`-lossy for genuinely mixed-degree `R`** — the per-degree energies can sum to
   `sqrt(log n) n beta` while `||R||_2 ~ n beta / sqrt(log n)`. Fine for *bounded* Walsh degree;
   for unbounded mixed degree you must keep the degrees together (cumulant route).
2. **Peel ONE sign layer, not all.** `R_D = sum_i Z_i q_i^{(D-1)}`: decouple the *single* front sign
   (absolute constant) then Khintchine in it → `||R_D||_p <= C_0 sqrt(p) ||h_D||_p`, `C_0`
   degree-free. Resist citing full tetrahedral decoupling — its `C^D` is what makes per-degree sums
   diverge spuriously.
3. **The `Z^2 = 1` collapse.** A square function `sum_i q_i^2 = f^2` turns into the *square of a
   single Lipschitz functional* `f = ||q||_2`, whose bounded difference is the slice budget times
   `sqrt(n)`. Then McDiarmid gives `||f||_p <= C sqrt(p) n beta` directly. This single `f`
   automatically interpolates sub-Gaussian (constant `f`) and sub-exponential (`f ~ |S|`) cases.
4. **Degree-weighted budget.** To bound `sum_d sqrt(E_d)` (energies per degree), use
   `sum_d d E_d = sum_i sum_S |S| qhat_i(S)^2 <= (max|qhat|)(sum|S||qhat|) <= (beta/2)(n beta/2) n`,
   then Cauchy-Schwarz with weights `1/d` gives `sum_d sqrt(E_d) <= (1/2) sqrt(ln n) n beta`. The
   degree weight `|S|` from summing the slice budget over coordinates is the key lever.
5. **Convert (H3) to the operative norm.** The stability budget is a per-row `ell_1` bound; turn it
   into the operator/injective norm actually controlling the chaos (`||A||_inj <= (3/2) sqrt(n) beta`
   for degree 2). Identify *which* tensor norm is binding before optimizing.

## Recurring obstruction: cross-degree coherence

The deepest lesson. When `R` has energy at several Walsh degrees, any method that replaces `R` by a
single **scalar proxy** that *multiplies* contributions from different degrees will overcount:
the proxy manufactures a product that, in `R` itself, appears only as *separate additive terms*.
This killed three routes (variance Cauchy-Schwarz, pointwise domination, Stein proxy). Diagnostics:
- The proxy's value is dominated by a *low* degree in one factor and a *high* degree in the other.
- Energy "adds where `R` cancels" — on a thin set the surrogate is large while `R ≈ 0`.
The escape is reduction move #1 (grade and sum): never form the cross-degree product.

## Separable subcases do not justify low-rank assembly

Many sharp chaos/contraction inequalities are easy on product or rank-one pieces because the target
factorizes into two one-dimensional budgets. This is useful, but it is not an assembly theorem.

- A proof for `a_{I,x}=u_I v_x` says the separable block is harmless; it does not bound
  `a=sum_{r=1}^R u^{(r)}\otimes v^{(r)}` without new control of the mixed profile terms.
- Summing rank-one bounds by triangle inequality typically introduces an `R`, `sqrt R`, or profile
  coherence loss. In trace/cumulant language, the dangerous terms are the cross-profile contractions,
  not the pure rank-one contractions.
- When product, row-uniform, and minimal-core cases all hold, the next diagnostic is the first
  nonseparable mixture: rank two with adversarially aligned profiles, two row classes with different
  label profiles, or the smallest number of cores for which two independent profiles can interact.
- Test any proposed low-rank route on symmetric rank-two mixtures and on skewed profile mixtures
  before treating it as a proof mechanism. If the actual target remains bounded but the assembled
  bound grows with rank/profile count, the defect is the assembly, not the inequality.

## The cumulant route (for mixed-degree `R`, where degree-grading is lossy)

Reduction move #1 (grade and sum) **loses `sqrt(log n)`** on mixed-degree `R` (the per-degree
energies can sum to `sqrt(log n) n beta` while `||R||_2 ~ n beta / sqrt(log n)`). Cumulants are the
escape: `kappa_q(R) = sum_{D_1..D_q} Cum(R_{D_1},...,R_{D_q})` is *multilinear*, not a triangle sum,
so cross-degree cancellation is retained. The linear rate is equivalent to a cumulant bound. What the
campaign established:

- **Target the Bernstein form** `|kappa_q(R)| <= C^q q! Var(R) (n beta)^{q-2}`, NOT the crude
  `(q-1)! (n beta)^q`. The Bernstein form yields the *full* two-term bound
  `||R||_p <= C(sqrt(Var p) + p n beta)` — the sub-Gaussian `sqrt(Var p) = M sqrt(pn)` and the tail
  `p n beta`. The crude form is `~n` too lossy at the variance level and drops the `M sqrt(pn)` term.
- **Connectivity collapse (proved).** Double degeneracy (`E[r_i|Z_i]=E[r_i|Z_{-i}]=0`) forces joint
  cumulants of Hoeffding components to vanish unless their coordinate supports form a *connected*
  hypergraph — this collapses `Bell(q) -> (q-1)!` with no smallness assumption.
- **Per-configuration bound (proved):** each connected cumulant configuration is a complete tensor
  contraction `Val(G)`; the **elimination-order bound** `|Val(G)| <= ||a||_HS^2 (max_J ||a||_J)^{q-2}`
  (proof: accumulator `A_t = A_{t-1} *_shared a` is a matrix product, `||XY||_HS <= ||X||_HS ||Y||_op`)
  controls it. With the slice-budget flattening bound `||a^{(D)}||_J <= C_D n beta` (Schur test) and
  energy bound `||a^{(D)}||_HS^2 = E_D <= (1/2)(n beta)^2`, every configuration obeys
  `|Val| <= C^q (n beta)^q`. This is the higher-degree analogue of `tr(M^q) <= ||M||_op^{q-2}||M||_HS^2`.
- **THE WALL — absolute-value assembly is dead.** `sum_configs |Val|` has the closed form
  `kappa_q(V(g))` for the scalar `V(g)=sum_d (E_d^{1/2}/d!) g^d`, which grows past the target while the
  true `kappa_q` decays (verify on the disjoint-multidegree adversary below). The per-config bound is
  sharp but **cannot be summed in absolute value**: cross-configuration Wick cancellation is essential
  (the "`tr(M^q)` not `tr(|M|^q)`" phenomenon — `tr(|M|^q)` blows up by `n^{q/2}`).
- **The assembly machinery is discrete Malliavin–Stein** (Nourdin–Peccati cumulants-via-`Gamma`-
  operators; **for Rademacher** use Döbler–Krokowski / Krokowski–Thäle — the *Gaussian* relaxation is
  lossy for degree `>= 3`, the star). The discrete product rule `D_k(FG) = F D_kG + G D_kF - 2 Z_k
  D_kF D_kG` produces *diagonal* (index-collision) corrections absent in the Gaussian chain rule;
  **Döbler–Krokowski bound them by the maximal influence** `Inf_k(a)=sum_{S ni k} a_S^2`:
  each collision is charged one factor of `sup_k Inf_k(a) <= E_D <= (1/2)(n beta)^2` (trivially, since
  the influence at one coordinate can't exceed the total energy). So corrections never exceed the main
  term. Keep the *top* contractions signed (operator norm) and bound only the *lower-order* diagonals
  absolutely — that is how you get cancellation where it matters and an affordable `ell_2` estimate
  where it doesn't. (Symmetric Rademacher `p_k=1/2` kills DK's first-order correction term outright.)
- **Status:** `q=2` proved sharp (`kappa_q = 2^{q-1}(q-1)! tr(M^q)`); `q=4` discrete mechanism
  validated; general-`q` carré-du-champ iteration (Ledoux / Azmoodeh–Campese–Poly style) is the
  remaining work.

## Do NOT route the moment bound through the carré-du-champ operator norm

The `Gamma`-tower (`Gamma_{j+1} = G_R Gamma_j`, `G_R h = <DR, -DL^{-1}h>`) tempts you to bound
`kappa_q` via the *operator norm* `||G_R||_op`: `||Gamma_{q-2}||_2 <= ||G_R||_op^{q-2} ||R||_2`. For
**bounded** Walsh degree `D` this is fine — `||G_R||_op <= D·n beta` at the *variance* scale. But the
operator norm at the *slice-budget* scale is **not** dimension-free, and the moment bound must not
factor through it:

- **`||G_R||_op <= C·B` (B = Fourier slice budget `sup_k ||d_k R||_A`) is FALSE.** The matching kernel
  `R = sum_b z_{2b} z_{2b+1}` (degree 2, `B=1`) has `||G_R||_op ~ sqrt(log n)` (exact, to `n=20`).
  Disjoint blocks do **not** decouple: `(-L)^{-1}` couples them through the global degree `|T|`, and
  the top singular vector spreads coherently across degrees `1,3,5,...`.
- **This is a proxy defect, not a moment obstruction.** The same `R` is sub-Gaussian
  (`||R||_p ~ 0.45 M sqrt(pn)`), well within the linear rate. `||G_R||_op` overcounts by `sqrt(log n)`.
- **Consequence for the unbounded-degree route.** Any proof of the unbounded-degree moment bound that
  passes through `||G_R||_op <= C·(budget)` inherits this `sqrt(log n)` defect. The right operator
  scale is the *variance* scale `||G_R||_op <= C·n beta` (`n beta >> B`), uniform in degree — still
  open — but more promising is a route that bounds `||R||_p` *directly*, never forming `||G_R||_op`.
- **The uniform kernel is NOT the worst case.** `||G_sym(n)||_op -> 2` (finite) for the uniform
  degree-2 kernel, provable by a clean Schur test on the `S_n`-symmetric subspace (`a_k, b_k <= 1`);
  but the matching beats it and grows. A bound proved only on the symmetric/uniform orbit says nothing
  about general kernels.

## The RIGHT operator quantities: Krylov restriction, spectral radius, numerical radius (Berger)

The operator-norm warning above has a constructive resolution — three facts that say *which* operator
quantity actually controls the tower, and which are provable.

- **The moments probe `G_R` only on the Krylov subspace `K(R) = span{R, G_R R, ...}`, never on its
  complement.** Because `kappa_q = c_q <R, G_R^{q-2} R>` applies `G_R` only to `R` and its iterates. The
  `sqrt(log n)` defect of `||G_R||_op` lives *off* `K(R)` (for the matching, `K(R) = span{R}` is
  one-dimensional and `G_R R = const`). So bound `G_R` *restricted to `K(R)`*, not globally.
- **Spectral radius `rho(G_R) <= iota` is PROVABLE (a one-line column-sum bound).** In the Walsh-coeff
  basis `(G_R)_{U,T} = a_{U△T} |T\U|/|T|`; the column `ell_1`-sums are `sum_U |(G_R)_{U,T}| =
  (1/|T|) sum_{m in T} sum_{S ni m}|a_S| <= iota`. Hence `||G_R||_{1->1} <= iota` and `rho(G_R) <=
  iota` for *every* doubly-degenerate `R`. So the `sqrt(log n)` in `||G_R||_op` is **pure
  non-normality**; the spectrum stays at the slice-budget scale.
- **The tower is governed by the NUMERICAL RADIUS, not the operator norm.** `<R, G_R^{q-2} R>` is a
  *quadratic form of a power*, so Berger's power inequality `w(A^k) <= w(A)^k` gives `|<R, G_R^{q-2}R>|
  <= w(G_R|_{K(R)})^{q-2} ||R||^2`. Since `rho <= w <= ||.|| <= 2w`, the numerical radius `w` is the
  *sharp* sufficient quantity — it can be `<= C iota` where `||.||_op` already grows. The remaining
  open inequality is exactly `w(G_R|_{K(R)}) <= C iota` ("bounded non-normality on the Krylov
  subspace"), strictly between the proved `rho <= iota` and the false `||.||_op <= iota`.
- **Degree two is then a free reproof of Hanson–Wright.** For `|S| = 2`, `G_R` cannot *raise* degree
  (the entry's `|T cap S|` factor vanishes), so `K(R)` lies in the degree-2 subspace, where `G_R` is the
  *symmetric* matrix `M_{{i,l},{i,j}} = (1/2) a_{{j,l}}`; self-adjoint ⇒ `w = rho <= iota`, with the
  optimal constant, no spectral decomposition.
- **Numerically `w(G_R|_K)/iota` saturates `~1.3–1.4`** (bounded, fit `1.31 - 2.06/n` for the matching
  lift; exact in the invariant subspace) — strong evidence the bound holds; the proof is the crux. If
  `w` should turn out unbounded, fall back to the *signed cumulant tower* directly, which provably
  saturates.

## A bounded-degree shortcut: hypercontractivity + boundedness, and the scale condition

For a residual of *bounded* Walsh degree `D` you can skip cumulants entirely: Bonami–Beckner gives
`||R||_p <= (p-1)^{D/2} sigma`, and boundedness gives `||R||_p <= ||R||_inf`. These meet at the linear
rate `||R||_p <= p iota` **iff the scale condition `||R||_inf^{D-2} sigma^2 <= iota^D`** holds (split at
`p_* = (iota/sigma)^{2/(D-2)}`: hypercontractivity below, boundedness above). It holds for disjoint
products and *polynomial functions of a single linear form* (a clean generalisation of `R = phi(S)` to
arbitrary weights), but **fails** for overlapping products (coordinate collisions `Z_m^2 = 1` inject a
degree-`<=1` part, so the product is not even doubly degenerate) and for *non-smooth* `g(L)` like
`|L|^3` (slowly-decaying Walsh mass ⇒ large effective degree `D` ⇒ `||R||_inf > iota`). Caveat on the
MGF/Gaussian-limit heuristic for products: a product of `k >= 3` standard normals is **sub-Weibull**
`(2/k)` (tail `e^{-c x^{2/k}}`, heavier than sub-exponential) with super-exponentially growing
cumulants; the heuristic `kappa_q ~ (Gaussian)` is valid only for `q << n/k`, and the deep tail must be
capped by boundedness — extrapolating it naively gives a *false* "Bernstein violated" alarm that exact
bounded computation refutes.

## Diagnostic adversaries (test EVERY candidate bound on these)

Pure, symmetric, low-rank families are **all benign** and hide the real obstructions. A bound that
holds on them can still be false. Always include genuinely *mixed* and *opposite-sign* constructions:

- **Parity** `g_i = Z_i prod_{j≠i} Z_j` (pure degree `n`): tests coherent addition; `R = n prod Z_j`.
- **Star** `g_i = (beta/2) Z_i Z_1 Z_2 Z_3` (few coords carry a bounded product): breaks
  Rademacher→Gaussian beyond degree 3.
- **BKZ / functions of `S = sum Z_i`** (rank-1, sub-exponential): the canonical *benign* family —
  exact-evaluable for huge `n`, but misses rank-2 and mixed-degree effects.
- **Rank-2 opposite sign** `A = (beta/4)(uu^T - ww^T)`: energy adds (`a^2+b^2`) while `R` cancels
  (`a^2-b^2`); the canonical *pointwise* counterexample.
- **deg-2 + parity** `g_i = (beta/4)(Z_i S_{-i} + prod_{j≠i} Z_j)`: the canonical *mixed-degree*
  counterexample — this is what killed the Stein route. **If you test only one adversary, test this.**
- **Fluctuating grow-staircase**: coordinate-blocks of growing size carrying growing degrees, each
  block multi-term — the worst case for summing per-degree fluctuations.
- **Disjoint-multidegree (slice-budget saturated)**: each `q_i` places a degree-`d` monomial at
  coefficient `beta/2` on a *fresh* block of `d` coordinates, for `d=1,2,3,...` until coordinates run
  out (`~sqrt(n)` active degrees). This is the adversary that **exposes the absolute-value-assembly
  blow-up** (`sum|Val| = kappa_q(V(g))` grows past target) while the true `kappa_q` decays, and it
  **confirms the Bernstein structure** holds with bounded `Var`. Use it whenever you suspect a route
  sums per-piece bounds without keeping signs.
- **Matching / disjoint blocks** `R = sum_b z_{2b} z_{2b+1}` (or blocks of fixed size `w`): sparse,
  structured, `B=1`, trivially sub-Gaussian. **The adversary that breaks operator-norm routes**:
  `||G_R||_op ~ sqrt(log n)` while `||R||_p` is sub-Gaussian. Use whenever a route bounds `||R||_p`
  via an *operator/Gamma-tower* quantity — it separates the proxy's defect from the moment's truth.
  Random *dense* sampling never finds it; you must hand-build it.

## Evaluation methodology

- **Ratio test.** Compute `||target||_p / ||bound||_p` (or `quantity / (p n beta)`) and watch its
  growth in `n`. Bounded/decreasing ⇒ viable; growth like `sqrt(n)`/`log n` ⇒ the tool or target is
  lossy. Print as a table across `n` and `p`.
- **Exact via symmetry.** If the construction is a function of `S = sum Z_i` only, compute exact
  moments over the binomial law of `S` for `n` up to thousands — far past cube enumeration (`n<=~24`).
  This is how mixed-degree counterexamples become decisive.
- **Monte Carlo for large `n`.** When no symmetry, sample `Z` and estimate `||.||_p`; square functions
  `h_D` are evaluable per sample without the full Walsh transform, so `sum_D ||h_D||_p` is MC-estimable
  to `n ~ 100+`.
- **Fast Walsh–Hadamard transform** to extract `R_D` exactly on the cube (`n <= ~16`).

## Bound vs. truth (critical discipline)

A *bound* being lossy by `sqrt(n)` does **not** mean the *quantity* grows. Always measure the actual
norm, not just the bound. McDiarmid on a square function admits a spurious `sqrt(n)`; the true
fluctuation is benign. When a bound is lossy, ask: is the target false (find an adversary), or is the
*tool* loose (measure the truth, then find the sharper tool)?

## Workflow

1. Identify the structural hypothesis (stability/slice budget) and write it as a Fourier `ell_1`/
   bounded-difference statement.
2. Decide whether to grade by degree (almost always yes for mixed degree).
3. For each degree, peel one sign layer (single-coordinate decoupling + Khintchine) to a square
   function; collapse the square function via `Z^2=1` to a Lipschitz `f`.
4. Pick the concentration tool by the table above; check its wall against your degree/`p` regime.
5. Before claiming, run the ratio test on ALL diagnostic adversaries — especially deg-2+parity and
   rank-2 opposite sign — at the largest `n` your evaluation method allows.
6. If a step is lossy, separate bound-vs-truth before abandoning the route.
