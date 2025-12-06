# 회귀분석 기말고사 초단기 완성 전략 (D-1)

**목표:** 12월 7일(토) 자정까지 전 범위(Ch 9~16, Ch 13 제외) 1회독 및 핵심 유형 마스터
**전략:** "선택과 집중" - 교수님 강조 사항(계산 문제, 정의 등) 위주로 공략

---

## 📅 타임라인 (Time-Blocked Schedule)

### 1. 오늘 밤: 기초 및 진단 (12/6 금 22:00 ~ 12/7 토 02:00)
*   **목표:** F-검정의 논리 이해 및 모형 진단 지표 암기
*   **Chapter 9 (Multiple Regression 3)**:
    *   [ ] **F-test (Reduced vs Full Model)**: 가설($H_0$) 설정에 따른 Reduced Model 식 세우기. 자유도($df_R - df_F$) 계산 확실히.
    *   [ ] **일반 선형 가설 (General Linear Hypothesis)**: $C\beta = h$ 행렬 표현법 익히기. (시험 출제 포인트)
*   **Chapter 10 (Diagnostics)**:
    *   [ ] **Studentized Residuals**: 내적(Internal) vs 외적(External/R-student) 차이점 (분모에 $s$냐 $s_{(i)}$냐).
    *   [ ] **영향점 진단**: Cook's D, DFFITS, DFBETAS 식의 구성 요소(크기 vs 영향력)와 기준값 대략적 이해.
    *   *Tip: 잔차 그림(Residual Plot)과 다중비교는 제외됨.*

### 2. 내일 오전: 계산 집중 공략 (12/7 토 09:00 ~ 12:00)
*   **목표:** **Ch 12 계산 문제** 완벽 대비 (출제 가능성 매우 높음)
*   **Chapter 11 (Leverage)**:
    *   [ ] **Leverage($h_{ii}$)의 성질 ($1/n \le h_{ii} \le 1$, $\sum h_{ii} = p+1$ 등). Hat matrix 의미.
*   **Chapter 12 (Qualitative Variables)**: **[★핵심 승부처]**
    *   [ ] **Dummy Variable Coding**: 범주 수 $k$개면 변수는 $k-1$개 (Baseline 설정 주의).
    *   [ ] **Interactions**: 기울기가 달라지는 모형 ($X \times D$) 해석.
    *   [ ] **One-way ANOVA와 회귀 모형의 관계** 수식 연결.

### 3. 내일 오후: 심화 주제 정리 (12/7 토 13:00 ~ 16:00)
*   **목표:** 시계열 오차의 특성과 모형 선택 기준 암기
*   **Chapter 14 (Correlated Errors)**:
    *   [ ] **AR(1) Model**: $\rho$의 의미, 오차항의 분산/공분산 구조.
    *   [ ] **Durbin-Watson 통계량**: $d \approx 2(1-\hat{\rho})$ 식과 범위(0~4) 해석 (2 근처=무상관).
*   **Chapter 15 (Model Selection)**:
    *   [ ] **Selection Criteria**: $R^2$ vs $Adj-R^2$, **Mallow's $C_p$** (값이 $p$ 근처여야 좋음), AIC/BIC 정의.
    *   [ ] **Search Strategy**: Forward, Backward, Stepwise 절차의 차이.

### 4. 내일 저녁: 개념 및 총정리 (12/7 토 17:00 ~ 20:00)
*   **Chapter 16 (Penalized Regression)**:
    *   [ ] **개념 위주**: Ridge ($L_2$) vs Lasso ($L_1$) 차이.
    *   [ ] **Bias-Variance Tradeoff**: 람다($\lambda$)가 커질수록 Bias 증가, Variance 감소 그래프 이미지화.
    *   *Tip: 심화 알고리즘(Elastic Net 등)은 제외됨.*

### 5. 파이널 백지 복습 (12/7 토 21:00 ~ 24:00)
*   **Action**: `회귀기말final.md`를 펴고 주요 키워드만 보고 수식/내용을 적을 수 있는지 테스트.
*   **Checklist**:
    1.  Full/Reduced Model F-통계량 식 적을 수 있는가?
    2.  $C\beta=h$ 행렬 만들 수 있는가?
    3.  Internal/External Studentized Residual 식 구별 가능한가?
    4.  Dummy 변수 모델 해석 가능한가? (이 그룹의 평균은? 저 그룹의 기울기는?)
    5.  Durbin-Watson 식과 판정 기준은?
    6.  Ridge/Lasso의 목적함수 형태 차이는?

---
> **마지막 팁:** 포기하지 말 것. 계산 문제는 Ch 12에서 나올 확률이 크니 예제(Salary, 힐 레이스 등)의 계수 해석을 꼼꼼히 볼 것.
