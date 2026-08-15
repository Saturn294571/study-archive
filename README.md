# Study Archive

학부 과정에서 작성한 경제학·통계학·컴퓨터과학 노트를 정리한 MkDocs Material 사이트입니다.

## 로컬 실행

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

브라우저에서 `http://127.0.0.1:8000/study-archive/`를 엽니다. 자세한 관리·가져오기·배포 방법은 [USAGE.md](USAGE.md)를 참고하세요.

`contents/`는 Git에서 추적하지 않는 원본 보관소입니다. 공개할 문서만 Python 도구로 `docs/notes/`에 복사합니다.

```bash
python3 scripts/import_notes.py contents \
  --include '4-1 학부/계량경제학/계량중간/*.md'
```
