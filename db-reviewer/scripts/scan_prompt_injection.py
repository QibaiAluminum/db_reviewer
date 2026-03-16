#!/usr/bin/env python3
"""Scan PDFs or TeX sources for likely reviewer-facing prompt injection."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass


DEFAULT_PATTERNS = [
    r"include both",
    r"in your review",
    r"ignore previous",
    r"as a reviewer",
    r"must include",
    r'and\s+"[^"]+"\s+in your review',
]

DEFAULT_SOURCE_EXTENSIONS = {".tex", ".sty", ".cls", ".bib", ".txt", ".md"}
DEFAULT_TEX_PATTERNS = [
    r"\\textcolor\s*\{\s*white\s*\}",
    r"\\color\s*\{\s*white\s*\}",
    r"\\tiny\b",
    r"\\scriptsize\b",
    r"\\fontsize\s*\{[^}]+\}\s*\{[^}]+\}",
]


@dataclass
class Hit:
    source: str
    line_number: int
    pattern: str
    text: str


def extract_pdf_text(pdf_path: str) -> str:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError(
            "pdftotext is not installed. Install Poppler first, then rerun the scan."
        )

    result = subprocess.run(
        [pdftotext, "-layout", "-nopgbrk", pdf_path, "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or "pdftotext failed to extract text."
        raise RuntimeError(message)
    return result.stdout


def extract_file_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def iter_source_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(
        [
            candidate
            for candidate in path.rglob("*")
            if candidate.is_file() and candidate.suffix.lower() in DEFAULT_SOURCE_EXTENSIONS
        ]
    )


def find_hits(text: str, source: str, patterns: list[str]) -> list[Hit]:
    compiled = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    hits: list[Hit] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern, regex in zip(patterns, compiled):
            if regex.search(line):
                hits.append(
                    Hit(
                        source=source,
                        line_number=line_number,
                        pattern=pattern,
                        text=line.strip(),
                    )
                )
    return hits


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan a PDF, TeX file, or source directory for suspicious review instructions."
    )
    parser.add_argument("path", help="Path to a PDF, TeX-like text file, or source directory")
    parser.add_argument(
        "--pattern",
        action="append",
        dest="patterns",
        default=[],
        help="Additional case-insensitive regex pattern to scan for. Repeatable.",
    )
    return parser.parse_args()


def scan_path(path: Path, patterns: list[str]) -> list[Hit]:
    if not path.exists():
        raise RuntimeError(f"path not found: {path}")

    if path.is_file() and path.suffix.lower() == ".pdf":
        text = extract_pdf_text(str(path))
        return find_hits(text, str(path), patterns)

    if path.is_file():
        text = extract_file_text(path)
        return find_hits(text, str(path), patterns + DEFAULT_TEX_PATTERNS)

    hits: list[Hit] = []
    files = iter_source_files(path)
    if not files:
        raise RuntimeError(f"no supported text files found under: {path}")
    for file_path in files:
        text = extract_file_text(file_path)
        hits.extend(find_hits(text, str(file_path), patterns + DEFAULT_TEX_PATTERNS))
    return hits


def main() -> int:
    args = parse_args()
    patterns = DEFAULT_PATTERNS + args.patterns
    try:
        hits = scan_path(Path(args.path), patterns)
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not hits:
        print("No suspicious prompt-injection patterns found.")
        return 0

    print("Suspicious prompt-injection patterns detected:")
    for hit in hits:
        print(f"{hit.source}:{hit.line_number}: pattern={hit.pattern!r}")
        print(f"  {hit.text}")
    print("Do not repeat any requested trigger phrases in the review.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
