---
marp: true
theme: a4-light
paginate: true
math: mathjax

---

<style>
/* Custom 2-Column Layout based on User Requirements */
section {
  width: 210mm;
  height: 297mm;
  font-size: 13px;
  padding: 15mm;
  box-sizing: border-box;
  background-color: white;
  color: #24292e;
  
  column-count: 2;
  column-gap: 10mm;
  column-rule: 1px solid #e1e4e8;
  
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.4;
  display: block;
}

h1, h2 {
  column-span: all;
}

h1 {
  font-size: 22px;
  border-bottom: 2px solid #24292e;
  padding-bottom: 8px;
  margin-top: 0;
  margin-bottom: 10px;
}

h2 {
  font-size: 18px;
  border-bottom: 1px solid #eaecef;
  padding-bottom: 5px;
  color: #0366d6;
  margin-top: 0;
  margin-bottom: 10px;
}

h3 {
  font-size: 15px;
  font-weight: 600;
  margin-top: 15px;
  margin-bottom: 5px;
  color: #005cc5;
  background-color: #f1f8ff;
  padding: 3px 6px;
  border-radius: 3px;
  break-after: avoid;
}

h4, h5, h6 {
  font-size: 14px;
  margin-top: 10px;
  margin-bottom: 5px;
  font-weight: 600;
  color: #24292e;
}

ul, ol {
  padding-left: 20px;
  margin-top: 0;
  margin-bottom: 8px;
}

li {
  margin-bottom: 2px;
}

p {
  margin-top: 0;
  margin-bottom: 8px;
}

code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
  background-color: rgba(27,31,35,0.05);
  padding: 2px 4px;
  border-radius: 3px;
  font-size: 85%;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 8px auto;
  border: 1px solid #dee2e6;
}

strong {
  font-weight: 600;
  color: #d73a49;
}

/* Hint highlighting */
strong:contains("hint") {
  color: #22863a;
}
</style>

# 계량경제학 기말고사 대비 총정리 자료
## (R-square, Dummy var., 이분산성, 자기상관, 내생성)
## 10. R-square (final)
### 3. $R^2$와 F-test
- 모집단 회귀식 : $Y_i = \beta_0+\beta_1X_{i1}+\cdots+\beta_pX_{ip}+\epsilon_i$
- $H_0 : \forall \beta_j = 0; j\in\{1, \cdots , p\}$    $H_1 : \exists \beta_j \neq 0; j\in\{1, \cdots , p\}$
	- full model(unrestricted) : $Y_i = \hat{\beta_0}+\hat{\beta_1} X_{i1}+\cdots+\hat{\beta_p}X_{ip}+\hat{\epsilon_i}$
	- restricted model : $Y_i = \hat{\beta_0^*}+\hat{\epsilon_i^*}$
- $H_0$가 참이라면, $\sum \hat{\epsilon}_i^2 \simeq \sum \hat{\epsilon^*}_i^2\implies R^2\simeq0$;     참이 아니라면, $R^2\gg0\to \text{Reject }H_0$
	- 검정통계량? : 불가능. ($\because$ 분포를 모르기 때문)
- (F-value) : $\frac{(\sum\hat{\epsilon^*}_i^2-\sum\hat{\epsilon}_i^2)/(k-1)}{\sum\hat{\epsilon}_i^2/(n-k)}=\frac{(SSE_{R}-SSE_{F})/P_R}{SSE_F(n-P_F)}$
$\sim F(P_R,n-P_F-1)=F(k-1,n-k)$
	- (J는 제약조건의 수, k는 모수의 수, P는 독립변수의 수)
- 제약된 회귀식에서 $E(\hat{\beta_0})=\beta_0=\bar{Y}$ 이므로, $\sum\hat{\epsilon^*}^2_i=\sum (Y_i-\bar{Y})^2=S_{yy}$
	- 이를 F-value 식에 대입하고 분자, 분모를 $S_{yy}$로 나누면, 
    $$\text{F-val} = \frac{(\frac{\sum (Y_i-\bar{Y})^2}{\sum (Y_i-\bar{Y})^2}-\frac{\sum (Y_i-\hat{Y}_i)^2}{\sum (Y_i-\bar{Y})^2})/(k-1)}{\frac{\sum (Y_i-\hat{Y}_i)^2}{\sum (Y_i-\bar{Y})^2}/(n-k)}$$
    $$= \frac{(1-\frac{SSE}{SST})/(k-1)}{\frac{SSE}{SST}/(n-k)} = \frac{R^2/(k-1)}{1-R^2/(n-k)}$$

---

## 11. Topics(Dummy var.)
### 1. 중요 변수를 빠트리고 추정시?
- Pop. reg. E.Q. $\Rightarrow y_i=\beta_1 x_{1i}+\beta_2 x_{2i}+\epsilon_i$     but, Smaple reg E.Q. $\Rightarrow \hat{\beta_2 }x_{2i}+\hat{\epsilon_i}$
- 다중회귀가 불가능한 상태에서 $\hat{\beta_1}$을 추가로 추정시
	1) reg. $X_2\to Y\Rightarrow \text{residual : } Y^*$
	2) reg. $X_2\to X_1\Rightarrow \text{residual : }X_1^*$
	3) reg. $X_1^*\to Y^* \Rightarrow \hat{\beta_1}$
	- $$y_i = \hat{\beta_1}x_{1i}+\epsilon_i\implies \hat{\beta_1}=\frac{\sum \tilde{x}_{1i}\tilde{y}_i}{\sum \tilde{x}_{1i}^2}$$
	  : 다중회귀가 불가능 하더라도 3번의 단순회귀식으로 $\hat{\beta_1}$추정 (증)
	- Let $M_2 = I-X_2(X_2'X_2)^{-1}X_2'$
    $\to \underbrace{M_2Y}_{1)}=\underbrace{M_2X_1}_{2)}\hat{\beta_1}+\underbrace{M_2\hat{\epsilon}}_{3)}$ 
- 각 변수가 선형 결합 관계에 있을 경우
	- $x_{1i}=\delta x_{2i}+\epsilon_i\implies \sum \tilde{x}_{1i}^2 > \sum \tilde{x}_{2i}^2\quad (\because \text{잔차})$의 관계, $\hat{\delta}=\frac{\partial x_{1i}}{\partial x_{2i}}$ 성립
- $X_{2i}$(중요변수)를 빠트리고 추정시?
	- (추정식) : $Y_i=\hat{\beta_1}X_{1i}+\hat{\epsilon_i}$        (pop. E.Q.) : $Y_i={\beta_1}X_{1i}+{\beta_2}X_{2i}+{\epsilon_i}$
	- $\hat{\beta}_1=\frac{\sum \tilde{x}_{1i}\tilde{y}_i}{\sum \tilde{x}_{1i}^2}$에서 $Y_i$에 pop EQ 대입. 그리고 $E(\cdot)$를 씌우면,
		- $E(\hat{\beta_1})=\beta_1+[E(\frac{\beta_2\sum \tilde{x}_{1i}\tilde{x}_{2i}}{\sum \tilde{x}_{1i}^2})\neq0]$
        $+[E(\frac{\sum \tilde{x}_{1i}\epsilon_i}{\sum \tilde{x}_{1i}^2})=0]\quad \therefore E(\hat{\beta_1})\neq\beta_1$
		- 따라서  중요 변수를 빠트린 OLS 추정식은 불편추정치가 아니다.

#### Frisch-warsh-Lovell theorm (Partitioned Regression)
- OLS : 
$Y = X\hat{\beta} + \hat{e},\quad \hat{e} = M_X$$(M_X= I_n - X (X'X)^{-1}X')$
- (기하학적 의미) OLS, FOC : $\quad X'\hat{e} = {0}$
- ![](../../기타/image/Pasted%20image%2020251107133336.png)
	- $\to X \perp \hat{e} \Rightarrow X'\hat{e} = 0$
- SSE의 기하적 의미를 M2 행렬에 적용했을 때 :
- ![](../../기타/image/Pasted%20image%2020251107133857.png)
	- $Y = \underbrace{X_1 \hat{\beta}_1 + X_2 \hat{\beta}_2}_{=\hat{Y}} + \hat{e}$
	- $X_1 \perp \hat{e} \implies X_1' \hat{e} = 0$;    $X_2 \perp \hat{e} \implies X_2' \hat{e} = 0$
- $M_2 Y = M_2 X_1 \hat{\beta}_1 + M_2 X_2 \hat{\beta}_2 + M_2 \hat{e}$ $\rightarrow Y^* = X_1^* \hat{\beta}_1 + \hat{e}$
	- $\hat{\beta}_1 = ({X_1^*}' X_1^*)^{-1} {X_1^*}' Y^*$

### 2. 불필요 변수를 추가하고 추정시?
- ex1) Pop E.Q. : $y_i = \beta_1 x_{1i} + \epsilon_i$    Sample E.Q. : $y_i = \hat{\beta}_0 + \hat{\beta}_1 x_{1i} + \hat{\epsilon}_i$
	1) $E(\hat{\beta_0})=\beta_0?\,\to$ OK 
		- \* $y_i$에 pop eq 식 대입
	2) $Var(\hat{\beta_1}) = \sigma^2/\sum\tilde{x}_i^2$
		- $Var(\hat{\beta_1})>Var(\hat{\beta}_1^{(T)})\to$ 효율적 추정량 X    ($\hat{\beta}_1^{(T)}$는 제대로된 추정치)
- ex2) (행렬) Pop E.Q : $\beta_1x_{1i}+\epsilon_i$    Sample E.Q. : $y_i=\hat{\beta}_1 x_{1i}+\hat{\beta}_2 x_{2i}+\hat{\epsilon}_i$
	 1) 불편성? :  
     $\hat{\beta}_1^*=({X_1^*}'X_1^*)^{-1}{X_1^*}'Y^*\Rightarrow E(\hat{\beta}_1^*)$$=\beta_1+(E[(\cdots)\epsilon]=0)$
		- \* $(M_2)^2=M_2,\quad X :$ non-stochastic 
	2) 효율적? : $Var(\hat{\beta_1})=({X_1^*}'X_1^*)^{-1}\sigma^2=\frac{\sigma^2}{\sum x_{1i}^*}$
		- $x_{1i}\text{ vs }x_{1i}^*$ : $x_{1i}=\hat{\delta_2}x_{2i}+x_{1i}^*\implies Var(\hat{\beta_1})>Var(\hat{\beta_1^*})$
---
### 3. Dummy variable
- 0 or 1의 값을 취하는 변수
- cross sectional data -> 그룹간/상태별 차이 (교육,성,국가,인종 등)
- time seris data -> 어떠한 이벤트 전후 (군대,출산,IMF 등)
#### 예1) 임금결정식 : 
$Y_i=\underbrace{\beta_1}_{\text{기본급?}}+\underbrace{\beta_2X_{2i}}_{\text{교육}}+\underbrace{\beta_3X_{3i}}_{\text{근속연수}}+\underbrace{\beta_4X_{4i}}_{\text{성별}}+e_i$
$i\in\{1,\cdots,n\}$
- $let : n=1000, n_M=400, n_F=600$
	- male : $y_i=\beta_0^M+\beta_1^Mx_{1i}+\beta_2^Mx_{2i}+\epsilon_i^M$
    $\overset{\text{OLS}}{\implies}\hat{\beta_0^M},\hat{\beta_1^M},\hat{\beta_2^M}$
	- female : $y_i=\beta_0^F+\beta_1^Fx_{1i}+\beta_2^Fx_{2i}+\epsilon_i^M$
    $\overset{\text{OLS}}{\implies}\hat{\beta_0^F},\hat{\beta_1^F},\hat{\beta_2^F}$
0) 귀무가설과 대립가설 : 
$H_0 : \forall \beta_k^M=\beta_k^F,\quad H_1 : \exists \beta_k^M\neq\beta_k^F$
$(k\in\{0,1,2\})$
	- Dummy var로 나타낸 임금식, female과 male의 식을 합치자 :
	  $y_i=(\beta_0+\alpha_0D_i)+(\beta_1+\alpha_1D_i)x_{1i}$
      $+(\beta_2+\alpha_2D_i)x_{2i}+e_i$
	  $i\in\{1,\cdots,n\}$
      $\text{if M}\to D_i=0,\text{else if F}\to D_i=1$
		- $\text{if }D_i=0\to(\text{male E.Q.})$$\text{else if }D_i=1\to(\text{female E.Q.})$
1) 수정된 귀무가설/대립가설 : 
$H_0 : \forall \alpha_k=0, H_1 : \exists \alpha_k\neq0$
$(k\in\{0,1,2\})$
2) F-테스트 :
	- Full. : $y_i=(\hat{\beta_0}+\hat{\alpha_0})+\cdots+\epsilon_i\implies\sum \hat{\epsilon}_i^2$
	- Res. : $y_i=\hat{\beta_0}+\cdots+\epsilon_i^*\implies\sum (\hat{\epsilon_i^*})^2$
	- $(F-val)=\frac{\sum (\hat{e_i^*})^2-\sum \hat{e}_i^2/3}{\sum \hat{e}_i^2/(n-3)}\sim F(3,n-3)$
3) $f-fal >> 0\to \text{reject }H_0$
###### 예2) 아이스크림의 수요함수 추정
- 수요에 대한 회귀식 : $\underbrace{Y_t}_{Q}=\beta_1+\beta_2\underbrace{X_t}_{P}=e_i$
- let 봄/여름/가을/겨울 
$\to D_{1i},D_{2i},D_{3i},D_{4i}$
$\text{if } k\to D_{ki}=1, else\, D_{ki}=0$
- 계절에 따른 더미 변수를 사용한 회귀식 
	- 옳은 회귀식 : 
    $y_t = [\alpha_1D_{1t}+\cdots+\alpha_4D_{4t}]+\beta_1x_{1t}+\epsilon_t$
	- 잘못된 회귀식 : 
    $y_t =\beta_0+[\cdots]+\beta_1x_{1t}+\epsilon_t$
1) $H_0:\forall \alpha_k=\alpha_l\quad H_1:\exists \alpha_k\neq\alpha_l$
$(k,l \in \{1,2,3,4\},k\neq l)$
2) F-test
	- Full : $\sum \hat{\epsilon}_t^2,\quad y_t=[\hat{\alpha_1}D_{1t}+\cdots]+\hat{\beta}_1x_t+\hat{\epsilon}_t$
	- res : $\sum \hat{\epsilon^*_t}^2,\quad y_t=\hat{\beta_0^*}+\hat{\beta}_1^*x_t+\hat{\epsilon}_t^*$
	- $(F-val)=\frac{\sum (\hat{\epsilon_i^*})^2-\sum \hat{\epsilon}_i^2/3}{\sum \hat{\epsilon}_i^2/(n-5)}\sim F(3,n-5)$

### 다중공선성(Multicolinearity)
###### Exact Multicolinearity
- Pop. E.Q. : $Y = X_1 \beta_1 + X_2 \beta_2 + e$    sample E.Q. : $Y = X_1 \hat{\beta}_1 + X_2 \hat{\beta}_2 + \hat{e}$
	1) $Y = X_2 \hat{\delta}_1 + Y^*$
	2) $X_1 = X_2 \hat{\delta}_2 + X_1^*; \quad \forall i,\, X_1^* = 0,\sum X_1^* = 0$
	3) $\hat{\beta}_1 = (X_1^{*'} X_1^*)^{-1} X_1^{*'} Y^*$
    $\implies \text{Var}(\hat{\beta}_1) = \sigma^2 (X_1^{*'} X_1^*)^{-1}$
- $\hat{\beta}_1 = (X_1^{*'} X_1^*)^{-1} X_1^{*'} Y^* = \frac{\sum X_{1i}^* Y_i^*}{\sum X_{1i}^{*2}}$에서 분모가 0, $\text{Var}(\hat{\beta}_1) = \frac{\sigma^2}{\sum X_{1i}^{*2}} \implies \text{(불능)}$ (증)
###### Near-Multicolinearity
- $\text{Var}(\hat{\beta}_1)$에서 분모가 0에 가까워져 분산$\uparrow\uparrow\,\Rightarrow$ $\text{(t-val)}(\hat{\beta}_1) = \frac{\hat{\beta}_1}{\sqrt{\hat{\text{var}}(\hat{\beta}_1)}}\simeq0$
- fail to reject $H_0$의 가능성 $\uparrow$, 의미 O 변수도 의미 X라 오판 가능성 $\uparrow$
###### 고전적 가정의 점검
- **SLR** : 
(1) $E(e_i) = 0;\forall i$
(2) $E(e_i^2) = \sigma^2;\forall i$
(3) $E(e_i e_j) = 0;\forall i \neq j$    
(4) $X: \text{non-stochastic}$
(5) $e_i \sim N(\cdot)$
(6) $X: \text{no exact linear relationship}$
- **MLR** :
(1) $E(e_i) = 0_{(n\times1)}$
(2) $Var(e) = \underbrace{\sigma^2 I_n}_{\text{이분산 X, 자기상관 X}}$
(3) $X: \text{non-stochastic}$
(4) $e\sim N(\cdot)$
(5) $\text{Col.Rank}(X) = k$ (완전 다중공선성 X)
###### 가우스-마르코프 정리
- 모든 고전적 가정이 성립할 시 OLS(또는 LSE)는 BLUE(Best Linear Unbiased Estimator)이다. 

---

## 12. 이분산성
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
		- $\text{if } e_i\sim N(0,\sigma_i^2)\implies Var(\hat{\beta}_2^\text{(OLS)})$$=(\frac{1}{\sum X_{2i}^2})^2\sum_{i=1}^n(\sum X_{2i}^2)\sigma_i^2$ - inefficient
			-  hint : $Var()$ 정의식 대입, $E(e_i^2)=\sigma^2_i$, $E(e_ie_j)=0$ 
		- $\text{if } e_i\sim N(0,\sigma^2)$$\implies Var(\hat{\beta}_2^\text{(OLS)})=\frac{\sigma^2}{\sum X_{2i}^2}$
		- 목표 : 고전적 가정 성립토록 모형 변환
- 가설검정시 문제점
	- $\text{(t-val)} = \frac{\hat{\beta}_2}{\sqrt{\hat{\text{Var}}(\hat{\beta}_2)}}\to$분모(var) $\uparrow\uparrow$, 따라서 $H_0$를 기각하기 어렵; 
	  유의한 변수임에도 유의X 라고 잘못 결론 가능
###### GLS(Generalized Least Squares)
- 정의 : 이분산 O? -> 고전적 가정이 성립토록 변환
- $Y_i=\beta_2X_{2i}+e_i, e_i\sim(0,\sigma_i^2)\to \tilde{Y}_i=\beta_2\tilde{X}_{2i}+\tilde{e}_i;$     
	- hint : $\tilde{\theta}_i=\frac{\theta_i}{\sigma_i}$
	- $\hat{\beta}_2=\frac{\sum\tilde{X}_{2i}\tilde{Y}_i}{\sum\tilde{X}_{2i}^2};\quad E(\hat{\beta}_2)=\beta_2;\quad Var(\hat{\beta}_2)=\frac{\sigma^2}{\sum \tilde{X}_{2i}^2}$
- 이분산의 분포(패턴)을 모를때 : 여전히 OLS사용
	- 단, 가설검정시 제대로된 분산 사용
	- FGLS(Feasible GLS) : unknown $\sigma^2$? : $\to\hat{\sigma}^2$
### 3. 이분산이 있는 다중회귀모형
#### pop eq. : 
$Y=X\beta+e,\quad e\sim(0_{(n\times1)},\sigma^2\Omega_{(n\times n)})$
- $Var(e)=E(ee')=\sigma^2\Omega\neq\sigma^2I_n$
- $\Omega = \begin{pmatrix}
Var(e_1)&Cov(e_2,e_1)& \cdots & Cov(e_n,e_1) \\
Cov(e_1,e_2) & Var(e_2) &  \cdots \\
\vdots & & \ddots
\end{pmatrix}$
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
---
###### 요약 및 비교 ($Y=X\beta+e, \quad e\sim N(0,\sigma^2\Omega$)

| OLS| GLS |
| ---| --- |
| $\hat{\beta}^{(OLS)}$<br>$=(X'X)^{-1}X'Y$| $\hat{\beta}^{(GLS)}$<br>$=(X'\Omega^{-1}X)^{-1}$<br>$X'\Omega^{-1}Y$ |
| $E(\hat{\beta}^{(OLS)})=\beta$| $E(\hat{\beta}^{(GLS)})=\beta$ |
| $Var(\hat{\beta}^{(OLS)})$<br>$=\sigma^2(X'X)^{-1}$<br>$X'\Omega X(X'X)^{-1}$ | $Var(\hat{\beta}^{(GLS)})$<br>$=\sigma^2(X'\Omega X)^{-1}$ |
| BLUE X                                                                  | BLUE O                                                    |
- $Var(\hat{\beta}^{(OLS)})\ge Var(\hat{\beta}^{(GLS)})$
- GLS : known $\Omega$
	- FGLS : unknown $\Omega$, able to estimate
	- OLS : known $\Omega$, cannot estimate
-
-
-
-
-
-
-
-
---

## 13. 자기상관 & 구조적 변화 -->
### 1. Eviews 실습 (없음)
### 2. 자기상관모형
$Y_t = \beta X_t+e_t,\quad e_t=\rho e_{t-1}+v_t,\quad v_t\overset{iid}{\sim}N(0,\sigma^2)$
- $E(e_te_s)\neq0,\quad\forall t\neq s$
- GLS의 아이디어 : 자기상관? -> 고.가 성립토록 모형 변형 -> OLS 적용
###### $\rho$가 알려진 경우
- $\tilde{Y}_t=\beta\tilde{X}_t+\tilde{e}_t(=v_t)$     hint : $Y_t-\rho Y_{t-1}$ 형태
### 3. Cochrane-Orcutt iterative Procedure
###### $\rho$가 알려지지 않은 경우($\rho$ 추정)
1) OLS reg. : $Y_t = \beta X_t+e_t\to\text{get }\hat{\beta},\hat{e}_t$
2) OLS reg. : $\hat{e}_t=\rho\hat{e}_{t-1}+v_t\to\text{get }\hat{\rho}$
3) GLS reg. with $\hat{\rho}$ : $\tilde{Y}_t = \beta \tilde{X}_t+v_t\to\text{get }\hat{\beta},\hat{e}_t$
4) $\hat{\rho}$에 대한 가설검정 -> if not 수렴? , then Goto 2) 
- \*\*(first-order Autocorrelation) AR(1) : 
$e_t=\rho e_{t-1}+v_t$
AR(2) : $e_t=\rho_1 e_{t-1}+\rho_2 e_{t-2}+v_t$
### 4. 구조적 변화가 있는 경우
#### 경제에 구조적 변화(structural change : $T^*$)가 있는지 test 하는 경우
- Dum. var.로 나타낼 수 O. : 
$Y_t = (\beta_1+\alpha_1D_t)+ (\beta_2+\alpha_2D_t)X_{2t}+e_t$
$e_t\sim N(0,\sigma^2)$
	- $=\gamma_1 +\gamma_2X_{2t}+e_t$
     where $D_t=\left\{\begin{matrix}0\quad \text{if } t\le T^*\\1\quad \text{if }t>T^*\end{matrix}\right.$
     $T^*$? : break-point test)
- 구조적 변화 X? : $\beta_1=\gamma_1,\beta_2=\gamma_2$ 일 것.
###### Chow test : $H_0 : \beta_1=\gamma_1,\beta_2=\gamma_2$ 회귀분석 3번 실시 (구.변이 있는가?)
- $H_0$가 맞다면? :
$\sum_{t=1}^T{\hat{e}_t^*}^2\approx\sum_{t=1}^{T^*}\hat{e}_{1t}^2+\sum_{t=T^*+1}^T\hat{e}_{2t}^2$$
	- (f-val) $= \frac{(\sum{\hat{e}_{t}^*}^2-\sum\hat{e}_{t}^2)/2}{T-4}\sim F(2,T-4)$    (but, $T^*$ unknown)
###### AR(1)에서 오차항과 관련 특성
1) $E(e_t)$ : 
$e_t=\rho e_{t-1}+v_t=\sum_{i=0}^\infty \rho^iv_{t-i}$$\implies E(e_t)=0\quad(\rho \in (-1,1))$
	- hint : 재귀함수꼴처럼 무한히 $e_{t-k}$를 제거. $v_t,v_{t-i}$의 분포
2) $E(e_t^2)$ : 
$\to Var(e_t)=\sum_{i=0}^\infty \rho^iVar(v_{t-i})=\frac{\sigma^2}{1-\rho^2}$
	- hint : Var()에서 확.변의 선.결, 무한등비급수 합, $Var(v_{t-i})=?$, $e_t$ 정의
3) $E(e_te_{t-s})$ : 
$\to Cov(e_t,e_{t-s})=E[(\sum_{i=0}^{T} \rho^iv_{t-i})(\sum_{i=s}^{T} \rho^{i-s}v_{t-i})]$ $=\sigma^2\frac{\rho^T}{1-\rho^2}$
	- hint : t-s이전 시점 terms 끼리만 생각, 
    $E(v_av_b)=0 \quad(\because v_t\overset{iid}{\sim}N(0,\sigma^2))$ 
	- $\text{if }s\uparrow\uparrow, \text{ then }\rho^s\approx0\quad (|p|<1)$    $(s\to\infty)\implies(\rho^s\to0)$ 즉, 시간 지남? -> 관계 희미

---

## 14. 내생성

### 1. 고전적 모형

### 2. 일치성

#### 일치성(consistency)

- 확변의 열 $\{X_1,X_2,\cdots\}$이 $\mu$로 확률 수렴(convergence in proability)할 때 $X_n\overset{p}{\to}\mu$라 쓰고,
  - $$
    \underset{n\to\infty}{\text{plim }}X_n=\mu\text{ iff }\lim_{n\to\infty}P(|X_n-\mu|<\epsilon)=1;\quad\forall\epsilon>0
    $$
  - $E(e|X)\neq0$일 때, $(n\to\infty)\to \underbrace{(|\theta-E(\hat{\theta})|\overset{p}{\to}0)}_{\text{(bias)}\to0}$? 즉, $\hat{\beta}\overset{p}{\to}\beta$?
    - 샘플의 갯수 무한? $\to$ 추정량 $\beta$로 수렴

#### 대수의 법칙

- 확변의 열 $\{X_1,X_2,\cdots,X_n\}$이 서로 독립적, 동일 분포 따름,
  $E(X_i)=\mu<\infty,Var(X_i)=\sigma^2<\infty$면,
  $$
  nderset{n\to\infty}{\text{plim}}\bar{X}_n=\mu\quad\text{or}\quad\bar{X}_n\overset{p}{\to}\mu
  $$

  - 표본평균의 일치성 : (표본크기$\uparrow\uparrow$) $\to$ ((확률)수렴 : 표본평균 $\to$ 모평균)

#### 내생성 문제 ($\text{X : stochastic}$일 때 고려)

1. $\text{if }E(e|X)=0,\quad\hat{\beta}:\text{unbiased}$
2. $\text{if }E(e|X)\neq0,\quad\hat{\beta}:\text{biased}$
   1) $(n\to\infty)\to(\text{(bias)}\to0)$ : OLS 가능

- is OLS $\hat{\beta}$ a consistent estimator?
  - large n : (or (in))consistent?    small n : (or (un))biased?

#### Unbiasedness VS Consistentcy

1) Unbiasedness : Given n with repeated sampling
   - ![](../../기타/image/Pasted%20image%2020251202124843.png)
2) Consistency : n이 점점 커지는 상황 ($E(e|X)\neq0$ 라면, $n\to\infty$가 아니다)
   - ![](../../기타/image/Pasted%20image%2020251202124901.png)

#### 수요-공급의 내생성 (내생성 ex1)

- ex) 수요-공급 곡선.    (수요) : $Q_i=\alpha P_i+e_{Di}$ , (공급) : $Q_i=\alpha P_i+e_{Si}$
  - ![](../../기타/image/Pasted%20image%2020251202125520.png)
    - 그렇다면 $\hat{\alpha},\hat{\beta}$는 unbiased?
  - ![](../../기타/image/Pasted%20image%2020251202125551.png)
    - 시장 내에서 각 점은 수많은 각 소비자 및 생산자의 수요-공급 곡선에 대한 교점.
    - ($\text{if }\bar{\text{D}},\text{then }S$만 움직이나?) or ($\text{if }\bar{\text{S}}, \text{then }D$만 움직이나?)
  - 수요 충격이 발생했다 하자. ($e_{Di}\to e_{Di}'$)
    - ![](../../기타/image/Pasted%20image%2020251202130615.png)
    - $\therefore(e_{Di}\uparrow\uparrow)\to(P_i\uparrow \&\&\, Q_i\uparrow),\text{COV}\neq0$
      - OLS는 포기해야한다
  - 대안? : 도구변수추정 (=2-stage LS)
    - ex) 필립스커브 : $\pi_t=\gamma g_t+\beta\pi_{t-1}+e_t\implies$(환율충격 : $e_t\uparrow)\to(\pi_{t-1}\uparrow,g_t\downarrow)$ OLS X

---
#### 필립스 커브와 내생성 (내생성 ex2)
- 오일쇼크 이전의 필립스 커브 : 
$(u\downarrow)\to(w\uparrow)\implies\pi_t=\alpha+\overset{(-)}{\beta} u_t+e_t$
	- (A : adaptive expectation) : 
    $(u\downarrow)\to(w\uparrow,\pi\uparrow)$
    $\implies\pi_t=\alpha+\beta_1 u_t+\beta_2\pi_{t-1}+e_{1t}$
- 70's 오일쇼크 이후 필커 : 
$(u\uparrow)\&\&(w\uparrow)$인 상황 직면; 
$\implies\pi_t$예측시, $E(\pi_{t+1}|I_t)=E_t\pi_{t+1}\quad (I_t:\text{info. up to t})$
	- (B : 뉴케인지안; rational expectation) : 
    $\pi_t=\alpha E_t\pi_{t+1}+\beta_1 u_t+e_{2t}$
	- (C : 뉴케인지안 하이브리드 : A,B 통합) : 
    $\pi_t=\alpha E_t\pi_{t+1}+\beta_2 u_t+\beta_3\pi_{t-1}+e_{3t}$
- 케인지안 (B),(C)의 문제점 : $E_t\pi_{t+1}$이 측정 가능한가? : $E_t\pi_{t+1}\to\pi_{t+1}$로 대체, $\text{let }\pi_{t+1}=E_t\pi_{t+1}+\epsilon_t$
	- (C') : $\pi_t=\alpha\pi_{t+1}+\beta_1 u_t+\beta_2\pi_{t-1}+\omega_t$
    $(\omega_t:\text{Measurement Error})$
		- (C) 에 의해, $\omega_t=e_{3t}+\alpha(\underbrace{E_t\pi_{t+1}-\pi_{t+1}}_{=\epsilon_t})$
#### 빠진 변수에 내생성이 있을 때 (내생성 ex3)
- ture model : $y_i=\beta_1+\beta_2X_{2i}+\beta_3X_{3i}+u_i$
- estimated reg. eq. : $y_i=\beta_1+\beta_2X_{2i}+e_i$;    $e_i=u_i+\beta_3X_{3i}$
	- if $X_{2i}$ is correlated with $(X_{3i} : \text{중요변수})$,    then $e_i$ is correlated with $X_{2i}$
 
### 3. $\hat{\beta}_{\text{OLS}}$의 일치성
- $$\underset{n\to\infty}{\text{plim}}\,\hat{\beta}_{OLS}=\underset{n\to\infty}{\text{plim}}(\frac{\sum x_iy_i}{\sum x_i^2})=\underset{n\to\infty}{\text{plim}}\,\beta+(\frac{\sum x_ie_i}{\sum x_i^2})$$
$\text{(분자) : }\underset{n\to\infty}{\text{plim}}\,\frac{1}{n}\sum_{i=1}^n x_ie_i\overset{p}{\to}E(X_ie_i)=0$
$\text{(분모) : }\underset{n\to\infty}{\text{plim}}\,\frac{1}{n}\sum_{i=1}^n x_i^2\overset{p}{\to}E(X_i^2)=M<\infty$
- 즉, $X,e$가 서로 독립X 여도, $Cov(X_i,e_i)=0$ 이기만 한다면 적어도 OLS추정량은 consistent.
- sample size가 충분히 크고, $Cov(X_i,e_i)=0$가 만족되면 OLS 추정량 사용 OK

#### 증명 : $\hat{\beta}_{OLS}$의 일치성
$\underset{(1\times1)}{y_i}=\underset{(1\times k)}{x_i'}\underset{(k\times1)}{\beta}+\underset{(1\times1)}{e_i};\quad\exists i, E(e_i|X)\neq0$
- $\hat{\beta}=(\sum x_i x_i')^{-1}\sum x_i y_i\implies (X'X)^{-1}X'Y$
    - Q : $\hat{\beta}$가 constitent 해지나? 언제? 어떻게?

- $\hat{\beta}=(\sum x_i x_i')^{-1}\sum x_i(x_i'\beta+e_i)$
$=\beta+\underbrace{\frac{1}{n}(\sum x_i x_i')^{-1}}_{\text{(1) 분모}\to L<\infty}\underbrace{\frac{1}{n}\sum x_ie_i}_{\text{(2) 분자}\to0}$
- 조건 (1), (2) 성립?? $\to$ $\hat{\beta}$는 consistent; large num일 때 OLS를 사용할 수 있다.
  - (1) : $\frac{1}{n}(\sum x_i x_i')^{-1}\overset{p}{\to}L=E(x_ix_i')?\quad(L<\infty)$
  - (2) : $\frac{1}{n}\sum x_ie_i\overset{p}{\to}0=E(x_ix_i')?$
- Law of iterative expactation (반복기대의 법칙) : 조건부 평균의 평균은 무조건부 평균과 같다.
  - $\underset{\text{무조건부 평균}}{E(\omega)}=\underset{\text{조건부 평균}}{E(E(\omega|\Omega))}$
  - (2) 증명 : $E(x_ie_i)=E(E(x_ie_i|x_i))\to$ $x_i$가 given? $x_i$는 더이상 확.변. X (밖으로 제거 가능)
    - $E(E(x_ie_i|x_i))=E(x_i\underbrace{E(e_i|x_i)}_{\text{let }\alpha})$;     $\text{if }\alpha=0,\quad\text{then }E(x_ie_i)=0$
    - 즉, $E(x_ie_i)=0$ 이면 $x_i,e_i$가 uncorrelated. 나란히 있는 것 끼리 관계 X
      - ($\implies$No contemporate relateionship; 동기간의 상관관계 X)
      - $\implies \therefore \hat{\beta}_{OLS}$ is consistent
#### OLS가 finite sample에선 biased, large sample에선 consistent 한 경우
  $y_t=\rho y_{t-1}+e_t;\quad e_t\overset{\text{iid}}{\sim}N(0,\sigma^2),|\rho|<1$
  - $y_t=\rho^k y_{t-k}+(e_t+\rho e_{t-1}+\rho^2 e_{t-2}+\cdots)$
  - $\underset{k\to\infty}{\lim}y_t = e_t+\rho e_{t-1}+\rho^2 e_{t-2}+\cdots$
    1) $E(y_t)=0+0+\cdots=0$
    2) $Var(y_t)=\sigma^2+\rho^2\sigma^2+\cdots=\frac{\sigma^2}{1-\rho^2}$    hint : var(ax+b), 무한등비급수
    3) $$Cov(y_{t-1},e_t)=E(y_{t-1}e_t)=0$$
		- hint : 대입 후 전개; $e_t,e_{t-1}$간 관계?
- $\hat{\rho}$ 는 biased 한가? : $\hat{\rho}=\frac{\sum y_{t-1}y_t}{\sum y_{t-1}^2}$
- $E(\hat{\rho})=\rho + E(\frac{\sum y_{t-1}e_t}{\sum y_{t-1}^2})$ ;    hint : $y_t$ 대입
	- 반복기대의 법칙 적용 : $E(\frac{\sum y_{t-1}e_t}{\sum y_{t-1}^2})=E(E(\frac{\sum y_{t-1}e_t}{\sum y_{t-1}^2}|\mathbb{Y}))$
    $\mathbb{Y}=(y_1\,y_2\,\cdots\,y_T)'$
		- $y_t$는 $\mathbb{Y}$가 주어졌을 때, 확변X. $E(e_t|\mathbb{Y})$꼴로 변환
	- $$y_t=\rho y_{t-1}+e_t\implies\begin{bmatrix}y_2\\y_3\\\vdots\\y_T\end{bmatrix}=\rho\begin{bmatrix}y_1\\y_2\\\vdots\\y_{T-1}\end{bmatrix}+\begin{bmatrix}e_2\\e_3\\\vdots\\e_{T}\end{bmatrix}$$
		- 각각의 기간에서 ex) $y_3=\rho y_2+e_3$ ; $e_t$들은 $y_{t-1}$들과 선형결합의 관계.
			- $\therefore E(e_t|\mathbb{Y})\neq0;\implies\hat{\rho}(\hat{\beta}_{OLS})$는 biased in finite sample; but, consistent in large sample. 
            ($\because Cov(y_{t-1},e_t)=0$ 이므로)
