---
name: expository-research-writing
description: >-
  Write or revise mathematical research papers in Olivier Bousquet's expository
  style: self-contained for motivated non-experts, rich in background and
  intuition, progressive disclosure from overview to full proofs, visual aids
  (diagrams/tables), worked examples, and candid scope/limitations.
---

# Expository Research Writing

Write mathematical papers that teach the domain while proving new results,
targeting a mathematically literate reader outside the immediate subfield.

## Core Principles

- **Self-contained setup:** define central objects, notation, and domain
  background cleanly before using them.
- **Standard mathematical prose:** keep intuition rigorous and subordinate to
  formal statements; avoid internal campaign nicknames and vague process jargon.
- **Progressive disclosure:** give readers three entry points—quick conceptual
  idea (first pass), theorem-and-roadmap architecture (second pass), and full
  technical proofs/appendices (third pass). Move long technical bulk to
  appendices when it interrupts the narrative arc.

## Paper & Theorem Architecture

1. **Motivation and landscape:** state the question, why it matters, and how it
   fits known work (without turning the introduction into a research log).
2. **Background & running examples:** supply minimal standard definitions and
   small worked examples concrete enough to revisit across sections.
3. **Main results & honest comparison:** present theorems cleanly alongside a
   compact comparison table or map stating precisely what prior results prove
   (weaker, stronger, orthogonal, different hypotheses) and avoiding unsourced
   priority or optimality claims (`literature-research` verifies comparisons).
4. **Proof strategy before proof details:** lead long proofs with a short roadmap
   explaining the main reductions, key lemmas, and where the hard step lies;
   state simpler special cases first when they illuminate the mechanism, keep
   intuition tied to lemma statements, and add post-proof remarks noting which
   hypotheses were indispensable.
5. **Examples, diagrams, and tables:** include small finite or low-dimensional
   examples near non-obvious definitions, commutative/dependency diagrams, and
   summary/comparison tables only when they reduce reader load.
6. **Candid limitations:** state which assumptions appear essential vs. open,
   sharpness vs. sufficiency of bounds, method robustness, and concrete open
   directions without defensive disclaimers.

## Revision Checklist

- Can a non-expert state the problem, main results, and proof idea after
  skimming only the intro, theorem statements, and roadmaps?
- Is every central symbol defined before use, backed by at least one worked
  example, and positioned cleanly against cited prior work?
- Are limitations explicit and all informal terms replaced by formal prose?

When this skill conflicts with terse brevity, favor reader orientation and place
routine technical bulk in appendices; use `proof-simplification` when proofs
themselves carry avoidable mathematical machinery.
