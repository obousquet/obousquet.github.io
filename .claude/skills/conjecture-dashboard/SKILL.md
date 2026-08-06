---
name: conjecture-dashboard
description: Maintain and render a tree-shaped HTML dashboard for a conjecture campaign. Use when a project has multiple live routes, ledgers, side drafts, or verifier scripts and needs an at-a-glance status view with links to the source-of-truth files.
---

# Conjecture Dashboard

Use this skill when a campaign needs a compact visual status tree that can be opened in a browser and
linked from a homepage. The dashboard is not a ledger replacement; it is a navigation surface that
summarizes the current route tree and points to the authoritative artifacts.

## When to use

- You have several live or recently closed routes and want a readable branch-status view.
- You need a browser-friendly page that links each branch to its ledger, draft, or TeX source.
- The active ledger has become hard to scan, but the route structure is still best understood as a
  tree.
- You want a stable HTML summary that can be linked from the repo homepage or site index.

## Dashboard contract

- The dashboard lives as generated HTML rendered from an authored JSON manifest.
- The manifest is the source of truth for the current route tree. It should be updated by the agent
  in the same pass that changes the ledger or TeX files.
- The manifest should describe proof routes, reductions, closed conjectures, counterexamples,
  verification branches, and helper tools. It is a synthetic route tree, not a file tree.
- Node labels and short summaries may contain inline markdown and LaTeX math. Use `$...$`,
  `$$...$$`, `\(...\)`, or `\[...\]` directly in those fields when a title or description needs
  math.
- The renderer may normalize inline `$...$` math to explicit `\(...\)` in the generated HTML so it
  stays inline and typesets consistently.
- If a node points at a local markdown file through a content field, render that file as markdown in
  the dashboard rather than as escaped plaintext.
- If a link target is a local markdown file, the renderer should rewrite it automatically to the
  generated HTML preview page; the manifest should still name the original `.md` file.
- Markdown previews should support ordinary GitHub-style pipe tables, including inline markdown and
  math inside table cells, and should wrap wide tables horizontally on small screens.
- Keep link groups tidy: render 1-3 links directly, but collapse longer link groups into a
  disclosure section so dense nodes do not dominate the dashboard.
- When a markdown file is meant to be read in the dashboard preview, write equations in normal
  LaTeX math delimiters such as `$...$`, `$$...$$`, `\(...\)`, or `\[...\]`. Do not fence
  mathematical content inside code blocks unless the intention is to show the literal source.
- Do not wrap reader-facing mathematical statements in backticks just to make them stand out. A
  span such as `` `NCTD<=VC` `` is rendered as literal code and MathJax will intentionally skip it;
  write `$NCTD \le VC$` or `\(NCTD \le VC\)` instead. Reserve backticks and fenced blocks for
  filenames, shell commands, JSON keys, literal identifiers, and source snippets.
- Current renderers may best-effort coerce obvious relation-style code spans in Markdown previews
  into inline math for legacy files, but do not rely on that compatibility path when writing new
  Markdown.
- The generated HTML should be static, linkable, and readable on mobile.
- The dashboard should show the current structure, not a chronology of every past attempt.

## Recommended manifest shape

- `title`: dashboard title.
- `subtitle`: one-line description of the campaign.
- `version`: optional monotonically increasing integer campaign-state version.
- `updated`: optional date stamp.
- `nodes`: top-level tree nodes.
- Each node may contain:
  - `label`
  - `kind` such as `route`, `reduction`, `conjecture`, `counterexample`, `lemma`, `tool`, or
    `archive`
  - `status`
  - `updated_version`: optional integer recording the dashboard version at which this node was last
    materially touched
  - `summary`
  - `links` as `{label, href}` objects
  - `children` as nested nodes

## Dashboard language discipline

- Dashboard labels and summaries are mathematical communication, not internal scratchpad shorthand.
  Keep them compact, but make every compact phrase precise enough for a reader who has not followed
  the whole chat history.
- Avoid generic proof-process words in labels or summaries unless they are qualified, contextualized,
  or formally defined in the linked ledger/TeX file. Terms that often become unclear include
  "gate", "obstruction", "proof debt", "proof obligation", "assay", "certificate", "finite
  certificate", "boundary", "sector", "mechanism", "proof spine", "proof package", "route",
  "pipeline", and "stratum".
- These words are not banned. Use them when they are standard or precise: for example a topological
  boundary, graph boundary, boundary operator, boundary condition, defined geometric sector,
  parameter sector, named obstruction, or formal certificate. Otherwise replace them with the
  actual mathematical content, such as "remaining lemma to prove", "necessary condition",
  "counterexample family", "main reduction", "induction step", "comparison lemma", "auxiliary
  construction", or "case split".
- Prefer node labels that name the mathematical state directly: `Alexander-dual CM criterion
  proved`, `endpoint-separation lemma stalled`, or `rank-3 counterexample search active` is better
  than `CM gate`, `boundary obstruction`, or `finite certificate route`.

## Status semantics

- Use stable status words such as `active`, `stalled`, `proved`, `refuted`, `draft`, `tool`,
  `verification`, `historical`, or `closed`.
- Keep the status vocabulary small and consistent across the tree.
- If a route changes status, update the manifest and regenerate the HTML in the same pass.

## Rendering workflow

- Maintain the manifest in the repo next to the route artifacts, typically as `dashboard.json`.
- Render it with `scripts/render_conjecture_dashboard.py`.
- For active multi-leaf campaigns, prefer version staleness over wall-clock staleness:
  - bump the top-level `version` whenever a round changes the campaign state;
  - set `updated_version` on each active node materially changed by that round;
  - compare `version - updated_version` to decide which active leaves need attention.
- If the renderer supports it, use an explicit command such as
  `scripts/render_conjecture_dashboard.py --bump-version --touch "Leaf label"` so version bumps and
  node touches are reproducible.  Do not bump the version for a render-only refresh.
- Commit the manifest and the generated HTML together when the dashboard is part of the repo record.
- Do not commit generated Markdown preview pages such as `notes.md.html`; they are reproducible
  side outputs and should be ignored by `.gitignore`.
- Link the generated `dashboard.html` from the repo homepage or site index.

## Maintenance rules

- Keep the tree shallow enough to scan quickly.
- Avoid duplicating the ledger; link to it instead.
- If literature packets materially affect a route, link to `literature/index.html` or directly to
  the relevant `literature/<citation-key>/key-results.md`.
- Put durable status changes in the ledger or TeX file first, then reflect them in the dashboard.
- Use the dashboard to answer three questions quickly: what is alive, what is dead, and where does
  each branch live in the route tree.
