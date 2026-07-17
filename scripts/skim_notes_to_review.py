#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SKIM_TEMPLATE = r"""$notes.@arraySortedByPageIndexAndBounds
---
type: <$type.typeName/>
page_index: <$pageIndex/>
page: <$page.label?><$page.label/><?$page.label?><$pageIndex.numberByAddingOne/></$page.label?>
bounds: <$bounds/>
skim_url: <$skimURL/>

selected_text:
<$selection.cleanedString?>
<$selection.cleanedString/>
</$selection.cleanedString?>
<$string?>
<$string/>
</$string?>

note:
<$text?>
<$text/>
</$text?>
/$notes.@arraySortedByPageIndexAndBounds
"""


FIELD_RE = re.compile(
    r"^(type|page_index|page|bounds|skim_url|selected_text|note):\s*(.*)$"
)


@dataclass
class Note:
    index: int
    type: str = ""
    page_index: int | None = None
    page: int | None = None
    bounds: tuple[float, float, float, float] | None = None
    skim_url: str = ""
    selected_text: str = ""
    note: str = ""


@dataclass
class SourceLocation:
    input: str
    line: int | None = None
    column: int | None = None

    def label(self) -> str:
        if self.line is None:
            return self.input
        if self.column is None:
            return f"{self.input}:{self.line}"
        return f"{self.input}:{self.line}:{self.column}"


def parse_int(value: str) -> int | None:
    match = re.search(r"-?\d+", value or "")
    return int(match.group(0)) if match else None


def parse_bounds(value: str) -> tuple[float, float, float, float] | None:
    numbers = re.findall(r"-?\d+(?:\.\d+)?", value or "")
    if len(numbers) < 4:
        return None
    x, y, width, height = (float(number) for number in numbers[:4])
    return x, y, width, height


def clean_multiline(value: str) -> str:
    lines = value.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def collapse_duplicate_blocks(value: str) -> str:
    value = clean_multiline(value)
    if not value:
        return ""
    blocks = [clean_multiline(block) for block in re.split(r"\n\s*\n", value)]
    kept: list[str] = []
    seen: set[str] = set()
    for block in blocks:
        key = re.sub(r"\s+", " ", block).strip()
        if not key or key in seen:
            continue
        seen.add(key)
        kept.append(block)
    return "\n\n".join(kept)


def parse_notes(text: str) -> list[Note]:
    raw_records = [record.strip("\n") for record in re.split(r"(?m)^---\s*$", text)]
    notes: list[Note] = []
    for raw in raw_records:
        if not raw.strip():
            continue
        fields: dict[str, str] = {}
        current: str | None = None
        current_lines: list[str] = []
        saw_field = False
        for line in raw.splitlines():
            match = FIELD_RE.match(line)
            if match:
                saw_field = True
                if current is not None:
                    fields[current] = clean_multiline("\n".join(current_lines))
                current = match.group(1)
                current_lines = [match.group(2)] if match.group(2) else []
                continue
            if current is not None:
                current_lines.append(line)
        if current is not None:
            fields[current] = clean_multiline("\n".join(current_lines))
        if not saw_field:
            continue

        page_index = parse_int(fields.get("page_index", ""))
        page = parse_int(fields.get("page", ""))
        if page is None and page_index is not None:
            page = page_index + 1
        notes.append(
            Note(
                index=len(notes) + 1,
                type=fields.get("type", "").strip(),
                page_index=page_index,
                page=page,
                bounds=parse_bounds(fields.get("bounds", "")),
                skim_url=fields.get("skim_url", "").strip(),
                selected_text=collapse_duplicate_blocks(fields.get("selected_text", "")),
                note=collapse_duplicate_blocks(fields.get("note", "")),
            )
        )
    return notes


def page_height_from_pdfinfo(pdf_path: Path, page: int) -> float | None:
    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo is None:
        return None
    result = subprocess.run(
        [pdfinfo, "-box", "-f", str(page), "-l", str(page), str(pdf_path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        return None
    for line in result.stdout.splitlines():
        match = re.search(
            r"(?:Page\s+\d+\s+)?size:\s+([0-9.]+)\s+x\s+([0-9.]+)\s+pts",
            line,
        )
        if match:
            return float(match.group(2))
    return None


def synctex_edit(
    pdf_path: Path,
    page: int,
    x: float,
    y: float,
    synctex_dir: Path | None = None,
    synctex_bin: str = "synctex",
) -> list[SourceLocation]:
    command = [synctex_bin, "edit", "-o", f"{page}:{x:.3f}:{y:.3f}:{pdf_path}"]
    if synctex_dir is not None:
        command.extend(["-d", str(synctex_dir)])
    result = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout).strip())
    return parse_synctex_locations(result.stdout)


def parse_synctex_locations(output: str) -> list[SourceLocation]:
    locations: list[SourceLocation] = []
    current: dict[str, str] = {}
    for line in output.splitlines():
        if line.startswith("SyncTeX result"):
            if line.endswith("end") and current:
                location = location_from_synctex_record(current)
                if location is not None:
                    locations.append(location)
                current = {}
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key == "Input" and current:
            location = location_from_synctex_record(current)
            if location is not None:
                locations.append(location)
            current = {}
        current[key] = value.strip()
    if current:
        location = location_from_synctex_record(current)
        if location is not None:
            locations.append(location)
    return locations


def location_from_synctex_record(record: dict[str, str]) -> SourceLocation | None:
    input_path = record.get("Input")
    if not input_path:
        return None
    line = parse_int(record.get("Line", ""))
    column = parse_int(record.get("Column", ""))
    if line is not None and line < 1:
        line = None
    if column is not None and column < 1:
        column = None
    return SourceLocation(input=input_path, line=line, column=column)


def best_location(locations: Iterable[SourceLocation]) -> SourceLocation | None:
    items = list(locations)
    if not items:
        return None
    for location in items:
        if location.input.endswith(".tex"):
            return location
    return items[0]


def quote_block(text: str) -> str:
    text = clean_multiline(text)
    if not text:
        return "_None exported._"
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def first_action_line(text: str) -> str:
    first = clean_multiline(text).splitlines()
    if not first:
        return ""
    return first[0].strip()


def render_review(
    notes: list[Note],
    mappings: dict[int, SourceLocation | None],
    errors: dict[int, str],
    pdf_path: Path,
    notes_path: Path,
) -> str:
    lines: list[str] = [
        "# PDF Review Notes",
        "",
        f"- PDF: `{pdf_path}`",
        f"- Skim notes export: `{notes_path}`",
        f"- Notes: {len(notes)}",
        "",
        "Use this file as an edit queue. The SyncTeX target is a best-effort source location; verify",
        "against the selected PDF text before editing.",
        "",
    ]
    if errors:
        lines.extend(["## Mapping Warnings", ""])
        for index, message in errors.items():
            lines.append(f"- A{index:03d}: {message}")
        lines.append("")

    for note in notes:
        location = mappings.get(note.index)
        target = location.label() if location else "unmapped"
        title_bits = [f"A{note.index:03d}", f"page {note.page or '?'}", target]
        lines.extend([f"## {' - '.join(title_bits)}", ""])
        if note.type:
            lines.append(f"- Type: `{note.type}`")
        if note.bounds is not None:
            bounds = ", ".join(f"{part:g}" for part in note.bounds)
            lines.append(f"- Bounds: `{bounds}`")
        if note.skim_url:
            lines.append(f"- Skim URL: `{note.skim_url}`")
        action = first_action_line(note.note)
        if action:
            lines.append(f"- First action line: {action}")
        lines.extend(["", "Selected PDF text:", "", quote_block(note.selected_text), ""])
        lines.extend(["Reviewer note:", "", quote_block(note.note), ""])
        lines.extend(
            [
                "Agent instruction:",
                "",
                "- Locate the target paragraph using the SyncTeX line and selected text.",
                "- Apply the reviewer note conservatively.",
                "- Preserve mathematical meaning and existing notation.",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_mappings(
    notes: list[Note],
    pdf_path: Path,
    synctex_dir: Path | None,
    synctex_bin: str,
    page_height: float | None,
    no_map: bool,
) -> tuple[dict[int, SourceLocation | None], dict[int, str]]:
    mappings: dict[int, SourceLocation | None] = {}
    errors: dict[int, str] = {}
    height_cache: dict[int, float] = {}

    if no_map:
        for note in notes:
            mappings[note.index] = None
        return mappings, errors

    if shutil.which(synctex_bin) is None:
        for note in notes:
            mappings[note.index] = None
            errors[note.index] = f"`{synctex_bin}` was not found; run with --no-map or install SyncTeX."
        return mappings, errors

    for note in notes:
        mappings[note.index] = None
        if note.page is None:
            errors[note.index] = "missing page number in Skim export"
            continue
        if note.bounds is None:
            errors[note.index] = "missing bounds in Skim export"
            continue
        if page_height is not None:
            height = page_height
        else:
            if note.page not in height_cache:
                detected = page_height_from_pdfinfo(pdf_path, note.page)
                if detected is not None:
                    height_cache[note.page] = detected
            height = height_cache.get(note.page)
        if height is None:
            errors[note.index] = "could not infer page height; pass --page-height"
            continue
        x, y_bottom, width, note_height = note.bounds
        query_x = x + width / 2
        query_y = height - (y_bottom + note_height / 2)
        try:
            mappings[note.index] = best_location(
                synctex_edit(
                    pdf_path=pdf_path,
                    page=note.page,
                    x=query_x,
                    y=query_y,
                    synctex_dir=synctex_dir,
                    synctex_bin=synctex_bin,
                )
            )
        except (OSError, RuntimeError) as exc:
            errors[note.index] = str(exc) or "SyncTeX query failed"
    return mappings, errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Map a Skim notes export back to TeX source lines and write an agent review file."
    )
    parser.add_argument("--print-skim-template", action="store_true", help="Print the recommended Skim export template and exit.")
    parser.add_argument("--pdf", type=Path, help="PDF file compiled with SyncTeX enabled.")
    parser.add_argument("--notes", type=Path, help="Text file exported from Skim using the recommended template.")
    parser.add_argument("--out", type=Path, help="Output Markdown review file.")
    parser.add_argument("--synctex-dir", type=Path, help="Directory containing the .synctex or .synctex.gz file, if not next to the PDF.")
    parser.add_argument("--synctex-bin", default="synctex", help="SyncTeX executable name or path.")
    parser.add_argument("--page-height", type=float, help="Manual page height in points, used when pdfinfo is unavailable.")
    parser.add_argument("--no-map", action="store_true", help="Do not call SyncTeX; only normalize notes into Markdown.")
    args = parser.parse_args()

    if args.print_skim_template:
        print(SKIM_TEMPLATE, end="")
        return 0

    missing = [name for name in ("pdf", "notes", "out") if getattr(args, name) is None]
    if missing:
        parser.error("missing required arguments: " + ", ".join(f"--{name}" for name in missing))

    assert args.pdf is not None
    assert args.notes is not None
    assert args.out is not None

    if not args.notes.exists():
        parser.error(f"notes file not found: {args.notes}")
    if not args.no_map and not args.pdf.exists():
        parser.error(f"PDF file not found: {args.pdf}")

    notes = parse_notes(args.notes.read_text(encoding="utf-8"))
    if not notes:
        parser.error("no notes found; export from Skim with the template printed by --print-skim-template")

    mappings, errors = build_mappings(
        notes=notes,
        pdf_path=args.pdf,
        synctex_dir=args.synctex_dir,
        synctex_bin=args.synctex_bin,
        page_height=args.page_height,
        no_map=args.no_map,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        render_review(
            notes=notes,
            mappings=mappings,
            errors=errors,
            pdf_path=args.pdf,
            notes_path=args.notes,
        ),
        encoding="utf-8",
    )
    mapped = sum(1 for location in mappings.values() if location is not None)
    print(f"wrote {args.out} ({mapped}/{len(notes)} notes mapped)")
    if errors:
        print(f"{len(errors)} mapping warning(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
