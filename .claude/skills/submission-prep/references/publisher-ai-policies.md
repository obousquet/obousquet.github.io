# Publisher and Community AI Policy Notes

Last checked: 2026-07-24.

Policies change quickly. Re-check the target venue immediately before submission.

## arXiv

- Official arXiv pages emphasize careful preparation, scholarly standards, moderation, and author responsibility under the Code of Conduct and submission policies.
- Current enforcement reporting in Nature and TechCrunch says arXiv is imposing a one-year posting ban when a submission contains hallucinated references or other clear signs of unchecked LLM output. Reported examples include fabricated references and comments to/from an LLM. Treat this as a serious current operational risk even if the formal public policy page is less explicit.
- Practical rule: no arXiv upload until every reference and citation claim has been verified against external records and no conversation/meta text remains.

Sources:
- https://info.arxiv.org/help/policies/code_of_conduct.html
- https://info.arxiv.org/help/submit/index.html
- https://www.nature.com/articles/d41586-026-01595-5
- https://techcrunch.com/2026/05/16/research-repository-arxiv-will-ban-authors-for-a-year-if-they-let-ai-do-all-the-work/

## Mathematics Community Consensus

- The Leiden Declaration on Artificial Intelligence and Mathematics, endorsed by the International Mathematical Union, recommends transparent disclosure of automated tools, precise references, formal proofs where appropriate, human responsibility for correctness and citation accuracy, proper attribution, and continued reliance on peer review/community scrutiny.
- The emerging norm for AI-assisted mathematics is not "AI-free prose"; it is accountable, inspectable mathematics: state what tools did, release prompts/intermediate artifacts when feasible, identify verification boundaries, and distinguish unreviewed claims from established theorems.
- Recent GPT-assisted mathematics examples point to the same pattern:
  - The GPT-5.5 Pro sum-product paper reports model snapshot, tools disabled, prompting pipeline, token usage, independent trials, failed trial behavior, code, intermediate outputs, and generated proofs.
  - OpenAI's First Proof report explicitly discusses expert feedback, limited human supervision, selected attempts, model/model-assistant verification, and an initially plausible proof later judged incorrect.
  - OpenAI's Cycle Double Cover artifacts include a statement of AI use and the full prompt, but remain a case where verification status and prior attribution must be handled very carefully.

Sources:
- https://leidendeclaration.ai/
- https://arxiv.org/abs/2607.20525
- https://openai.com/index/first-proof-submissions/
- https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf
- https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf

## Cross-Publisher Scientific Publishing Norms

- AI tools cannot be listed as authors or treated as accountable sources.
- Human authors remain responsible for accuracy, attribution, copyright, plagiarism, data, code, analyses, and conclusions.
- Substantive AI use should be disclosed with enough detail for readers and editors to understand what was done and how it was checked.
- Pure grammar/spelling/copy-editing may be exempt from disclosure at some venues, but this varies; check the venue and disclose uncertain or nontrivial use.
- AI-generated or AI-suggested citations are high risk. A reference can fail by not existing, by having mismatched metadata, or by existing but not supporting the cited claim.

Sources:
- ICMJE: https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html
- WAME: https://wame.org/page3.php?id=106
- Springer Nature: https://www.springer.com/gp/editorial-policies/artificial-intelligence--ai-/25428500
- APS: https://journals.aps.org/authors/appropriate-use-ai-tools
- SSRN/Elsevier: https://www.elsevier.support/ssrn/answer/AI
- CDC: https://www.cdc.gov/ai/resources/considerations-for-generative-ai-use-in-scientific-work.html
- Reporting checklist: https://doi.org/10.1186/s41073-026-00212-3

## Practical Synthesis

Before submission, require:

1. A complete citation verification table.
2. A claim-support audit for all important references.
3. Removal of conversation residue and placeholder text.
4. Prose cleanup of vague AI-style terms unless precisely defined.
5. A disclosure decision with venue-specific wording.
6. A record of verification boundaries for AI-assisted proofs, computations, code, data, and literature review.
7. A final PDF inspection after all edits.
