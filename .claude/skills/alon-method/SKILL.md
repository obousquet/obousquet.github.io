---
name: alon-method
description: >-
  Attack a mathematical problem by importing techniques from adjacent fields
  (probabilistic, polynomial, topological, spectral, geometric, algebraic,
  entropic, coding, or convex/LP methods). Use when a direct native proof stalls
  or an external encoding and theorem transfer can expose hidden structure.
---

# Alon Method

When native reductions stall, import a stronger viewpoint: find a neighboring
theorem or method, encode the problem into its language, and turn the original
difficulty into the gap between true and desired hypotheses. Inside a campaign,
`honest-conjecture-resolution` tracks progress and route limits. Use
`theory-building` instead when the work shifts to inventing operations/calculi,
refining lossy invariants, or building a full two-way correspondence.

## Method-Import Workflow

1. **Frame the target or capability.** Decide whether the import serves an open
   conjecture or develops a general transfer principle. At a plateau, consider
   encoding the whole target rather than a convenient local subclaim.
2. **Try multiple external languages.** Brainstorm distinct encodings before
   committing: probabilistic method (expectation, alteration, LLL, concentration,
   entropy compression), polynomial vanishing/Combinatorial Nullstellensatz,
   linear-algebraic rank/vectors/eigenvalues, topological fixed-point/Borsuk–Ulam
   /Tucker obstructions, spectral expansion, Shannon/Shearer entropy, convexity/LP
   duality/Helly–Radon, or algorithmic analysis. Use
   [examples](references/examples.md) as analogical prompts only.
3. **Write the exact dictionary.** Map objects, constraints, witnesses, and
   extremizers explicitly, recording which data (signs, colors, compatibility,
   normalizations) are preserved vs. forgotten.
4. **Stress the encoding early.** Test whether the encoding still distinguishes
   hard counterexamples and equality cases; if it flattens them away, it is a
   false proxy.
5. **Isolate the missing transfer.** State the exact lemma bridging true inputs
   to the imported theorem's hypotheses. Explain why it is genuinely simpler than
   the original obstacle rather than the same difficulty renamed, and test its
   weakest assumption before proving routine consequences.
6. **Verify primary source & return cleanly.** Check the exact theorem statement
   in its primary source via `literature-research`, translate the conclusion back
   to the native setting, and verify quantifiers, constants, and edge cases.

## Scope Of Failed Imports & Return

- Two objects with identical encoded data and opposite target status rule out
  characterizing the target from that encoding alone; they never refute an entire
  mathematical discipline (for example, all polynomial or spectral methods).
- Distinguish a verified counterexample, a proved limitation, an unproved
  transfer lemma, and a fruitless search. Return the dictionary, checked source,
  native consequence or obstruction, and honest decision for the campaign.
