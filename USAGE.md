# Study Archive 사용 가이드

이 저장소는 로컬 `contents/`의 원본 중 공개할 Markdown만 골라 MkDocs 사이트로 게시합니다.

## 1. 구조

```text
study-archive/
├── contents/               # 비공개 원본, Git 추적 제외
├── docs/
│   ├── notes/              # 공개 노트: 학기/과목/분류 계층
│   ├── index.md
│   └── about.md
├── scripts/
│   ├── archive_schema.py   # Python 학기·과목·노트 스키마
│   └── import_notes.py     # 안전한 선택 가져오기
├── mkdocs.yml              # 사이트·테마 설정
└── requirements.txt        # Python 패키지
```

MkDocs는 `docs/` 아래의 폴더 구조를 탐색 메뉴와 URL에 그대로 반영합니다. 예를 들어:

```text
docs/notes/4-1-학부/계량경제학/계량중간/4.-가설검정.md
→ /study-archive/notes/4-1-학부/계량경제학/계량중간/4.-가설검정/
```

## 2. 설치와 로컬 미리보기

최초 한 번 가상환경을 만들고 패키지를 설치합니다.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

개발 서버를 실행합니다.

```bash
mkdocs serve
```

`http://127.0.0.1:8000/study-archive/`에서 확인합니다. Markdown이나 설정을 저장하면 자동으로 다시 빌드됩니다. 종료는 `Ctrl+C`입니다.

배포 전 검사는 다음처럼 합니다.

```bash
mkdocs build --strict
```

결과는 `site/`에 생기며 자동 생성물이므로 직접 수정하거나 커밋하지 않습니다.

## 3. 원본에서 선택 가져오기

파일 하나:

```bash
python3 scripts/import_notes.py contents \
  --include '4-1 학부/계량경제학/계량중간/4. 가설검정.md'
```

여러 폴더나 파일:

```bash
python3 scripts/import_notes.py contents \
  --include '24-2 학부 공부/컴퓨터네트워크/**/*.md' \
  --include '4-1 학부/계량경제학/계량중간/*.md' \
  --limit 5
```

- 경로는 `contents/` 기준이며 한글·공백이 있으므로 작은따옴표로 감쌉니다.
- `*`는 한 단계, `**`는 하위 폴더까지 선택합니다.
- `--include`를 생략하면 공개 가능하다고 판단된 Markdown 전체가 대상입니다.
- 강의자료, 학습자료, 강의 음성·전사, 시험 문제·정답, 임시 문서는 기본 제외됩니다.

가져온 문서에는 `generated: true`가 붙습니다. 같은 자동 생성 문서는 다시 실행할 때 갱신합니다. `generated: true`가 없는 수동 문서와 이름이 겹치면 수동 문서는 그대로 두고 새 파일에 `-imported`를 붙입니다. 스크립트는 기존 문서를 일괄 삭제하지 않습니다.

## 4. 노트 직접 작성

`docs/notes/학기/과목/분류/노트.md`를 만들면 됩니다. MkDocs는 front matter 없이도 게시하지만, 과목 정보와 자동 가져오기 구분을 위해 다음 형식을 권장합니다.

```yaml
---
title: "새 노트"
semester: "4학년 · 1학기"
course: "계량경제학"
section: "계량중간"
path_segments: ["계량중간"]
---

# 새 노트
```

수동 문서에는 `generated: true`를 넣지 않습니다. 수식은 `$...$` 또는 `$$...$$`, 코드 블록·표·각주·알림 상자는 Material 확장 문법으로 작성할 수 있습니다.

## 5. Python 스키마 수정

학기와 원본 폴더 대응은 `scripts/archive_schema.py`의 `SEMESTERS`, 과목 분야는 `AREAS`에서 관리합니다.

```python
Semester("11", "새 학기", "contents 안의 새 학기 폴더")
```

```python
AREAS = {
    "새 과목": "Economics",
}
```

제외할 폴더·과목은 같은 파일의 `EXCLUDED_PARTS`, `EXCLUDED_COURSES`에 추가합니다.

## 6. MkDocs 설정

`mkdocs.yml`이 전체 사이트를 제어합니다.

- `site_name`, `site_url`: 사이트 이름과 Pages 주소
- `theme`: Material 테마, 밝은/어두운 화면, 탐색 기능
- `plugins.search`: 한글·영문 검색
- `markdown_extensions`: 수식, 코드, 탭, 체크리스트 등
- `extra_css`, `extra_javascript`: 디자인과 MathJax

현재 `nav`를 고정하지 않았으므로 `docs/` 폴더 구조가 자동 메뉴가 됩니다. 메뉴 순서를 완전히 고정하고 싶을 때만 `mkdocs.yml`에 `nav`를 추가해야 하며, 그 경우 새 문서도 목록에 직접 추가해야 합니다.

## 7. GitHub Pages 배포

`main`에 반영되면 `.github/workflows/pages.yml`이 Python 설치 → MkDocs 빌드 → Pages 배포를 수행합니다. 저장소 **Settings → Pages → Source**는 **GitHub Actions**로 설정합니다.

일반적인 작업 순서:

```bash
git status
git add docs scripts mkdocs.yml requirements.txt .python-version .github/workflows/pages.yml
git commit -m "Add selected study notes"
git push
```

`contents/`, `.venv/`, `site/`는 커밋하지 않습니다. PR 브랜치에서는 병합 후 `main` 배포가 시작됩니다.

## 8. 문제 해결

- 가져오기가 0개면 `--include`가 `contents/` 기준인지, 제외 폴더인지 확인합니다.
- 메뉴 계층이 이상하면 파일이 `docs/notes/학기/과목/...` 아래 있는지 확인합니다.
- 수식이 안 보이면 브라우저 콘솔 오류와 `mkdocs.yml`의 MathJax 스크립트를 확인합니다.
- 배포 실패는 먼저 로컬에서 `mkdocs build --strict`를 실행한 뒤 Actions 로그를 확인합니다.
