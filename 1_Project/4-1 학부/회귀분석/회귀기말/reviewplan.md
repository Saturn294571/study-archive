# 회귀분석 기말고사 초단기 완성 전략 (D-1)

**목표:** 12월 7일(토) 자정까지 전 범위(Ch 9~16, Ch 13 제외) 1회독 및 핵심 유형 마스터
**전략:** "선택과 집중"
## 📅 타임라인 (Time-Blocked Schedule) - D-Day (12/7 일)

### 1. [오전: 이론 압축 및 암기] (07:00 ~ 12:00)
*   **전략**: 정의(Definition)와 성질(Properties) 위주로 암기하여 서술형 60점 확보.
*   **Ch 10~11 (Diagnostics & Leverage)**:
    *   [x] **Hat Matrix ($H$)**: $h_{ii}$ (Leverage) 정의 및 성질. (Ch 11 핵심)
    *   [x] **Influence Measures**: Cook's D, DFFITS, DFBETAS 정의 및 차이점(모델 전체 vs 예측값 vs 계수).
*   **Ch 14 (Autocorrelation)**:
    *   [x] **AR(1) Model**: $\epsilon_t = \rho \epsilon_{t-1} + w_t$ 식 이해.
    *   [x] **Durbin-Watson**: $d \approx 2(1-\hat{\rho})$ 식과 판정 기준($d<2$ 양의상관).
*   **Ch 16 (Multicollinearity)**:
    *   [x] **VIF (분산팽창지수)**: $1/(1-R_j^2)$ 식과 기준($>10$) 암기.
    *   *Note: PCR, SVD 이후 심화 내용은 제외.*

### 2. [오후: 계산형 문제 집중 공략] (13:00 ~ 17:00)
*   **전략**: **기출/과제 $\to$ 음성강의(14-2) $\to$ 실전 모의고사** 순서로 60점 완벽 확보.
*   **Step 1: 기출 풀이**:
    *   [ ] `기말 계산관련 출제문제.pdf` (Q5, Q6 유형) 직접 풀기.
    *   [ ] `HW2_2025-1.pdf` 풀고 템플릿 체화.
*   **Step 2: 개념 점검**:
    *   [ ] `회귀분석/음성/회귀14-1음성.txt` (기말 범위 및 출제 포인트 가이드 청취).
*   **Step 3: 실전 모의고사**:
    *   [ ] **AI 생성 유사 문제 3세트** 풀기 (F-test 변형, 더미 해석 심화).
    *   *Action:* 기출 다 풀면 AI에게 "유사 문제 내줘" 요청하기.

### 3. [저녁: 편향-분산 & 파이널 인출] (18:00 ~ 22:00)
*   **Ch 16 (Penalized Regression)**:
    *   [ ] **Bias-Variance Tradeoff**: $MSE = Var + Bias^2$ 분해 식 쓰고 의미 설명.
    *   [ ] **Ridge vs Lasso**: 제약식($L_2$ vs $L_1$) 차이 및 축소추정량의 목적.
*   **Final 백지 테스트**:
    *   `blackboard.md`의 핵심 질문들에 대해 막힘없이 답할 수 있는지 최종 점검.
    *   계산 공식(F, VIF, AIC, Adjusted $R^2$) 최종 암기 확인.

### 4. [밤: 최종 약점 보완] (22:00 ~ )
*   기출/과제 문제 중 틀렸던 계산 문제 다시 풀어보기.
*   Ch 13(전체) 및 Ch 11(그림), Ch 16(심화) 제외 확인.
