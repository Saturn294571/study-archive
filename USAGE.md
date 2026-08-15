# Study Archive 사용 가이드

이 저장소는 `contents`에 보관한 원본 자료 중 공개할 Markdown만 골라 Jekyll 사이트로 게시합니다.

## 1. 폴더 구조

```text
study-archive/
├── contents/          # 원본 학부 자료, Git 추적 제외
├── _notes/            # 사이트에 공개할 노트
├── _data/             # 학기·과목 목록
├── _layouts/          # 페이지 HTML 틀
├── _includes/         # 헤더·푸터 같은 공통 HTML
├── assets/            # CSS와 JavaScript
├── scripts/           # 노트 가져오기 도구
├── _config.yml        # Jekyll 및 사이트 설정
└── .github/workflows/ # GitHub Pages 자동 배포
```

`contents`에는 강의자료와 개인 기록을 보관할 수 있지만 GitHub에는 올라가지 않습니다. 실제 공개 범위는 `_notes`에 들어간 파일로 결정됩니다.

## 2. 원본에서 노트 가져오기

저장소 루트에서 `scripts/import_notes.py`를 실행합니다.

### 과목 또는 폴더 하나 가져오기

```bash
python3 scripts/import_notes.py contents \
  --include '4-1 학부/계량경제학/계량중간/*.md'
```

### 여러 폴더 가져오기

```bash
python3 scripts/import_notes.py contents \
  --include '4-1 학부/계량경제학/계량중간/*.md' \
  --include '4-1 학부/회귀분석/회귀기말/필기/*.md'
```

`--include`에는 `contents` 기준 상대 경로와 glob 패턴을 사용합니다.

- `*.md`: 해당 폴더 바로 아래의 Markdown
- `**/*.md`: 하위 폴더까지 포함한 모든 Markdown
- `4. 가설검정.md`: 파일 하나만 선택
- `--limit 3`: 조건에 맞는 문서 중 최대 3개만 가져오기

예:

```bash
python3 scripts/import_notes.py contents \
  --include '24-2 학부 공부/컴퓨터네트워크/**/*.md' \
  --limit 3
```

`--include`를 생략하면 공개 가능한 Markdown 전체를 가져오므로, 처음에는 선택 경로를 명시하는 편이 안전합니다.

### 자동 제외 항목

가져오기 도구는 다음 경로와 문서를 기본 제외합니다.

- 강의자료·학습자료
- 강의 음성·음성 전사·강의 텍스트
- 시험 문제 및 정답
- `3_기타`, `AAPM`, `학습효율`
- 빈 문서와 일부 임시·중복 문서

가져온 파일에는 `generated: true`가 추가됩니다. 같은 자동 생성 파일을 다시 가져오면 갱신하지만, 수동 파일은 삭제하거나 덮어쓰지 않습니다. 이름이 겹치면 자동 파일에 `-imported`가 붙습니다.

## 3. 생성되는 계층과 URL

원본:

```text
contents/4-1 학부/계량경제학/계량중간/4. 가설검정.md
```

가져온 노트:

```text
_notes/4-1-학부/계량경제학/계량중간/4.-가설검정.md
```

게시 URL:

```text
/study-archive/notes/4-1-학부/계량경제학/계량중간/4.-가설검정/
```

Jekyll 컬렉션의 `:path` permalink를 사용하므로 `_notes` 아래의 폴더 구조가 URL에도 반영됩니다.

## 4. 노트 직접 작성하기

`_notes/학기/과목/분류/노트명.md`에 Markdown 파일을 만들고 YAML front matter를 작성합니다.

```yaml
---
title: "가설검정"
semester: "4학년 · 1학기"
course: "계량경제학"
section: "계량중간"
path_segments: ["계량중간"]
math: true
---

# 가설검정

본문을 작성합니다.
```

필드 의미:

- `title`: 페이지와 과목 목록에 표시할 제목
- `semester`: `_data/semesters.yml`의 학기명과 정확히 일치
- `course`: `_data/courses.yml`의 과목명과 정확히 일치
- `section`: 과목 목록에 표시할 세부 경로
- `path_segments`: 세부 폴더 목록
- `math`: MathJax 수식이 필요하면 `true`

수동 노트에는 `generated: true`를 넣지 않습니다. 그래야 가져오기 도구가 수동 파일로 인식하고 보존합니다.

## 5. Jekyll 사용법

### Jekyll이 하는 일

Jekyll은 Markdown과 HTML 템플릿을 결합해 정적 사이트를 만듭니다.

- `_config.yml`: 사이트 주소, 컬렉션, URL 형식 설정
- `_notes`: `notes` 컬렉션의 문서
- `_layouts/default.html`: 전체 페이지의 기본 HTML
- `_layouts/note.html`: 노트 상세 페이지
- `courses.html`: 학기·과목·노트 목록
- `assets/css/main.css`: 디자인
- `assets/js/main.js`: 검색, 다크 모드, 목차

설정을 바꾼 뒤에는 개발 서버를 재시작해야 반영되는 경우가 있습니다.

### 로컬 실행

Ruby와 Bundler가 설치되어 있어야 합니다.

```bash
bundle install
bundle exec jekyll serve
```

브라우저에서 다음 주소를 엽니다.

```text
http://localhost:4000/study-archive/
```

파일 변경을 자동 감지하지 못하면:

```bash
bundle exec jekyll serve --livereload
```

### 배포 전 빌드 확인

```bash
bundle exec jekyll build
```

성공하면 결과물이 `_site/`에 생성됩니다. `_site`는 자동 생성 폴더이므로 직접 수정하거나 커밋하지 않습니다.

### 자주 수정하는 설정

`_config.yml`:

```yaml
title: Study Archive
url: "https://saturn294571.github.io"
baseurl: "/study-archive"

collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- 저장소 이름이 바뀌면 `baseurl`도 수정합니다.
- 사용자 사이트 저장소가 아니라 프로젝트 사이트이므로 링크에는 `baseurl`이 필요합니다.
- 템플릿에서는 직접 경로를 붙이기보다 Liquid의 `relative_url` 필터를 사용합니다.

예:

```liquid
{{ '/courses/' | relative_url }}
```

## 6. 학기와 과목 관리

가져오기 도구를 실행하면 `contents`의 폴더를 읽어 다음 파일을 갱신합니다.

- `_data/semesters.yml`
- `_data/courses.yml`

새로운 학기 폴더를 인식시키려면 `scripts/import_notes.py`의 `SEMESTERS`에 항목을 추가합니다.

```python
{"number": "11", "label": "새 학기", "directory": "새 학기 폴더"}
```

과목 영역을 지정하려면 같은 파일의 `AREAS`에 추가합니다.

```python
"새 과목": "Economics"
```

## 7. GitHub Pages 배포

`main`에 변경이 반영되면 `.github/workflows/pages.yml`이 자동으로 다음 작업을 수행합니다.

1. 저장소 checkout
2. Jekyll 빌드
3. Pages artifact 업로드
4. GitHub Pages 배포

진행 상태는 저장소의 **Actions → Deploy Jekyll site to Pages**에서 확인합니다.

일반적인 게시 순서:

```bash
git status
git add _notes _data
git commit -m "Add selected course notes"
git push
```

PR 브랜치라면 PR을 `main`에 병합한 후 실제 사이트가 갱신됩니다.

## 8. 문제 해결

### 과목 페이지에 노트가 안 보임

- front matter의 `semester`와 `course`가 `_data` 값과 같은지 확인합니다.
- 파일이 `_notes` 아래에 있는지 확인합니다.
- front matter 시작과 끝에 `---`가 있는지 확인합니다.

### 스타일이나 링크가 깨짐

- 템플릿 링크에 `relative_url`이 적용됐는지 확인합니다.
- `_config.yml`의 `baseurl`이 `/study-archive`인지 확인합니다.

### 가져오기가 0개로 끝남

- `--include` 경로가 `contents` 기준인지 확인합니다.
- 공백과 한글이 있는 패턴은 작은따옴표로 감쌉니다.
- 선택한 파일이 자동 제외 폴더에 있는지 확인합니다.

### 배포가 실패함

로컬에서 먼저 `bundle exec jekyll build`를 실행하고, GitHub Actions 실패 단계의 로그를 확인합니다.
