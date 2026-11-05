# Research Skills Architecture

## Responsibility And Entry Points

In the source/template repository, `AGENTS.md` links to `CLAUDE.md`. Consuming
repositories may retain separate files with local guidance; keep their shared
routing consistent.
It selects the entry point and establishes shared correctness, ownership, and
build conventions. It does not duplicate every specialist workflow.

For mathematical campaigns, `honest-conjecture-resolution` is the main driver:
recover context → select objective and mode → assign specialist work → integrate
evidence → review or continue. Its
[routing map](../.claude/skills/honest-conjecture-resolution/references/skill-routing.md)
is the maintained catalogue of specialist responsibilities and expected returns.
Detailed procedures live in the named skills. A return to the driver is an update
to the existing state, not another recursive invocation or a second ledger.

Focused tasks can enter a specialist directly. Biomedical evidence enters
`biomed-research`; a requested session retrospective enters `self-improve`.
Shared knowledge and literature services support both research domains without
conflating mathematical proof with empirical evidence.

## Research Modes And Their Boundaries

Method import adapts an existing technique. Surrounding theory develops a
mathematical world. Proof calculus develops operations, their compositions,
models, and validity theorems. Representation refinement diagnoses lost information
and proves a repair relative to intended observations and operations. Framework design constructs the setting or a
substantial correspondence, with comparison theorems. Proof exegesis interprets
an existing argument and can discover questions for any of these modes.

The driver's [abstraction-development workflow](../.claude/skills/honest-conjecture-resolution/references/abstraction-development.md)
owns the overall process: shared mathematical data, selection among closure,
calculus, and refinement, feedback between them, and consolidation. Specialist
references own the detailed procedures. AGENTS/CLAUDE links to that workflow;
it does not maintain a second version.

These modes can be combined. The driver records which objective is active and
which criteria apply; specialists provide the mathematical work and its status.
In particular, a theory programme is not a short proof-search detour subject to
automatic expiry after a fixed number of unsuccessful attempts. It is assessed
through cumulative foundations, examples, constructions, and understanding.
Actual user budgets and correctness standards remain binding. Independent
contributions can be important even when the initiating conjecture is unchanged.

Writing and review skills have different deliverables: interpreting a proof,
converting a ledger, designing exposition, filling a draft, reviewing correctness,
auditing terminology, checking submission readiness, and building an archive.
The routing map selects the relevant task. None automatically requires running
the entire publication sequence after an ordinary research step.

## Inconsistencies Addressed

- The campaign driver named computation and proof but omitted several theory
  methods. It now routes all mathematical modes and the writing/review lifecycle.
- Some direct-proof review requirements conflicted with sustained theory work.
  Cheapest-test and four-attempt defaults now have direct proof/search scope;
  theory consolidation follows its selected mode's criteria.
- Repository guidance presented a fixed literature–test–proof sequence and an
  incomplete flat list. It now explains entry points and links the maintained map.
- The historical playbook repeated the driver's skill metadata and contained
  superseded mandatory export/deletion rules. It is explicitly a non-operative
  archive; current instructions and focused references govern.
- Literature and draft-completion workflows could restart scope negotiation
  after a campaign assignment. They now inherit settled scope and ask only for
  consequential missing information.

## Manual Routing And Consistency Review

These contrasting cases were used to inspect the instructions. This is a manual
scenario review, not independent agent testing or evidence of improved research
performance.

| Case | Required routing or decision |
|------|------------------------------|
| Objects or phenomena deserve a theory, with no specified conjecture | `grothendieck-rising-sea` develops constructions, invariants, and internal questions without manufacturing a target reduction |
| An operation suggests hidden algebra but no reusable proof corpus exists | `proof-calculus` develops expressions, laws, models, and controls together; a ready master theorem is not required |
| A precise lemma is ready for proof without numerical testing | Driver → `proof-developer`; computation is optional |
| A computation refutes a sufficient surrogate but not the target | `conjecture-explorer` returns the witness's exact scope; driver revises the route, not the conjecture's truth status |
| A known external theorem almost applies | `alon-method` identifies the exact transfer gap; no unnecessary new framework |
| Repeated argument operations suggest a general calculus | `proof-calculus` develops models and composition validity; driver records assumptions and independent theory value |
| Equal summaries give different required exact values | `representation-refinement` refutes exact recovery, chooses operation-motivated extra data, and proves the repaired law |
| Two values differ but a common upper bound is requested | Unequal values alone do not refute the bound; test the stated inequality |
| A supplied finite action system needs a sufficient quotient | `representation-refinement` uses stable partition refinement; the result may retain every state |
| A construction leaves the current object class | Closure-driven rising-sea development or framework design compares enlargements and proves realization; formal syntax alone is insufficient |
| An abstract class simply assumes the desired inequality | Record an interface or conditional result; require proofs of concrete instances |
| Natural foundations develop while the return to the conjecture stays unknown | `grothendieck-rising-sea` consolidation can continue; no forced immediate application or fixed-attempt termination |
| Numerical invariants match across two domains | `mathematical-framework-design` treats the match as a clue; construct and verify the claimed correspondence |
| A formally checked proof has unclear conceptual meaning | `proof-exegesis` inspects the statement and dependencies, then explains mechanisms without inventing generalizations |
| The same failed shortcut returns under a new name | Driver reuses the recorded failure; require a relevant changed assumption or ingredient |
| The user requests an exhaustive finite census | `conjecture-explorer` completes the requested coverage within resources; generic anti-enumeration advice does not replace the task |
| The user asks for a focused terminology edit | `latex-jargon-auditor` directly; no campaign launch or automatic full submission audit |
| A biomedical claim needs evidence assessment | `biomed-research` routes domain appraisal/synthesis; mathematical proof labels do not replace evidence grading |
| A source changes after a result card was curated | `research-knowledge` checks freshness and source evidence; the cache does not revalidate the result automatically |

Structural validation checks skill metadata, local references, discovery links,
and routing coverage. Future observed routing failures should lead to a focused
revision in the responsible owner rather than another parallel checklist.
