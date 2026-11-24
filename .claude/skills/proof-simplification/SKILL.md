---
name: proof-simplification
description: >-
  Shorten, reorganize, and structurally streamline an already-valid
  mathematical proof while preserving exact theorem strength, rigor, and
  readability. Use when an argument works but feels bloated, indirect,
  over-engineered, branch-heavy, or tangled with constants—distinct from
  constructing a new proof, interpreting an opaque proof, or routine prose
  editing.
---

# Proof Simplification

Treat an existing valid proof as working mathematics ready for structural
refactoring. The goal is minimum machinery and maximum directness without
sacrificing completeness or reader comprehension.

Inside a research campaign, `honest-conjecture-resolution` selects objectives
and retains status authority; return simplified arguments, failed-shortcut
obstructions, verified dependencies, and any discovered hypothesis changes to
that driver. A standalone manuscript or proof needs no campaign machinery.

## Directness, Not Code-Golfing

Refactoring a proof is an iterative mathematical workflow, not cosmetic prose
trimming. Hold every pass to these invariants:

- **Preserve what is proved.** Keep exact theorem statements, quantifiers,
  domains, conventions, and degenerate/boundary cases. If a proposed shortcut
  requires stronger hypotheses or yields a weaker bound, surface it explicitly
  as a changed claim rather than silently substituting it.
- **Never trade rigor for line count.** Do not shorten by compressing genuine
  steps into "clearly," "by a routine check," or "similarly," or by dropping
  orienting transitions that keep the proof readable.
- **Measure total verification load.** A shorter derivation that hides its
  complexity in an unchecked citation, an opaque definition, or an intricate
  reindexing is not simpler than an explicit elementary argument.

## Staged Pass Workflow

Run focused passes rather than rewriting structure, constants, citations, and
prose simultaneously. Apply only the passes that meaningfully reduce complexity
in the current proof.

### 1. Baseline & Load-Bearing Audit

Before altering the argument, map its dependency graph: definitions, auxiliary
maps or spaces, helper lemmas, case splits, proof steps, and outputs.

Systematically test deleting, merging, or bypassing each heavy ingredient.
Maintain a compact **failed-shortcut / obstruction table** as a working note:
whenever a candidate shortcut fails, record what was dropped and the minimal
obstruction or counterexample showing what job that ingredient performs. This
exposes historical residue while preventing repeated attempts at impossible
shortcuts.

### 2. Structural & Operator-Level Refactoring

Load [the move catalogue](references/simplification-moves.md) and test whether
the core mechanism admits a more direct formulation:

- **Collapse multi-stage constructions** into one construction defined directly
  over the target space so admissibility holds automatically.
- **Eliminate case splits and threshold switches** by deriving one
  unconditional tradeoff inequality and closing it globally.
- **Compare dual closure mechanisms** (e.g., fixed-budget iteration with
  telescoping, maximal achievable step without loop indices, or static
  penalized potential) and keep the one with the smallest algebraic overhead.
- **Replace exact optima with near-optima** whenever existence of an exact
  maximizer or minimizer forces compactness, continuity, or quotient plumbing.
- **Drop proxy or quotient spaces** when finitely supported objects in the
  ambient space work directly.
- **Refactor toward target-first operators:** express the goal directly as an
  extremal quantity (`min`/`max`/`sup` or a single named functional) and defer
  existential witness extraction as late as possible so quantifiers shrink and
  independent variables visibly drop out.

Verify quantifiers, quantifier order, and boundary cases on the new skeleton
before smoothing prose.

### 3. Targeted Literature & Black-Box Tradeoff

Inspect auxiliary lemmas that serve only one or two internal call sites. Search
`literature-research` for standard
theorems with better-matched hypotheses (for example, average-case instead of
worst-case, or one-sided instead of two-sided) that remove the auxiliary lemma
cleanly.

Before replacing a self-contained argument with a citation, inspect the primary
source verbatim: verify theorem number, exact hypotheses, conventions, and
constants. Reject the substitution whenever hypothesis-translation caveats or
unfamiliar imports cost more than the self-contained lines they replace.

### 4. Structure First, Numbers Last

Separate conceptual architecture from numerical bookkeeping:

- Keep parameters symbolic through the conceptual steps, recording only the
  minimal side conditions each inequality actually needs.
- Collapse loosely coupled scaling constants or penalty weights into a single
  natural scale or unified parameter so the true scaling law is visible.
- Defer all explicit numerical choices to one dependency-ordered parameter
  block at the end (base constants -> derived scales -> side-condition checks
  -> final bound) with no forward-referenced numbers.
- Use natural units and coarse elementary inequalities instead of calculus or
  transcendentals to produce clean, hand-checkable constants; replace vague
  "sufficiently large" constants when an explicit constant checks in one line.

### 5. Interface Hygiene & Dependency-Driven Reordering

- **Minimal lemma interfaces:** strip proof-internal helper objects from lemma
  statements when downstream callers only consume the output guarantee.
- **Reorder by real dependency:** if Step `k + 1` does not use an object
  introduced in Step `k`, consider swapping them so all reasoning about each
  mechanism stays contiguous and the generality of independent steps is clear.
- **Merge or split at true mathematical seams:** split to isolate distinct
  toolboxes or genuinely reusable results; merge when splitting forces exporting
  awkward intermediate hypotheses or shared expectation steps.
- **Prune clutter:** consolidate standing conventions, let general rules absorb
  degenerate base cases naturally, and sweep for unused or overloaded symbols.

### 6. Optional Fresh-Eyes Critique & Triage

After major structural passes, run an adversarial fresh-eyes audit to surface
hidden blind spots, lingering detours, or accidental gaps. When subagent spawning
is permitted and worthwhile, an optional fresh read-only critic subagent can
execute this audit; invoking this skill does not by itself authorize spawning
agents.

Triage every suggestion critically before editing: adopt genuine structural
wins, patch boundary conditions where needed, and reject regressions, weakened
statements, or coined terminology.

### 7. Synchronization, Verification & Stopping Rule

After the proof stabilizes, synchronize every affected surface of the manuscript:
abstract, overview/roadmap, theorem and lemma statements, comparison remarks, and
`\label`/`\ref` keys. Re-verify all boundary cases, parameter side conditions,
and primary-source citations against the final text. Rebuild LaTeX with SyncTeX
enabled (for example `latexmk -pdf -synctex=1 main.tex`) and check logs and
rendered pages for undefined references, overfull boxes, or awkward page breaks.

Stop once every remaining heavy ingredient corresponds to a recorded
obstruction, each step has a single clear job, and further edits would be
cosmetic churn or degrade readability.
