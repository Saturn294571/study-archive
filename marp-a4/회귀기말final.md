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


# 회귀분석 기말고사 대비 백지 테스트 자료

## Final Exam Scope & Tips (Audio Analysis)
* **일정:** 다음 주 월요일
* **범위:** Lecture Note 9 ~ 16 (제외: 13장 전체, 16장 심화)
* **Chapter 9 (Hypothesis):** F-test, General Linear Hypothesis 중요.
* **Chapter 10 (Diagnostics):** Influence measures (Cook's D, DFFITS, DFBETAS), Studentized Residuals. **(제외: Residual Plot, Multiple Comparison)**.
* **Chapter 11 (Leverage):** Leverage 개념 및 성질 중요.
* **Chapter 12 (Qualitative):** **계산 문제 출제 가능성 높음.** Interactions, Dummy Variables 꼼꼼히 볼 것.
* **Chapter 13 (WLS):** **시험 범위 제외.**
* **Chapter 14 (Correlated Errors):** 시계열 관련 중요. AR(1), Durbin-Watson 등 포함.
* **Chapter 15 (Model Selection):** Criteria, Selection Procedures 중요.
* **Chapter 16 (Penalized):** Collinearity, Bias-Variance, Ridge/Lasso **기본 개념(Concept)만**. **(제외: PCR, SVD, Elastic Net 알고리즘 등 심화 내용)**.

---
## 9. Multiple regression 3
### 다중 회귀 추론 (Inference for Multiple Regression)
#### 1개 이상 변수를 Dropping 하는 과정
* 귀무가설과 대립가설 
$H_0 : \beta_6 = \beta_7 = 0\quad H_1 : \beta_6, \beta_7 \text{ 중 적어도 하나는 } 0\text{이 아님}.$
* 검정 방법: 두 모형간 비교
    * 축소 모형 (Reduced Model) : $\text{Reduced}(H_0) : Y_i = \beta_0 + \sum_{j=1}^5 \beta_j X_{ij} + \epsilon_i$
    * 완전 모형 (Full Model) : $\text{Full}(H_1) : Y_i = \beta_0 + \sum_{j=1}^7 X_{ij} \beta_j + \epsilon_i$
        * $\text{(F-값)}\geq F_\alpha(2,n-p-1)$일때 $H_0$를 기각
### F-test 유형별 가설 설정 및 모형 비교

#### F-test type I (모형의 유의성 검정)
* **가설:** $H_0 : \beta_1 = \beta_2 = \cdots = \beta_p = 0$        $H_1 : \exists \beta_k\neq 0$    $k \in \{i_1, \cdots , i_j\}\subset \{0, 1, \dots, p\}$
#### F-test type II (두 계수의 동일성 검정)
* 가설 : $H_0 : \beta_{a} = \beta_b$ ($\beta^*$)        $H_1 : \beta_{a} \neq \beta_{b}$
* **모형 재정의 (Full Model)**
    * $\text{Full model} : Y_i = \beta_0 + \cdots + \beta_{a} x_{ia} + \cdots$ $+ \beta_{b} x_{ib} + \cdots + \beta_p x_{ip} + \epsilon_i$    $\text{df}_F = n - p-1$
* **모형 재정의 (Reduced Model)**
    * $H_0: \beta_{a} = \beta_{b} = \beta^*$ 로 치환 $(\beta_{b} = \beta^*)$
    * $\text{Reduced model} : Y_i = \beta_0 + \cdots + \beta^* x_{ia} +\cdots$ $+\beta^* x_{ib} + \cdots + \beta_p x_{ip} + \epsilon_i$
      $= \beta_0 + \cdots + \beta^* (x_{ia} + x_{ib}) + \cdots + \beta_p x_{ip} + \epsilon_i$        $\text{df}_R = n - p$ (제약 조건으로 계수 1개$\downarrow$ )
#### F-test type III (일반 선형 가설 검정)
* 가설: $H_0 : \beta_{a} + \beta_{b} = C$        $H_1 : \beta_{a} + \beta_{b} \neq C$
* **모형 재정의 (Full Model)**
    * $\text{Full model} : Y_i = \beta_0 + \cdots + \beta_{a} x_{ia} +\cdots$ $+\beta_{b} x_{ib} + \cdots + \beta_p x_{ip} + \epsilon_i$
    * $\text{df}_F = n - p$ (총 계수 개수가 $p$)
* **모형 재정의 (Reduced Model)**
    * $H_0: \beta_{a} = C - \beta_{b}$ 로 치환 
    * $\text{Reduced model : } Y_i = \beta_0 + \cdots + (C - \beta_{b}) x_{ia}$ $+ \cdots+\beta_{b} x_{ib}$ $+ \cdots + \beta_p x_{ip} + \epsilon_i$
      $\implies Y_i - C x_{ib} = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_{a} (x_{ia} - x_{ib})$ $+ \cdots + \beta_p x_{ip} + \epsilon_i$
    * $\text{df}_R = n - (p - 1)$ (제약 조건 $\beta_{a} + \beta_{b} = C$로 계수가 1개 줄어듦)

### General Linear Hypothesis (일반 선형 가설)
* **핵심:** 모델을 재추정할 필요 없는 $F$ 검정의 대안 버전이 유도될 수 있다.)
##### 귀무가설과 대립가설 : $H_0 : C_{q \times (p+1)} \boldsymbol{\beta}_{(p+1) \times 1} = \mathbf{h}$         $H_a : C_{q \times (p+1)} \boldsymbol{\beta}_{(p+1) \times 1} \neq \mathbf{h}$

##### F-통계량을 통해 검증한 일반 식
* $\mathbf{F} = \frac{(C\hat{\boldsymbol{\beta}} - \mathbf{h})^{\intercal} (C(X^{\intercal}X)^{-1} C^{\intercal})^{-1} (C\hat{\boldsymbol{\beta}} - \mathbf{h})/q}{SSE(F)/df_F}$ $\underset{H_0}{\sim} F(q, n - p - 1).$
    * 랭크 $\text{rank}(C(X^{\intercal}X)^{-1}C^{\intercal}) = q.$ 임을 가정하고 있음
##### 예시
* **Full Model** : $Y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_5 x_{i5} + \epsilon_i$
* **귀무가설 (Null Hypothesis, $H_0$)**
    * $\beta_1 + \beta_2 = 0$    $\beta_3 - \beta_4 = 1$    $\beta_1 + \beta_5 = 5$
* **대립가설 (Alternative Hypothesis, $H_1$)**
    * $H_1 : (H_0\text{의 적어도 하나의 등식은 성립 X})$
* **일반 선형 가설 행렬 표현 $C\boldsymbol{\beta} = \mathbf{h}$**
    * $H_0 : \begin{pmatrix} 0 & 1 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & -1 & 0 \\ 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix}_{3 \times 6} \begin{pmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ \beta_3 \\ \beta_4 \\ \beta_5 \end{pmatrix}_{6 \times 1} = \begin{pmatrix} 0 \\ 1 \\ 5 \end{pmatrix}_{3 \times 1}$
    * $\mathbf{C} \boldsymbol{\beta} = \mathbf{h}$

---

## 10. Diagnostics in multiple linear regression
![](../../기타/image/Pasted%20image%2020251029233212.png)
### 어떤 것이 틀릴 수 있나?
- 모델에 대한 가정
    - 회귀함수는 틀릴 수 있다 : 만일 회귀 함수가 다른 형태를 가져야만 한다면 (SLR 진단 참조)
- 예측치에 대한 가정
    - 1) 비확률적 예측치일 수 있고, 2) 수집 오차가 있을 수 있다
- 관측치에 대한 가정
    - 몇개의 관측치가 influential하거나 아웃라이어일 수 있다
- 문제를 감지하는건 기술이라기 보단 예술의 영역이다. 회귀식의 모든 가능한 문제에 대해 테스트 할 순 없다
![](../../기타/image/Pasted%20image%2020251029234147.png)
### 가능한 문제 및 진단 체크
- 오차는 정규분포를 따르지 않을 수 있고, 동일 분산을 가지지 않을 수 있다 (거대 샘플에서는 덜 중요)
- 분산은 상수가 아닐 수 있다. (오차 e가 부채꼴 모양으로 퍼지거나 혹은 추세선이 나타나 분산이 상수항이 아닐 수 있음)
- influential 관측치의 경우 : 어떤 점이 회귀모델에 가장 영향을 주는가?
- 아웃라이어 : 데이터 전처리 실수나 실험 오차등이 포함되어있을 수 있다

### 내적 스튜던트화 잔차 (Internally Studentized Residuals)
#### $r_i=e_i/SE(e_i)=\frac{e_i}{\hat{\sigma}\sqrt{1-H_{ii}}}$

* 잔차 $e_i$의 정의 및 벡터 표현
    * $e_i = Y_i - \hat{Y}_i \rightarrow \begin{pmatrix} e_1 \\ \vdots \\ e_n \end{pmatrix} = \begin{pmatrix} Y_1 \\ \vdots \\ Y_n \end{pmatrix} - \begin{pmatrix} \hat{Y}_1 \\ \vdots \\ \hat{Y}_n \end{pmatrix}$ $=Y - X\hat{\beta}$
    $\text{where } \hat{\beta} = (X^TX)^{-1}X^TY$
* Hat Matrix ($H$)를 이용한 $e$ 표현
    * $e = Y - \underbrace{X(X^TX)^{-1}X^T}_{H} Y$ $= (I - H)Y=(I - H)(X\beta + e)=(I - H)e$
        * $(\because (I - H)X\beta = X\beta - X\beta = 0)$
* $e$의 기댓값과 공분산 : 
    * 기댓값 : $E(e) = (I - H) E(\epsilon) = 0$
    * $Var(e) = Var((I - H)\epsilon) = (I - H) Var(\epsilon) \underbrace{(I - H)^T}_{\text{대칭, 멱등}}$ $=(I - H) (\sigma^2 I)= \sigma^2 (I - H)$
* 잔차와 hat matrix
    * $Var(\epsilon_i) \rightarrow (1 - h_{ii}) \sigma^2$ (행렬 $I-H$의 $i$-번째 대각 원소)
    * $\frac{e_i}{\sigma \sqrt{1 - h_{ii}}} \quad \text{(표준화된 잔차)}$
    * $H = \begin{pmatrix} h_{11} & \cdots & h_{1n} \\ \vdots & \ddots & \vdots \\ h_{n1} & \cdots & h_{nn} \end{pmatrix}_{n \times n}$
### 외적 스튜던트화 잔차 (Externally Studentized Residuals)
$t_i=\frac{e_i}{\hat{\sigma_{(i)}}\sqrt{1-H_{ii}}}\sim t(n-p-2)$
#### 관측치 $i$를 제외한 추정량 ($\hat{\sigma}^2_{(i)}$, $\hat{\beta}_{(i)}$)
* 잔차 제곱합 및 분산 추정 : 
$\hat{\sigma}^2_{(i)} = \frac{SSE_{(i)}}{n - p - 1}$    $SSE_{(i)} = \sum_{j \neq i}^n (y_j - \hat{y}_{(i)j})^2$
* $i$번째를 제외한 예측값 : 
$\hat{y}_{(i)j} = x_j^T \hat{\beta}_{(i)} = \hat{\beta}_{0(i)} + \hat{\beta}_{1(i)} x_{j1} + \cdots + \hat{\beta}_{p(i)} x_{jp}$
* $\hat{\beta}_{(i)}$: $i$ 번째 관측치를 제외하고 추정한 회귀계수 추정량.
---
#### OLS 추정량과 Leave-One-Out 행렬 정의
* 원래 LSE 를 $\hat{\beta} = (X^TX)^{-1}X^TY$ 라고 한다면, 관측치 $i$를 제외한 행렬 ($X_{-i}, Y_{-i}$) :

    * $X_{-i} = \begin{pmatrix} x_{11} & \cdots & x_{1p} \\ \vdots & & \vdots \\ x_{i-1, 1} & \cdots & x_{i-1, p} \\ x_{i+1, 1} & \cdots & x_{i+1, p} \\ \vdots & & \vdots \\ x_{n1} & \cdots & x_{np} \end{pmatrix} \quad Y_{-i} = \begin{pmatrix} Y_1 \\ \vdots \\ Y_{i-1} \\ Y_{i+1} \\ \vdots \\ Y_n \end{pmatrix}$

* **$\hat{\beta}_{(i)}$ 공식 (행렬 대수적 근사)**
    * $\hat{\beta}_{(i)} = (X_{-i}^T X_{-i})^{-1} X_{-i}^T Y_{-i}$ $= (X^TX - x_i x_i^T)^{-1} (X^TY - Y_i x_i)$
        * 참고: $x_i$는 $X_{i}$의 $i$번째 행 벡터.; $x_i^T = (1 \quad x_{i1} \quad \cdots \quad x_{ip})$
###### 예시
- 기본 행렬식 정의 :
    - Let, $X = \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{pmatrix} \quad Y = \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix}$
* $A^TB$ 형식으로 나타내기
    * $X^T X = \begin{pmatrix} \sum_{i=1}^3 x_{i1}^2 & \sum_{i=1}^3 x_{i1} x_{i2} \\ \sum_{i=1}^3 x_{i1} x_{i2} & \sum_{i=1}^3 x_{i2}^2 \end{pmatrix}$,    $X^T Y = \begin{pmatrix} \sum_{i=1}^3 y_i x_{i1} \\ \sum_{i=1}^3 y_i x_{i2} \end{pmatrix}$
* 행벡터의 합과 $X^TX$간 관계
    * Let, $x_1^T = (x_{11}, x_{12}) \quad x_2^T = (x_{21}, x_{22}) \quad x_3^T = (x_{31}, x_{32})$
     $x_1 x_1^T = \begin{pmatrix} x_{11} \\ x_{12} \end{pmatrix} (x_{11} \quad x_{12}) = \begin{pmatrix} x_{11}^2 & x_{11} x_{12} \\ x_{11} x_{12} & x_{12}^2 \end{pmatrix}$
    * $\sum_{i=1}^3 x_i x_i^T = x_1 x_1^T + x_2 x_2^T + x_3 x_3^T = X^T X$
- i=2 관측치를 제거한 행렬 ($X^TX$, $X^TY$의 경우)
    * $X_{-2}^T X_{-2} = \begin{pmatrix} \sum_{i \neq 2} x_{i1}^2 & \sum_{i \neq 2} x_{i1} x_{i2} \\ \sum_{i \neq 2} x_{i1} x_{i2} & \sum_{i \neq 2} x_{i2}^2 \end{pmatrix}$= X^T X - x_2 x_2^T$     (**참고:** $X^T X = \sum_{i=1}^n x_i x_i^T$)
    * $X_{-2}^T Y_{-2} = \begin{pmatrix} \sum_{i \neq 2} y_i x_{i1} \\ \sum_{i \neq 2} y_i x_{i2} \end{pmatrix} = X^T Y - y_2 x_2$ $\text{where } x_2 = \begin{pmatrix} x_{21} \\ x_{22} \end{pmatrix}$
---
### leave 1 out 행렬 관련 성질
#### 1. $\hat{\beta}_{(i)}$
$= (X^T X - x_i x_i^T)^{-1} (X^T Y - y_i x_i)$,    $X = \begin{pmatrix} x_1^T \\ \vdots \\ x_n^T \end{pmatrix}_{n \times (p+1)}$

#### 2. Sherman-Morrison-Woodbury 공식
* 공식 (일반 형태) : 
$(A - u u^T)^{-1} = A^{-1} + \frac{A^{-1} u u^T A^{-1}}{1 - u^T A^{-1} u} \quad \text{if } \exists A^{-1}$
* 공식 적용 (회귀분석) : 
$(X^T X - x_i x_i^T)^{-1} = (X^T X)^{-1}$ $+ \frac{(X^T X)^{-1} x_i x_i^T (X^T X)^{-1}}{1 - \underbrace{x_i^T (X^T X)^{-1} x_i}_{=h_{ii}\cdots(*)}}$
* $(*)\quad H$ 행렬의 대각 원소 ($h_{ii}$) 정의
    * $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = (u_1 \quad u_2)$
    * $u_1^T H u_1 = \begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{pmatrix}  \begin{pmatrix} 1 \\ 0 \end{pmatrix} = h_{ii}$ $H u_i = \begin{pmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} h_{12} \\ h_{22} \end{pmatrix}$
    * $H(\text{Hat mat.}) = X(X^T X)^{-1} X^T$,     $\underbrace{u_i^TX}_{=(X^Tu_i)^T}(X^T X)^{-1} \underbrace{X^Tu_i}_{=x_i\text{(참고)}}= x_i^T (X^T X)^{-1} x_i$
        * (참고) : $X^Te_i \to X^T$ 의 i 번째 열
    $\to$원래 X의 i번째 행벡터의 전치$=x_i$

#### 3. $\hat{\beta}_{(i)}$
$= \left( (X^T X)^{-1} + \frac{(X^T X)^{-1} x_i x_i^T (X^T X)^{-1}}{1 - h_{ii}} \right)$ $(X^T Y - y_i x_i)$
$= \underbrace{(X^T X)^{-1} X^T Y}_{=\hat{\beta}} - y_i (X^T X)^{-1} x_i$
$+ \frac{1}{1 - h_{ii}} (X^T X)^{-1} x_i x_i^T \underbrace{(X^T X)^{-1} X^TY}_{=\hat{\beta}}$
$- \frac{1}{1 - h_{ii}} (X^T X)^{-1} x_i \underbrace{x_i^T (X^T X)^{-1} x_i}_{=h_{ii}}y_i$

#### 4. $\hat{y}_{j(i)} = x_j^T \hat{\beta}_{(i)}$
* $= x_j^T \hat{\beta} - \underbrace{x_j^T(X^T X)^{-1} x_i}_{=h_{ij}} y_i$ $+ \frac{1}{1 - h_{ii}} \underbrace{x_j^T (X^T X)^{-1} x_i}_{=h_{ij}} \underbrace{x_i^T\hat{\beta}}_{=\hat{y_i}}$ $- \frac{1}{1 - h_{ii}} \underbrace{x_j^T (X^T X)^{-1} x_i}_{=h_{ij}}h_{ii}y_i$
    * $= x_j^T \hat{\beta} - h_{ij} y_i + \frac{1}{1 - h_{ii}} h_{ij} \hat{y}_i - \frac{1}{1 - h_{ii}} h_{ij} h_{ii} y_i$

#### 5. $y_j - \hat{y}_{j(i)}$
* $= h_{ij}y_j -\frac{1}{1 - h_{ii}} h_{ij} \hat{y}_i - \frac{1}{1 - h_{ii}} h_{ij} h_{ii} y_i$
* $= \frac{h_{ij}}{1-h_{ii}}((1-h_{ii})y_i - \hat{y_i} +h_{ii} y_i)=\frac{h_{ij}}{1-h_{ii}}(y_i-\hat{y_i})$

#### 6. $\sum_{j=1}^n (\hat{Y}_j - \hat{Y}_{j(i)})^2$
$= \sum_{j=1}^n h_{ij}^2 (\frac{e_i}{1 - h_{ii}})^2$ $= \frac{e_i^2}{(1 - h_{ii})^2} \cdot \underbrace{\sum_{j=1}^n h_{ij}^2= h_{ii}}_{=h_{ii}\cdots(*)} \cdot \frac{e_i^2}{(1 - h_{ii})^2}$
* 표준화 잔차$r_i$와 SSE :
$r_i = \frac{e_i}{\hat{\sigma} \sqrt{1 - h_{ii}}}, \quad r_i^2 = \frac{e_i^2}{\hat{\sigma}^2 (1 - h_{ii})}$
    * $\rightarrow \sum_{j=1}^n (\hat{y}_j - \hat{y}_{j(i)})^2 = h_{ii} \cdot \frac{\hat{\sigma}^2}{(1 - h_{ii})}\frac{e_i^2}{\hat{\sigma}^2(1-h_{ii})}$ $= \frac{h_{ii}}{1 - h_{ii}} \cdot \hat{\sigma}^2 r_i^2$
* $(*)$: Hat Matrix의 성질**
    * $(*)$ $\sum_{j=1}^n h_{ij}^2 = h_{ii} \quad (\because H \cdot H = H)$ $\text{즉, } (h_{i1} \quad \cdots \quad h_{in}) \begin{pmatrix} h_{1i} \\ \vdots \\ h_{ni} \end{pmatrix} = \sum_{j=1}^n h_{ij}^2=h_{ii}$

#### 7. $\frac{1}{\hat{\sigma}^2(p+1)} \sum_{j=1}^n (\hat{Y}_j - \hat{Y}_{j(i)})^2$
$= \frac{r_i^2}{p+1} \cdot \frac{h_{ii}}{1 - h_{ii}}$ $\rightarrow C_i: \text{Cook's distance.}$
* 영향력 분석 관련 용어: $\frac{h_{ii}}{1 - h_{ii}} : \text{potential}$ (잠재력)

#### 8. $\hat{y}_j - \hat{y}_{j(i)} = \frac{h_{ii}}{1 - h_{ii}} \cdot e_i$

####  9. $y_i - \hat{y}_{i(i)}$
$= y_i - \hat{y}_i + \hat{y}_i - \hat{y}_{i(i)}$ $= e_i + \frac{h_{ii}}{1 - h_{ii}} e_i = \frac{e_i - h_{ii} e_i + h_{ii} e_i}{1 - h_{ii}} = \frac{1}{1 - h_{ii}} e_i$

#### 10. $\text{PRESS}$
$= \underbrace{\sum_{i=1}^n (y_i - \hat{y}_{i(i)})^2}_{\text{Leave-one-out cross validation}}$$= \sum_{i=1}^n = \left(\frac{e_i}{1 - h_{ii}}\right)^2\quad ()$

#### 11. $y_j - \hat{y}_{j(i)}$
$= y_j - \hat{y}_j + \hat{y}_j - \hat{y}_{j(i)} = e_j + \frac{h_{ij}}{1 - h_{ii}} e_i$

#### 12. $SSE_{(i)}$
$= \sum_{\substack{j=1 \\ j \neq i}}^n (Y_j - \hat{Y}_{j(i)})^2$ $= \sum_{\substack{j=1 \\ j \neq i}}^n \left(e_j + \frac{h_{ij}}{1 - h_{ii}} e_i\right)^2$
- $\hat{\sigma_{(i)}}^2=SSE_{(i)}/(n-p-2)$

### 관측치의 영향력 (Influence of an Observation)
- 관측치의 영향력을 측정하기 위한 지표가 있음
1) DFFITS :
$DFFITS_i=\frac{\hat{Y_i}-\hat{Y}_{i(i)}}{\hat{\sigma_{(i)}\sqrt{H_{ii}}}}$
2) Cook's distance : 
$D_i = \frac{\sum_{j=1}^n (\hat{Y}_j - \hat{Y}_{j(i)})^2}{(p + 1)\hat{\sigma}^2}$
3) DFBETAS : 
$DFBETAS_{j(i)} = \frac{\hat{\beta}_j - \hat{\beta}_{j(i)}}{\sqrt{\hat{\sigma}_{(i)}^2 (X^{\intercal} X)^{-1}_{jj}}}$

---

## 11. Diagnostics in multiple linear regression II

### Leverage (레버리지)
* **정의:**
    * $\hat{y} = X \hat{\beta} = \underbrace{X(X'X)^{-1} X'}_{H} Y$
    * $\hat{y}_i = h_{i1} y_1 + h_{i2} y_2 + \cdots + h_{ii} y_i + \cdots + h_{in} y_n$
    * $h_{ii} = X_i' (X'X)^{-1} X_i$ ($X_i$는 i번째 row)
        * 의미 : i번째 관측치의 레버리지
* Properties of leverage (레버리지의 성질)
    1) $\frac{1}{n} \le h_{ii} \le 1$
    2) $-0.5 \le h_{ij} \le 0.5$
    3) $\text{tr}(H) = \sum_{i=1}^n h_{ii} = p+1$
        * $(\text{for model } Y_i = \beta_0 + \beta_1 x_{1i} + \cdots + \beta_p x_{pi} + \epsilon_i)$

### 중심화된 관측치 (Centered Observations)
$Y_i^* = Y_i - \bar{Y}, \quad X_{ij}^* = X_{ij} - \bar{X}_j,$ $\text{where } \bar{X}_j = \frac{1}{n} \sum_{i=1}^n X_{ij}, \quad \bar{Y} = \frac{1}{n} \sum_{i=1}^n Y_i$

### 중심화된 관측치를 이용한 모형 (Model with Centered Observations)
* **표현:**
    * $Y_i - \bar{Y} = \beta_1 (X_{i1} - \bar{X}_1) + \cdots + \beta_p (X_{ip} - \bar{X}_p) + \epsilon_i$
    * $\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}_1 - \cdots - \hat{\beta}_p \bar{X}_p$
* **계수 벡터 분리:**
    * $\hat{\beta} = \begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \vdots \\ \hat{\beta}_p \end{pmatrix} \implies \hat{\beta}_C = \begin{pmatrix} \hat{\beta}_1 \\ \vdots \\ \hat{\beta}_p \end{pmatrix}$

* **중심화된 LSE $\hat{\beta}_C$**
    * $\hat{\beta}_C = (X_C' X_C)^{-1} X_C' (Y - \bar{Y} 1_n)$

* **중심화된 설명 변수 행렬 $X_C$**
    * $X_C = \begin{pmatrix} X_{11}-\bar{X}_1 & \cdots & X_{1p}-\bar{X}_p \\ \vdots & \ddots & \vdots \\ X_{n1}-\bar{X}_1 & \cdots & X_{np}-\bar{X}_p \end{pmatrix}_{n \times p}$
* **중심화된 행렬의 특성:**
    * $1_n' X_C^{(j)} = \sum_{i=1}^n (X_{ij} - \bar{X}_j) = 0$ (각 열 벡터의 합이 0이다.)
* **$\hat{Y}$와 $Y-\bar{Y} 1_n$의 관계**
    * $\hat{Y} = H Y = X(X'X)^{-1} X' Y$
    * $Y - \bar{Y} 1_n$ (중심화된 $Y$ 벡터)
      $=X_C \hat{\beta}_C =X_C (X_C' X_C)^{-1} X_C' Y$
* **Centered (중심화된) 데이터를 이용한 $\hat{Y}$ 표현**
    * $\hat{Y} = \bar{Y} 1_n + X_C (X_C' X_C)^{-1} X_C' Y$
        * $\bar{Y} = \frac{1}{n} \sum_{i=1}^n Y_i = \frac{1}{n} 1_n' Y$
* **$\hat{Y}$ 전개 및 $H$ 행렬 유도** (증)
    * $\hat{Y} = \left(\frac{1}{n} 1_n 1_n' + X_C (X_C' X_C)^{-1} X_C'\right) Y$
* **$H$ 행렬 정의**
    * $\implies H = X (X'X)^{-1} X'$ $= \left(\frac{1}{n} \underbrace{1_n 1_n'}_{\frac{1}{n}\leq h_{ii}\leq1} + \underbrace{X_C (X_C' X_C)^{-1}}_{H_C} X_C'\right)$
        * $H_C$ : 대칭행렬, idempotent

### Hat Matrix $H$의 성질 유도

* $\mathbf{H} = \frac{1}{n} 1_n 1_n' + H_C$

#### 1. $h_{ii} \ge \frac{1}{n}$ 유도 (최소값)

* $h_{ii} = e_i' H e_i = e_i' \left(\frac{1}{n} 1_n 1_n' + H_C\right) e_i$
* $e_i: I_n \text{ 행렬의 } i \text{번째 열 (basis vector)}$
* $h_{ii} = \frac{1}{n} (e_i' 1_n) (1_n' e_i) + e_i' H_C e_i$
* $h_{ii} = \frac{1}{n} \cdot 1 \cdot 1 + e_i' H_C e_i$
* $h_{ii} = \frac{1}{n} + e_i' H_C e_i$
    * $H_C$는 양의 준정부호 행렬 (Positive Semidefinite Matrix)
    * $e_i' H_C e_i \ge 0$
* $\implies h_{ii} \ge \frac{1}{n}$

#### 2. $h_{ii} \le 1$ 유도 (최대값)

* $\text{*} H \text{는 멱등 행렬(Idempotent) }$

---

## 12. interactions and qualitative variable

### Two-Group Mean Comparison (Regression Approach)
* **Matrix Formulation ($Y = X\beta + \epsilon$):**
    * $Y$: 두 그룹 ($Z, W$)의 결합 벡터.
    * $X$: 1로 구성된 블록 대각 행렬(Block diagonal with 1s).
    * **Hypothesis:** $H_0: \beta_1 = \beta_2 \iff H_0: \mu_1 = \mu_2$
* **Dummy Variable Approach:**
    * Model: $Y_i = \beta_0 + \beta_1 X_i + \epsilon_i$
    * $X_i$: 그룹 2에 대한 지시 변수(Indicator for Group 2).
    * Interpretation: $\beta_0 = \mu_1$, $\beta_1 = \mu_2 - \mu_1$.
    * Test: $H_0: \beta_1 = 0$은 동일 평균을 검정하는 것과 동치임.

### Three-Group Linear Trend Model
* **Model:** $Y_i = \beta_0 + \beta_1 x_i + \epsilon_i$ w/ $x_i \in \{1, 2, 3\}$.
* **Mean Structure:** $\mu_k = \beta_0 + k\beta_1$.
    * **Assumption:** 그룹 인덱스와 평균 간의 선형 관계 가정 ($\mu_{k+1} - \mu_k = \beta_1$).

### Three-Group One-Way ANOVA (Regression Formulation)
* **Model:** $Y_i = \mu_1 + (\mu_2-\mu_1)E_{i2} + (\mu_3-\mu_1)E_{i3} + \epsilon_i$
* **Matrix Form:** $Y = X\beta + \epsilon$, where $X = [1, E_2, E_3]$.
* **Equivalence:**
    * 회귀에서의 $H_0: \beta_1 = \beta_2 = 0$ $\iff$ ANOVA에서의 $H_0: \mu_1 = \mu_2 = \mu_3$.

### Cell Means Model & Perfect Multicollinearity
* **Problem:** 절편($\mathbf{1}$)과 모든 그룹 지시 변수($E_1, E_2, E_3$)를 포함할 경우.
    * $\mathbf{1} = \sum E_i \implies$ 선형 종속(Linear Dependence) $\implies X'X$ 특이 행렬(Singular).
* **Solution (Cell Means Model):** 절편 제거.
    * $Y = (E_1, E_2, E_3)(\mu_1, \mu_2, \mu_3)' + \epsilon$.
    * **hint:** $X'X$가 역행렬을 가지려면 열벡터들이 선형 독립이어야 함.

### 계산 팁 (강의 14-2)
* **Dummy Variable Trap:**
    * $k$개 범주 구분 시 반드시 **$k-1$개** 더미변수만 사용 (상수항 포함 시).
    * **Baseline (Reference):** 더미변수가 모두 0인 그룹. 모든 해석은 Baseline 대비 효과로 해석.
    * **Example:** 휘발유(Base), 디젤($E_1$), 하이브리드($E_2$).
        * $Y = \beta_0 + \beta_1 E_1 + \beta_2 E_2$.
        * 디젤 vs 하이브리드 비교: $H_0: \beta_1 = \beta_2$.
* **Hypothesis Construction Strategy:**
    * "국산($D=1$) 하이브리드($H=1$)가 외제($D=0$) 디젤($H=0$)보다 연비가 좋은가?" 
    * Model: $Y = \beta_0 + \beta_1 D + \beta_2 H + \beta_3 (D \times H)$.
    * **Construct Means:**
        * 국산 하이브리드: $\beta_0 + \beta_1 + \beta_2 + \beta_3$.
        * 외제 디젤: $\beta_0$. (H=0이므로 하이브리드 관련 항 0, D=0이므로 국산 관련 항 0)
    * **Correct Logic (General):** 항상 $E(Y|Condition)$을 계수들의 합으로 표현한 뒤 차이를 검정.
* **Pitfall Warning (Causality):**
    * 문제: "무게가 증가할수록 연비가 감소하는가?"
    * 모델 선택 시 $Y=$연비, $X=$무게 인 모델을 골라야 함. 반대로 $Y=$무게 인 모델(Model D in Audio)은 인과관계가 반대이므로 기각.
### salary example (stratification)
- 매니저 여부, 학력수준 (고/대/석)졸 2\*3=6가지 케이스중 각 E와 M의 조합에 따라 모델을 6개로 분리

#### Use qualitative variables (케이스마다 서로 다른 절편)
- 또는 6가지의 경우의 수를 dummy variable을 사용해 나타낼 수 있음
    - (각 관측치는 동분산 $\sigma^2$을 가정)
    - $S_i = \beta_0 + \beta_1 X_i + \beta_2 E_{i2} + \beta_3 E_{i3} + \beta_4 M_i + \epsilon_i$
    - $E_{i2} = \begin{cases} 1 & \text{if } E_i=2 \\ 0 & \text{otherwise.},\quad \end{cases}E_{i3} = \begin{cases} 1 & \text{if } E_i=3 \\ 0 & \text{otherwise.},\quad \end{cases}$ $M_{i} = \begin{cases} 1 & \text{if } M \\ 0 & \text{otherwise.}\quad \end{cases}$
- 절편에 dummy var 추가 시 : 경우의 수가 3개라면, 하나를 디폴트 케이스, dummy var은 2개만 쓴다

#### Interactions (케이스마다 서로 다른 기울기)
$S_i = \beta_0 + \beta_1 X_i + \beta_2 E_{i2} + \beta_3 E_{i3} + \beta_4 M_i$
$+ \beta_5 E_{i2} X_i + \beta_6 E_{i3} X_i + \epsilon_i$

### Connection to One-way ANOVA
* **Regression with Dummy Variables $\approx$ One-way ANOVA**
    * 더미 변수를 이용한 회귀는 One-way ANOVA와 수학적으로 동치.
* **가설 검정**
    * $H_0: \beta_2 = \beta_3 = \dots = 0$ (모든 더미 계수가 0)
    * $\iff H_0: \mu_1 = \mu_2 = \dots = \mu_k$ (모든 그룹 평균이 동일)
    * F-test (Partial F-test)를 사용하여 검정.
* **Parameter Constraints (제약조건)**
    * 회귀식 추정을 위해 제약조건 필요 (Design Matrix가 Full Rank가 아님).
    1. **Baseline Constraint (Treatment Contrast)**: 특정 그룹(Base)의 효과를 0으로 둠. (R 기본값)
    2. **Sum-to-zero Constraint**: 모든 그룹 효과의 합을 0으로 둠 ($\sum \tau_i = 0$).

---

## 14. Correlated Errors

### AutoCorrelation & AR(1) Process
* **AR(1) Model:** $\epsilon_t = \rho \epsilon_{t-1} + w_t, \quad |\rho| < 1, \quad w_t \sim iid N(0, \sigma^2)$
* **Properties (Stationarity assumed):**
    * $E(\epsilon_t) = 0$
    * $Var(\epsilon_t) = \frac{\sigma^2}{1-\rho^2}$
        * **hint:** $\epsilon_t = \sum \rho^k w_{t-k}$로 전개하고 무한 등비 급수 분산 합 이용.
    * $Cov(\epsilon_t, \epsilon_{t-k}) = \rho^k \frac{\sigma^2}{1-\rho^2}$
    * $Corr(\epsilon_t, \epsilon_{t-k}) = \rho^k$

### Durbin-Watson Statistic ($d$)
* **Definition:** $d = \frac{\sum (e_t - e_{t-1})^2}{\sum e_t^2}$
* **Approximation:** $d \approx 2(1 - \hat{\rho})$
    * **hint:** 분자 $\sum e_t^2 + \sum e_{t-1}^2 - 2\sum e_t e_{t-1}$ 전개 및 큰 $n$에 대해 $\sum e_t^2 \approx \sum e_{t-1}^2$ 가정.
* **Decision Rules:**
    * $\hat{\rho} \approx 0 \implies d \approx 2$ (자기상관 없음).
    * $\hat{\rho} > 0 \implies d < 2$ (양의 상관).
    * $\hat{\rho} < 0 \implies d > 2$ (음의 상관).
    * 임계값 $d_L, d_U$ 사용.

### Regression with Autocorrelated Errors (Transformation)
* **Model:** $y_t = \beta_0 + \beta_1 x_t + \epsilon_t$ with AR(1) errors.
* **Transformed Variables ($y^*, x^*$):**
    * $y_t^* = y_t - \rho y_{t-1}$
    * $x_t^* = x_t - \rho x_{t-1}$
* **Resulting Model:** $y_t^* = \beta_0(1-\rho) + \beta_1 x_t^* + w_t$
    * 오차항 $w_t$는 이제 iid $N(0, \sigma^2)$ 임 (OLS 적용 가능).
    * **Simultaneous Estimation:** $\rho, \beta$에 대해 $\sum (y_t - \rho y_{t-1} - \dots)^2$ 를 최적화 가능 (Grid Search).

### $\rho$의 추정 (Unknown $\rho$)
* **Cochrane-Orcutt 절차 (반복법):**
    1. 원본 데이터에 OLS 수행 ($y_t = \beta_0 + \beta_1 x_t + \epsilon_t$).
    2. 잔차 $e_t$를 얻고 $\frac{\sum e_t e_{t-1}}{\sum e_{t-1}^2}$를 이용해 $\hat{\rho}$ 추정.
    3. 데이터 변환: $y_t^* = y_t - \hat{\rho} y_{t-1}, \quad x_t^* = x_t - \hat{\rho} x_{t-1}$.
    4. 변환된 데이터에 OLS를 수행하여 $\hat{\beta}$ 업데이트.
    5. 수렴할 때까지 반복.
* **탐색 방법 (Grid Search):**
    * $\rho$ 고정 (예: $0, 0.01, \dots, 0.99$).
    * 고정된 $\rho$에 대해 SSE를 최소화하는 $\beta$ 찾기.
    * 전역 최소 SSE를 주는 $\rho$ 선택.
    * **hint:** $\rho$가 고정되면 $\beta$ 추정은 Convex OLS 문제임.

### Generalized Least Squares (GLS)
* **Assumption:** $Var(\epsilon) = \Sigma$ (비대각, Non-diagonal).
* **Spectral Decomposition:** $\Sigma = U D U'$
    * 변환 행렬: $S = \Sigma^{-1/2} = U D^{-1/2} U'$
* **Transformed Model:** $\tilde{Y} = S Y, \quad \tilde{X} = S X, \quad \tilde{\epsilon} = S \epsilon$
    * $Var(\tilde{\epsilon}) = S \Sigma S' = I$ (등분산성 회복, Homoscedasticity restored).
* **GLS Estimator:** $\hat{\beta}_{GLS} = (X'\Sigma^{-1}X)^{-1}X'\Sigma^{-1}Y$
    * **hint:** 변환된 $\tilde{Y}, \tilde{X}$에 OLS 적용.


### Durbin-Watson Statistic ($d$)
* **Definition:** $d = \frac{\sum (e_t - e_{t-1})^2}{\sum e_t^2}$
* **Approximation:** $d \approx 2(1 - \hat{\rho})$
    * **hint:** Expand numerator $\sum e_t^2 + \sum e_{t-1}^2 - 2\sum e_t e_{t-1}$ and assume $\sum e_t^2 \approx \sum e_{t-1}^2$ for large $n$.
* **Decision Rules:**
    * $\hat{\rho} \approx 0 \implies d \approx 2$ (No Autocorrelation).
    * $\hat{\rho} > 0 \implies d < 2$ (Positive).
    * $\hat{\rho} < 0 \implies d > 2$ (Negative).
    * Use critical values $d_L, d_U$.
---
### Regression with Autocorrelated Errors (Transformation)
* **Model:** $y_t = \beta_0 + \beta_1 x_t + \epsilon_t$ with AR(1) errors.
* **Transformed Variables ($y^*, x^*$):**
    * $y_t^* = y_t - \rho y_{t-1}$
    * $x_t^* = x_t - \rho x_{t-1}$
* **Resulting Model:** $y_t^* = \beta_0(1-\rho) + \beta_1 x_t^* + w_t$
    * Error term $w_t$ is now iid $N(0, \sigma^2)$ (OLS applicable).
    * **Simultaneous Estimation:** Can optimize $\sum (y_t - \rho y_{t-1} - \dots)^2$ over $\rho, \beta$ (Grid Search).

### Estimation of $\rho$ (Unknown $\rho$)
* **Cochrane-Orcutt Procedure (Iterative):**
    1. Run OLS on original data ($y_t = \beta_0 + \beta_1 x_t + \epsilon_t$).
    2. Obtain residuals $e_t$ and estimate $\hat{\rho}$ using $\frac{\sum e_t e_{t-1}}{\sum e_{t-1}^2}$.
    3. Transform data: $y_t^* = y_t - \hat{\rho} y_{t-1}, \quad x_t^* = x_t - \hat{\rho} x_{t-1}$.
    4. Run OLS on transformed data to updated $\hat{\beta}$.
    5. Iterate until convergence.
* **Search Method (Grid Search):**
    * Fix $\rho$ (e.g., $0, 0.01, \dots, 0.99$).
    * Find $\beta$ minimizing SSE for that fixed $\rho$.
    * Select $\rho$ that gives global minimum SSE.
    * **hint:** $\rho$가 고정되면 $\beta$ 추정은 Convex OLS 문제임.

### Generalized Least Squares (GLS)
* **Assumption:** $Var(\epsilon) = \Sigma$ (Non-diagonal).
* **Spectral Decomposition:** $\Sigma = U D U'$
    * Transformation Matrix: $S = \Sigma^{-1/2} = U D^{-1/2} U'$
* **Transformed Model:** $\tilde{Y} = S Y, \quad \tilde{X} = S X, \quad \tilde{\epsilon} = S \epsilon$
    * $Var(\tilde{\epsilon}) = S \Sigma S' = I$ (Homoscedasticity restored).
* **GLS Estimator:** $\hat{\beta}_{GLS} = (X'\Sigma^{-1}X)^{-1}X'\Sigma^{-1}Y$
    * **hint:** Just Apply OLS to transformed $\tilde{Y}, \tilde{X}$.

---

## 15. Model Selection
#### Outline (Model Selection)
- 회귀 상황에서 Y와 X가 centered 되었다 가정. : $Y_{(n\times 1)}=X_{(n\times p)}\beta_{(p\times 1)} + \epsilon_{(n\times 1)}$
- 부분집합 $A\subset\{1,\cdots,p\}$에 대해 새 회귀 모형 :$M(A) : Y_{(n\times 1)}=X[,A]\beta[A] + \epsilon_{(n\times 1)}$
    - ($\beta[A^c]=0$라 세팅;    총 가능한 모델선택은 $2^p$)
    - 모델선택 $\to$ 1) 어떤 기준?    2) 어떻게 탐색?(p가 크면 전수조사 어렵)

#### Problem & Goals (문제 및 목표)
- $x_1,x_2,x_3$에 대해, $x_3 = [x_{31},\cdots,x_{39}]$;  가능한 모델 갯수=29
    1) $x_1,x_2,x_{31},\cdots,x_{39}\to11$개;
  2) $x_1x_{31},\cdots,x_1x_{39}\to9$개
  3) $x_2x_{31},\cdots,x_2x_{39}\to9$개
    - main effect(1) + interactions (2),(3)
#### Justifying parsimony (검약성의 정당성)
- Principle of parsimony(오컴의 면도날)
    - p개의 설명변수로 설명 가능한 모델보단 j(j<p)개의 설명변수로 설명 가능한 모델이 최선.
- 예시) (model 1) :
$Y_i=\beta_1x_{i1}+\beta_2x_{i2}+\epsilon_i;\quad(\beta_2=0)$
    - $Var(\hat{\beta}_1^{M1})=\sigma^2((X'X)^{-1})_{11}$
      $=\frac{\sigma^2S_{2,2}}{S_{1,1}S_{2,2}-S_{1,2}^2}$
        - hint : $\text{let }S_{a,b}=\sum_{i=1}^n x_{ia}x_{ib}$ ; $X,\,X'X,\,X'Y$ 행렬 정의, 역행렬 정의 
- (model 2) : $Y_i=\beta_1x_{i1}+\epsilon_i$ ;    $Var(\hat{\beta}_1^{M2})=\frac{\sigma^2}{S_{1,1}}$
    - $Var(\hat{\beta}_1^{M1})/Var(\hat{\beta}_1^{M2})$
      $=1+\frac{S_{1,2}^2}{S_{1,1}S_{2,2}-S_{1,2}^2}\ge1$
        - hint : 코시-슈바르츠 부등식 : $S_{1,1}S_{2,2}\ge S_{1,2}^2$
### Candidate criteria (후보 기준)
##### Candidate criteria
- $R^2$ : 좋은 평가 지표X; 단순히 파라미터 갯수가 늘어도 증가함
- $adj.R^2$ : 더 나은 평가 지표; 과적합을 일부 방지;
- Mallow's $C_p$ : 모델의 예측력을 평가함 (새 관측치에 대한 예측력)
- (실무) : AIC(예측), BIC(true model), Cross-validation 등 평가 지표
##### Mallow's $C_p$
- $C_p(M)=\frac{SSE(M)}{\hat{\sigma}^2}+2p_M-n$    ($p_M :$ \# of params in Model) 
    - $=\frac{S_A-\hat{\sigma}^2}{\hat{\sigma}^2/(n-p_M)}+p_M$;
        $\text{if }S_A^2\to\hat{\sigma}^2,\text{ then }C_p(M(A))\to p_M$
    - hint : $S_A^2 = SSE(M(A))/(n-p_M)$라 하자;    $p_M$ : 모델 M의 예측변수 개수.

##### AIC (Akaike Information Criterion) 유도 (Derivation)
* **Likelihood Function ($L(\beta)$):**
    * Model: $Y_i = x_i'\beta + \epsilon_i, \quad \epsilon_i \sim iid \ N(0, \sigma^2)$
    * $L(\beta) = (2\pi\sigma^2)^{-\frac{n}{2}} \exp\left\{-\frac{1}{2\sigma^2} \sum (y_i - x_i'\beta)^2\right\}$
* **Log-Likelihood:**
    * $\log L(\beta) = -\frac{n}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2} SSE$
* **AIC Definition:**
    * $AIC = -2 \log L(\hat{\beta}) + 2p$
    * MLE $\hat{\sigma}^2 = SSE/n$ 이용:
        * $-2 \log L(\hat{\beta}) = n \log(2\pi\hat{\sigma}^2)$ $+ \frac{1}{\hat{\sigma}^2} SSE = n \log(2\pi\hat{\sigma}^2) + n$
    * $\Rightarrow AIC = n \log(SSE/n) + 2p + \text{const}$ (상수는 비교 시 종종 무시됨).
---
### Search strategies (탐색 전략)

| start                    | step 1   | ...        | step p      |
| ------------------------ | -------- | ---------- | ----------- |
| $Y_i=\beta_0+\epsilon_i$ | $+X_1$   |            |             |
|                          | $\vdots$ | $\implies$ | 1스탭에 1개씩 추가 |
| (Forward Selection)       | $+X_p$   |            | 개선X? stop   |

-

| start                                              | step 1   | ...        | step p      |
| -------------------------------------------------- | -------- | ---------- | ----------- |
| $Y_i=\beta_0$$+\sum_{j=1}^p\beta_jX_{ij}$$+\epsilon_i$ | $-X_1$   |            |             |
|                                                    | $\vdots$ | $\implies$ | 1스탭에 1개씩 추가 |
| (Backward Elimination)                               | $-X_p$   |            | 개선X? stop   |
-
-
-
| start                | step 1     | step 2           | ...        | step p              |
| -------------------- | ---------- | ---------------- | ---------- | ------------------- |
|                      | ex) foward | ex) $X_1$ choice |            |                     |
| (Forward or Backward)  | $+X_1$     | $+X_2$           |            |                     |
|         | $+X_2$     | $\vdots$         | $\implies$ | for, back 둘 중 하나 따름 |
|                      | $\vdots$   | $+X_p$           |            | 다음 스탭에 이전걸 뺄지 결정    |
| (Stepwise Selection) | $+X_p$     | (선택 : $-X_1$)    |            |                     |
- 계산비용 : 총 p개의 step중 step j에서 p-j+1개의 모형 적합
    - (모형의 수)
  $= \sum_{j=1}^pp-j+1=\sum_{j=1}^pj=p(p+1)/2$

---

## 16. Penalized Regression

### 다중공선성 진단 (Multicollinearity Diagnostics)
* **VIF (분산 팽창 요인):**
    * $VIF_j = \frac{1}{1-R_j^2}$
    * $R_j^2$: $X_j$를 다른 설명변수들에 대해 회귀했을 때의 $R^2$.
    * **Criterion:** $VIF > 10 \implies$ Severe(심각).
* **Condition Number ($k$):**
    * $k = \sqrt{\frac{\lambda_{max}}{\lambda_{min}}}$, 여기서 $\lambda$는 $X'X$ (또는 상관 행렬)의 고유값.
    * **Criterion:** $k > 15 \sim 30 \implies$ Problematic(문제 있음).

### Penalized Regression Concepts
* **Idea:** MSE를 최소화하기 위해 편향(Bias)을 희생하여 분산(Variance)을 낮추는 상충 관계(Trade-off) 활용.
* **Ridge Regression ($L_2$ Penalty):**
    * Minimize: $\sum (y_i - x_i'\beta)^2 + \lambda \sum_{j=1}^p \beta_j^2$
    * **Effect:** 계수를 0으로 수축시키지만 완전히 0이 되지는 않음. 다중공선성 해결 ($X'X + \lambda I$ 역행렬 존재).
* **Lasso Regression ($L_1$ Penalty):**
    * Minimize: $\sum (y_i - x_i'\beta)^2 + \lambda \sum_{j=1}^p |\beta_j|$
    * **Effect:** 계수를 **정확히 0**으로 수축 가능 (변수 선택).
    * **Geometry:** 제약 영역이 다이아몬드($\diamond$) 형태. 코너 솔루션(Corner solution) 발생 가능성 높음.
* **Bias-Variance Trade-off:**
    * MSE = $Bias^2 + Variance$.
    * 벌점 모델은 편향($\lambda > 0$, 0으로 편향된 추정)을 도입하지만 분산을 크게 줄여 종종 더 낮은 MSE를 유도함.
    * **hint:** OLS는 비편향(Bias=0)이지만 분산이 클 수 있음 (특히 다중공선성 존재 시). 벌점화는 약간의 편향을 대가로 큰 분산 감소를 얻음.
