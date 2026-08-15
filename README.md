# Study Archive

학부 과정에서 작성한 경제학·통계학·컴퓨터과학 노트를 정리한 Jekyll 사이트입니다.

## 로컬 실행

```bash
bundle install
bundle exec jekyll serve
```

사이트는 GitHub Actions를 통해 GitHub Pages에 배포됩니다. `contents`는 Git에서 추적하지 않는 원본 보관소입니다. 선택한 노트만 가져오려면 상대 경로 glob을 지정합니다.

```bash
python3 scripts/import_notes.py contents \
  --include '4-1 학부/계량경제학/계량중간/*.md'
```

`--include`는 여러 번 지정할 수 있습니다. 생략하면 공개 가능한 Markdown 전체를 가져옵니다. 강의자료·음성·강의 전사·시험 정답은 기본 제외되며, 기존 `_notes`를 초기화하지 않습니다. `generated: true`가 없는 수동 노트와 이름이 겹치면 수동 노트를 보존하고 가져온 파일에 `-imported`를 붙입니다.
