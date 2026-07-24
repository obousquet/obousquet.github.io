#!/usr/bin/env python3
"""Static preflight scanner for AI residue and citation risks in manuscripts."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SKIP_DIRS = {
    ".claude",
    ".codex",
    ".git",
    ".venv",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
}

TEXT_EXTS = {".tex", ".bib", ".md", ".txt", ".rst"}


@dataclass(frozen=True)
class Pattern:
    severity: str
    name: str
    regex: re.Pattern[str]
    hint: str


PATTERNS = [
    Pattern("BLOCK", "conversation residue", re.compile(r"\b(as an ai language model|i cannot|i can't|i apologize|i'm sorry)\b", re.I), "remove assistant/persona text"),
    Pattern("BLOCK", "chat handoff", re.compile(r"\b(let me know if|would you like me to|here(?:'s| is) (?:a|the)|sure[,!])\b", re.I), "rewrite as manuscript prose"),
    Pattern("BLOCK", "placeholder", re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum|placeholder|fill in|insert citation|citation needed)\b", re.I), "resolve before submission"),
    Pattern("MAJOR", "unsupported superlative", re.compile(r"\b(state[- ]of[- ]the[- ]art|best known|optimal|sharp|well[- ]known|classical|standard)\b", re.I), "verify local citation support"),
    Pattern("MAJOR", "generic ai prose", re.compile(r"\b(delves?|pivotal|realm|landscape|tapestry|intricate|nuanced|seamless|underscores?|robust framework|opens? (?:new )?avenues)\b", re.I), "replace by precise mathematical content"),
    Pattern("MAJOR", "generic proof jargon", re.compile(r"\b(proof spine|proof package|proof debt|proof obligation|mechanism|stratum|sector|gate|assay|finite certificate|certificate|boundary)\b", re.I), "define precisely or replace"),
    Pattern("MAJOR", "ai disclosure marker", re.compile(r"\b(ChatGPT|Claude|Gemini|Grok|GPT-?[0-9]|Codex|large language model|LLM)\b", re.I), "check disclosure/provenance treatment"),
]


def iter_files(paths: list[Path], max_files: int | None) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            if path.suffix.lower() in TEXT_EXTS:
                files.append(path)
            continue
        if path.is_dir():
            for child in path.rglob("*"):
                if max_files is not None and len(files) >= max_files:
                    break
                if any(part in SKIP_DIRS for part in child.parts):
                    continue
                if child.is_file() and child.suffix.lower() in TEXT_EXTS:
                    files.append(child)
    return files[:max_files] if max_files is not None else files


def line_context(text: str, match: re.Match[str]) -> tuple[int, str]:
    line_no = text.count("\n", 0, match.start()) + 1
    line_start = text.rfind("\n", 0, match.start()) + 1
    line_end = text.find("\n", match.end())
    if line_end == -1:
        line_end = len(text)
    return line_no, text[line_start:line_end].strip()


def scan_patterns(path: Path, text: str) -> list[tuple[str, str, int, str, str]]:
    findings = []
    for pattern in PATTERNS:
        for match in pattern.regex.finditer(text):
            line_no, line = line_context(text, match)
            findings.append((pattern.severity, pattern.name, line_no, line, pattern.hint))
    return findings


def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", text))


def tex_cite_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for body in re.findall(r"\\(?:cite|citet|citep|citealp|citealt|autocite|parencite|textcite)(?:\[[^\]]*\]){0,2}\{([^}]+)\}", text):
        keys.update(key.strip() for key in body.split(",") if key.strip())
    return keys


def scan_bib_entry(path: Path, entry: str) -> list[tuple[str, str, int, str, str]]:
    findings = []
    key_match = re.match(r"@\w+\s*\{\s*([^,\s]+)", entry)
    key = key_match.group(1) if key_match else "<unknown>"
    required = ["title", "author", "year"]
    for field in required:
        if not re.search(rf"\b{field}\s*=", entry, re.I):
            findings.append(("MAJOR", f"bib missing {field}", 1, key, "verify bibliographic metadata"))
    if re.search(r"\bdoi\s*=\s*[{\"']?\s*(10\.xxxx|tbd|todo|example|dummy)", entry, re.I):
        findings.append(("BLOCK", "placeholder DOI", 1, key, "replace with verified DOI or remove DOI"))
    if re.search(r"\barxiv\s*=\s*[{\"']?\s*(tbd|todo|example|dummy)", entry, re.I):
        findings.append(("BLOCK", "placeholder arXiv id", 1, key, "replace with verified arXiv id or remove field"))
    if re.search(r"\?{2,}|citation needed|insert", entry, re.I):
        findings.append(("BLOCK", "bibliography placeholder", 1, key, "resolve bibliography placeholder"))
    return [(sev, name, line, msg, hint) for sev, name, line, msg, hint in findings]


def scan_bib_entries(path: Path, text: str) -> list[tuple[str, str, int, str, str]]:
    findings = []
    for match in re.finditer(r"@\w+\s*\{", text):
        next_match = re.search(r"\n@\w+\s*\{", text[match.end():])
        end = match.end() + next_match.start() if next_match else len(text)
        entry = text[match.start():end]
        line_no, _ = line_context(text, match)
        for sev, name, _line, msg, hint in scan_bib_entry(path, entry):
            findings.append((sev, name, line_no, msg, hint))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan manuscript text for AI residue and citation-risk signals.")
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    parser.add_argument("--max-files", type=int, default=None, help="Limit files scanned")
    args = parser.parse_args()

    files = iter_files(args.paths, args.max_files)
    all_findings: list[tuple[Path, str, str, int, str, str]] = []
    all_bib_keys: set[str] = set()
    all_cite_keys: set[str] = set()

    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"ERROR: could not read {path}: {exc}", file=sys.stderr)
            continue
        for sev, name, line_no, line, hint in scan_patterns(path, text):
            all_findings.append((path, sev, name, line_no, line, hint))
        if path.suffix.lower() == ".bib":
            all_bib_keys.update(bib_keys(text))
            for sev, name, line_no, line, hint in scan_bib_entries(path, text):
                all_findings.append((path, sev, name, line_no, line, hint))
        if path.suffix.lower() == ".tex":
            all_cite_keys.update(tex_cite_keys(text))

    missing = sorted(all_cite_keys - all_bib_keys) if all_bib_keys else []
    for key in missing:
        all_findings.append((Path("<citations>"), "BLOCK", "missing bibliography key", 0, key, "add verified bibliography entry or remove cite"))

    counts = {"BLOCK": 0, "MAJOR": 0, "MINOR": 0}
    for _path, sev, _name, _line_no, _line, _hint in all_findings:
        counts[sev] = counts.get(sev, 0) + 1

    print("AI slop preflight static scan")
    print(f"Files scanned: {len(files)}")
    print(f"Findings: {counts.get('BLOCK', 0)} blocking, {counts.get('MAJOR', 0)} major, {counts.get('MINOR', 0)} minor")
    if all_cite_keys:
        print(f"Citation keys used: {len(all_cite_keys)}")
    if all_bib_keys:
        print(f"Bibliography keys seen: {len(all_bib_keys)}")
    print()

    for path, sev, name, line_no, line, hint in all_findings:
        loc = f"{path}:{line_no}" if line_no else str(path)
        print(f"[{sev}] {loc} {name}: {line}")
        print(f"       hint: {hint}")

    if not all_findings:
        print("No static findings. Manual citation and disclosure audits are still required.")

    return 1 if counts.get("BLOCK", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
