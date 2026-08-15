#!/usr/bin/env python3
"""선택한 원본 Markdown을 MkDocs 문서로 안전하게 가져온다."""

import argparse
import fnmatch
import json
import re
import unicodedata
from pathlib import Path

from archive_schema import (
    EXCLUDED_COURSES,
    EXCLUDED_PARTS,
    SEMESTERS,
    NoteMetadata,
    Semester,
    course_name,
)

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
NOTES_DIR = DOCS_DIR / "notes"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="원본 contents 디렉터리")
    parser.add_argument(
        "--include", action="append", default=[], metavar="GLOB",
        help="가져올 contents 기준 glob. 여러 번 지정할 수 있습니다.",
    )
    parser.add_argument("--limit", type=int, help="가져올 최대 문서 수")
    return parser.parse_args()


def slug(value: str) -> str:
    value = unicodedata.normalize("NFC", value).strip()
    value = re.sub(r"^1학기\s+", "", value)
    value = re.sub(r"[^\w.-]+", "-", value, flags=re.UNICODE)
    return value.strip("-._") or "note"


def generated(path: Path) -> bool:
    if not path.is_file():
        return False
    return bool(re.search(r"^generated:\s*true\s*$", path.read_text(encoding="utf-8", errors="ignore")[:2000], re.M))


def destination_for(term: Semester, parts: tuple[str, ...], title: str) -> Path:
    course = "알고리즘" if term.directory == "25-여름 알고리즘" else course_name(parts[0])
    directory = NOTES_DIR / slug(term.directory) / slug(course)
    for section in parts[1:-1]:
        directory /= slug(section)
    candidate = directory / f"{slug(title)}.md"
    if not candidate.exists() or generated(candidate):
        return candidate
    suffix = 1
    while True:
        marker = "-imported" if suffix == 1 else f"-imported-{suffix}"
        alternative = candidate.with_name(f"{candidate.stem}{marker}.md")
        if not alternative.exists() or generated(alternative):
            return alternative
        suffix += 1


def clean_body(path: Path) -> str:
    body = path.read_text(encoding="utf-8")
    body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", body, flags=re.S)
    body = re.sub(r"!\[\[([^\]]+)\]\]", r"*첨부 이미지: \1*", body)
    body = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", body)
    body = re.sub(r"\[\[([^\]]+)\]\]", r"\1", body)
    return "\n".join(line.rstrip() for line in body.splitlines()).strip()


def frontmatter(metadata: NoteMetadata, *, math: bool) -> str:
    values = metadata.as_dict() | {"math": math}
    lines = [f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in values.items()]
    return "---\n" + "\n".join(lines) + "\n---\n"


def selected(path: Path, patterns: list[str]) -> bool:
    return not patterns or any(fnmatch.fnmatch(path.as_posix(), pattern) for pattern in patterns)


def main() -> None:
    args = parse_args()
    source = args.source.resolve()
    if not source.is_dir():
        raise SystemExit(f"Source directory not found: {source}")
    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    candidates = []
    for term in SEMESTERS:
        base = source / term.directory
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            relative_source = path.relative_to(source)
            parts = path.relative_to(base).parts
            title = path.stem
            if not selected(relative_source, args.include):
                continue
            if (parts[0].startswith("_") or parts[0] in EXCLUDED_COURSES
                    or any(part in EXCLUDED_PARTS for part in parts)
                    or re.search(r"^Index$|^무제|\(old\)|문제 및 정답|TEACHER$", title, re.I)):
                continue
            candidates.append((term, path, parts, title))
    if args.limit is not None:
        candidates = candidates[:args.limit]

    count = 0
    for term, path, parts, title in candidates:
        body = clean_body(path)
        if not body:
            continue
        course = "알고리즘" if term.directory == "25-여름 알고리즘" else course_name(parts[0])
        sections = tuple(parts[1:-1])
        destination = destination_for(term, parts, title)
        destination.parent.mkdir(parents=True, exist_ok=True)
        metadata = NoteMetadata(
            title=title, semester=term.label, course=course,
            section=" · ".join(sections) or "학습 노트", path_segments=sections,
            source_path=path.relative_to(source).as_posix(),
        )
        math = bool(re.search(r"\$[^$]+\$|\\\(|\\\[", body))
        destination.write_text(frontmatter(metadata, math=math) + "\n" + body + "\n", encoding="utf-8")
        count += 1
        print(f"imported: {path.relative_to(source)} -> {destination.relative_to(ROOT)}")

    print(f"Imported {count} notes. Existing manual documents were preserved.")


if __name__ == "__main__":
    main()
