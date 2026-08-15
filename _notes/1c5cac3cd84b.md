---
title: "8.VAR"
semester: "4학년 · 2학기"
course: "금융계량경제학"
section: "1_요약 및 정리 · 기말"
math: true
source_path: "_notes/1c5cac3cd84b.md"
---
## 8. Vector Auto-Regression (VAR)

### Idea
- VAR : 여러 sta.(stationary) ts를 **vector로 묶은 AR**
	- scalar AR : $y_t=c+\phi y_{t-1}+e_t$
	- VAR : $Y_t=A_0+A_1Y_{t-1}+\cdots+A_pY_{t-p}+u_t$
- 왜? : 경제 shock는 한 변수에만 X, 여러 시장/부문에 동시 전파
	- ex) 금리 shock -> $\pi_t$, GDP, 실업률, 환율 등 같이 움직임
	- partial eq. 직관($ceteris paribus$) 약함 -> system으로 같이 추정
- VARMA? 가능하지만 복잡 -> 보통 VAR로 approx.
- 주의 : 변수 “막” 넣기 X -> 경제이론/데이터 variation/추정가능성 필요

### Before VAR
- 전제 : VAR 기본형은 sta. 변수 사용
	- unit root test -> non-sta.면 차분/성장률/추세제거
	- 정보손실 걱정? non-sta. 그대로 쓰는 모형 : VECM, UC 등
- 변수 선택 : 같이 움직일 경제적 이유 O?
- lag order : 너무 크게 X
	- 변수 수↑, lag↑ -> parameter 폭증 -> 추정불안정/비경제적 부호
	- 실증 hint : 데이터 graph + theory + IC(AIC/BIC) + robustness

### VAR(p)
- $Y_t=(y_{1t},\cdots,y_{nt})'$
- reduced-form VAR(p)
	- $Y_t=c+A_1Y_{t-1}+\cdots+A_pY_{t-p}+u_t,\quad E(u_t)=0,\quad E(u_tu_t')=\Sigma_u$
- each eq. : 같은 RHS($Y_{t-1},...,Y_{t-p}$) -> eq별 OLS 가능
	- OLS처럼 쉬움; 어려운 건 변수/lag/식별/해석
- 활용
	1. dynamics 파악 : 변수간 lead-lag
	2. forecast : 과거 $Y$로 미래 경로 예측
	3. policy/shock analysis : shock가 각 변수에 퍼지는 경로(IRF)

### Reduced Form vs Structural Form
- foundation : simultaneous eq.(수요/공급처럼 동시결정); 관측은 구조곡선 X, 균형값 O
- reduced form : data로 바로 추정 가능
	- $Y_t=c+\sum_i A_iY_{t-i}+u_t$
	- $u_t$끼리 동시상관 가능 : $\Sigma_u$ non-diagonal
	- reduced coeff. 자체를 causal structural effect로 읽기 X
- structural form : 경제 구조/동시관계 포함
	- $B_0Y_t=b+\sum_i B_iY_{t-i}+\varepsilon_t,\quad E(\varepsilon_t\varepsilon_t')=D$
	- $\varepsilon_t$ : structural shock, 서로 orthogonal하게 해석하고 싶음
- 연결
	- $Y_t=B_0^{-1}b+\sum_i B_0^{-1}B_iY_{t-i}+B_0^{-1}\varepsilon_t$
	- $u_t=B_0^{-1}\varepsilon_t,\quad \Sigma_u=B_0^{-1}D(B_0^{-1})'$
- 핵심 문제 : reduced form은 추정 O, structural shock은 바로 관측 X -> identification 필요

### Normalization / Identification
- 단순 예
	- $\alpha^*y_t=\beta^*X_t+e_t,\quad e_t\sim N(0,\sigma^{*2})$
	- $y_t=\frac{\beta^*}{\alpha^*}X_t+\frac{e_t}{\alpha^*}=\beta X_t+\epsilon_t,\quad Var(\epsilon_t)=\sigma^{*2}/\alpha^{*2}$
- 함의 : $(\alpha^*,\beta^*,\sigma^{*2})$ 여러 조합 -> 같은 $(\beta,\sigma^2)$ 가능
	- structural unknown 3개, reduced-form info 2개 -> 식별불가
- 해결 : 모르는 것 하나를 normalize/restrict
	- $\alpha^*=1$ 또는 $\sigma^{*2}=1$
	- VAR에서도 structural parameter 수 > reduced-form moments -> 제약 필요
- 식별 직관 : 관측되는 건 균형값/축약형 shock; 수요/공급/정책 shock는 구조제약 없이는 분리 X

### Recursive / Cholesky Identification
- 목적 : $\Sigma_u=PP'$인 $P$를 찾아 $u_t=P\varepsilon_t,\quad Var(\varepsilon_t)=I$
- Cholesky : $P$ lower triangular -> ordering으로 동시반응 제약 부여
	- 위에 둔 변수 : 같은 시점에 뒤 변수 shock에 즉시 반응 X
	- 아래 변수 : 앞 변수 shock에 즉시 반응 O
- 함의 : variable ordering = 경제적 가정
	- 순서 바꾸면 IRF 달라질 수 있음 -> theory로 justify 필요
- shock scale : 보통 1 s.d. shock; 보고서용으론 1% shock로 normalize 가능

### IRF(Impulse Response Function)
- IRF : structural shock 1회 발생 -> 각 변수의 미래 반응 경로
	- $\varepsilon_{jt}$ 1단위/1 s.d. shock -> $Y_{t+h}$ 변화
- VAR(1) intuition
	- $Y_t=A_1Y_{t-1}+u_t,\quad u_t=P\varepsilon_t$
	- $h$기 반응 : $\partial Y_{t+h}/\partial\varepsilon_t=A_1^hP$
- 해석 hint
	- 금리↑ shock -> 이론상 $\pi$↓, output↓, unemployment↑ 예상
	- 초기 반응 이상하면? ordering/변수/proxy/lag/sample 문제 의심
	- 실업률 등 slow-moving 변수는 즉시반응 작고 후행 가능
- 장기효과
	- sta. VAR이면 shock 효과는 시간이 지나며 0으로 수렴
	- 정책은 주로 cycle에 영향, trend 영구효과 주장은 별도 이론 필요

### Forecast / FEVD
- Forecast : $\hat Y_{T+h}$를 VAR recursion으로 생성
	- in-sample fit 좋음 ≠ forecast 좋음
	- forecast error가 새 info. update의 핵심
- FEVD(forecast error variance decomposition)
	- $h$기 예측오차 분산 중 각 shock가 설명하는 비중
	- “어떤 shock가 변동을 주로 설명?” 질문

### Practical Checklist
- 1. data plot : 충분한 variation O?
- 2. stationarity check : unit root -> 차분/성장률/추세제거 or VECM/UC
- 3. variables : theory로 묶기; proxy 필요시 검토
- 4. lag order : 너무 크게 X, IC/robustness
- 5. reduced-form VAR estimate : eq별 OLS
- 6. identification : Cholesky/order/restriction 명시
- 7. IRF/FEVD : shock 방향/scale/ordering 해석

### 백지복원
- VAR : $Y_t$ vector의 AR. 경제 shock는 여러 변수에 동시 전파 -> scalar eq.보다 system 필요. 기본 reduced-form은 $Y_t=c+\sum_iA_iY_{t-i}+u_t$, sta. 변수 사용, eq별 OLS 가능. 그러나 $u_t$는 reduced-form shock라 구조적 정책 shock 아님. Structural form $B_0Y_t=b+\sum_iB_iY_{t-i}+\varepsilon_t$에서 $u_t=B_0^{-1}\varepsilon_t$이므로 $\varepsilon_t$ 복원하려면 identification 필요. reduced-form moments만으론 structural parameter 부족 -> normalization/restriction. Cholesky는 ordering으로 동시반응 제약을 둬 $u_t=P\varepsilon_t$ 분해. IRF는 shock 1회가 미래 $Y_{t+h}$에 미치는 경로이며, VAR(1)에선 $A_1^hP$로 복원. 변수/lag/order를 막 넣으면 X; stationarity, theory, data variation 확인.
