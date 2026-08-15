#!/usr/bin/env python3
"""Import selected Markdown notes while preserving manual files and hierarchy."""
import argparse
import fnmatch
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = ROOT / "_notes"
DATA_DIR = ROOT / "_data"

SEMESTERS = [
    {"number": "01", "label": "1학년 · 1학기", "directory": "1-1 학부 수업"},
    {"number": "02", "label": "1학년 · 2학기", "directory": "1-2 학부 수업"},
    {"number": "03", "label": "2학년 · 1학기", "directory": "2-1 학부 수업"},
    {"number": "04", "label": "2학년 · 2학기", "directory": "2-2 학부 수업"},
    {"number": "05", "label": "2024 · 2학기", "directory": "24-2 학부 공부"},
    {"number": "06", "label": "3학년 · 1학기", "directory": "3-1 학부 공부"},
    {"number": "07", "label": "여름 집중 과정", "directory": "25-여름 알고리즘"},
    {"number": "08", "label": "3학년 · 2학기", "directory": "3-2학부"},
    {"number": "09", "label": "4학년 · 1학기", "directory": "4-1 학부"},
    {"number": "10", "label": "4학년 · 2학기", "directory": "4-2학기"},
]

AREAS = {
    "경제수학": "Mathematics", "선형대수학": "Mathematics", "통계학": "Statistics",
    "회귀분석": "Statistics", "경제원론": "Economics", "경제원론 2": "Economics",
    "거시경제학": "Economics", "미시경제학": "Economics", "경제학사": "Economics",
    "금융경제학": "Economics", "글로벌경제론": "Economics", "사회보장론": "Economics",
    "금융투자론": "Economics", "기술경제학": "Economics", "후생경제학": "Economics",
    "계량경제학": "Econometrics", "금융계량경제학": "Econometrics", "회계원리": "Accounting",
    "전산통계": "Data Science", "데이터마이닝": "Data Science", "데이터베이스": "Computer Science",
    "컴퓨터네트워크": "Computer Science", "프로그램언어": "Computer Science",
    "자료구조론": "Computer Science", "컴퓨터시스템": "Computer Science", "알고리즘": "Computer Science",
    "컴퓨터공학 입문": "Computer Science", "미래사회와 소프트웨어": "Computer Science",
    "소프트웨어와 인공지능 이해 및 응용": "Computer Science",
}

EXCLUDED_PARTS = {
    "음성", "강의 음성", "강의 텍스트", "강의자료", "강의 자료", "학습자료", "2_학습자료", "3_기타",
}
EXCLUDED_COURSES = {"AAPM", "학습효율"}


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="contents 디렉터리")
    parser.add_argument(
        "--include", action="append", default=[], metavar="GLOB",
        help="가져올 상대 경로 glob. 여러 번 지정 가능하며, 생략하면 공개 가능한 Markdown 전체를 가져옵니다.",
    )
    parser.add_argument("--limit", type=int, help="가져올 최대 문서 수")
    return parser.parse_args()


def slug(value):
    value = unicodedata.normalize("NFC", value).strip()
    value = re.sub(r"^1학기\s+", "", value)
    value = re.sub(r"[^\w.-]+", "-", value, flags=re.UNICODE)
    return value.strip("-._") or "note"


def course_name(value):
    return re.sub(r"^1학기\s+", "", value).strip()


def has_generated_marker(path):
    if not path.is_file():
        return False
    head = path.read_text(encoding="utf-8", errors="ignore")[:1000]
    return bool(re.search(r"^generated:\s*true\s*$", head, re.MULTILINE))


def destination_for(parts, term, title):
    course = "알고리즘" if term["directory"] == "25-여름 알고리즘" else course_name(parts[0])
    directory = NOTES_DIR / slug(term["directory"]) / slug(course)
    for section in parts[1:-1]:
        directory /= slug(section)
    candidate = directory / f"{slug(title)}.md"
    if not candidate.exists() or has_generated_marker(candidate):
        return candidate
    imported = candidate.with_name(f"{candidate.stem}-imported.md")
    counter = 2
    while imported.exists() and not has_generated_marker(imported):
        imported = candidate.with_name(f"{candidate.stem}-imported-{counter}.md")
        counter += 1
    return imported


def clean_body(path):
    body = path.read_text(encoding="utf-8")
    body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", body, flags=re.S)
    body = re.sub(r"!\[\[([^\]]+)\]\]", r"*첨부 이미지: \1*", body)
    body = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", body)
    body = re.sub(r"\[\[([^\]]+)\]\]", r"\1", body)
    return "\n".join(line.rstrip() for line in body.splitlines()).strip()


def write_yaml(path, items):
    lines = []
    for item in items:
        for index, (key, value) in enumerate(item.items()):
            lines.append(f"{'- ' if index == 0 else '  '}{key}: {json.dumps(value, ensure_ascii=False)}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_catalog(source):
    courses = []
    for term in SEMESTERS:
        term_dir = source / term["directory"]
        if not term_dir.is_dir():
            continue
        names = sorted(
            course_name(path.name) for path in term_dir.iterdir()
            if path.is_dir() and not path.name.startswith("_") and path.name not in EXCLUDED_COURSES
        )
        if term["directory"] == "25-여름 알고리즘":
            names = ["알고리즘"]
        courses.extend({"name": name, "semester": term["label"], "area": AREAS.get(name, "Course")} for name in names)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    write_yaml(DATA_DIR / "semesters.yml", [{k: v for k, v in term.items() if k != "directory"} for term in SEMESTERS])
    write_yaml(DATA_DIR / "courses.yml", courses)
    return courses


def selected(relative, patterns):
    return not patterns or any(fnmatch.fnmatch(relative.as_posix(), pattern) for pattern in patterns)


def main():
    args = parse_args()
    source = args.source.resolve()
    if not source.is_dir():
        raise SystemExit(f"Source directory not found: {source}")
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    courses = build_catalog(source)
    candidates = []
    for term in SEMESTERS:
        base = source / term["directory"]
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            relative_source = path.relative_to(source)
            relative_term = path.relative_to(base)
            parts = relative_term.parts
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

    imported = 0
    for term, path, parts, title in candidates:
        body = clean_body(path)
        if not body:
            continue
        course = "알고리즘" if term["directory"] == "25-여름 알고리즘" else course_name(parts[0])
        sections = list(parts[1:-1])
        destination = destination_for(parts, term, title)
        destination.parent.mkdir(parents=True, exist_ok=True)
        relative_destination = destination.relative_to(ROOT).as_posix()
        metadata = {
            "title": title, "semester": term["label"], "course": course,
            "section": " · ".join(sections) or "학습 노트", "path_segments": sections,
            "math": bool(re.search(r"\$[^$]+\$|\\\(|\\\[", body)),
            "generated": True, "source_path": relative_destination,
        }
        frontmatter = "---\n" + "\n".join(
            f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in metadata.items()
        ) + "\n---\n"
        destination.write_text(frontmatter + body + "\n", encoding="utf-8")
        imported += 1
        print(f"imported: {path.relative_to(source)} -> {destination.relative_to(ROOT)}")
    print(f"Imported {imported} selected notes across a {len(courses)}-course catalog. Manual notes were preserved.")


if __name__ == "__main__":
    main()
