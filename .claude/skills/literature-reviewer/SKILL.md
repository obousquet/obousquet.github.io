---
name: literature-reviewer
description: Conduct comprehensive literature searches for a mathematical research paper. Use this skill when the user wants to find related work, discover connections to existing results, identify missing references, or situate their contributions within the broader mathematical landscape. Searches across arXiv, MathSciNet, Google Scholar, and other sources. Produces structured reports with citations, relevance assessments, and suggestions for how found results connect to the current work.
---

# Literature Reviewer: Comprehensive Mathematical Literature Search

Systematically search for and review mathematical literature related to the current research. Find references, discover connections, and identify results that strengthen the paper's context or yield new consequences.

## How to Use This Skill

The user wants to find related work for their paper or a specific result. Follow the workflow below.

### Step 0: Scope the Search

Determine the search scope by asking (if not specified):

1. **Focus**: Are we searching broadly for the whole paper, or for a specific definition/theorem/technique?
2. **Goals**: What are we looking for?
   - Missing references for the bibliography
   - Prior results that overlap with or imply our results
   - Connections to other areas that could yield new results
   - Standard terminology and notation to align with
   - All of the above
3. **Known references**: What does the user already know about? (to avoid redundant results)

---

## Step 1: Identify Search Terms

### 1.1 Extract Key Concepts

From the paper or the user's description, identify:
- **Core mathematical objects** (e.g., simplicial complexes, Yang-Baxter equation, Betti numbers)
- **Techniques used** (e.g., shellability, discrete Morse theory, spectral sequences)
- **Properties studied** (e.g., acyclicity, Cohen-Macaulay, collapsibility)
- **Equivalent or related formulations** in other areas

### 1.2 Generate Search Queries

For each concept, generate multiple query variants:
- Standard mathematical terminology
- Alternative names for the same concept (different communities may use different terms)
- Broader and narrower terms
- Combinations of key concepts that capture the paper's unique angle

---

## Step 2: Search

### 2.1 Sources

Search across multiple sources:
- **arXiv** (math sections: math.CO, math.AT, math.AC, etc.) — preprints and recent work
- **Google Scholar** — broad coverage, citation counts
- **MathSciNet / zbMATH** — reviewed publications with MSC classification
- **Specific journals** relevant to the area
- **Textbooks and surveys** — for foundational results and standard references

### 2.2 Search Strategy

1. **Direct keyword search**: search for the core terms.
2. **Citation tracking**: from known key papers, check what cites them (forward) and what they cite (backward).
3. **Author search**: identify the main contributors to the area and check their recent work.
4. **Survey/textbook search**: find surveys that cover the area — their bibliographies are goldmines.
5. **Cross-area search**: search for the same structures under different names in adjacent fields.

### 2.3 Record Findings

For each potentially relevant result, record:
- Full citation (authors, title, year, venue/arXiv ID)
- The specific result or concept that is relevant
- How it connects to our work
- Relevance level: essential / important / useful context / tangential

---

## Step 3: Analyze Connections

### 3.1 Classify Found Results

Organize findings into categories:

**Direct predecessors** — Results our work builds on or generalizes.
- How does our work extend or differ from these?
- Are we citing them? Should we?

**Parallel results** — Results that prove similar things with different methods or in different settings.
- Can their techniques be adapted to our setting?
- Do their results imply any of ours (or vice versa)?
- Should we discuss the relationship explicitly?

**Connectable results** — Results in adjacent areas that could combine with ours.
- Can we derive new corollaries by combining their results with ours?
- Do they provide alternative characterizations of our objects?
- Do they suggest new conjectures?

**Contextual references** — Standard references for definitions, techniques, or background.
- Are we using standard terminology consistently with these references?
- Should we cite them for definitions we use?

**Contradictions or overlaps** — Results that conflict with or subsume our claims.
- Does any found result already prove what we claim as new?
- Does any result contradict our conjectures?
- These must be addressed immediately.

### 3.2 Identify Gaps

After reviewing the literature:
- Are there obvious related papers we haven't found?
- Are there areas where the literature is thin (opportunity for our contribution)?
- Are there open problems in found papers that our work addresses?

---

## Step 4: Report

### 4.1 Literature Report Structure

```
# LITERATURE REVIEW: [Topic/Paper Title]
Date: [date]

## Search Summary
- Terms searched: [list]
- Sources checked: [list]
- Papers reviewed: [count]

## Essential References (must cite)
1. [Citation] — [one-line relevance]. Connection: [how it relates to our work]
2. ...

## Important Connections
1. [Citation] — [Result X] connects to our [Theorem Y] because [reason].
   Potential consequence: [what we could derive]
2. ...

## Suggested New Directions
1. [Citation] suggests that [idea]. This could lead to [conjecture/extension].
2. ...

## Terminology and Notation Alignment
- Our "[term A]" is called "[term B]" in [reference] — consider aligning.
- Standard notation for [concept] is [notation] per [reference].

## Potential Issues
- [Citation] may already prove [our result] — verify.
- [Citation] uses a different definition of [term] — clarify relationship.

## Missing Coverage
- No good reference found for [concept] — may need to be self-contained here.
- The area of [X] seems unexplored in connection with our work.
```

### 4.2 Bibliography Entries

For references to add, provide ready-to-use BibTeX entries:

```bibtex
@article{AuthorYear,
  author  = {Last, First and Last, First},
  title   = {Title},
  journal = {Journal},
  year    = {2024},
  volume  = {XX},
  pages   = {YY--ZZ},
  doi     = {10.xxxx/...}
}
```

### 4.3 Actionable Recommendations

Prioritize recommendations by impact:
1. **Cite immediately** — references that should be added to the paper now.
2. **Investigate further** — results that may yield new consequences and need closer reading.
3. **Track** — recent preprints or ongoing work to watch.

---

## Guidelines

### Search Quality
- **Thoroughness over speed**: a missed key reference is worse than a long search.
- **Verify relevance**: read abstracts and key results, don't just match keywords.
- **Check recency**: prioritize recent work but don't ignore foundational older references.
- **Cross-community awareness**: the same result may appear under different names in combinatorics, topology, algebra, or computer science.

### Honesty
- If a found result appears to subsume or contradict our work, report it immediately — do not downplay.
- If the search is inconclusive for a topic, say so rather than claiming nothing exists.
- Distinguish between "no results found" and "this area is unexplored."

### When to Trigger This Skill
- At the start of a project, to understand the landscape.
- After proving a new result, to check novelty and find connections.
- Before submission, for a final bibliography check.
- When entering a new sub-topic or using a new technique.
- When a reviewer or collaborator suggests "have you seen...?"
