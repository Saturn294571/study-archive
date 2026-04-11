###### Estimation 
- 벡터형태의 미분 : $\underset{\sim}{a}=(a_1,a_2)^T,\underset{\sim}{x}=(x_1,x_2)^T,  \underset{\sim}{a}^T\underset{\sim}{x}=a_1x_1+a_2x_2=f(\underset{\sim}{x})$
	1) $\frac{\partial f}{\partial \underset{\sim}{x}}=\begin{pmatrix}\frac{\partial f}{\partial x_1}\\ \frac{\partial f}{\partial x_x}\end{pmatrix}=\triangledown f(\underset{\sim}{x})\,(\text{gradient of }f(\underset{\sim}{x})) \to \frac{\partial \left(\mathbf{a}^{\intercal}\mathbf{x}\right)}{\partial \mathbf{x}} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} = \underset{\sim}{a} = \frac{\partial \left(\mathbf{x}^{\intercal}\mathbf{a}\right)}{\partial \mathbf{x}}$
	2) $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \quad \underset{\sim}{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \\ \quad f(\underset{\sim}{x}) = A\underset{\sim}{x} = \begin{pmatrix} a_{11}x_1 + a_{12}x_2 \\ a_{21}x_1 + a_{22}x_2 \end{pmatrix}$
		- $\frac{\partial \mathbf{f}}{\partial \underset{\sim}{x}} = \begin{pmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_2}{\partial x_1} \\ \frac{\partial f_1}{\partial x_2} & \frac{\partial f_2}{\partial x_2} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{21} \\ a_{12} & a_{22} \end{pmatrix} = A^{\intercal}$
			- $\frac{\partial (A\underset{\sim}{x})}{\partial \underset{\sim}{x}} = A^{\intercal}, \quad \frac{\partial (\underset{\sim}{x}^{\intercal}A)}{\partial \underset{\sim}{x}} = A$
		- $g(\underset{\sim}{x}) = \underset{\sim}{x}^{\intercal}A = (a_{11}x_1 + a_{21}x_2, \quad a_{12}x_1 + a_{22}x_2), \quad \frac{\partial g}{\partial \underset{\sim}{x}} = \begin{pmatrix} \frac{\partial g_1}{\partial x_1} & \frac{\partial g_2}{\partial x_1} \\ \frac{\partial g_1}{\partial x_2} & \frac{\partial g_2}{\partial x_2} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = A$
- 이차형식 (quadratic form) : $\forall \underset{\sim}{x} \in \mathbb{R}^n, \forall A \in \mathbb{R}^{n \times n}, \quad \underset{(1\times n),\, (n\times n),\, (n\times 1)}{\underbrace{\underset{\sim}{x}^{\intercal}A\underset{\sim}{x} }}= \sum_{i=1}^n \sum_{j=1}^n a_{ij}x_i x_j$
	- $\text{ex) } \underset{\sim}{x} = (x_1, x_2)^{\intercal}, A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}; \quad \underset{\sim}{x}^{\intercal}A\underset{\sim}{x} = \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$
	  $= \begin{pmatrix} a_{11}x_1 + a_{21}x_2 & a_{12}x_1 + a_{22}x_2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = a_{11}x_1^2 + a_{21}x_1x_2 + a_{12}x_1x_2 + a_{22}x_2^2$
- $\frac{\partial (\underset{\sim}{x}^{\intercal}A\underset{\sim}{x})}{\partial \underset{\sim}{x}} = \begin{pmatrix} \frac{\partial (\underset{\sim}{x}^{\intercal}A\underset{\sim}{x})}{\partial x_1} \\ \frac{\partial (\underset{\sim}{x}^{\intercal}A\underset{\sim}{x})}{\partial x_2} \end{pmatrix} = \begin{pmatrix} 2a_{11}x_1 + (a_{12}+a_{21})x_2 \\ 2a_{22}x_2 + (a_{12}+a_{21})x_1 \end{pmatrix}$
  $= \begin{pmatrix} a_{11}x_1 + a_{12}x_2 \\ a_{21}x_1 + a_{22}x_2 \end{pmatrix} + \begin{pmatrix} a_{11}x_1 + a_{21}x_2 \\ a_{12}x_1 + a_{22}x_2 \end{pmatrix}= A\underset{\sim}{x} + A^{\intercal}\underset{\sim}{x}$
	- $\text{** If } A \text{ is symmetric, } \quad \frac{\partial (\underset{\sim}{x}^{\intercal}A\underset{\sim}{x})}{\partial \underset{\sim}{x}} = 2A\underset{\sim}{x} \quad$ 
	  $\text{** tr}(A) = \sum_{i=1}^n a_{ii},\quad \text{tr}(\underset{\sim}{x}^{\intercal}A\underset{\sim}{x}) = \underset{\sim}{x}^{\intercal}A\underset{\sim}{x}\to\text{tr}(A\underset{\sim}{x}\underset{\sim}{x}^{\intercal})$
- LSE : $\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 = \sum_{i=1}^n \epsilon_i^2, \quad \underset{\sim}{\epsilon} = (\epsilon_1, \epsilon_2, \dots, \epsilon_n)^{\intercal}$
  $\underset{\sim}{y} = (y_1, y_2, \dots, y_n)^{\intercal}, \quad \mathcal{X} = (\mathbb{1}_n, \underset{\sim}{x_1}), \quad \underset{\sim}{x_1} = (x_1, x_2, \dots, x_n)^{\intercal}, \quad \underset{\sim}{\epsilon} = \underset{\sim}{y} - \mathcal{X}\underset{\sim}{\beta}, \quad \underset{\sim}{\beta} = (\beta_0, \beta_1)^{\intercal}$
	- $\rightarrow \text{SSE}(\beta_0, \beta_1) = \underset{\sim}{\epsilon}^{\intercal}\underset{\sim}{\epsilon} = (\underset{\sim}{y} - \mathcal{X}\underset{\sim}{\beta})^{\intercal}(\underset{\sim}{y} - \mathcal{X}\underset{\sim}{\beta}) = \underset{\sim}{y}^{\intercal}\underset{\sim}{y} - \underset{\sim}{\beta}^{\intercal}\mathcal{X}^{\intercal}\underset{\sim}{y} - \underset{\sim}{y}^{\intercal}\mathcal{X}\underset{\sim}{\beta} + \underset{\sim}{\beta}^{\intercal}\mathcal{X}^{\intercal}\mathcal{X}\underset{\sim}{\beta}$
	  $\frac{\partial (\underset{\sim}{\epsilon}^{\intercal}\underset{\sim}{\epsilon})}{\partial \underset{\sim}{\beta}} = 0 - \mathcal{X}^{\intercal}\underset{\sim}{y} - \mathcal{X}^{\intercal}\underset{\sim}{y} + 2\mathcal{X}^{\intercal}\mathcal{X}\underset{\sim}{\beta} = 0, \quad \mathcal{X}^{\intercal}\mathcal{X}\underset{\sim}{\beta} = \mathcal{X}^{\intercal}\underset{\sim}{y}, \quad$
	  $\text{if } \mathcal{X} \text{ is full rank (i.e., }\mathcal{X}^{\intercal }\mathcal{X}\text{ is nonsingular)}, \quad \hat{\underset{\sim}{\beta}} = (\mathcal{X}^{\intercal}\mathcal{X})^{-1}\mathcal{X}^{\intercal}\underset{\sim}{y}$
	- $\mathbf{X} = \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{pmatrix}, \quad \underset{\sim}{x_1}^{\intercal} = (x_{11}, x_{12}), \quad \underset{\sim}{x_2}^{\intercal} = (x_{21}, x_{22}), \quad \underset{\sim}{x_3}^{\intercal} = (x_{31}, x_{32}),$
	   $\mathbf{X}^{\intercal}\mathbf{X} = \begin{pmatrix} x_{11} & x_{21} & x_{31} \\ x_{12} & x_{22} & x_{32} \end{pmatrix} \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{pmatrix} = \begin{pmatrix} \sum_{i=1}^3 x_{i1}^2 & \sum_{i=1}^3 x_{i1}x_{i2} \\ \sum_{i=1}^3 x_{i1}x_{i2} & \sum_{i=1}^3 x_{i2}^2 \end{pmatrix},$
	   $\underset{\sim}{x_1}\underset{\sim}{x_1}^{\intercal} = \begin{pmatrix} x_{11} \\ x_{12} \end{pmatrix}(x_{11}, x_{12}) = \begin{pmatrix} x_{11}^2 & x_{11}x_{12} \\ x_{11}x_{12} & x_{12}^2 \end{pmatrix},$
	   $\underset{\sim}{x_1}\underset{\sim}{x_1}^{\intercal} + \underset{\sim}{x_2}\underset{\sim}{x_2}^{\intercal} + \underset{\sim}{x_3}\underset{\sim}{x_3}^{\intercal} = \begin{pmatrix} \sum_{i=1}^3 x_{i1}^2 & \sum_{i=1}^3 x_{i1}x_{i2} \\ \sum_{i=1}^3 x_{i1}x_{i2} & \sum_{i=1}^3 x_{i2}^2 \end{pmatrix} = \mathbf{X}^{\intercal}\mathbf{X}$
	   $\text{normally, }\mathbf{X} \in \mathbb{R}^{n \times p}, \quad \mathbf{X} = \begin{pmatrix} \underset{\sim}{x_1}^{\intercal} \\ \vdots \\ \underset{\sim}{x_n}^{\intercal} \end{pmatrix}, \quad \mathbf{X}^{\intercal}\mathbf{X} = \sum_{i=1}^n \underset{\sim}{x_i}\underset{\sim}{x_i}^{\intercal}$
   - Properties of LSE : $e_i \ (\text{residual}) = Y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i \neq \epsilon_i \ (\text{true error})$
	   - $\sum_{i=1}^n e_i = 0 \to \frac{\partial \text{SSE}}{\partial \beta_0} = \sum_{i=1}^n (Y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)(-1) = 0$
	 $\sum_{i=1}^n x_i e_i = 0\to\frac{\partial \text{SSE}}{\partial \beta_1} = \sum_{i=1}^n (Y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)(-x_i) = 0$
	 $\sum_{i=1}^n \hat{y}_i e_i = 0\to\sum_{i=1}^n (\hat{\beta}_0 + \hat{\beta}_1 x_i)e_i = \sum_{i=1}^n \hat{\beta}_0 e_i + \sum_{i=1}^n \hat{\beta}_1 x_i e_i$
	 $= \hat{\beta}_0 \sum_{i=1}^n e_i + \hat{\beta}_1 \sum_{i=1}^n x_i e_i = 0$
	+ LSE의 기하학적 의미 : LSE는 $\epsilon^\intercal\epsilon=||\epsilon||_2^2$ 를 최소. e는 전부
		+ Column space of $\mathbb{X}=(\mathbb{1}_n,\underset{\sim}{x}) \to C(\mathbb{X}); e\text{는 }C(\mathbb{X})\text{와 모두 직교}$
		+ $(1) \quad \underset{\sim}{e}^{\intercal}\mathbb{1}_n = 0 \rightarrow \sum_{i=1}^n e_i = 0, \quad$ $(2) \quad \underset{\sim}{x}^{\intercal}\underset{\sim}{e} = 0 \rightarrow \sum_{i=1}^n x_i e_i = 0, \quad$
		  $(3) \quad \hat{\underset{\sim}{y}}^{\intercal}\underset{\sim}{e} = 0 \rightarrow \sum_{i=1}^n \hat{y}_i e_i = 0, \quad \therefore \mathbb{1}_n, \underset{\sim}{x}, \quad \hat{\underset{\sim}{y}} \in C(\mathcal{X}), \quad \text{and } \underset{\sim}{e} \perp C(\mathcal{X})$
+ Distribution of $\hat{\beta}_1$
	+ $\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}} = \frac{1}{S_{xx}}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) = \frac{1}{S_{xx}}\sum_{i=1}^n (x_i - \bar{x}) y_i = \sum_{i=1}^n \left(\frac{x_i - \bar{x}}{S_{xx}}\right)y_i$$
	  $= \sum_{i=1}^n C_i y_i, \quad C_i = \frac{x_i - \bar{x}}{S_{xx}}$
	  $\text{Since } y_i\text{'s are independent,} \quad Y_i \sim N(\beta_0 + \beta_1 x_i, \sigma^2), \quad C_i Y_i \sim N(C_i(\beta_0 + \beta_1 x_i), C_i^2 \sigma^2)$
	+ $E\left(\sum_{i=1}^n C_i Y_i\right) = \sum_{i=1}^n C_i E(Y_i) = \sum_{i=1}^n C_i(\beta_0 + \beta_1 x_i)$
	  $= \beta_0 \overset{(1)}{\sum_{i=1}^n C_i} + \beta_1 \overset{(2)}{\sum_{i=1}^n C_i x_i} = 0 \cdot \beta_0 + 1 \cdot \beta_1 = \beta_1$
		+ $(1) \quad \sum_{i=1}^n C_i = \sum_{i=1}^n \frac{(x_i - \bar{x})}{S_{xx}} = \frac{1}{S_{xx}}\sum_{i=1}^n (x_i - \bar{x}) = 0,$
		  $(2) \quad \sum_{i=1}^n C_i x_i = \sum_{i=1}^n \frac{(x_i - \bar{x})x_i}{S_{xx}} = \frac{1}{S_{xx}}\sum_{i=1}^n (x_i - \bar{x})x_i = 1$
			+ $\text{**} \quad \sum_{i=1}^n C_i^2 = \sum_{i=1}^n \frac{(x_i - \bar{x})^2}{S_{xx}^2} = \frac{1}{S_{xx}^2}\sum_{i=1}^n (x_i - \bar{x})^2 = \frac{1}{S_{xx}^2}S_{xx} = \frac{1}{S_{xx}}$
---
###### LOSS Functions
- linear combination : $C_1 Y_1 + C_2 Y_2 + C_3 Y_3 + \cdots + C_n Y_n$
- PDF, joint PDF, Likelihood ftn : $X_1, X_2, \dots, X_n \overset{\text{iid}}{\sim} N(\mu, \sigma^2)$
	- $(\text{pdf}) \quad X \sim N(\mu, \sigma^2) \quad f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{1}{2\sigma^2}(x-\mu)^2\right)$ 
	- $(\text{joint pdf}) \quad f(x_1, x_2, \dots, x_n; \mu, \sigma^2) = \prod_{i=1}^n f(x_i) = (2\pi\sigma^2)^{-\frac{n}{2}} \exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (x_i-\mu)^2\right)$
	- $(\text{Likelihood ftn}) \quad L(\mu, \sigma^2; x_1, \dots, x_n) = \prod_{i=1}^n f(x_i; \mu, \sigma^2) = (2\pi\sigma^2)^{-\frac{n}{2}}\exp\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n (x_i - \mu)^2\right)$
		- $\text{만약 } \mu \text{에만 관심. } \quad x_1, \dots, x_n \text{ 주어졌을 때 } \mu \text{를 찾자! }$
		  $\quad L(\mu), \mu^* \text{를 } L(\mu) \text{를 최대화하는 값}(\text{Maximum Likelihood Estimator (MLE)})$
		  $\rightarrow \mu^* = \arg \max_{\mu} L(\mu) \text{로 정의}.$

		- $\text{SSE}(\mu) = \sum_{i=1}^n (y_i - \mu)^2 \rightarrow f(\mu) = \sum_{i=1}^n (y_i - \mu)^2$
		  $\hat{\mu} = \arg\min_{\mu} \sum_{i=1}^n (y_i - \mu)^2 \quad \frac{\partial f}{\partial \mu} = 2\sum_{i=1}^n (y_i - \mu)(-1) = 0$$n\mu = \sum_{i=1}^n y_i \rightarrow \hat{\mu} = \frac{1}{n}\sum_{i=1}^n y_i$
		- $\text{SAD}(\mu) = \sum_{i=1}^n |y_i - \mu| = \sum_{i=1}^k (\mu - y_{(i)}) + \sum_{i=k+1}^n (y_{(i)} - \mu)$
		  $= (2k-n)\mu + \sum_{i=1}^k (-y_{(i)}) + \sum_{i=k+1}^n y_{(i)}$
		  $\text{n is even} \rightarrow y_{(n/2)} \le \mu \le y_{(n/2+1)} \quad \text{n is odd} \rightarrow \mu = y_{((n+1)/2)}$
- 