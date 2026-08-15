"""Study Archive의 학기·과목·공개 노트 스키마."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Semester:
    number: str
    label: str
    directory: str


@dataclass(frozen=True)
class Course:
    name: str
    semester: Semester
    area: str = "Course"


@dataclass(frozen=True)
class NoteMetadata:
    title: str
    semester: str
    course: str
    section: str
    path_segments: tuple[str, ...]
    source_path: str
    generated: bool = True

    def as_dict(self) -> dict[str, object]:
        return {
            "title": self.title,
            "semester": self.semester,
            "course": self.course,
            "section": self.section,
            "path_segments": list(self.path_segments),
            "source_path": self.source_path,
            "generated": self.generated,
        }


SEMESTERS = (
    Semester("01", "1학년 · 1학기", "1-1 학부 수업"),
    Semester("02", "1학년 · 2학기", "1-2 학부 수업"),
    Semester("03", "2학년 · 1학기", "2-1 학부 수업"),
    Semester("04", "2학년 · 2학기", "2-2 학부 수업"),
    Semester("05", "2024 · 2학기", "24-2 학부 공부"),
    Semester("06", "3학년 · 1학기", "3-1 학부 공부"),
    Semester("07", "여름 집중 과정", "25-여름 알고리즘"),
    Semester("08", "3학년 · 2학기", "3-2학부"),
    Semester("09", "4학년 · 1학기", "4-1 학부"),
    Semester("10", "4학년 · 2학기", "4-2학기"),
)

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

EXCLUDED_PARTS = frozenset({
    "음성", "강의 음성", "강의 텍스트", "강의자료", "강의 자료", "학습자료", "2_학습자료", "3_기타",
})
EXCLUDED_COURSES = frozenset({"AAPM", "학습효율"})


def course_name(path: Path | str) -> str:
    name = path.name if isinstance(path, Path) else path
    return name.removeprefix("1학기 ").strip()
