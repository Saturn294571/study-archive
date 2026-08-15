---
title: "12. 이분산성"
semester: "4학년 · 1학기"
course: "계량경제학"
section: "계량기말"
math: true
source_path: "_notes/ae7daca5ac13.md"
---
### 1. Gauss-Markov Theorem
- $Y_i=\beta_1+\beta_2X_{2i}+\cdots+\beta_kX_{ki}+e_i$에 대해 고전적 가정
	1) $E(e_i)=0,\quad \forall i$
	2) $E(e_i^2)=\sigma^2,\quad \forall i$
	3) $E(e_ie_j)=0,\quad\forall i\neq j$
	4) $X : \text{ non-stochastic}$
	5) $\text{rank}(X)=k\text{ : no exact multicollinearity}$
- Gauss-Markov Theorem : 고전적 가정이 성립O -> 선형인 불편추정량 중 OLS가 BLUE.
### 2. 이분산이 있는 단순회귀모형
###### 이분산성
- 정의 : 오차항$e_i$의 분산$\sigma^2$이 관측치에 따라 달라지는 상황
	- 고전적 가정중 동분산 $\text{Var}(e_i) = \sigma^2, \sigma^2 I$ 가정이 성립 X
	- 시간 : $\sigma_t^2$,     개별관측치에 따라 : $\sigma_i^2$
- OLS 추정량의 성질 변화
	- 불편성 : 이분산성 있어도 $E(\hat{\beta}_2^\text{(OLS)})={\beta}_2^\text{(OLS)}$
		- hint : $E()$ 정의식 대입, $E(e_i)=0$
	- 효율성 : but, 더이상 BLUE중 best, 즉 최소 분산 추정량 X
		- $\text{if } e_i\sim N(0,\sigma_i^2)\implies Var(\hat{\beta}_2^\text{(OLS)})=(\frac{1}{\sum X_{2i}^2})^2\sum_{i=1}^n(\sum X_{2i}^2)\sigma_i^2$ - inefficient
			-  hint : $Var()$ 정의식 대입, $E(e_i^2)=\sigma^2_i$, $E(e_ie_j)=0$
		- $\text{if } e_i\sim N(0,\sigma^2)\implies Var(\hat{\beta}_2^\text{(OLS)})=\frac{\sigma^2}{\sum X_{2i}^2}$
		- 목표 : 고전적 가정 성립토록 모형 변환
- 가설검정시 문제점
	- $\text{(t-val)} = \frac{\hat{\beta}_2}{\sqrt{\hat{\text{Var}}(\hat{\beta}_2)}}\to$분모(var) $\uparrow\uparrow$, 따라서 $H_0$를 기각하기 어렵;
	  유의한 변수임에도 유의X 라고 잘못 결론 가능
###### GLS(Generalized Least Squares)
- 정의 : 이분산 O? -> 고전적 가정이 성립토록 변환
- $Y_i=\beta_2X_{2i}+e_i, e_i\sim(0,\sigma_i^2)\to \tilde{Y}_i=\beta_2\tilde{X}_{2i}+\tilde{e}_i;$     hint : $\tilde{\theta}_i=\frac{\theta_i}{\sigma_i}$
	- $\hat{\beta}_2=\frac{\sum\tilde{X}_{2i}\tilde{Y}_i}{\sum\tilde{X}_{2i}^2};\quad E(\hat{\beta}_2)=\beta_2;\quad Var(\hat{\beta}_2)=\frac{\sigma^2}{\sum \tilde{X}_{2i}^2}$
- 이분산의 분포(패턴)을 모를때 : 여전히 OLS사용
	- 단, 가설검정시 제대로된 분산 사용
	- FGLS(Feasible GLS) : unknown $\sigma^2$? : $\to\hat{\sigma}^2$
### 3. 이분산이 있는 다중회귀모형
###### pop eq. : $Y=X\beta+e,\quad e\sim(0_{(n\times1)},\sigma^2\Omega_{(n\times n)})$
- $Var(e)=E(ee')=\sigma^2\Omega\neq\sigma^2I_n$
- $$\Omega = \begin{pmatrix}
Var(e_1)&Cov(e_2,e_1)& \cdots & Cov(e_n,e_1) \\
Cov(e_1,e_2) & Var(e_2) &  \cdots \\
\vdots & & \ddots
\end{pmatrix}$$
- 자기상관/이분산의 유형 : (1) : 이분산, (2) : 자기상관, (3) : 이분산+자기상관
$$
\text{(1) : }
\sigma^2\begin{pmatrix}
k_1 & &  (0)\\
& \ddots & \\
(0) & & k_3
\end{pmatrix}
\quad
\text{(2) : }
\sigma^2\begin{pmatrix}
1 & &  (\neq0)\\
& \ddots & \\
(\neq0) & & 1
\end{pmatrix}
\quad
\text{(3) : }
\sigma^2\begin{pmatrix}
k_1 & &  (\neq0)\\
& \ddots & \\
(\neq0) & & k_n
\end{pmatrix}
$$
###### 모수의 추정량 ($\sigma^2\Omega$를 무시한 OLS)
- $\hat{\beta}^{(OLS)}=(X'X)^{-1}X'Y$
- $E(\hat{\beta}^{(OLS)})=\beta$ ;    hint : Y에 pop. eq. 대입, $E(e)=0$
- $Var(\hat{\beta}^{(OLS)})=\sigma^2(X'X)^{-1}X'\Omega X(X'X)^{-1}$ : Sandwich formula
	- hint : var() 정의 대입, $E(\hat{\beta}^{(OLS)})=\beta$, $E(ee')=\sigma^2\Omega$
- \*\* 참고 : 파이썬/통계 패키지에서 이분산/자기상관 고려 X? -> $\sigma^2\Omega$무시, $\sigma^2I$로 계산;
	- -> t-val 등 모두 wrong
###### GLS 추정량 (Cholesky Decomposition) : $\Omega^{-1}=C'C$
- pop. eq. 양변에 C 곱함 : $CY=CX\beta+Ce;\implies \tilde{Y}=\tilde{X}\beta+\tilde{e}$
	- $e\sim N(0,\sigma^2\Omega)\to \tilde{e}\sim N(0,\sigma^2I)$;    hint : $C'C=\Omega^{-1}$
- 모수 추정량
	- $\hat{\beta}^{(GLS)}=(X'\Omega^{-1}X)^{-1}(X'\Omega^{-1}Y)$;    hint : $C'C=\Omega^{-1},\tilde{\theta}$ 정의 대입
	- $E(\hat{\beta}^{(GLS)})=\beta$;    hint : E() 정의 대입, $E(e)=0$
	- $Var(\hat{\beta}^{(GLS)})=\sigma^2(X'\Omega^{-1}X)^{-1}$;     hint : var() 정의, $\Omega^{-1}$정의
###### 요약 및 비교 ($Y=X\beta+e, \quad e\sim N(0,\sigma^2\Omega$)

| OLS                                                                     | GLS                                                       |
| ----------------------------------------------------------------------- | --------------------------------------------------------- |
| $\hat{\beta}^{(OLS)}=(X'X)^{-1}X'Y$                                     | $\hat{\beta}^{(GLS)}=(X'\Omega^{-1}X)^{-1}X'\Omega^{-1}Y$ |
| $E(\hat{\beta}^{(OLS)})=\beta$                                          | $E(\hat{\beta}^{(GLS)})=\beta$                            |
| $Var(\hat{\beta}^{(OLS)})$<br>$=\sigma^2(X'X)^{-1}X'\Omega X(X'X)^{-1}$ | $Var(\hat{\beta}^{(GLS)})=\sigma^2(X'\Omega X)^{-1}$      |
| BLUE X                                                                  | BLUE O                                                    |
- $Var(\hat{\beta}^{(OLS)})\ge Var(\hat{\beta}^{(GLS)})$
- GLS : known $\Omega$
	- FGLS : unknown $\Omega$, able to estimate
	- OLS : known $\Omega$, cannot estimate
