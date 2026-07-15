---
name: conjecture-explorer
description: Explore and test mathematical conjectures computationally before attempting proofs. Use this skill when the user formulates a conjecture, hypothesis, or pattern and wants to test it on small cases, search for counterexamples, enumerate structures, or build computational evidence. Guides the cycle of conjecture → code → test → refine until the statement is sharp enough to prove. Essential for the exploratory phase of mathematical research.
---

# Conjecture Explorer: Computational Testing of Mathematical Hypotheses

Systematically test mathematical conjectures through computation. Write Python scripts that check small cases, search for counterexamples, enumerate relevant structures, and surface patterns — building confidence and sharpening statements before proof attempts.

## How to Use This Skill

The user provides a conjecture, hypothesis, or observed pattern. Follow the workflow below.

### Step 0: Understand the Conjecture

1. **Parse the statement**: Restate the conjecture precisely in mathematical notation. Identify all objects, quantifiers, and conditions.
2. **Identify the parameters**: What can be varied? (e.g., dimension n, graph size, group order)
3. **Clarify scope**: Ask the user (if not obvious):
   - What parameter ranges are tractable to test?
   - Are there known special cases or boundary cases to check first?
   - Is there a related conjecture or weaker version to test alongside?

---

## Step 1: Design the Computational Test

### 1.1 Choose the Testing Strategy

Select one or more approaches based on the conjecture type:

| Conjecture type | Strategy |
|----------------|----------|
| Universal ("for all X, P(X) holds") | Enumerate all X up to feasible size, check P(X). Any failure is a counterexample. |
| Existential ("there exists X such that P(X)") | Search for a witness. Try structured search before random. |
| Asymptotic ("P(n) grows like f(n)") | Compute P(n) for increasing n, fit against candidate functions, plot. |
| Equality/inequality ("A(X) ≤ B(X)") | Compute both sides for all feasible X, report the gap distribution. |
| Pattern ("the sequence satisfies recurrence R") | Compute terms, check the recurrence, look up in OEIS if applicable. |
| Structural ("objects of type A biject with type B") | Enumerate both sides, compare counts, attempt explicit matching. |

### 1.2 Plan the Enumeration

- Identify the mathematical objects to enumerate (e.g., graphs, simplicial complexes, partitions, permutations).
- Determine the feasible range: what sizes can be exhaustively checked?
- Decide on representation: how to encode the objects in Python.
- Plan the output: what to print to make patterns visible.

---

## Step 2: Write the Exploration Script

### 2.1 Script Structure

Follow this template:

```python
"""
Conjecture: [precise statement]
Test: [what this script checks]
"""

# 1. Generate/enumerate the objects
# 2. For each object, compute the relevant quantities
# 3. Check the conjecture condition
# 4. Report results: confirmations, counterexamples, patterns

# Print a summary table at the end
# If counterexample found, print it with full detail
```

### 2.2 Coding Priorities

- **Correctness over speed** — a wrong test is worse than a slow one.
- **Clarity of mathematical logic** — the code should read like the math. Name variables after the mathematical objects they represent.
- **Verbose output** — print intermediate results so patterns are visible. Use tables, sorted output, and summaries.
- **Counterexample detail** — when a counterexample is found, print everything about it: the object, the quantities computed, why it fails.
- **Progressive parameter sizes** — start with the smallest non-trivial case and increase.

### 2.3 Output Format

Structure the output to make patterns jump out:

```
=== Testing conjecture: [short name] ===

n=2: [result] ✓
n=3: [result] ✓
n=4: [result] ✓
n=5: COUNTEREXAMPLE FOUND
  Object: [description]
  LHS = [value], RHS = [value]
  Details: [why it fails]

Summary: Conjecture holds for n ≤ 4, fails at n=5.
```

Or for pattern discovery:

```
=== Sequence values ===
n=1: 1
n=2: 3
n=3: 7
n=4: 15
n=5: 31

Pattern: 2^n - 1 (confirmed up to n=10)
```

---

## Step 3: Run and Analyze

### 3.1 Execute the Script

- Run with `uv run python explore_<topic>.py`
- Start with small parameters to validate the code itself.
- Increase parameter size gradually.
- Be a good EC2 citizen: do not saturate CPU or memory with unconstrained searches. Start with small
  limits, estimate memory growth before scaling, and avoid launching several heavy jobs at once.
- For heavy or long-running computations, prefer a lower-priority invocation such as
  `nice -n 10 uv run python explore_<topic>.py ...`. If the script supports worker counts, set a
  conservative value instead of using every core. Use timeouts or explicit max-parameter limits for
  exploratory runs.
- If a job starts swapping, consuming all cores for a long time, or threatening the shared web/server
  workload, stop it and restart with smaller parameters, chunking, checkpointing, or a sampled search.

### 3.2 Interpret Results

**If the conjecture holds for all tested cases:**
- Report the range tested and any patterns in the data.
- Identify the hardest cases (closest to failure, largest gap, etc.).
- Suggest whether the tested range is convincing or if larger tests are needed.
- Note any patterns that might hint at a proof strategy.

**If a counterexample is found:**
- Analyze the counterexample: what makes it special? Is it minimal?
- Search for the minimal counterexample.
- Suggest how to refine the conjecture: can we add a condition that excludes the counterexample while preserving the interesting cases?
- Test the refined conjecture.

**If the data suggests a different pattern:**
- Propose the alternative conjecture.
- Test the new conjecture with the same rigor.

### 3.3 Iterate

The conjecture-test-refine loop may run several rounds:

```
Conjecture v1 → test → counterexample found
Conjecture v2 (refined) → test → holds for n ≤ 8
Conjecture v2 → larger test → holds for n ≤ 12
→ Ready for proof attempt
```

Report clearly which version of the conjecture is the current best.

---

## Step 4: Prepare for Proof

Once the conjecture is computationally validated:

1. **State the final conjecture** precisely, incorporating all refinements.
2. **Summarize the evidence**: range tested, number of cases checked, notable patterns.
3. **Identify proof hints** from the computation:
   - Did the proof of small cases suggest an inductive structure?
   - Did the enumeration reveal a bijection or structural decomposition?
   - Are there invariants that the computation surfaced?
4. **Flag edge cases** the proof must handle.
5. **Save the script** as `explore_<descriptive_name>.py` for future reference.

---

## Guidelines

### Script Naming
- Use `explore_<topic>.py` for exploration scripts.
- These are working tools, not production code — but they must be correct.

### When to Stop Testing
- The conjecture has been tested over a range large enough that patterns are clear.
- Or a counterexample has been found and the conjecture refined.
- Or computational limits are reached and the evidence is as strong as feasible.

### Common Pitfalls
- Testing only "nice" cases (e.g., only prime dimensions, only connected graphs).
- Not checking boundary cases (n=0, n=1, empty set, trivial group).
- Assuming the conjecture is true because the first few cases work — always push to larger cases.
- Not printing enough detail to understand why a counterexample fails.
