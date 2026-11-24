# Campaign Skill Routing

`honest-conjecture-resolution` selects and integrates the work. This map owns
cross-skill routing; specialist files own detailed procedures. Consult it when
selecting work, not as a checklist to run in full every round.

## Context & Literature

- `research-knowledge`: run `sync`, bounded `context`, and `search` across
  campaign and sibling repos at start/resume and before substantial new work.
  When unavailable or outside sandbox, fall back to `grep -rn` and record limits.
- `literature-research`: search the local shared library first, verify primary
  sources verbatim, reserve/maintain canonical packets, and update indexes.

## Choose Mathematical Work

| Need or objective | Specialist | Returns to campaign state |
|---|---|---|
| Prove a selected precise claim | `proof-developer` | Argument, exact assumptions, checked implications, or gap |
| Test a conjecture, find a witness, or run a finite search | `conjecture-explorer` | Reproducible evidence, coverage, compute scope, script link |
| Import an existing technique from another area | `alon-method` | Dictionary, hypotheses, missing transfer, native consequence |
| Build closures/theory, generative calculi, refined representations, or correspondences | `theory-building` | Objects, operations/models, repaired invariants, comparison laws, open obligations |
| Understand an opaque existing argument | `proof-exegesis` | Elementary mechanism, reusable methods, candidate extensions |
| Shorten or structurally streamline a valid proof | `proof-simplification` | Direct proof, failed-shortcut table, verified citations, synced prose |
| Choose or audit a moment/tail inequality | `concentration-inequalities` | Exact hypotheses, parameter losses, appropriate adversaries |
| Formalize a statement or check a formal proof | `lean4-formalization` | Inspectable Lean statement, check status, axioms, formal gaps |

Follow the **Thinker -> Builder** hand-off (`swarm-coordination.md`) before
spending heavy `lean4-formalization` compute: survive paper checks and
non-author faithfulness review first. Combine specialists only as needed on one
shared objective without spawning parallel ledgers.

## Write, Review, And Publish

| Task | Specialist and boundary |
|---|---|
| Turn ledgers/notes into a clean, self-contained mathematical paper | `ledger-to-journal-writeup`; audit proof contracts, collapse one-use lemmas, prune superseded modules |
| Design exposition, motivation, examples, and progressive detail | `expository-research-writing`; narrative, worked examples, roadmaps, limitations |
| Shorten or refactor an already-correct proof without losing rigor | `proof-simplification`; structural reduction, symbolic-then-numeric separation, interface cleanup |
| Extract understanding before rewriting an opaque proof | `proof-exegesis`; conceptual mechanism first, then writing/simplification skill |
| Peer review, jargon/terminology audit, or Skim PDF review queue | `latex-research-reviewer`; rigor, conventions, structural navigability, terminology audit, SyncTeX visual check |
| Scholarly preflight (citations, AI residue, disclosure) and arXiv bundling | `submission-prep`; verification tables, minimal allowlisted bundle, clean-room compile |
| Render and maintain a campaign's status dashboard | `conjecture-dashboard`; renders tree/board/DAG/graveyard views, never decides status |

Reuse recent audits for unchanged sections; rerun only checks affected by actual
changes. Packaging and public release require explicit user authorization.

## Outside A Mathematical Campaign

- Focused standalone tasks (single proof, experiment, literature check, review,
  simplification, or submission bundle) invoke the specialist directly.
- `biomed-research` drives biomedical evidence via `biomed-literature-reviewer`,
  `biomed-study-appraiser`, `biomed-evidence-synthesizer`, and
  `clinical-translational-checker`, using `literature-research` for packets.
- `self-improve` owns requested session retrospectives and tool/process lessons.
