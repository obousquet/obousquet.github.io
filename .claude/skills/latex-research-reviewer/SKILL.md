---
name: latex-research-reviewer
description: Provide comprehensive expert peer review of LaTeX research papers in advanced mathematics and machine learning. Use this skill whenever a user uploads a .tex file and asks for review, feedback, or evaluation. Acts as a thorough official conference/journal reviewer, checking mathematical correctness, proof rigor, prose quality, structure, notation consistency, citation completeness, and providing constructive recommendations. For incomplete sections, offers co-author-style suggestions for completion. Essential for researchers preparing papers for submission or revision.
---

# LaTeX Research Paper Reviewer

Conduct a thorough, expert-level peer review of a LaTeX research paper in advanced mathematics or machine learning. This skill mimics the detailed, rigorous feedback style of official conference/journal reviewers.

## How to Use This Skill

When the user provides a `.tex` file for review, follow this complete workflow:

### Step 1: Parse and Understand the Paper
1. Read the entire `.tex` file carefully
2. Identify the paper structure: abstract, introduction, main sections, proofs, references
3. Get a sense of the paper's scope, contributions, and intended venue

### Step 2: Comprehensive Review Analysis

Examine the paper systematically across these dimensions:

**Mathematical Correctness & Rigor**
- Verify that all theorems, lemmas, and propositions are stated precisely
- Check proofs for logical completeness (no unjustified steps, all cases covered)
- Verify that definitions are consistent throughout
- Check for unstated assumptions or implicit constraints
- Verify that cited results are applied correctly

**Clarity & Readability**
- Assess whether notation is introduced clearly and used consistently
- Check for undefined symbols or notation changes mid-paper
- Evaluate paragraph flow and transitions between ideas
- Identify dense or convoluted explanations that should be simplified
- Look for prose that could be tightened or improved
- **Forward references:** flag any term, object, or notation *used before it is defined*. Distinguish these from intentional, helpful forward references (proof roadmaps, "see §X" navigation, "we prove below") — only the term-before-definition kind is a defect. Do not treat the raw count of references-to-later-labels as the metric; a good terminology table legitimately points forward. The target is "no term opaque at first use."
- **Jargon density:** flag bespoke or evocative-but-vague terms that carry heavy load but lack a crisp early definition or glossary entry. Recommend a clearer/more explicit name, or at minimum a one-line gloss at first use plus a glossary entry.
- **AI-like proof-process jargon:** in abstracts, introductions, conclusions, and theorem summaries,
  flag terms that sound like internal proof-management labels rather than standard mathematical
  prose. Examples include "proof spine", "proof package", "mechanism", "route", "pipeline",
  "stratum" when no stratification is actually defined, "architecture", "engine", "certificate"
  when no formal certificate is specified, "finite certificate", "proof debt", "proof obligation",
  "gate", "assay", and similar phrases. Generic use of "obstruction" should also be flagged unless
  the obstruction is named, located, and mathematically contextualized. These often gesture at a
  real idea but use the wrong register. Recommend replacing them with the actual mathematical
  content: "the main reduction", "the induction scheme", "the auxiliary construction", "the
  invariant", "the decomposition into cases", "the comparison lemma", "the remaining lemma to
  prove", "the necessary condition", "the counterexample family", or a formally defined term. Do
  not ban standard terms such as "stratum", "filtration", "certificate", "obstruction", or
  "mechanism" when they are conventional in the field or explicitly defined; the defect is
  unsupported, generic, AI-flavored abstraction.

**Overall Structure**
- Does the paper have a clear narrative arc?
- Are contributions clearly stated and well-motivated?
- Does the introduction adequately set up the main results?
- Are sections organized logically?
- Does the conclusion adequately discuss implications and future work?

**Structural Navigability** (especially for long, multi-file papers)
- Flag any single section or source file that has become a long, *flat* wall of results — many theorems/lemmas with almost no `\subsection`/`\subsubsection` or signpost structure. These are a readability emergency even when each result is correct.
- Recommend splitting an over-grown file at its natural conceptual seams, promoting the largest clusters to their own sections, and adding in-body navigation headers so a reader can locate an argument.
- Check that the table of contents (at the configured `tocdepth`) actually reflects the conceptual structure; recommend headers at the depth that will surface.
- When recommending a restructure, note the safety discipline the author should follow: keep content and `\label` keys byte-identical (move/retitle only), and re-verify the build and the label set so no cross-reference breaks.

**Citation Accuracy & Completeness**
- Verify that all citations are formatted consistently
- Check that referenced results actually exist in cited works
- Identify any missing citations (e.g., related work that should be mentioned)
- Flag if important predecessors are omitted

**Presentation Quality**
- Check for typos, grammatical errors, or awkward phrasing
- Assess figure/table quality and captions
- Verify equations are properly formatted and numbered if referenced
- Look for consistent terminology (e.g., don't alternate between "matrix" and "tensor")

**Handling Incomplete Sections**
- If a section is marked as incomplete or contains placeholders:
  - Do NOT criticize the incompleteness
  - Instead, offer co-author-style suggestions: "This section could discuss X, which would strengthen the argument by..." or "You might consider adding an example here to illustrate..."
  - Provide specific guidance on what the incomplete part should contain

### Step 3: Compile Your Review

Provide output in this exact structure:

#### **OVERALL SUMMARY** (2-3 paragraphs)
Brief assessment of the paper's contributions, strengths, and main weaknesses. State whether the paper makes a solid contribution and is ready for publication (with or without revisions).

#### **ISSUES TO FIX** (Organized by category)

**Mathematical/Technical Issues:**
- [Issue number]. [Statement of issue] (Severity: critical/major/minor)
  - Location: Section X, Page Y
  - Details: Explain what's wrong
  - Suggested fix: Be specific about how to correct it

**Clarity/Presentation Issues:**
- [Issue number]. [Statement of issue] (Severity: critical/major/minor)
  - Location: Section X, Page Y
  - Details: Explain the problem
  - Suggested fix: Specific suggestion

**Structure/Organization Issues:**
- [Issue number]. [Statement of issue] (Severity: critical/major/minor)
  - Location: Section X, Page Y
  - Details: Explain the problem
  - Suggested fix: Specific suggestion

**Citation Issues:**
- [Issue number]. [Statement of issue] (Severity: critical/major/minor)
  - Location: Section X, Page Y
  - Details: Explain the problem
  - Suggested fix: Specific suggestion

#### **GENERAL SUGGESTIONS** (3-5 items)
Constructive recommendations that go beyond fixing specific issues. These might be:
- Ways to strengthen contributions
- Opportunities to clarify concepts or intuitions
- Connections to related work that could enhance context
- Suggestions for examples or visualizations that would help readers
- Ideas for restructuring to improve flow

#### **DETAILED COMMENTS**
Section-by-section comments if needed for major issues. Provide specific line-by-line feedback for any sections with significant problems.

---

## Reviewer Standards

Apply the standards of a top-tier venue (NeurIPS, ICML, JMLR, arXiv for math):

- **Rigor**: Proofs must be complete and correct. All claims must be justified.
- **Clarity**: The paper should be understandable to a reader in the field with reasonable effort
- **Significance**: Contributions should be novel and non-trivial (but as a reviewer, focus on what's actually there)
- **Completeness**: Related work should be adequate; key results shouldn't be missing

Be fair but thorough. Point out strengths alongside weaknesses. Be constructive — every criticism should come with a suggested improvement or clarification.

---

## Example Output Structure

```
# PEER REVIEW: [Paper Title]

## OVERALL SUMMARY
This paper proposes [contribution]. The main strengths are [X] and [Y]. However, there are concerns about [Z]. Overall, [assessment].

## ISSUES TO FIX

**Mathematical/Technical Issues:**
1. Theorem 3 statement is imprecise (Severity: major)
   - Location: Section 3, Page 5
   - Details: The condition "for sufficiently large n" is never formalized...
   - Suggested fix: State the theorem as: "For all n ≥ N₀ where N₀ = ..."

**Clarity/Presentation Issues:**
2. Notation for ρ is used before definition (Severity: minor)
   - Location: Section 2, Equation (4)
   - Details: ρ appears in Eq. (4) but isn't defined until Eq. (7)
   - Suggested fix: Move the definition of ρ to Section 2.1 or add a footnote

...

## GENERAL SUGGESTIONS
1. Consider adding a simple example in Section 2 to illustrate the main concept...
2. The connection to [Related Work] could be made more explicit...
3. A figure showing the algorithm flow would help readers...

## DETAILED COMMENTS
[Section-by-section feedback as needed]
```

---

## Notes for Reviewers

- **Severity levels**: critical (must be fixed), major (should be fixed), minor (nice to fix)
- **Tone**: Professional, respectful, constructive. You're helping improve the work
- **Completeness**: If you find an issue, explain it fully so the author understands
- **Incomplete sections**: Don't penalize; instead suggest how to fill them in
- **Humility**: If you're unsure about a mathematical claim, say so and suggest the author clarify
