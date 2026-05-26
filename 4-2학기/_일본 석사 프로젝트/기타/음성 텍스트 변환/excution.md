- 실행
```powershell
python "g:\내 드라이브\private_archive\1_Project\4-2학기\_일본 석사 프로젝트\기타\whisper.py" "D:\recordings\finance_week5.m4a" --mode finance --model small
```
```powershell
python "g:\내 드라이브\private_archive\1_Project\4-2학기\_일본 석사 프로젝트\기타\whisper.py" "D:\recordings\accounting_week5.m4a" --mode accounting --model small
```

- 폴더 전체 처리
```powershell
python "G:\내 드라이브\private_archive\1_Project\4-2학기\_일본 석사 프로젝트\기타\음성 텍스트 변환\whisper.py" "C:\Users\shehd\OneDrive\문서\소리 녹음\금계" --mode finance
```
- 패키지 설치
```powershell
python -m pip install -U openai-whisper
```