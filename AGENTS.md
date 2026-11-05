# Research workspace

## Shared Literature

Before any web search for prior work, search the common extracted literature
with `python3 scripts/research_library.py search 'terms'`. It searches titles,
identifiers, succinct result extractions, merged summaries, and project notes;
add `--sources` for full extracted text, or `--limit 0` for every hit.
Local result statements may be more useful than abstracts or web snippets.
Browse for gaps, verification, or updates after checking the local results.

Resolve the shared location from `.research-library.json`; all subjects share
one library. Use the `shared-literature` skill to reuse or reserve a canonical
packet before downloading or extracting. Never start another repo-local cache.
Keep different source versions and project interpretations, and link to common
results. Existing `literature/` and `references/` links are compatibility views.
Commit source packets and refreshed indexes in the library's owning repository;
project symlinks do not stage their target files. Preserve restricted views.

## Existing Results Before New Work
- When the shared knowledge registry is configured, use `research-knowledge`: run
  `python3 scripts/research_knowledge.py sync`, then read a task-specific `context --campaign .
  --task 'current question'` bundle at campaign start/resume. Search before substantial new work;
  inspect original sources and corrections. Register reusable writeups as internal packets and
  run `audit` after meaningful changes. The database is a rebuildable cache, not proof authority.
- Before a substantial proof attempt, computation, or new route, check what is already known in the
  current campaign and related repositories. Recover this context after handoffs or compaction;
  the latest round and dashboard alone are not a complete account of earlier results.
- Search current and archived ledgers, theorem/proof files, result inventories, and relevant
  experiments by mathematical statement, equivalent formulations, and old terminology. Use project
  guides and cross-references to identify related repos; search their authoritative artifacts too.
  Also search the shared literature library, but do not assume it indexes campaign results.
- Inspect matching statements and proofs, including hypotheses, quantifiers, conventions, and later
  corrections. Reuse established results with a source path and theorem/round reference. Reopen a
  failed route only when a changed assumption or new ingredient escapes the recorded failure.
- Before calling a result new or reporting progress, state what it adds to the closest existing
  result. Rediscovery is reuse or verification; a stronger statement, new proof, or new application
  needs its precise difference recorded. An unsuccessful keyword search does not establish novelty.
- Keep a compact, searchable result map in the existing ledger or inventory: statements and aliases,
  status, proof/source links, known failures, and relevant related-repo links. Preserve these links in
  handoffs. Reuse recent checks for unchanged work; search again when the target or evidence changes.

### Choosing And Integrating Work

For a mathematical campaign, use `honest-conjecture-resolution` as the main driver.
It recovers prior work, chooses the research mode and next assignment, routes to
specialists, reviews their evidence, and updates the existing campaign state.
Its [specialist map](.claude/skills/honest-conjecture-resolution/references/skill-routing.md)
is the maintained source for detailed routing; load only the skills needed now.

Literature, conjecture formulation, computation, proof, theory development,
writing, and review can inform one another in any useful order. Computation is
not a prerequisite for proof, and theory-building need not wait for a proof route
to fail. Distinguish direct conjecture progress from independent theory value.
Use the selected theory mode's cumulative review criteria while retaining the
driver's correctness standards and the user's actual scope and resource limits.


When developing higher abstractions, use the driver's
[three-process workflow](.claude/skills/honest-conjecture-resolution/references/abstraction-development.md):
close objects under meaningful constructions, develop operations with models and
validity theorems, and refine representations when they lose required information.
Choose and combine these processes according to the mathematical question; they
are not consecutive gates. Keep cumulative theory development and the initiating
problem's actual status separately visible.

## Skills

Choose the entry point by the task:

| Task | Entry point |
|------|-------------|
| Start, resume, or coordinate a mathematical campaign | [honest-conjecture-resolution](.claude/skills/honest-conjecture-resolution/SKILL.md), then its specialist map |
| A focused proof, computation, search, explanation, edit, or review | The corresponding specialist directly; no campaign machinery required |
| Biomedical evidence research | [biomed-research](.claude/skills/biomed-research/SKILL.md), which routes to domain specialists |
| A requested session retrospective or process review | [self-improve](.claude/skills/self-improve/SKILL.md) |

Specialists inherit the assigned question, sources, assumptions, and scope. They
own execution details and return statements, evidence, limitations, and possible
new questions to the driver. They do not start competing campaign ledgers or
reset resource allowances. Skill selection does not authorize subagent spawning.

`research-knowledge` and `shared-literature` support all relevant research modes:
the former retrieves campaign and sibling results and maintains internal result
records; the latter owns common source packets and source identity. Manuscripts,
proofs, and experiments remain authoritative in their owning campaign. Update
result records after substantive changes and derived views when displayed claims
change. Do not rerun every skill or rebuild every artifact after each lemma.
