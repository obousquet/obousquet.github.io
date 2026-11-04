# Campaign Skill Routing

`honest-conjecture-resolution` selects and integrates the work. This map owns the
cross-skill routing; specialist files own their detailed procedures. Use it when
selecting work, not as a checklist to run in full every round.

## Establish The Task And Context

For a mathematical campaign, recover the user's objectives, current source files,
prior results and corrections, resource scope, and selected research mode. Use
`research-knowledge` at start/resume and before substantial new work. It owns
bounded retrieval, campaign/sibling searches, result cards, and freshness checks.
Follow its fallback when the index is unavailable rather than repeatedly retrying.

For literature, `shared-literature` owns local reuse, identity, reservations,
canonical packets, and indexes. `literature-reviewer` owns mathematical source
discovery and relevance assessment, after the local check. A result in a packet
still requires inspection of its source hypotheses before application.

## Choose Mathematical Work

| Need or objective | Specialist | What returns to the campaign |
|-------------------|------------|------------------------------|
| Prove a selected precise claim | `proof-developer` | Argument, exact assumptions, checked implications, or remaining gap |
| Test a conjecture, find a witness, or complete a finite reduction | `conjecture-explorer` | Reproducible evidence, coverage, resource use, and exact scope |
| Import an existing technique from another area | `alon-method` | Dictionary, theorem hypotheses, missing transfer, and native consequence |
| Develop the objects' surrounding theory in depth | `grothendieck-rising-sea` | Foundations, constructions, examples, structural results, and evolving questions |
| Invent operations generating families of arguments | `proof-calculus` | Operations, composition laws, concrete models, and validity theorem or open obligations |
| Construct a new setting or substantial two-way correspondence | `mathematical-framework-design` | Construction, retained/lost information, comparison laws, and transfer status |
| Understand an opaque existing argument | `proof-exegesis` | Elementary mechanism, reusable methods, and justified or conjectural generalizations |
| Choose or audit a moment/tail inequality | `concentration-inequalities` | Exact assumptions, parameter losses, appropriate adversaries, and applicable bound |
| Formalize a statement or check a formal proof | `lean4-formalization` | Inspectable statement, proof/checking result, axioms, and remaining formal gaps |

Use the smallest useful combination. A calculus may use `proof-developer` for a
composition theorem and `conjecture-explorer` for adversaries; a rising-sea
programme may include framework design and method imports. This is shared work
on one objective, not a reason to start parallel campaigns or repeat retrieval.
A known theorem import need not become framework design, and a new invariant
does not automatically require a calculus.

The driver records the chosen mode and the reason for changing it. Within the
user's research scope, specialists can uncover valuable theory objectives without
requesting permission at each transition. They should return those opportunities
explicitly rather than silently presenting them as advances on the old target.
An unknown return to the conjecture is compatible with a worthwhile theory.

## Write, Review, And Publish At The Appropriate Milestone

| Task | Specialist and boundary |
|------|-------------------------|
| Turn ledgers and exploratory notes into a coherent mathematical paper | `ledger-to-journal-writeup`; audit proof dependencies while replacing chronology |
| Design exposition or write substantial new sections | `expository-research-writing`; owns narrative, motivation, examples, and progressive detail |
| Complete or improve an existing draft | `latex-paper-completer`; targeted self-containedness, intuition, and structure |
| Extract understanding before rewriting an opaque proof | `proof-exegesis`; conceptual analysis, then the relevant writing skill |
| Comprehensive mathematical manuscript review | `latex-research-reviewer`; correctness, scope, sources, structure, and presentation |
| Focused terminology review | `latex-jargon-auditor`; also a component of comprehensive review, reused rather than duplicated |
| Submission readiness for AI artifacts, attribution, and disclosure | `ai-slop-preflight`; distinct from mathematical correctness review |
| Package and validate an arXiv submission | `arxiv-prep`; source bundle, clean compilation, metadata, and submission checks |
| Maintain a campaign's displayed state | `conjecture-dashboard`; renders and links evidence, does not decide mathematical status |

Writing can expose a gap and return work to proof development. Formal checking
can detect a statement mismatch and return work to the mathematical formulation.
Do not require every writing, review, or publication skill after every lemma.
Reuse a recent audit for unchanged material; refresh the checks affected by an
actual change. Packaging or publication needs its own task authorization.

## Integrate Once

Give each specialist the question, exact inputs and allowed assumptions, source
links, expected output, and resource scope. Inherit already settled scope rather
than restarting discovery or asking the same questions. Returning to the driver
means updating the existing campaign state, not recursively invoking another
copy of the whole workflow.

Check the returned statements and their dependencies. Record separately their
mathematical status, contribution to the selected objective, and relationship to
the initiating conjecture. A discovered gap can be a useful outcome; a completed
assignment is not necessarily a proved result. Select the next work or conduct
the mode-appropriate review. Keep manuscript/proof owners authoritative, update
shared knowledge when substantive findings change, and refresh dashboards only
when their displayed claims change. No second result ledger is needed.

## Entry Points Outside A Mathematical Campaign

- A standalone proof, search, explanation, edit, or review can invoke its
  specialist directly. Do not create campaign machinery solely to route it.
- `biomed-research` remains the domain driver for biomedical evidence. It routes
  to `biomed-literature-reviewer`, `biomed-study-appraiser`,
  `biomed-evidence-synthesizer`, and `clinical-translational-checker` as needed,
  using the same shared literature infrastructure. Mathematical proof status is
  not a substitute for clinical evidence grading.
- `self-improve` owns a requested session retrospective and reusable process
  lessons. It does not replace routine campaign review or authorize deployment
  of its recommendations. Bring supported generic improvements to the tools
  workspace; keep project findings in their source repositories.
