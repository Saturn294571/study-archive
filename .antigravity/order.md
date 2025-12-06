# 회귀분석 기말고사 대비 작업 지침 및 명령 (Order)

## 1. 시험 개요 및 범위
*   **과목:** 회귀분석 (Regression Analysis)
*   **시험 일시:** 12월 7일 09:00
*   **목표:** A4 2단 레이아웃의 `회귀기말총정리.md`를 완벽하게 정리하고, 이를 바탕으로 백지 테스트(Blank Test)를 수행하여 이론 및 계산 문제 완벽 대비.

### 포함 범위 (Scope)
*   **Ch 9:** Multiple Regression Inference (F-test Types I, II, III).
*   **Ch 10:** Diagnostics (Residuals, Influence Measures, Hat Matrix).
*   **Ch 11:** Diagnostics II (**Leverage 만 포함**; Residual Plot, Multiple Comparison 제외).
*   **Ch 12:** Qualitative Variables & Interaction (Calculations 중요).
*   **Ch 14:** Correlated Errors (F-test for constrained coefficients, Full vs Reduced models).
*   **Ch 15:** Model Selection (AIC, BIC, Cp, Stepwise - **중요**).
*   **Ch 16:** Penalized Regression (Collinearity, Ridge, Lasso 개념, Bias-Variance Tradeoff; PCR, SVD 제외).

### 제외 범위 (Excluded)
*   **Ch 13:** 전체 제외 (Delta Method, WLS).
*   **Ch 11:** Residual Plot, Multiple Comparison.
*   **Ch 16:** PCR, SVD, 복잡한 수리적 유도.

### 배점 및 유형
*   **이론 (60점):** Ch 9, 10, 11, 15, 16 (Short answer/Theory).
*   **계산 (60점):** Q5(35점), Q6(25점). Ch 12 (Dummy/Interaction) 및 Ch 14 (Hypothesis Testing) 위주.
*   **핵심 팁:** "복잡하게 모델링하지 말고 가장 심플한 모델을 골라라/가정을 세워라."

## 2. 문서 작업 지침 (`회귀기말총정리.md`)

### 파일 형식 및 스타일
*   **파일:** `g:\내 드라이브\study-archive\1_Project\4-1 학부\회귀분석\회귀기말\필기\회귀기말총정리.md`
*   **테마:** Marp `a4-light` 테마 사용 (`paginate: true`, `math: mathjax`).
*   **레이아웃:** A4 세로, 2단(2-column) 레이아웃.
    *   커스텀 CSS를 파일 상단 `<style>` 블록에 포함하여 2단 적용.
    *   글자 크기 및 여백 최적화 (가독성 유지하며 정보 밀도 높임).
*   **내용 구성:**
    *   핵심 아이디어, 주요 공식, 'Hint' 섹션 위주.
    *   불필요한 긴 유도 과정이나 지엽적인 예제는 생략 (요청 시에만 추가).

### 수식 (LaTeX) 포맷팅 규칙
*   **환경:** `\begin{aligned}` 등 복잡한 환경 사용 금지.
*   **구분자:** **모든 수식은 인라인 수식 기호 `$` 사용.**
    *   이유: `$$` (Display Math) 사용 시 2단 레이아웃에서 글자가 지나치게 작아지는 문제 발생.
    *   긴 수식은 `$` 내부에서 줄바꿈이 되지 않으므로, 시각적으로 적절한 위치에서 `$`를 닫고 다시 `$`를 여는 방식으로 수동 줄바꿈 유도.
    *   *예시:* `$긴 수식 앞부분 = ...$ (줄바꿈) $+ 뒷부분 ...$`

### 이미지 경로 규칙
*   **형식:** 상대 경로(Relative Path) 및 URL 인코딩 사용.
*   **경로 패턴:** `![](../../기타/image/Pasted%20image%20...png)`
*   **주의:** Windows 경로 역슬래시(`\`) 사용 금지, 공백은 반드시 `%20`으로 치환.

## 3. 학습 및 테스트 워크플로우 (AI 역할)

### 역할 (Persona)
*   **Gemini Prep Manager (Socratic Edition):** 정답을 바로 알려주기보다 질문을 통해 사용자가 스스로 인출하도록 유도.

### 단계별 프로세스
1.  **자료 분석:** 녹음 본(`음성/*.txt`) 및 필기 노트 분석하여 내용 파악.
2.  **백지 테스트 (Blank Test):**
    *   챕터별(또는 주제별) 핵심 토픽 제시.
    *   사용자가 인출(입력)한 내용 확인.
    *   피드백: 누락된 핵심 키워드, 틀린 개념 교정, 심화 질문(Hint) 제공.

## 4. 현재 상태 및 우선순위
1.  **테스트 전환:** 문서 작업 완료 승인 후, 즉시 Ch 9부터 백지 테스트 모드 진입.
