# Lean Project Workflow

## Worker Setup

Configure `LEAN_REMOTE_HOST`, `LEAN_REMOTE_ROOT`, and (for direct commands)
`LEAN_REMOTE_WORKDIR` in the project's environment. Set `LEAN_REMOTE_KEY` if a
specific SSH identity is needed. Install Lean through `elan` on that worker.

Use:

```bash
lake +leanprover-community/mathlib4:lean-toolchain new <ProjectName> math
lake exe cache get
lake build
```

The `math` template pins Lean through `lean-toolchain` and configures Mathlib. After creating or
updating dependencies, run `lake exe cache get` before building so Mathlib `.olean` files are fetched
from the cache when available.

The worker does not need GitHub credentials for ordinary Lean checks. The preferred wrapper mode
commits/pushes on the local machine, then streams a `git archive` of the Lean project directory to
the worker. Install worker-side GitHub credentials only if the worker is expected to clone private
repos independently.

## Repository Layout

For a research repo, prefer:

```text
formalization/
  lean-toolchain
  lakefile.toml or lakefile.lean
  lake-manifest.json
  Formalization/
    Basic.lean
    <PaperName>.lean
  TRANSLATION_LEDGER.md
```

Commit the Lean source, `lean-toolchain`, `lakefile.*`, `lake-manifest.json`, and translation ledger.
Do not commit `.lake/`.

## Validation Checklist

Before reporting a formalization as checked:

1. Run the target file with `lake env lean <file>` or run `lake build`.
2. Search the formalization directory for `sorry`, `admit`, `axiom`, `unsafe`, and placeholder names.
3. Inspect the theorem statement with `#check` or by reading Lean's elaborated output when implicit
   arguments matter.
4. Compare the Lean statement against the LaTeX theorem line by line: objects, assumptions,
   quantifier order, finiteness, decidability, nonemptiness, equality/inequality direction, and
   conclusion.
5. Record any mismatch or dependency on a custom definition in `TRANSLATION_LEDGER.md`.

## Remote Command Examples

```bash
scripts/lean_worker_sync_run.sh --sync-mode archive --sync-path formalization \
  --commit "Formalize theorem X" --stage formalization --workdir formalization -- lake build

scripts/lean_worker_sync_run.sh --workdir formalization -- lake env lean Formalization/Main.lean

LEAN_REMOTE_WORKDIR=$HOME/lean/MathlibSmoke \
  .claude/skills/lean4-formalization/scripts/remote_lean.sh lake build

LEAN_REMOTE_WORKDIR=/path/to/project/formalization \
  .claude/skills/lean4-formalization/scripts/remote_lean.sh lake env lean Formalization/Main.lean
```

Use `--commit MSG` only when the local changes are intended to be committed. Without `--commit`, the
wrapper refuses to sync a dirty worktree so the worker cannot accidentally check stale code.

Useful options:

- `--stage PATH`, repeatable, to commit only selected paths.
- `--sync-mode archive --sync-path formalization` to avoid worker GitHub credentials and sync only the
  Lean project directory.
- `--sync-mode auto` to try worker-side `git clone`/`git pull` first and fall back to archive sync.
- `--sync-mode git` only when the worker has working GitHub credentials for the repo.
- `--skip-git-sync --remote-repo PATH` for smoke tests in an already-existing worker project.
- `--jobs N` to set `LEAN_NUM_THREADS=N` and pass `-Kjobs=N` to Lake commands.
- `--no-cache-get` only when a `lake build` should deliberately skip `lake exe cache get`.
