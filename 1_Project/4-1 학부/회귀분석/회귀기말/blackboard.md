# 🎓 회귀분석 기말고사 "교수님 피셜" 출제 포인트 (from 14-1 Audio)

**🚨 최우선 확인 사항**
*   **시험 일시**: 12월 8일 (월) 09:00 - 10:15 (75분)
*   **시험 장소**: 5서 360호
*   **준비물**: 계산기 (필수)
*   **배점**: 총 120점 만점 (`Q1-4: 60점`, `Q5: 35점`, `Q6: 25점`)
*   **특이사항**: 기출문제(족보)는 12/4(목) 수업 시간에 풀이해줌.

---

## ✅ 시험 범위 및 핵심 포인트 (Chapter-by-Chapter)

| 챕터 | 주제 | 출제 여부 / 포인트 | 비고 |
| :--- | :--- | :--- | :--- |
| **Ch 9** | **F-test & 가설검정** | **[필수]** $F$ 통계량 계산, 가설($H_0$) 수립 | Q5 계산 문제와 직결 |
| **Ch 10** | **Diagnostics** | **[이론]** 잔차 종류, 가정, 영향력(Influence) 지표 정의 | Cook's D, DFFITS 등 정의 숙지 |
| **Ch 11** | **Leverage** | **[이론]** **Leverage ($h_{ii}$) 집중** | **(제외)** Residual Plot 해석, 다중비교 |
| **Ch 12** | **Dummy & Interaction** | **[필수]** Qualitative 변수 해석, 교호작용 | Q6 계산 문제의 핵심 (꼼꼼히 볼 것) |
| **Ch 13** | **WLS & Delta Method** | **❌ 통째로 제외** | (Lec 11-2 내용 중 WLS 부분 skip) |
| **Ch 14** | **Autocorrelation** | **[포함]** 시계열 관련성 때문에 포함 | Durbin-Watson 등 기본 개념 |
| **Ch 15** | **Model Selection** | **[이론/중요]** AIC, BIC, 선택 절차/기준 | 실제 데이터 분석 프로세스 강조 |
| **Ch 16** | **Multicollinearity** | **[부분 포함]** 공선성(Collinearity)까지 | **(제외)** PCR(주성분회귀)의 SVD 심화 |

---

## 🚀 전략적 학습 가이드 (Study Strategy)

### 1. **버릴 것 과감히 버리기 (Time Save)**
   - **Ch 13 제외**: 가중최소자승법(WLS), 델타 메소드(Delta Method) 공부 X.
   - **그래프 해석 제외**: Residual Plot 보고 "이게 무슨 문제냐" 맞추는 문제 안 나옴.
   - **PCR 심화 제외**: SVD 분해 등 복잡한 수식 제외.

### 2. **이론/서술형 (Q1-4, 60점) 대비**
   - **Ch 10 & 11**: Leverage와 Influence Measure들의 **정의(Definition)**와 **차이점** 명확히 암기.
     - *Leverage ($h_{ii}$)* vs *Cook's D*
   - **Ch 15 & 16**:
     - **AIC vs BIC**: 페널티 항의 차이 ($\ln(n)$ vs $2$), 언제 무엇을 쓰나? (BIC는 True model, AIC는 Prediction).
     - **Ridge vs Lasso**: 제약식 형태($L_2$ vs $L_1$), 변수 선택 가능 여부(Lasso 가능).
     - **Bias-Variance Tradeoff**: MSE 분해 ($Var + Bias^2$), 그림 해석.

### 3. **계산형 (Q5, Q6, 60점) 마무리**
   - **Q5 (F-test)**: 기계적으로 풀 수 있도록 연습 (이미 마스터함).
   - **Q6 (Dummy/Interaction)**: "가장 단순한 모델" 찾기, 범주형 변수 해석 연습.
   - **⚠️ 함정 주의 (from Lec 14-2)**:
     - 더미변수가 $k$개 카테고리를 위해 $k-1$개($E_1, E_2$) 필요한데, 모델에 $E_1$만 넣으면?
     - $\rightarrow$ $E_2$(디젤)와 Base(휘발유)가 **섞여서 구분 불가**. "휘발유 대비 효과" 해석 불가능.
     - "정보가 없는 변수는 모델이 구분 못함" 명심.

---

## 📝 백지 복습(Recall) 체크리스트

- [ ] **Leverage**: $h_{ii}$의 범위, Hat matrix의 Trace ($=p$ or $p+1$).
- [ ] **Influence**: Cook's distance 식의 의미 (베타 변화량), DFFITS 정의.
- [ ] **Model Selection**: AIC, BIC 공식, Forward/Backward/Stepwise 설명.
- [ ] **Regularization**: Ridge($\lambda \sum \beta^2$), Lasso($\lambda \sum |\beta|$) 식 쓰기, 기하학적 의미(원 vs 마름모).
- [ ] **Multicollinearity**: VIF 정의 ($1/(1-R_j^2)$), 10 이상이면 문제.

---

*(이전 내용은 저장되었습니다. 새로운 내용 암기에 집중하세요!)*

## ➕ Durbin-Watson Statistic (Q&A)
*   **Formula**: $$d = \frac{\sum_{t=2}^n (e_t - e_{t-1})^2}{\sum_{t=1}^n e_t^2}$$
*   **$e_t$란?**: $t$ 시점의 **잔차 (Residual)** ($= y_t - \hat{y}_t$).
*   **Note**:
    *   **분자**: $t=2$부터 $n$까지 (이전 시점 $t-1$이 있어야 하므로).
    *   **분모**: $t=1$부터 $n$까지 (전체 잔차 제곱합).
