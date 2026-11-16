# Readable Campaign Reports

Use this guidance for round summaries, dashboard overviews, and current-state openings. The reader
knows mathematics but may know neither this campaign's terminology nor its recent history. The
report should let them understand the question, assess the achievement, and see the remaining
difficulty without opening other files. Full proofs and historical detail belong in linked sources.

## Explain The Mathematics Before Naming It

Start with the objects and the question, then the current answer or uncertainty. State the few
definitions and hypotheses that make the claim intelligible. Keep necessary mathematical language:
"jargon-free" means no unexplained private vocabulary, not imprecise or notation-free mathematics.
Introduce notation after its meaning, and use a small example when it makes an unfamiliar idea
concrete. A specialist term's expansion alone may not explain the concept.

A result's name, status badge, round number, or file path cannot replace its statement. Prefer
"We proved that the construction works when the two choices agree on their shared vertices" to
"The compatibility gate is green". Then say whether such agreeing choices are known to exist.
Definitions, reductions, computations, proofs, and independent reviews have different evidential
roles; use the verb appropriate to the actual work.

## Describe Both The Change And Its Limits

A useful short report answers these questions in connected prose or a compact list:

- What problem are we trying to settle, and for which objects or assumptions?
- What did we know before this round, and what exactly is now added or corrected?
- What supports the claim, and how does it affect the original question or an independent theory?
- What is still missing, and what would the proposed next step clarify?

Do not measure progress by new names, files, case counts, or completed tasks. Say when a round
only verified earlier work, found no decisive evidence, corrected an error, or ruled out a method
without resolving the original question. For finite tests, state the tested class and range and
whether coverage was exhaustive or sampled. For a reduction, explain what still has to be proved.
For an independent theory result, state its demonstrated value and whether its connection to the
original question is proved, conjectured, or unknown. Do not invent percentages or imply that a
short remaining statement must be easy.

## Link To The Public Dashboard

Include a descriptive Markdown link such as "Campaign dashboard" to the campaign's full public
HTTPS dashboard URL in each round's chat summary. Use the shared research site's configured domain
and the campaign's published path, resolved from its inventory, existing site links, or deployment
guidance. Link directly to the dashboard, rather than only the site's homepage or a local HTML file.
Keep deployment addresses in the owning workspace rather than hard-coding them into reusable skills.

Reuse a known published URL; do not infer its path from a repository name. If the dashboard has
unpublished changes, distinguish the live page from the local update. If no public URL is configured
or the dashboard is known to be unavailable, say so briefly and offer the local dashboard link when
available. Do not invent a link or deploy a site merely to satisfy this reporting convention.

## Illustrative Rewrite

This is a hypothetical report, not a campaign result.

Opaque: "R18 closes the forest gate; the C3 witness kills the extension package. General assembly
remains red. Next: repair the boundary interface."

Readable: "We are asking which finite graphs can be colored with two colors so that adjacent
vertices have different colors. Previously we had a construction for paths. This round we proved
that it works for every graph with no cycles: in each connected component, choose a starting vertex
and color each vertex according to whether its distance from that vertex is even or odd. This is a
proof for that class, not yet a classification of all graphs that admit such a coloring.

"We also checked why the claim cannot extend to every graph: a triangle needs three colors because
each of its vertices is adjacent to both others. This refutes the unrestricted extension, not the
classification problem. The remaining question is exactly which graphs containing cycles still
admit two colors. Next we will investigate whether the decisive condition is the absence of a cycle
of odd length; that characterization has not been proved in this hypothetical round."

In a real report, attach links to the proof and counterexample records after stating their content.
This illustrates reporting structure, not a novelty claim about elementary graph theory.

## Prevent Terminology From Drifting

At each round's close, read the proposed summary without earlier messages or source files. Can the
reader say what the objects are, what changed, and what is still unknown? Replace an unexplained
label with its meaning; add the missing condition; remove an unsupported implication of progress.
This is a short editorial check on the report, not a new research audit or separate review artifact.

When updating the dashboard, do the same for its overview and affected nodes. Rewrite current-state
prose rather than stacking updates. A node may rely on definitions in its overview or parent, but
should not require a tour of other branches. Keep a small glossary in an existing guide if the
campaign genuinely needs recurring specialized concepts; still explain the essentials in the report.
Preserve old names as searchable aliases in source records when renaming them for clarity.

Keep summaries short through selection, not unexplained compression. Lead with the most consequential
change and current limitation; group routine checks and link the details. A report does not need to
reproduce the full ledger, and an unchanged dashboard need not be regenerated merely because another
round ended. Every round still needs an intelligible account of its outcome, including no advance.
