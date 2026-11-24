#!/usr/bin/env python3
"""Audit the static structure of an arXiv source directory or tar archive."""

from __future__ import annotations

import argparse
import io
import re
import sys
import tarfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


ALLOWED_COMPONENT = re.compile(r"^[A-Za-z0-9_+\-.,=]+$")
TEX_INPUT = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")
DOCUMENTCLASS = re.compile(r"\\documentclass(?:\[[^]]*\])?\s*\{")
JUNK_NAMES = {".DS_Store", "Thumbs.db"}
JUNK_SUFFIXES = {
    ".aux",
    ".log",
    ".out",
    ".toc",
    ".fls",
    ".fdb_latexmk",
    ".synctex",
}


@dataclass
class Bundle:
    names: list[str]
    data: dict[str, bytes]


def normalize_name(name: str) -> str:
    return name[2:] if name.startswith("./") else name


def load_directory(path: Path) -> Bundle:
    names: list[str] = []
    data: dict[str, bytes] = {}
    for child in sorted(path.rglob("*")):
        if child.is_symlink():
            names.append(child.relative_to(path).as_posix())
            continue
        if not child.is_file():
            continue
        name = child.relative_to(path).as_posix()
        names.append(name)
        data[name] = child.read_bytes()
    return Bundle(names, data)


def load_archive(path: Path, errors: list[str]) -> Bundle:
    names: list[str] = []
    data: dict[str, bytes] = {}
    try:
        archive = tarfile.open(path, mode="r:*")
    except (tarfile.TarError, OSError) as exc:
        raise SystemExit(f"cannot read archive: {exc}") from exc
    with archive:
        for member in archive.getmembers():
            name = normalize_name(member.name)
            if member.isdir():
                continue
            names.append(name)
            if not member.isfile():
                errors.append(f"non-regular archive member: {name}")
                continue
            extracted = archive.extractfile(member)
            if extracted is None:
                errors.append(f"unreadable archive member: {name}")
                continue
            data[name] = extracted.read()
    return Bundle(names, data)


def unsafe_name(name: str) -> bool:
    pure = PurePosixPath(name)
    return pure.is_absolute() or not pure.parts or any(part in {"", ".", ".."} for part in pure.parts)


def audit(bundle: Bundle, root: str | None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    seen: set[str] = set()

    for name in bundle.names:
        if name in seen:
            errors.append(f"duplicate member: {name}")
        seen.add(name)
        if unsafe_name(name):
            errors.append(f"unsafe path: {name}")
            continue
        for component in PurePosixPath(name).parts:
            if not ALLOWED_COMPONENT.fullmatch(component):
                errors.append(f"filename may be arXiv-incompatible: {name}")
                break
        if any(part.startswith(".") for part in PurePosixPath(name).parts):
            warnings.append(f"hidden path included: {name}")
        if PurePosixPath(name).name in JUNK_NAMES:
            errors.append(f"operating-system metadata included: {name}")
        if name.endswith(".synctex.gz") or Path(name).suffix in JUNK_SUFFIXES:
            errors.append(f"build artifact included: {name}")

    tex_text: dict[str, str] = {}
    for name, raw in bundle.data.items():
        if name.endswith(".tex"):
            tex_text[name] = raw.decode("utf-8", errors="replace")

    roots = sorted(name for name, text in tex_text.items() if DOCUMENTCLASS.search(text))
    if root is not None:
        root = normalize_name(root)
        if root not in bundle.data:
            errors.append(f"requested root is absent: {root}")
        elif root not in roots:
            errors.append(f"requested root has no documentclass: {root}")
    elif len(roots) != 1:
        warnings.append(f"found {len(roots)} TeX roots with documentclass: {', '.join(roots) or 'none'}")

    for source, text in tex_text.items():
        parent = PurePosixPath(source).parent
        for target in TEX_INPUT.findall(text):
            target = target.strip()
            if not target or "\\" in target or "#" in target:
                warnings.append(f"macro-generated input needs manual review: {source}: {target}")
                continue
            dependency = PurePosixPath(target if target.endswith(".tex") else f"{target}.tex")
            resolved = (parent / dependency).as_posix()
            alternatives = {dependency.as_posix(), resolved}
            if not any(candidate in bundle.data for candidate in alternatives):
                errors.append(f"missing TeX input from {source}: {target}")

    top_components = {PurePosixPath(name).parts[0] for name in bundle.data}
    if len(top_components) == 1 and not any("/" not in name for name in bundle.data):
        warnings.append("all files lie under one enclosing directory; arXiv bundles normally place the root TeX file at archive root")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path, help="source directory or .tar/.tar.gz archive")
    parser.add_argument("--root", help="expected top-level TeX file, for example main.tex")
    args = parser.parse_args()

    load_errors: list[str] = []
    bundle = load_directory(args.bundle) if args.bundle.is_dir() else load_archive(args.bundle, load_errors)
    errors, warnings = audit(bundle, args.root)
    errors = load_errors + errors

    print("arXiv bundle static audit")
    print(f"Files: {len(bundle.data)}")
    print(f"TeX files: {sum(name.endswith('.tex') for name in bundle.data)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for message in errors:
        print(f"[ERROR] {message}")
    for message in warnings:
        print(f"[WARN] {message}")
    if not errors:
        print("Static structure passed. A clean TeX build and manual policy review are still required.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
