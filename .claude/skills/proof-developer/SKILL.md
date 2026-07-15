---
name: proof-developer
description: Develop rigorous mathematical proofs from validated conjectures. Use this skill when a conjecture has been tested computationally and the user wants to construct a formal proof. Guides the process from proof strategy selection through step-by-step development to publication-ready LaTeX. Handles strategy identification, lemma decomposition, gap checking, and iterative refinement. Works for proofs in combinatorics, topology, algebra, and related areas of pure mathematics.
---

# Proof Developer: From Conjecture to Rigorous Proof

Systematically develop a complete, rigorous proof of a validated mathematical conjecture. This skill guides the full process: choosing a proof strategy, decomposing into lemmas, developing each step with full justification, checking for gaps, and producing publication-ready LaTeX.

## How to Use This Skill

The user provides a conjecture (ideally with computational evidence) and wants a rigorous proof. Follow the workflow below.

### Step 0: Understand the Statement

1. **Restate the conjecture** in precise mathematical language with all quantifiers, conditions, and definitions explicit.
2. **Identify what we need to show**: What is the logical structure? (implication, equivalence, existence, universality, bound)
3. **Review the evidence**: What computational testing has been done? What patterns were observed? What do the small cases look like?
4. **Check the literature**: Does the user know of related results, partial results, or proof techniques that apply in this area?

---

## Step 1: Identify Proof Strategies

### 1.1 List Candidate Strategies

Consider which approaches fit the statement:

| Strategy | When to consider |
|----------|-----------------|
| Direct proof | The conclusion follows naturally from definitions and known results |
| Induction | The statement is parameterized (by n, by size, by dimension) and has recursive structure |
| Contradiction | The negation leads to a clearly absurd situation |
| Contrapositive | The contrapositive is easier to prove than the original |
| Bijection/counting | We need to show two quantities are equal, or establish a correspondence |
| Construction | We need to exhibit an object with certain properties |
| Case analysis | The hypothesis splits naturally into cases |
| Double counting | A quantity can be computed two ways, yielding the result |
| Pigeonhole/extremal | An extremal argument or counting argument gives the result |
| Topological/algebraic | The structure admits tools from topology, algebra, or homological algebra |

### 1.2 Evaluate and Select

For each candidate strategy:
- **Feasibility**: Can we see how the proof would start and what the key step would be?
- **Hints from computation**: Did the small cases suggest a particular structure (e.g., inductive decomposition, bijection)?
- **Known techniques**: Are there standard proof techniques for this type of result?

Present the 2-3 most promising strategies to the user with a recommended approach and reasoning.

---

## Step 2: Decompose into Lemmas

### 2.1 Identify the Proof Skeleton

Break the proof into a sequence of logically ordered steps:

```
PROOF SKELETON:

Goal: [Main theorem statement]

Step 1 (Setup): [Establish notation, recall definitions]
Step 2 (Key Lemma): [State the main technical lemma]
Step 3 (Lemma Proof): [Prove the key lemma]
Step 4 (Assembly): [Combine to get the main result]

Dependencies: Step 4 uses Steps 2-3. Step 3 uses Step 1.
```

### 2.2 Formulate Lemmas

For each intermediate result:
- State it as a self-contained lemma with precise hypotheses and conclusions.
- Check that the lemmas chain together to give the main result.
- Verify that no circular dependencies exist.
- Consider whether any lemma is independently interesting (worth highlighting).

### 2.3 Check for Missing Pieces

Before proceeding to write proofs:
- Are all the lemmas sufficient to conclude the main result?
- Are there implicit assumptions that need their own justification?
- Are there edge cases or degenerate cases that need separate handling?

---

## Step 3: Develop Each Step

### 3.1 Write Proofs Incrementally

For each lemma/step, develop the proof with full rigor:

1. **State what we prove** at the start.
2. **Justify every step**: cite the definition, lemma, or known result used.
3. **Handle all cases**: if there is case analysis, enumerate all cases and prove each.
4. **Be explicit about quantifiers**: "for all", "there exists" — never ambiguous.
5. **Flag any step that feels non-trivial**: if a step requires more than one line of justification, it may need its own sub-lemma.

### 3.2 Verify Each Step

After writing each proof:
- **Re-read from the reader's perspective**: can someone follow this without filling in gaps?
- **Check logical direction**: are implications going the right way?
- **Test against examples**: does this step hold for the concrete examples from computational testing?
- **Check boundary cases**: does the argument work for the smallest/degenerate cases?

### 3.3 When Stuck

If a step resists proof:
- **Go back to computation**: test the specific sub-claim on small cases. Is it actually true?
- **Try the contrapositive**: sometimes the reverse direction is easier.
- **Strengthen or weaken**: can we prove a slightly stronger/weaker statement that suffices?
- **Look for a different decomposition**: maybe the lemma structure needs adjustment.
- **Report honestly**: tell the user which step is problematic and what we've tried.

---

## Step 4: Assemble and Verify

### 4.1 Write the Complete Proof

Combine all steps into a single, flowing proof. Ensure:
- The logical flow is clear from start to finish.
- Cross-references between lemmas are correct.
- Notation is consistent throughout.
- The proof sketch (if included) accurately reflects the full proof.

### 4.2 Gap Check

Systematically verify:

```
GAP CHECK:

□ Every quantifier is explicit
□ Every step cites its justification
□ All cases are handled (no "similarly" without verification)
□ No circular reasoning
□ Boundary/degenerate cases addressed
□ Definitions used consistently with their statements
□ The conclusion matches the theorem statement exactly
```

### 4.3 Test Against Computational Evidence

- Verify that the proof is consistent with all tested examples.
- Walk through the proof on one concrete small example to check it works.
- If the proof implies something stronger than the conjecture, verify that computationally too.

---

## Step 5: Produce LaTeX

### 5.1 Structure the Output

```latex
\begin{theorem}[Descriptive name]\label{thm:name}
[Precise statement with all hypotheses]
\end{theorem}

\begin{proof}[Proof sketch]
[High-level roadmap: 3-5 sentences covering the main ideas and key steps]
\end{proof}

\begin{lemma}\label{lem:key-lemma}
[Key technical lemma]
\end{lemma}

\begin{proof}
[Complete proof with all steps justified]
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:name}]
[Full proof, referencing lemmas]
\end{proof}
```

### 5.2 Add Supporting Content

- **Examples** illustrating the theorem (before or after the proof).
- **Remarks** connecting to other results in the paper.
- **Corollaries** that follow immediately.
- **Remark on sharpness**: can any assumption be weakened? Is the bound tight?

### 5.3 Match Paper Style

- Use the existing macro and notation conventions from the paper.
- Place the result in the appropriate section.
- Add labels consistent with the paper's labeling scheme.
- Add cross-references to related definitions and results.

---

## Guidelines

### Intellectual Honesty
- If a step cannot be rigorously justified, say so explicitly. Never hide a gap.
- Distinguish between "we believe this is true based on evidence" and "this is proved."
- If the proof only works under additional assumptions, state them clearly.

### Proof Quality Standards
- **No hand-waving**: every "clearly", "obviously", "it follows that" must be backed by a specific justification.
- **No "similarly"**: if two cases are claimed to be similar, either prove both or explain precisely what changes.
- **No implicit assumptions**: if the proof requires a property, it must appear in the hypotheses or be proved.

### When the Proof Fails
- If a gap cannot be closed, this is valuable information.
- Report what was proved (partial result) and what remains open.
- Suggest whether the conjecture should be weakened, the approach changed, or more computational evidence gathered.
- A failed proof attempt that identifies the precise difficulty is more useful than no attempt.

### Iterative Development
- Proofs rarely come out perfect on the first attempt.
- After writing a draft proof, review it critically, then refine.
- The user may spot issues or suggest alternative approaches — incorporate these and iterate.
