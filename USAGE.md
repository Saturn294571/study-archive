# Study Archive 사용법

## 기본 구조

- `contents/`: 원본 학부 자료. Git에 올리지 않습니다.
- `_notes/`: GitHub Pages에 공개할 Markdown 노트입니다.
- `_data/`: 학기와 과목 목록입니다.

## 원본에서 노트 가져오기

저장소 루트에서 가져올 경로를 지정합니다.

```bash
python3 scripts/import_notes.py contents \
  --include '4-1 학부/계량경제학/계량중간/*.md'
```

여러 경로를 가져오려면 `--include`를 반복합니다.

```bash
python3 scripts/import_notes.py contents \
  --include '4-1 학부/계량경제학/계량중간/*.md' \
  --include '4-1 학부/회귀분석/회귀기말/필기/*.md'
```

가져온 노트는 다음처럼 원본 계층을 유지합니다.

```text
_notes/4-1-학부/계량경제학/계량중간/4.-가설검정.md
```

가져오기 스크립트는 기존 수동 노트를 삭제하지 않습니다. 강의자료, 음성, 강의 전사와 시험 정답은 기본적으로 제외합니다.

## 노트 직접 추가하기

`_notes/학기/과목/분류/노트명.md`에 파일을 만들고 맨 위에 정보를 작성합니다.

```yaml
---
title: "노트 제목"
semester: "4학년 · 1학기"
course: "계량경제학"
section: "계량중간"
math: true
---
```

수식이 없으면 `math: false`로 설정합니다. 수동 노트에는 `generated: true`를 넣지 않습니다.

## 로컬에서 확인하기

Ruby와 Bundler가 설치되어 있다면:

```bash
bundle install
bundle exec jekyll serve
```

브라우저에서 `http://localhost:4000/study-archive/`를 엽니다.

## 게시하기

변경할 파일만 확인한 뒤 커밋하고 푸시합니다.

```bash
git status
git add _notes _data
git commit -m "Add selected course notes"
git push
```

`main`에 반영되면 GitHub Actions가 Pages를 자동으로 다시 배포합니다.
