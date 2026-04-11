- Covarience and Corelation Coeffient (for r.v. $(X_i,Y_i),\forall i\in\mathbb{N}; X\sim(\mu_x,\sigma_x^2),Y\sim(\mu_Y,\sigma_Y^2);$)
- Covariance : $\text{COV}(X,Y) = E[(X-\mu_x)(Y-\mu_y)]$
	- $S_{xx}=\sum_{i=1}^n x_i^2-n \bar{x}^2=\sum_{i=1}^n (x_i-\bar{x})^2 \quad S_{yy}\sum_{i=1}^n (y_i- \bar{y})^2\quad S_{xy}=\sum_{i=1}^n x_iy_i-n \bar{x}\bar{y}$
	- $\hat{\text{COV}}(X,V)=\frac{\sum_{i=1}^{n}(X_i-\bar{X})(Y_i-\bar{Y})}{n-1}=\frac{1}{n-1}S_{xy}$
- Corelation coeffieient : $\rho=\frac{E(X-\mu_x)(Y-\mu_Y)}{\sigma_X\sigma_Y}=\frac{E(XY)-E(X)E(Y)}{\sigma_X\sigma_Y}$; (if X,Y are independent, $E(XY)=E(X)E(Y).\to\rho=0$)
	- Sample Pearson's correlation coeffiecint : $\hat{\text{Cor}}(X,Y)=\hat{\rho}=r=\frac{\sum_{i=1}^{n}(X_i-\bar{X})(Y_i-\bar{Y})}{\sqrt{\sum_{i=1}^{n}(X_i-\bar{X})^2\sum_{i=1}^{n}(Y_i-\bar{Y})^2}}=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}=\frac{S_{xy}/(n-1)}{S_xS_y}\quad \text{where}\,S_x=\sqrt{S_{xx}/(n-1)}$
	- $\text{with }z_x=(x-\bar{x})/s_x\,\text{and}\,z_y=(y-\bar{y})/s_y, Cor(X,Y)=Cov(z_X,z_Y)=Cor(z_X,z_Y)$
- Spearman's rank correlation coef. :
  $(X_1,Y_1),\cdots,(X_n,Y_n)\to(R_{X_{11}},R_{Y_{11}}),\cdots,(R_{X_{1n}},R_{Y_{1n}}); \quad R_{X_{1i}},R_{Y_{1i}}\text{는 각각}X_i,Y_i\text{의 Rank}$
  $\hat{r}_s=\frac{\text{COV}(R_X,R_Y)}{\sigma_{R_{X}}\sigma_{R_{Y}}}$
- kendall's tar($\tau$) :
	- $\text{Concordant pair}:\left.\begin{matrix}x_i<x_j\,\&\,y_i<y_j \\x_i>x_j\,\&\,y_i>y_j\end{matrix}\right\}a_{ij}= I((x_i-x_j)(y_i-y_j)>0)$
	- $\text{Discordant pair}:\left.\begin{matrix}x_i<x_j\,\&\,y_i>y_j \\x_i>x_j\,\&\,y_i<y_j\end{matrix}\right\}b_{ij}= I((x_i-x_j)(y_i-y_j)<0)$
	- kendall's tar($\tau$) : $\tau=\frac{\sum_{i<j}^{}a_{ij}-\sum_{i<j}^{}b_{ij}}{\sum_{i<j}^{}(a_{ij}^2+b_{ij}^2)}$
---
###### Introduction to Simple Linear Regression
- 단순선형회귀 모델은 scatter plot 위의 직선을 각 slice의 평균 도출해 최적화하는 방식
	- 모집단에서 새로운 딸의 키를 추정하려함 -> slice of data를 고려하여 가능
	- slice of data : 데이터를 구간별로 자름 ($M_{new}\text{에 대해}D_{new}\text{를 추정시, }M=66\to65\leq M \leq 67$)
	- $(\text{slice M의 평균})\to\beta_{0}+\beta_{1}M;\quad {D=f(M)+\epsilon};$
	  $(\text{f는 엄키에 대해 딸키의 평균, }\epsilon\text{은 slice의 random variation})$
- simple linear regression model
	- $Y_i = \underbrace{\hat{\beta}_0 + \hat{\beta}_1 X_i}_{\text{regression equation}} + \underbrace{\epsilon_i}_{\text{error}}+\text{iid}\;\epsilon_i \sim N(0, \sigma^2)$ ; iid = identically independently distributed
- Fitting the model
	- 최소제곱법은 이식을 최소화 하는 직선을 선택 : $\text{SSE}(\beta_0, \beta_1) = \sum_{i=1}^n (Y_i - \beta_0 - \beta_1 X_i)^2 \quad$
	- 편차의 절댓값 합계(sum of absolute deviation) : $\text{SAD}(\beta_0, \beta_1) = \sum_{i=1}^n |Y_i - \beta_0 - \beta_1 X_i|$
	- 손실함수로 채택 : $L(\beta_0, \beta_1) = \sum_{i=1}^n L(Y_i - \beta_0 - \beta_1 X_i)$
---
### 통계학 - 압축 노트


