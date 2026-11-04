#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
usage:
  lean_worker_sync_run.sh [options] -- <lean/lake command...>

Common:
  scripts/lean_worker_sync_run.sh --sync-mode archive --sync-path formalization --commit "Formalize lemma X" --workdir formalization -- lake build
  scripts/lean_worker_sync_run.sh --skip-git-sync --remote-repo /path/to/remote/project -- lake build

Options:
  --commit MSG          Stage, commit if needed, and push before running remotely.
  --stage PATH          Stage this path before committing. Repeatable. Defaults to -A with --commit.
  --sync-mode MODE      Worker sync mode: auto, git, or archive. Default: auto.
  --sync-path PATH      Path to include for archive sync. Repeatable. Default: --workdir, or . when --workdir is .
  --workdir REL         Directory inside the remote repo where the command runs. Default: .
  --remote-repo PATH    Exact repo/project path on the worker. Default: $LEAN_REMOTE_ROOT/<repo-name>.
  --remote-root PATH    Parent directory for worker clones. Default: $LEAN_REMOTE_ROOT; required unless --remote-repo is set.
  --host USER@HOST      Worker host. Default: $LEAN_REMOTE_HOST; required.
  --key PATH            SSH key. Default: $LEAN_REMOTE_KEY or SSH configuration.
  --cpu SECONDS         prlimit CPU seconds. Default: $LEAN_CPU_LIMIT or 14400.
  --nice N              nice level. Default: $LEAN_NICE or 10.
  --jobs N              Set LEAN_NUM_THREADS and Lake jobs to N for the remote command.
  --no-cache-get        Do not run "lake exe cache get" before "lake build".
  --skip-git-sync       Do not commit/push/pull; just run the command in --remote-repo.
  -h, --help            Show this help.
EOF
}

commit_msg=""
workdir="."
sync_mode="${LEAN_SYNC_MODE:-auto}"
remote_root="${LEAN_REMOTE_ROOT:-}"
remote_repo=""
host="${LEAN_REMOTE_HOST:-}"
key="${LEAN_REMOTE_KEY:-}"
cpu_limit="${LEAN_CPU_LIMIT:-14400}"
nice_level="${LEAN_NICE:-10}"
jobs="${LEAN_JOBS:-}"
skip_git_sync=0
cache_get=1
stage_paths=()
sync_paths=()

while [ "$#" -gt 0 ]; do
  case "$1" in
    --commit)
      commit_msg="${2:?missing commit message after --commit}"
      shift 2
      ;;
    --stage)
      stage_paths+=("${2:?missing path after --stage}")
      shift 2
      ;;
    --sync-mode)
      sync_mode="${2:?missing mode after --sync-mode}"
      shift 2
      ;;
    --sync-path)
      sync_paths+=("${2:?missing path after --sync-path}")
      shift 2
      ;;
    --workdir)
      workdir="${2:?missing directory after --workdir}"
      shift 2
      ;;
    --remote-repo)
      remote_repo="${2:?missing path after --remote-repo}"
      shift 2
      ;;
    --remote-root)
      remote_root="${2:?missing path after --remote-root}"
      shift 2
      ;;
    --host)
      host="${2:?missing host after --host}"
      shift 2
      ;;
    --key)
      key="${2:?missing key after --key}"
      shift 2
      ;;
    --cpu)
      cpu_limit="${2:?missing seconds after --cpu}"
      shift 2
      ;;
    --nice)
      nice_level="${2:?missing nice value after --nice}"
      shift 2
      ;;
    --jobs)
      jobs="${2:?missing job count after --jobs}"
      shift 2
      ;;
    --no-cache-get)
      cache_get=0
      shift
      ;;
    --skip-git-sync)
      skip_git_sync=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      break
      ;;
    *)
      echo "unknown option: $1" >&2
      usage
      exit 2
      ;;
  esac
done

if [ "$#" -eq 0 ]; then
  echo "missing remote command" >&2
  usage
  exit 2
fi

if [ -z "$host" ]; then
  echo "Set LEAN_REMOTE_HOST or supply --host where supported" >&2
  exit 2
fi
ssh_options=()
if [ -n "$key" ]; then
  ssh_options+=(-i "$key")
fi

if [ -z "$remote_repo" ] && [ -z "$remote_root" ]; then
  echo "Set LEAN_REMOTE_ROOT or supply --remote-root/--remote-repo" >&2
  exit 2
fi

case "$sync_mode" in
  auto|git|archive) ;;
  *)
    echo "invalid --sync-mode: $sync_mode" >&2
    exit 2
    ;;
esac

if [ "$skip_git_sync" -eq 0 ]; then
  repo_root="$(git rev-parse --show-toplevel)"
  cd "$repo_root"
  repo_name="$(basename "$repo_root")"
  branch="$(git branch --show-current)"
  if [ -z "$branch" ]; then
    echo "detached HEAD; refusing to sync automatically" >&2
    exit 1
  fi
  origin_url="$(git config --get remote.origin.url)"
  if [ -z "$origin_url" ]; then
    echo "missing remote.origin.url" >&2
    exit 1
  fi
  if [ -z "$remote_repo" ]; then
    remote_repo="$remote_root/$repo_name"
  fi

  if [ -n "$commit_msg" ]; then
    if [ "${#stage_paths[@]}" -eq 0 ]; then
      git add -A
    else
      git add -A -- "${stage_paths[@]}"
    fi
    if ! git diff --cached --quiet; then
      git diff --cached --check
      git commit -m "$commit_msg"
    fi
  elif ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
    echo "worktree has local changes; pass --commit MSG or commit/stash manually before syncing" >&2
    git status --short >&2
    exit 1
  fi

  if git rev-parse --abbrev-ref --symbolic-full-name '@{u}' >/dev/null 2>&1; then
    git push
  else
    git push -u origin "$branch"
  fi
else
  repo_root="$(pwd)"
  repo_name="$(basename "$repo_root")"
  branch=""
  origin_url=""
  if [ -z "$remote_repo" ]; then
    remote_repo="$remote_root/$repo_name"
  fi
fi

sync_paths_defaulted=0
if [ "${#sync_paths[@]}" -eq 0 ]; then
  sync_paths_defaulted=1
  if [ "$workdir" = "." ]; then
    sync_paths=(".")
  else
    sync_paths=("$workdir")
  fi
fi

for path in "${sync_paths[@]}"; do
  case "$path" in
    ""|/*|*"/../"*|../*|*".." )
      echo "unsafe --sync-path: $path" >&2
      exit 2
      ;;
  esac
done

run_remote_git_sync() {
  local quoted_remote_repo quoted_origin quoted_branch
  quoted_remote_repo="$(printf '%q' "$remote_repo")"
  quoted_origin="$(printf '%q' "$origin_url")"
  quoted_branch="$(printf '%q' "$branch")"
  ssh "${ssh_options[@]}" "$host" "set -euo pipefail
export PATH=\"\$HOME/.elan/bin:\$PATH\"
remote_repo=$quoted_remote_repo
origin_url=$quoted_origin
branch=$quoted_branch
mkdir -p \"\$(dirname \"\$remote_repo\")\"
if [ ! -d \"\$remote_repo/.git\" ]; then
  git clone \"\$origin_url\" \"\$remote_repo\"
fi
cd \"\$remote_repo\"
git fetch origin \"\$branch\"
git checkout \"\$branch\"
git pull --ff-only origin \"\$branch\"
"
}

run_archive_sync() {
  local quoted_remote_repo delete_args path
  quoted_remote_repo="$(printf '%q' "$remote_repo")"
  delete_args=""
  for path in "${sync_paths[@]}"; do
    if [ "$path" != "." ]; then
      delete_args+=" $(printf '%q' "$path")"
    fi
  done
  echo "syncing archive to worker: ${sync_paths[*]}" >&2
  git archive --format=tar HEAD -- "${sync_paths[@]}" | ssh "${ssh_options[@]}" "$host" "set -euo pipefail
remote_repo=$quoted_remote_repo
mkdir -p \"\$remote_repo\"
cd \"\$remote_repo\"
if [ -n \"$delete_args\" ]; then
  rm -rf -- $delete_args
fi
tar -xf -
"
}

if [ "$skip_git_sync" -eq 0 ]; then
  case "$sync_mode" in
    git)
      run_remote_git_sync
      ;;
    archive)
      run_archive_sync
      ;;
    auto)
      if ! run_remote_git_sync; then
        if [ "$sync_paths_defaulted" -eq 1 ]; then
          echo "worker git sync failed; falling back to archive sync of ${sync_paths[*]}" >&2
        else
          echo "worker git sync failed; falling back to archive sync of selected paths: ${sync_paths[*]}" >&2
        fi
        run_archive_sync
      fi
      ;;
  esac
fi

cmd_args=("$@")
if [ -n "$jobs" ] && [ "${cmd_args[0]}" = "lake" ]; then
  cmd_args=(lake "-Kjobs=$jobs" "${cmd_args[@]:1}")
fi

run_cache_get=0
cache_args=()
if [ "$cache_get" -eq 1 ] && [ "${cmd_args[0]}" = "lake" ]; then
  for arg in "${cmd_args[@]:1}"; do
    if [ "$arg" = "build" ]; then
      run_cache_get=1
      cache_args=(lake)
      if [ -n "$jobs" ]; then
        cache_args+=("-Kjobs=$jobs")
      fi
      cache_args+=(exe cache get)
      break
    fi
  done
fi

quoted_remote_repo="$(printf '%q' "$remote_repo")"
quoted_workdir="$(printf '%q' "$workdir")"
quoted_cpu="$(printf '%q' "$cpu_limit")"
quoted_nice="$(printf '%q' "$nice_level")"
quoted_jobs="$(printf '%q' "$jobs")"
quoted_cmd="$(printf '%q ' "${cmd_args[@]}")"
quoted_cache_cmd=""
if [ "$run_cache_get" -eq 1 ]; then
  quoted_cache_cmd="$(printf '%q ' "${cache_args[@]}")"
fi
quoted_run_cache="$(printf '%q' "$run_cache_get")"

ssh "${ssh_options[@]}" "$host" "set -euo pipefail
export PATH=\"\$HOME/.elan/bin:\$PATH\"
remote_repo=$quoted_remote_repo
workdir=$quoted_workdir
jobs=$quoted_jobs
run_cache_get=$quoted_run_cache
cd \"\$remote_repo\"
cd \"\$workdir\"
mem_cap=\$(awk '/MemAvailable:/ {printf \"%.0f\\n\", \$2 * 1024 * 0.75}' /proc/meminfo)
if [ -n \"\$jobs\" ]; then
  export LEAN_NUM_THREADS=\"\$jobs\"
fi
if [ \"\$run_cache_get\" -eq 1 ]; then
  echo \"remote=\$(hostname) repo=\$remote_repo workdir=\$PWD mem_cap=\$mem_cap cpu_limit=$quoted_cpu command=$quoted_cache_cmd\" >&2
  nice -n $quoted_nice prlimit --as=\"\$mem_cap\" --cpu=$quoted_cpu -- bash -lc $(printf '%q' "$quoted_cache_cmd")
fi
echo \"remote=\$(hostname) repo=\$remote_repo workdir=\$PWD mem_cap=\$mem_cap cpu_limit=$quoted_cpu command=$quoted_cmd\" >&2
nice -n $quoted_nice prlimit --as=\"\$mem_cap\" --cpu=$quoted_cpu -- bash -lc $(printf '%q' "$quoted_cmd")
"
