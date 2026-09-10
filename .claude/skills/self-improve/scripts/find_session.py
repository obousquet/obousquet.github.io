#!/usr/bin/env python3

import argparse
import json
import os
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class SessionCandidate:
    path: str
    client: str
    modified_at: str
    cwd: str | None
    cwd_matches: bool
    session_id: str | None


def _encoded_project_path(cwd: Path) -> str:
    return str(cwd.resolve()).replace("/", "-")


def _iter_json_objects(path: Path, max_lines: int = 128) -> Iterable[dict[str, Any]]:
    try:
        with path.open(encoding="utf-8") as stream:
            for index, line in enumerate(stream):
                if index >= max_lines:
                    return
                try:
                    value = json.loads(line)
                except json.JSONDecodeError:
                    # An active JSONL transcript may end with a partial record.
                    continue
                if isinstance(value, dict):
                    yield value
    except (OSError, UnicodeError):
        return


def _first_key(value: Any, keys: frozenset[str]) -> str | None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in keys and isinstance(child, str):
                return child
        for child in value.values():
            result = _first_key(child, keys)
            if result is not None:
                return result
    elif isinstance(value, list):
        for child in value:
            result = _first_key(child, keys)
            if result is not None:
                return result
    return None


def _metadata(
    path: Path, client: str, expected_cwd: Path | None
) -> SessionCandidate:
    transcript_cwd: str | None = None
    session_id: str | None = None
    for value in _iter_json_objects(path):
        transcript_cwd = transcript_cwd or _first_key(value, frozenset({"cwd"}))
        session_id = session_id or _first_key(
            value, frozenset({"session_id", "sessionId"})
        )
        if transcript_cwd is not None and session_id is not None:
            break

    cwd_matches = False
    if expected_cwd is not None:
        try:
            cwd_matches = (
                transcript_cwd is not None
                and Path(transcript_cwd).resolve() == expected_cwd.resolve()
            )
        except OSError:
            cwd_matches = False

    modified_at = datetime.fromtimestamp(
        path.stat().st_mtime, tz=timezone.utc
    ).isoformat()
    return SessionCandidate(
        path=str(path.resolve()),
        client=client,
        modified_at=modified_at,
        cwd=transcript_cwd,
        cwd_matches=cwd_matches,
        session_id=session_id,
    )


def _existing_jsonl(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if path.is_file() and path.suffix == ".jsonl":
            yield path


def _iter_jsonl_recursive(root: Path) -> Iterable[Path]:
    if root.is_file():
        if root.suffix == ".jsonl":
            yield root
        return
    if not root.is_dir():
        return
    for base, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            dirname
            for dirname in dirnames
            if dirname not in {"__pycache__", ".pytest_cache", "node_modules"}
        ]
        base_path = Path(base)
        for filename in filenames:
            path = base_path / filename
            if path.suffix == ".jsonl" and path.is_file():
                yield path


def _session_paths(root: Path) -> Iterable[Path]:
    if not root.is_dir():
        return
    yield from _existing_jsonl(root.glob("*.jsonl"))
    yield from _existing_jsonl(root.glob("*/*/*/*.jsonl"))


def _client_from_path(path: Path) -> str:
    parts = set(path.parts)
    if ".codex" in parts:
        return "codex"
    if ".agents" in parts:
        return "agents"
    if ".claude" in parts:
        return "claude"
    return "unknown"


def _candidate_paths(home: Path, cwd: Path) -> Iterable[tuple[Path, str]]:
    encoded_cwd = _encoded_project_path(cwd)
    project_roots = (
        (home / ".claude" / "projects" / encoded_cwd, "claude"),
        (home / ".agents" / "projects" / encoded_cwd, "agents"),
    )
    for root, client in project_roots:
        if root.is_dir():
            for path in _existing_jsonl(root.glob("*.jsonl")):
                yield path, client

    session_roots = (
        (home / ".codex" / "sessions", "codex"),
        (home / ".agents" / "sessions", "agents"),
        (home / ".claude" / "sessions", "claude"),
        (cwd / ".codex" / "sessions", "codex"),
        (cwd / ".agents" / "sessions", "agents"),
        (cwd / ".claude" / "sessions", "claude"),
    )
    for root, client in session_roots:
        for path in _session_paths(root):
            yield path, client


def find_sessions(home: Path, cwd: Path, limit: int) -> list[SessionCandidate]:
    unique: dict[Path, str] = {}
    for path, client in _candidate_paths(home, cwd):
        try:
            unique[path.resolve()] = client
        except OSError:
            continue

    newest = sorted(
        unique.items(), key=lambda item: item[0].stat().st_mtime, reverse=True
    )[:200]
    candidates = [_metadata(path, client, cwd) for path, client in newest]
    candidates.sort(
        key=lambda candidate: (candidate.cwd_matches, candidate.modified_at),
        reverse=True,
    )
    return candidates[:limit]


def find_recent_sessions(
    session_dirs: Iterable[Path], limit: int, expected_cwd: Path | None = None
) -> list[SessionCandidate]:
    unique: dict[Path, str] = {}
    for session_dir in session_dirs:
        for path in _iter_jsonl_recursive(session_dir):
            try:
                unique[path.resolve()] = _client_from_path(path)
            except OSError:
                continue

    newest = sorted(
        unique.items(), key=lambda item: item[0].stat().st_mtime, reverse=True
    )[:limit]
    return [_metadata(path, client, expected_cwd) for path, client in newest]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Locate likely persisted transcripts for the current session."
    )
    parser.add_argument(
        "--cwd",
        type=Path,
        default=Path.cwd(),
        help="Working directory used to rank transcript candidates.",
    )
    parser.add_argument(
        "--home",
        type=Path,
        default=Path(os.environ.get("HOME", str(Path.home()))),
        help="Home directory containing .claude, .agents, or .codex.",
    )
    parser.add_argument(
        "--limit", type=int, default=5, help="Maximum number of candidates to print."
    )
    parser.add_argument(
        "--sessions-dir",
        type=Path,
        action="append",
        default=[],
        help=(
            "Directory or JSONL file to scan directly. When supplied, candidates "
            "are the --limit newest JSONL transcripts under the given path(s)."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.limit < 1:
        raise ValueError(f"Expected --limit to be positive, got {args.limit}")
    if args.sessions_dir:
        candidates = find_recent_sessions(args.sessions_dir, args.limit, args.cwd)
    else:
        candidates = find_sessions(args.home, args.cwd, args.limit)
    result = [asdict(candidate) for candidate in candidates]
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
