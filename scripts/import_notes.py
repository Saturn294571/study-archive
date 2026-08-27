#!/usr/bin/env python3
"""선택한 원본 Markdown을 MkDocs 문서로 안전하게 가져온다."""

import argparse
import fnmatch
import json
import re
import shutil
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote

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
    parser.add_argument(
        "--summary-only", action="store_true",
        help="각 과목의 1_요약 및 정리 폴더만 가져옵니다.",
    )
    parser.add_argument(
        "--flatten", action="store_true",
        help="정리 폴더의 Markdown과 PDF를 과목 폴더 바로 아래에 배치합니다.",
    )
    parser.add_argument(
        "--include-pdf", action="store_true",
        help="선택된 정리 폴더 안의 PDF도 함께 가져옵니다.",
    )
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


def course_directory(term: Semester, course: str) -> Path:
    return NOTES_DIR / slug(term.output_directory) / slug(course)


def destination_for(term: Semester, parts: tuple[str, ...], title: str, *, flatten: bool) -> Path:
    course = "알고리즘" if term.directory == "25-여름 알고리즘" else course_name(parts[0])
    directory = course_directory(term, course)
    if not flatten:
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


def find_local_asset(reference: str, note: Path, course_root: Path) -> Path | None:
    decoded = unquote(reference.split("#", 1)[0]).strip().strip("<>")
    if not decoded or re.match(r"^(?:https?:|data:|mailto:)", decoded, re.I):
        return None
    direct = (note.parent / decoded).resolve()
    if direct.is_file():
        return direct
    name = Path(decoded).name
    matches = sorted(path for path in course_root.rglob(name) if path.is_file())
    return matches[0] if matches else None


def copy_image(reference: str, note: Path, course_root: Path, destination: Path) -> str | None:
    source = find_local_asset(reference, note, course_root)
    if source is None or source.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
        return None
    image_dir = destination.parent / "img"
    image_dir.mkdir(parents=True, exist_ok=True)
    target = image_dir / source.name
    if target.exists() and target.read_bytes() != source.read_bytes():
        target = image_dir / f"{source.stem}-{slug(str(source.parent.relative_to(course_root)))}{source.suffix.lower()}"
    shutil.copy2(source, target)
    return f"img/{quote(target.name)}"


def clean_body(path: Path, course_root: Path, destination: Path) -> str:
    body = path.read_text(encoding="utf-8")
    body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", body, flags=re.S)

    def replace_obsidian_image(match: re.Match[str]) -> str:
        reference = match.group(1).split("|", 1)[0]
        copied = copy_image(reference, path, course_root, destination)
        return f"![]({copied})" if copied else f"*이미지 파일을 찾을 수 없음: {reference}*"

    def replace_markdown_image(match: re.Match[str]) -> str:
        alt, reference = match.group(1), match.group(2)
        copied = copy_image(reference, path, course_root, destination)
        return f"![{alt}]({copied})" if copied else match.group(0)

    def replace_markdown_link(match: re.Match[str]) -> str:
        label, reference = match.group(1), match.group(2)
        decoded = unquote(reference).strip().strip("<>")
        if re.match(r"^(?:https?:|mailto:|#)", decoded, re.I):
            return match.group(0)
        source = find_local_asset(reference, path, course_root)
        if source and source.suffix.lower() == ".pdf" and "1_요약 및 정리" in source.parts:
            return f"[{label}]({quote(source.name)})"
        return f"{label} *(비공개 원자료)*"

    body = re.sub(r"!\[\[([^\]]+)\]\]", replace_obsidian_image, body)
    body = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_markdown_image, body)
    body = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", replace_markdown_link, body)
    body = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", body)
    body = re.sub(r"\[\[([^\]]+)\]\]", r"\1", body)
    return "\n".join(line.rstrip() for line in body.splitlines()).strip()


def frontmatter(metadata: NoteMetadata, *, math: bool) -> str:
    values = metadata.as_dict() | {"math": math}
    lines = [f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in values.items()]
    return "---\n" + "\n".join(lines) + "\n---\n"


def selected(path: Path, patterns: list[str]) -> bool:
    return not patterns or any(fnmatch.fnmatch(path.as_posix(), pattern) for pattern in patterns)


def is_summary(parts: tuple[str, ...]) -> bool:
    return len(parts) >= 3 and parts[1] == "1_요약 및 정리"


def write_course_index(
    term: Semester,
    course: str,
    notes: list[tuple[str, Path]],
    pdfs: list[Path],
) -> None:
    directory = course_directory(term, course)
    index = directory / "index.md"
    if index.exists() and not generated(index):
        print(f"preserved manual index: {index.relative_to(ROOT)}")
        return
    lines = [
        "---", f"title: {json.dumps(course, ensure_ascii=False)}", "generated: true", "---", "",
        f"# {course}", "", f"{term.label} 정리·필기본입니다.", "", "## 노트", "",
    ]
    lines.extend(f"- [{title}]({quote(path.name)})" for title, path in sorted(notes))
    if pdfs:
        lines.extend(["", "## PDF 정리본", ""])
        lines.extend(f"- [{path.stem}]({quote(path.name)})" for path in sorted(pdfs))
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
            if args.summary_only and not is_summary(parts):
                continue
            if (parts[0].startswith("_") or parts[0] in EXCLUDED_COURSES
                    or any(part in EXCLUDED_PARTS for part in parts)
                    or re.search(r"^Index$|^무제|\(old\)|문제 및 정답|TEACHER$|^CHEATSHEET$", title, re.I)):
                continue
            candidates.append((term, path, parts, title))
    if args.limit is not None:
        candidates = candidates[:args.limit]

    imported_notes: dict[tuple[Semester, str], list[tuple[str, Path]]] = {}
    imported_pdfs: dict[tuple[Semester, str], list[Path]] = {}
    count = 0
    for term, path, parts, title in candidates:
        course = "알고리즘" if term.directory == "25-여름 알고리즘" else course_name(parts[0])
        destination = destination_for(term, parts, title, flatten=args.flatten)
        body = clean_body(path, source / term.directory / parts[0], destination)
        if not body:
            continue
        sections = tuple(parts[2:-1] if args.summary_only else parts[1:-1])
        destination.parent.mkdir(parents=True, exist_ok=True)
        metadata = NoteMetadata(
            title=title, semester=term.label, course=course,
            section=" · ".join(sections) or "학습 노트", path_segments=sections,
            source_path=path.relative_to(source).as_posix(),
        )
        math = bool(re.search(r"\$[^$]+\$|\\\(|\\\[", body))
        destination.write_text(frontmatter(metadata, math=math) + "\n" + body + "\n", encoding="utf-8")
        imported_notes.setdefault((term, course), []).append((title, destination))
        count += 1
        print(f"imported: {path.relative_to(source)} -> {destination.relative_to(ROOT)}")

    pdf_count = 0
    if args.include_pdf:
        for term in SEMESTERS:
            base = source / term.directory
            if not base.is_dir():
                continue
            for path in sorted(base.rglob("*.pdf")):
                relative_source = path.relative_to(source)
                parts = path.relative_to(base).parts
                if not selected(relative_source, args.include):
                    continue
                if args.summary_only and not is_summary(parts):
                    continue
                if parts[0].startswith("_") or parts[0] in EXCLUDED_COURSES:
                    continue
                course = "알고리즘" if term.directory == "25-여름 알고리즘" else course_name(parts[0])
                directory = course_directory(term, course)
                if not args.flatten:
                    for section in parts[1:-1]:
                        directory /= slug(section)
                directory.mkdir(parents=True, exist_ok=True)
                destination = directory / path.name
                shutil.copy2(path, destination)
                imported_pdfs.setdefault((term, course), []).append(destination)
                pdf_count += 1
                print(f"imported PDF: {path.relative_to(source)} -> {destination.relative_to(ROOT)}")

    for key in sorted(set(imported_notes) | set(imported_pdfs), key=lambda item: item[0].number + item[1]):
        write_course_index(key[0], key[1], imported_notes.get(key, []), imported_pdfs.get(key, []))

    print(f"Imported {count} notes and {pdf_count} PDFs. Existing manual documents were preserved.")


if __name__ == "__main__":
    main()
