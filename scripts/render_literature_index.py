#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RESULT_HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$")
RESULT_BULLET_RE = re.compile(
    r"^\s*[-*]\s+(?:\*\*)?"
    r"((?:Theorem|Lemma|Proposition|Corollary|Definition|Question|Conjecture|Example|Remark)"
    r"[^:*–—]*)(?:\*\*)?\s*[:–—-]\s*(.+?)\s*$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Packet:
    key: str
    path: Path
    title: str
    authors: str
    year: str
    url: str
    tags: tuple[str, ...]
    source_text: Path | None
    key_results: Path | None
    metadata: dict[str, Any]


@dataclass(frozen=True)
class KeyResult:
    packet: Packet
    label: str
    summary: str
    href: str


def esc(value: object) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def as_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def first_metadata_value(data: dict[str, Any], *keys: str) -> str:
    for key in keys:
        value = data.get(key)
        text = as_text(value).strip()
        if text:
            return text
    return ""


def packet_from_dir(packet_dir: Path, literature_dir: Path) -> Packet | None:
    metadata_path = packet_dir / "metadata.json"
    if not metadata_path.exists():
        return None
    data = read_json(metadata_path)
    key = first_metadata_value(data, "citation_key", "key", "bibtex_key") or packet_dir.name
    tags_value = data.get("tags") or data.get("keywords") or []
    tags = tuple(str(tag).strip() for tag in tags_value if str(tag).strip()) if isinstance(tags_value, list) else ()
    source_text = packet_dir / "source.txt"
    key_results = packet_dir / "key-results.md"
    return Packet(
        key=key,
        path=packet_dir,
        title=first_metadata_value(data, "title") or key,
        authors=first_metadata_value(data, "authors", "author"),
        year=first_metadata_value(data, "year", "date"),
        url=first_metadata_value(data, "url", "source_url", "doi", "arxiv", "arxiv_url"),
        tags=tags,
        source_text=source_text if source_text.exists() else None,
        key_results=key_results if key_results.exists() else None,
        metadata=data,
    )


def discover_packets(literature_dir: Path) -> list[Packet]:
    if not literature_dir.exists():
        return []
    packets = [
        packet
        for child in sorted(literature_dir.iterdir(), key=lambda p: p.name.lower())
        if child.is_dir()
        for packet in [packet_from_dir(child, literature_dir)]
        if packet is not None
    ]
    return sorted(packets, key=lambda packet: (packet.year, packet.key.lower()), reverse=True)


def first_summary_line(lines: list[str]) -> str:
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            stripped = stripped[2:].strip()
        return stripped
    return ""


def extract_key_results(packet: Packet, output_dir: Path) -> list[KeyResult]:
    if packet.key_results is None:
        return []
    try:
        text = packet.key_results.read_text(encoding="utf-8")
    except OSError:
        return []
    results: list[KeyResult] = []
    current_label: str | None = None
    current_anchor = ""
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_label, current_lines, current_anchor
        if current_label is None:
            return
        summary = first_summary_line(current_lines)
        href = relative_href(output_dir, packet.key_results)
        if current_anchor:
            href += f"#{current_anchor}"
        results.append(KeyResult(packet=packet, label=current_label, summary=summary, href=href))
        current_label = None
        current_anchor = ""
        current_lines = []

    for line in text.splitlines():
        heading = RESULT_HEADING_RE.match(line)
        if heading:
            flush()
            label = heading.group(2).strip()
            if looks_like_result(label):
                current_label = label
                current_anchor = slugify(label)
                current_lines = []
            continue
        bullet = RESULT_BULLET_RE.match(line)
        if bullet:
            results.append(
                KeyResult(
                    packet=packet,
                    label=bullet.group(1).strip(),
                    summary=bullet.group(2).strip(),
                    href=relative_href(output_dir, packet.key_results),
                )
            )
            continue
        if current_label is not None:
            current_lines.append(line)
    flush()
    return results


def looks_like_result(label: str) -> bool:
    lowered = label.lower()
    return any(
        word in lowered
        for word in (
            "theorem",
            "lemma",
            "proposition",
            "corollary",
            "definition",
            "conjecture",
            "question",
            "example",
            "remark",
        )
    )


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9 -]", "", text.lower())
    return re.sub(r"\s+", "-", slug).strip("-")


def relative_href(base_dir: Path, path: Path) -> str:
    return path.relative_to(base_dir).as_posix()


def render_markdown(output_dir: Path, packets: list[Packet], results: list[KeyResult]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Literature Index",
        "",
        f"Generated: {now}",
        "",
        "This index is generated from durable literature packets. Edit packet metadata and",
        "`key-results.md` files, then rerun `scripts/render_literature_index.py`.",
        "",
        f"- Packets: {len(packets)}",
        f"- Key results: {len(results)}",
        "",
        "## Papers",
        "",
        "| Key | Year | Title | Authors | Artifacts |",
        "|---|---:|---|---|---|",
    ]
    for packet in packets:
        artifacts = []
        artifacts.append(f"[metadata]({relative_href(output_dir, packet.path / 'metadata.json')})")
        if packet.source_text is not None:
            artifacts.append(f"[source text]({relative_href(output_dir, packet.source_text)})")
        if packet.key_results is not None:
            artifacts.append(f"[key results]({relative_href(output_dir, packet.key_results)})")
        title = f"[{packet.title}]({packet.url})" if packet.url else packet.title
        lines.append(
            "| "
            + " | ".join(
                [
                    packet.key,
                    packet.year,
                    title.replace("|", "\\|"),
                    packet.authors.replace("|", "\\|"),
                    ", ".join(artifacts),
                ]
            )
            + " |"
        )
    lines.extend(["", "## Key Results", ""])
    if not results:
        lines.append("_No key results extracted yet._")
    for result in results:
        summary = f" — {result.summary}" if result.summary else ""
        lines.append(f"- **{result.packet.key}: [{result.label}]({result.href})**{summary}")
    return "\n".join(lines).rstrip() + "\n"


def render_html(output_dir: Path, packets: list[Packet], results: list[KeyResult]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    paper_rows = []
    for packet in packets:
        artifacts = [f'<a href="{esc(relative_href(output_dir, packet.path / "metadata.json"))}">metadata</a>']
        if packet.source_text is not None:
            artifacts.append(f'<a href="{esc(relative_href(output_dir, packet.source_text))}">source text</a>')
        if packet.key_results is not None:
            artifacts.append(f'<a href="{esc(relative_href(output_dir, packet.key_results))}">key results</a>')
        title = esc(packet.title)
        if packet.url:
            title = f'<a href="{esc(packet.url)}">{title}</a>'
        paper_rows.append(
            "<tr>"
            f"<td><code>{esc(packet.key)}</code></td>"
            f"<td>{esc(packet.year)}</td>"
            f"<td>{title}</td>"
            f"<td>{esc(packet.authors)}</td>"
            f"<td>{', '.join(artifacts)}</td>"
            "</tr>"
        )
    result_items = []
    for result in results:
        summary = f" — {esc(result.summary)}" if result.summary else ""
        result_items.append(
            f'<li><strong><code>{esc(result.packet.key)}</code>: '
            f'<a href="{esc(result.href)}">{esc(result.label)}</a></strong>{summary}</li>'
        )
    if not result_items:
        result_items.append("<li>No key results extracted yet.</li>")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Literature Index</title>
  <style>
    body {{ margin: 0; font-family: system-ui, sans-serif; background: #f6f8fb; color: #17212b; }}
    main {{ max-width: 980px; margin: 0 auto; padding: 28px 16px 44px; }}
    h1 {{ margin-bottom: 0.25rem; }}
    .muted {{ color: #516173; }}
    table {{ width: 100%; border-collapse: collapse; background: white; }}
    th, td {{ border: 1px solid #d8e0ea; padding: 0.45rem 0.55rem; vertical-align: top; }}
    th {{ text-align: left; background: #eef3f8; }}
    code {{ background: #eef3f8; padding: 0.1rem 0.25rem; border-radius: 0.2rem; }}
    a {{ color: #114b8b; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    li {{ margin-bottom: 0.45rem; }}
  </style>
</head>
<body>
<main>
  <h1>Literature Index</h1>
  <p class="muted">Generated {esc(now)} from durable literature packets.</p>
  <p>Packets: {len(packets)}. Key results: {len(results)}.</p>
  <h2>Papers</h2>
  <table>
    <thead><tr><th>Key</th><th>Year</th><th>Title</th><th>Authors</th><th>Artifacts</th></tr></thead>
    <tbody>
      {''.join(paper_rows)}
    </tbody>
  </table>
  <h2>Key Results</h2>
  <ul>
    {''.join(result_items)}
  </ul>
</main>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a literature packet index.")
    parser.add_argument("--repo-root", type=Path, default=Path("."), help="Repository root.")
    parser.add_argument("--literature-dir", type=Path, default=None, help="Literature packet directory.")
    parser.add_argument("--md", type=Path, default=None, help="Markdown output path.")
    parser.add_argument("--html", type=Path, default=None, help="HTML output path.")
    args = parser.parse_args()

    root = args.repo_root.resolve()
    literature_dir = (args.literature_dir or root / "literature").resolve()
    md_path = args.md or literature_dir / "index.md"
    html_path = args.html or literature_dir / "index.html"

    packets = discover_packets(literature_dir)
    result_base_dir = md_path.parent.resolve()
    results = [
        result
        for packet in packets
        for result in extract_key_results(packet, result_base_dir)
    ]
    results.sort(key=lambda result: (result.packet.key.lower(), result.label.lower()))

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_markdown(md_path.parent.resolve(), packets, results), encoding="utf-8")
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(render_html(html_path.parent.resolve(), packets, results), encoding="utf-8")
    print(f"wrote {md_path} and {html_path} ({len(packets)} packets, {len(results)} key results)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
