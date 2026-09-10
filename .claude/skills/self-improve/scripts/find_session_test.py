import json
import os
from pathlib import Path

from find_session import find_recent_sessions, find_sessions


def _write_session(path: Path, *, cwd: Path, session_id: str, modified_at: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"payload": {"cwd": str(cwd), "session_id": session_id}}
    path.write_text(json.dumps(record, ensure_ascii=False) + "\n", encoding="utf-8")
    os.utime(path, (modified_at, modified_at))


def test_find_sessions_prefers_cwd_match_over_newer_session(tmp_path: Path) -> None:
    home = tmp_path / "home"
    workspace = tmp_path / "workspace"
    matching = home / ".codex/sessions/2026/09/02/matching.jsonl"
    newer_other = home / ".codex/sessions/2026/09/02/newer-other.jsonl"
    _write_session(
        matching,
        cwd=workspace,
        session_id="matching-session",
        modified_at=100,
    )
    _write_session(
        newer_other,
        cwd=tmp_path / "other",
        session_id="other-session",
        modified_at=200,
    )

    candidates = find_sessions(home, workspace, limit=2)

    assert [candidate.session_id for candidate in candidates] == [
        "matching-session",
        "other-session",
    ]
    assert candidates[0].cwd_matches
    assert not candidates[1].cwd_matches


def test_find_sessions_supports_claude_project_layout(tmp_path: Path) -> None:
    home = tmp_path / "home"
    workspace = tmp_path / "workspace/project"
    encoded_workspace = str(workspace.resolve()).replace("/", "-")
    transcript = home / ".claude/projects" / encoded_workspace / "session.jsonl"
    _write_session(
        transcript,
        cwd=workspace,
        session_id="claude-session",
        modified_at=100,
    )

    candidates = find_sessions(home, workspace, limit=1)

    assert len(candidates) == 1
    assert candidates[0].client == "claude"
    assert candidates[0].session_id == "claude-session"


def test_find_recent_sessions_scans_arbitrary_directory_by_mtime(
    tmp_path: Path,
) -> None:
    workspace = tmp_path / "workspace"
    sessions = tmp_path / "exported-sessions"
    older = sessions / "nested" / "older.jsonl"
    newest = sessions / "newest.jsonl"
    middle = sessions / "2026" / "09" / "middle.jsonl"
    _write_session(older, cwd=workspace, session_id="older-session", modified_at=100)
    _write_session(middle, cwd=workspace, session_id="middle-session", modified_at=200)
    _write_session(newest, cwd=workspace, session_id="newest-session", modified_at=300)

    candidates = find_recent_sessions([sessions], limit=2, expected_cwd=workspace)

    assert [candidate.session_id for candidate in candidates] == [
        "newest-session",
        "middle-session",
    ]
    assert all(candidate.cwd_matches for candidate in candidates)
