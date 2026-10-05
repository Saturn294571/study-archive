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

배포 전 검사는 `python3 scripts/deploy.py`, 검증된 `main`의 배포는 `python3 scripts/deploy.py --push`로 실행합니다. 배포 스크립트는 자동 커밋하지 않습니다.

`contents/`는 Git에서 추적하지 않는 원본 보관소입니다. 공개할 정리·필기본은 `_notes/학기/과목/`에 선별하고, Python 도구로 `docs/notes/`에 복사합니다.

```bash
python3 scripts/import_notes.py _notes \
  --include '4-1학부/계량경제학/*' \
  --include-pdf
```

## 저작권과 라이선스

저장소 소유자가 직접 창작한 코드, 스크립트, 사이트 구성 및 독창적인 학습 정리는 [MIT License](LICENSE)를 따릅니다.

다만 강의, YouTube 영상, 서적, 논문, 웹사이트 등 외부 학습 자료에서 가져오거나 인용한 내용은 MIT 라이선스의 적용 대상이 아닙니다. 강의 슬라이드, 사진, 도표, 캡처, 인용문을 포함한 원저작물의 저작권은 인하대학교, 담당 교수자 또는 해당 원저작자에게 있습니다. 외부 자료를 사용한 노트에는 가능한 범위에서 제목, 저작자와 링크 등 출처를 개별적으로 표시합니다.

출처나 권리관계가 불분명한 자료는 MIT 라이선스가 적용된다고 간주하지 않습니다.
