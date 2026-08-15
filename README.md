# Study Archive

학부 과정에서 작성한 경제학·통계학·컴퓨터과학 노트를 정리한 Jekyll 사이트입니다.

## 로컬 실행

```bash
bundle install
bundle exec jekyll serve
```

사이트는 GitHub Actions를 통해 GitHub Pages에 배포됩니다. 원본 백업에서 노트를 다시 가져올 때는 아래 명령을 사용합니다.

```bash
python3 scripts/import_notes.py "/path/to/undergraduate-backup"
```

가져오기 스크립트는 학부 과목의 Markdown 노트만 복사하며 음성 전사, 중복 초안, 시험 정답과 기타 바이너리는 제외합니다.
