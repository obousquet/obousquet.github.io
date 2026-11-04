#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -eq 0 ]; then
  echo "usage: remote_lean.sh <remote lean/lake command...>" >&2
  exit 2
fi

host="${LEAN_REMOTE_HOST:-}"
key="${LEAN_REMOTE_KEY:-}"
workdir="${LEAN_REMOTE_WORKDIR:?Set LEAN_REMOTE_WORKDIR to the remote project directory}"
cpu_limit="${LEAN_CPU_LIMIT:-14400}"
nice_level="${LEAN_NICE:-10}"

if [ -z "$host" ]; then
  echo "Set LEAN_REMOTE_HOST or supply --host where supported" >&2
  exit 2
fi
ssh_options=()
if [ -n "$key" ]; then
  ssh_options+=(-i "$key")
fi

quoted_cmd="$(printf '%q ' "$@")"
quoted_workdir="$(printf '%q' "$workdir")"
quoted_cpu="$(printf '%q' "$cpu_limit")"
quoted_nice="$(printf '%q' "$nice_level")"

ssh "${ssh_options[@]}" "$host" "set -euo pipefail
export PATH=\"\$HOME/.elan/bin:\$PATH\"
cd $quoted_workdir
mem_cap=\$(awk '/MemAvailable:/ {printf \"%.0f\\n\", \$2 * 1024 * 0.75}' /proc/meminfo)
echo \"remote=\$(hostname) workdir=\$PWD mem_cap=\$mem_cap cpu_limit=$quoted_cpu\" >&2
nice -n $quoted_nice prlimit --as=\"\$mem_cap\" --cpu=$quoted_cpu -- bash -lc $(printf '%q' "$quoted_cmd")
"
