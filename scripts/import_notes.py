#!/usr/bin/env python3
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

source = Path(sys.argv[1])
root = Path(__file__).resolve().parent.parent
notes_dir = root / "_notes"
data_dir = root / "_data"
shutil.rmtree(notes_dir, ignore_errors=True)
notes_dir.mkdir(parents=True)
data_dir.mkdir(parents=True, exist_ok=True)

semesters = [
    {"number": "01", "label": "1학년 · 1학기", "directory": "1-1 학부 수업"},
    {"number": "02", "label": "1학년 · 2학기", "directory": "1-2 학부 수업"},
    {"number": "03", "label": "2024 · 2학기", "directory": "24-2 학부 공부"},
    {"number": "04", "label": "3학년 · 1학기", "directory": "3-1 학부 공부"},
    {"number": "05", "label": "여름 집중 과정", "directory": "25-여름 알고리즘"},
    {"number": "06", "label": "3학년 · 2학기", "directory": "3-2학부"},
    {"number": "07", "label": "4학년 · 1학기", "directory": "4-1 학부"},
    {"number": "08", "label": "4학년 · 2학기", "directory": "4-2학기"},
]
areas = {
    "글로벌경제론": "Economics", "사회보장론": "Economics", "금융투자론": "Economics",
    "기술경제학": "Economics", "후생경제학": "Economics", "계량경제학": "Econometrics",
    "회귀분석": "Statistics", "전산통계": "Data Science", "데이터마이닝": "Data Science",
    "선형대수학": "Mathematics", "데이터베이스": "Computer Science", "컴퓨터네트워크": "Computer Science",
    "프로그램언어": "Computer Science", "자료구조론": "Computer Science", "컴퓨터시스템": "Computer Science",
    "컴퓨팅사고와 데이터분석 기초": "Data Science", "알고리즘": "Computer Science",
    "경제수학": "Mathematics", "경제원론": "Economics", "경제원론 2": "Economics",
    "금융계량경제학": "Econometrics", "회계원리": "Accounting",
    "소프트웨어와 인공지능 이해 및 응용": "Computer Science",
    "통계학": "Statistics", "미래사회와 소프트웨어": "Computer Science",
    "대학 기초 영어": "Liberal Arts", "의사소통 영어 [중급]": "Liberal Arts",
    "문제해결을 위한 글쓰기": "Liberal Arts", "크로스오버 1": "Liberal Arts",
    "크로스오버 2": "Liberal Arts", "프로네시스 세미나": "Liberal Arts",
    "나눔 프로젝트": "Project", "실전 스타트업": "Entrepreneurship",
    "인하특강 [기업가정신과 창업]": "Entrepreneurship",
}

def course_name(name):
    return re.sub(r"^1학기\s+", "", name)

courses = []
for term in semesters:
    term_dir = source / term["directory"]
    if not term_dir.is_dir():
        continue
    names = sorted(
        course_name(path.name) for path in term_dir.iterdir()
        if path.is_dir() and not path.name.startswith("_") and path.name not in {"AAPM", "학습효율"}
    )
    if term["directory"] == "25-여름 알고리즘":
        names = ["알고리즘"]
    courses.extend({"name": name, "semester": term["label"], "area": areas.get(name, "Course")} for name in names)

candidates = []
for term in semesters:
    base = source / term["directory"]
    if not base.is_dir():
        continue
    for path in sorted(base.rglob("*.md")):
        relative = path.relative_to(base)
        parts = relative.parts
        course = "알고리즘" if term["directory"] == "25-여름 알고리즘" else course_name(parts[0])
        title = path.stem
        if (parts[0].startswith("_") or parts[0] in {"AAPM", "학습효율"} or "음성" in parts
                or "강의 텍스트" in parts or "3_기타" in parts
                or re.search(r"^Index$|^무제|\(old\)|숙제|문제 및 정답|TEACHER$", title, re.I)):
            continue
        section_parts = [part for part in parts[1:-1] if part != "필기"]
        candidates.append({
            "path": path, "title": title, "course": course, "semester": term["label"],
            "section": " · ".join(section_parts) or "학습 노트", "raw": str(relative), "in_notes": "필기" in parts,
        })

groups = {}
for item in candidates:
    groups.setdefault((item["semester"], item["course"], item["title"]), []).append(item)
for versions in groups.values():
    item = min(versions, key=lambda version: (version["in_notes"], len(version["raw"])))
    body = item["path"].read_text(encoding="utf-8")
    body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", body, flags=re.S)
    body = re.sub(r"!\[\[([^\]]+)\]\]", r"*첨부 이미지: \1*", body)
    body = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", body)
    body = re.sub(r"\[\[([^\]]+)\]\]", r"\1", body)
    body = "\n".join(line.rstrip() for line in body.splitlines()).rstrip() + "\n"
    if not body.strip():
        continue
    digest = hashlib.sha1(f'{item["semester"]}/{item["course"]}/{item["raw"]}'.encode()).hexdigest()[:12]
    filename = f"{digest}.md"
    metadata = {
        "title": item["title"], "semester": item["semester"], "course": item["course"],
        "section": item["section"], "math": bool(re.search(r"\$[^$]+\$|\\\(|\\\[", body)),
        "source_path": f"_notes/{filename}",
    }
    frontmatter = "---\n" + "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in metadata.items()) + "\n---\n"
    (notes_dir / filename).write_text(frontmatter + body, encoding="utf-8")

def write_yaml(path, items):
    lines = []
    for item in items:
        first = True
        for key, value in item.items():
            lines.append(f"{'- ' if first else '  '}{key}: {json.dumps(value, ensure_ascii=False)}")
            first = False
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

write_yaml(data_dir / "semesters.yml", [{key: value for key, value in term.items() if key != "directory"} for term in semesters])
write_yaml(data_dir / "courses.yml", courses)
print(f"Imported {len(list(notes_dir.glob('*.md')))} notes across {len(courses)} courses.")
