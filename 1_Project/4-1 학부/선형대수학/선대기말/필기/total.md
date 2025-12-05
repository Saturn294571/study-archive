---
marp: true
theme: a4-light
paginate: true
math: mathjax

---

# 선형대수학 기말고사 대비 백지 테스트 자료
## (Matlab, Determinants, Eigenvalues, Diagonalization)

---

<!-- 9. Matlab (1/2) -->
###### 행렬 조작
-  submatrices
	- 한 벡터를 다른 벡터의 인덱스로 사용 가능
	- ```matlab
	  a = [100 200 300 400 500 600 700];
	  b = [3 5 6];
	  c = a(b);
	  
	  disp(c);
	  % [300 500 600]
	  ```
	- 한 행렬의 부분 구간을 원한다면 콜론 연산자로 나타냄
	```matlab
	disp(a(2:5));
	% 200 300 400 500
	```
-  행렬에서 벡터를 빼기
```Matlab
A=magic(3); % 마방진
C=mean(A);
disp(A-C);
```
-  create a diagonal matrix
``` matlab
v = [2 1 -1 -2 5];
D = diag(v)
D1 = diag(v,1) % 컬럼 추가
eye(m,n) % 단위 대각행렬
```
-  adding row/column vec
- ```matlab
  a=[1 2 3 4];
  b=[5;6;7];
  disp(a+b) % 3*4 행렬 형태로 나옴
  ```
  - 다항식 표기
	  - $p(x)=x^2-4x+4\to\text{p=[1 -4 4];}$
	  - $p(x)=4x^5-3x^2+2x+33\to\text{p=[4 0 0 -3 2 33];}$
	  - 다항식은 특정 값에 대한 해나 근을 계산 가능
		  - polyval(p,2)        roots(p)
***
###### 행렬연산
- 행렬곱 : dot(A,B) or $A*B$      외적의 경우 : cross(A,B)
- 전치와 역행렬 : A'       inv(A)
- 방정식의 해 도출
1) ```matlab
   syms xyz
   e1 = 2*x+y+z == 2;
   e2 = -x+y-z == 3;
   e3 = x+2*y+3*z == -10;
   
   [A,B] = equationsToMatrix([e1,e2,e3],[x,y,z]);
   X = linsolve(A,B);
   
   sol = solve([eq1,eq2,eq3],[x,y,z]);
   xSol = sol.x
   ySol = sol.y
   zSol = sol.z
   ```
2) ```
   syms
   eq = a*x^2+b*x+c == 0;
   solx = solve(eq,x)
   solb = solve(eq,b)
   ```

---

<!-- 9. Matlab (2/2) -->
###### 조건문과 반복문
- if-elseif-else 문
``` matlab
if (조건문)
	(실행)
elseif (조건문)
	(실행)
else (조건문)
	(실행)
end
```
- for문
``` matlab
for i = [(시작),(step),(끝)]
	(실행)
end
```
***
###### 함수
``` 
% 파일 이름 : funcName.m
function [x,y,z] = funcName(a,b)
x = (...);
y = (...);
z = (...);
end
```
- $[x,y,z]$가 출력, $a,b$가 입력
###### 내장함수
```matlab
% 차원 추출
[m1 m2 ... mn] = size(X)
m = size(x,dim)
```

```matlab
ones(r,c)     % 1로 채운 행렬
zeros(r,c)    % 0으로 채운 행렬
diag(x)       % x값을 가지는 대각행렬
size(A)       % 차원
A'            % 전치
inv(A)        % 역행렬
pinv(A)       % 의사역행렬
det(A)        % 행렬식
eig(A)        % 고유값, 고유벡터
sdv(A)        % 특이값 분해
```
###### 고유값, 고유벡터
```matlab
[V,D]=eig(A);
Ar = V*D*inv(V);
% A == A1이 성립
```
- V : 고유벡터가 column인 행렬,     D : 대각성분이 $\lambda$들인 행렬

---

<!-- 10. Determinants -->
###### Introduction to Determinants
- (scaling factor for the transformation of a matrix(단위행렬에 대해,))
- 행렬에 1보다 큰 스칼라배를 할 경우 행렬식이 1보다 커짐 
- 행렬을 squeeze할 경우 1보다 작아짐
	- ![[Pasted image 20251110223556.png]]
- rotation의 경우 변화 X
- 행렬식이 0이면 같은 직선상에 두 기저가 놓임
	- ![[Pasted image 20251110223611.png]]
- 음수인 스칼라배를 할경우 넓이는 한 기저가 반대방향(음/양)으로 가리킴
	- ![[Pasted image 20251110223658.png]]
###### Determinants using Cofactor expansion
- 수반행렬을 포함한 행렬식 정의
	- $$|A|=\sum_{j=1}^n(-1)^{1+j}a_{1j}|A_{1j}|$$
	- 소행렬 $A_{ij}$는 i번째 row와 j번째 column을 제거한 행렬,
	- 수반행렬 $C_{ij}=(-1)^{i+j}|A_{ij}|$
- cofactor expansion along **i/jth row/column**
	- $$|A|=\sum_{j/i=1}^na_{ij}((-1)^{i+j}|A_{ij}|=C_{ij})$$
- cof. exp.시 행과 열을 고르기 : 0이 많이 포함된 행/열을 골라라
###### Determinants using Row Reduction
- Row operation의 종류와 갯수에 상관없이 $|A|$의 값은 변하지 않음
- $$|A|=(-1)^r \cdot \frac{\text{(B의 모든 대각성분들의 곱)}}{\text{(모든 스케일링 팩터들의 곱)}}$$
	- B는 A에 row OP.를 통해 얻은 사다리꼴 행렬
	- r은 row스왑의 횟수
***
###### Special Properties of Determinants (for $A_{(n\times n)}$)
1) $|A^n|=|A|^n$
2) $A_{(n\times n)} \iff |A|\neq0$
3) $|A'|=|A|$
###### Column Operations (for $A_{(n\times n)}$)
1) column replacement는 $|A|$에 영향 X (ex : $C_1\leftarrow C_1-4C_3$)
2) $|cA|=c|A|,\quad c \in \mathbb{R}$
3) 두 column의 swap은 $-|A|$
	1) 두 row의 swap은 $|A|$에 영향 X
4) $|I_n|=1$
###### Cramer's Rule
- $A_{(n\times n)}, \forall b \in \mathbb{R}^n,\quad Ax=b$에서 유일한 해 x는,
	- $$x_i=\frac{|A_i(b)|}{|A|},\quad i \in \{1,\cdots,n\}$$
		- $A_i(b)$는 i번째 행벡터를 b로 교체한 행렬
###### Determinants as Area and Volume
- $A_{(2\times 2)},$각 column vector가 만들어 내는 평행사변형의 넓이는 $|A|$
	- ![[Pasted image 20251110221355.png]]
- $A_{(3\times 3)},$각 column vector가 만들어 내는 도형의 부피는 $|A|$
	- ![[Pasted image 20251110221522.png]]

---

<!-- 11. Eigenvalues & Eigenvectors -->
###### Introduction
- $Av=\lambda v$ ;    $(A-\lambda I)v=0$
	- $\lambda\to0$ 가능;    but, $v\to0$ 불가능
- ![[Pasted image 20251125104338.png]]
###### Eigenvalues and EigeVectors
- 고유값, 고유벡터의 성질
	- $Av$를 하면 $\lambda$만큼 스칼라 곱이 된다 (방향 유지)
	- 그러나 고유벡터가 아닌 $Au$는 방향이 달라짐 (스칼라곱 X)
	- (1) ![[Pasted image 20251125104715.png]]
	- (2) ![[Pasted image 20251125104908.png]] (3) ![[Pasted image 20251125105026.png]]
		- v는 고유벡터, w는 고유벡터 X
	- $Av=\lambda v$의 의미는 $Av$와 $\lambda v$가 원점에 대해 공선성(colinear) 관계에 있다
		- 따라서 v, Av는 같은 원점을 지나는 일직선상에 놓임
### Graphical Examples
- 대전제 : 0, v, Av가 한 직선 위? (공선성) -> 고유벡터
1) Reflection : 방향에 따라 $\lambda = 1, -1$ 그외엔 고.벡. X
	-  ![[Pasted image 20251125121655.png]]  ![[Pasted image 20251125121750.png]]  ![[Pasted image 20251125121902.png]]
2) Projection : (x축,y축 벡터) -> (원점) : $\lambda=0$ ; -> (자기자신) : $\lambda=1$; 그 외엔 고.벡. X
	- ![[Pasted image 20251125123247.png]]  ![[Pasted image 20251125123325.png]]  ![[Pasted image 20251125123337.png]]
3) Rotation : 모든 벡터가 공선성이 깨짐 -> 모두 고.벡. X
4) Dilation : 방향을 유지, 늘리고 줄임 -> 모두 고.벡. O ($\lambda=\text{(계수)}$) 
5) Shear : x축에 있다면? -> $\lambda=1$(밀어버릴게 없음);    그 외? -> 고.벡. X
	- (3) ![[Pasted image 20251125123726.png]] (4) ![[Pasted image 20251125124044.png]] (5) ![[Pasted image 20251125124105.png]]
6) Identitiy Matrix : 0이 아닌 모든 벡터가 고.벡; $\lambda=1$

---

<!-- 12. Eigen Space & Characteristic EQ -->
###### Introduction
- Eigenspace의 특성
	- Dimensionality : 
	- Subspace : 고유공간은 벡터공간에 대해 A가 작용하는 부분공간
	- Null space : $(A-\lambda I)$의 null space (kernel)이 $\lambda$에 따른 고유공간
###### Eigenspace
- 정의 : $(A-\lambda I_n)v=0$의 해 집합이 eigenspace. 즉, $\text{Nul}(A-\lambda I_n)$
- ex) $A-3I_2=\begin{pmatrix}2&-4\\-1&-1\end{pmatrix}-3\begin{pmatrix}1&0\\0&1\end{pmatrix}=\begin{pmatrix}-1&-4\\-1&-4\end{pmatrix}\to\begin{pmatrix}1&4\\0&0\end{pmatrix}$
	- parametric form : $\{x=-4y,\quad y=y\}\to\begin{pmatrix}x\\ y\end{pmatrix}=y\begin{pmatrix}-4\\ 1\end{pmatrix}$
		- $\therefore$이 고유공간의 기저(basis)는 $\{[-4,1]\}$.
- ex2) $A-2I_3=\begin{pmatrix}4&-1&6\\2&-1&6\\2&-1&8\end{pmatrix}-2\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}=\begin{pmatrix}2&-1&6\\2&-1&6\\2&-1&6\end{pmatrix}\sim\begin{pmatrix}2&-1&6\\0&0&0\\0&0&0\end{pmatrix}$
	- general solution : $\begin{pmatrix}x\\ y\\ z\end{pmatrix}=y\begin{pmatrix}1/2\\ 1\\ 0\end{pmatrix}+z\begin{pmatrix}-3\\ 0\\ 1\end{pmatrix}$
		- $\therefore$ basis : $\{[1,2,0],[-3,0,1]\}$
###### The Characteristic Equation
- 행렬의 고유값($\lambda$)를 찾는데 사용하는 스칼라 방정식
	- $\det(A-\lambda I_n)=0$ 임을 이용
- $f(\lambda)=(-1)^n\lambda^n+(-1)^{n-1}\lambda^{n-1}S_1+ \cdots +(-1)\lambda S_{n-1}+ S_n$
	- $S_k$는 크기가$k\times k$인 주소행렬식의 합 ($S_1=tr(A), S_n=|A|$)

---

<!-- 13. Similarity & Diagonalization -->
###### Similarity
- 정의 : $n\times n$행렬 $A,B$가 서로 닮음(similar) 행렬 ->동일 고유값 $\lambda$들을 가짐
	- invertible matrix $P$ : $P^{-1}AP=B,\quad PBP^{-1}=A$를 만족.
		- similarty transformation : $A\to P^{-1}AP$
- 의미 : 동일한 선형 변환(linear transformation)이나, 
  서로 다른 좌표계(coordinate sys.) 또는 기저(base)
- 연산의 특징
	1) reflexivity : $A\sim A$
	2) symmetric : $(A\sim B)\to(B\sim A)$
	3) transitive : $(A\sim B)\wedge (B\sim C)\to(A\sim C)$
- 닮음의 특성
	- 1) $\lambda_A=\lambda_B$    2) $|A|=|B|$    3) $tr(A)=tr(B)$
	- 4) $f(\lambda_A)=f(\lambda_B)$    5) A,B는 각각 다른 base에 대한 동일한 transformation
	- 6)  $A:\text{diagonalizable}\to\exists P:\text{invertible},A=PDP^{-1}\quad(D:\text{diagonal mat.})$
- 행렬$P$의 특성 : $P:\text{invertible}$, P의 column들은 새롭게 표현되는 기저들
	- ex) $A=\begin{bmatrix}2&1\\0&2\end{bmatrix},P=\begin{bmatrix}1&1\\0&1\end{bmatrix}B=\begin{bmatrix}2&1\\0&2\end{bmatrix}$
###### Diagonalization
- 정의 : $A=PDP^{-1},D:\text{diagonal}\to A:\text{diagonalizable}$
	- $D=\begin{bmatrix}\lambda_1& &0\\  & \ddots &  \\ 0 &  & \lambda_n \end{bmatrix}$
- D의 특성 : $D^k=\begin{bmatrix}a^k&0\\0&b^k\end{bmatrix}\quad(k\ge1)$
- 의미 : 대각화는 basis를 교체하여 대각행렬로 더 단순화함
- 구하는 과정 $A=\begin{bmatrix}4&1\\2&3\end{bmatrix}$
	1) A의 $\lambda_1,\cdots,\lambda_n$을 찾아라
		- $f(\lambda)=\lambda^2-7\lambda+10=0;\quad \lambda_1=5,\lambda_2=2$
	2) A의 3개의 선형독립적인 고유벡터를 찾아라
		- $\lambda_1=5$에 대해 $\begin{bmatrix}1\\1\end{bmatrix}$,    $\lambda_2=2$에 대해 $\begin{bmatrix}1\\-2\end{bmatrix}$
	3) 고유벡터로 P를 구성 : $P=\begin{bmatrix}1&1\\1&-2\end{bmatrix}$
	4) 고유값들로 D를 구성 : $D=\begin{bmatrix}5&0\\0&2\end{bmatrix}$
	- D와 P에 대한 검증 : $AD=DP$임을 활용
- 삼각행렬에 대한 고유값의 특징 : (상/하) 삼각행렬에서 대각성분은 $\lambda$들이다
	- ex) $\begin{bmatrix}5&-8&1\\0&0&7\\0&0&-2\end{bmatrix}\to[\lambda_1,\lambda_2,\lambda_3]=[5,0,-2]$ 
###### Markov chain
- 정의 : 다음 상태가 현재의 상태에 영향을 받을 때, n차례 이후 확률을 구함. 
	- ex) $P=\begin{bmatrix}0.9&0.1\\0.5&0.5\end{bmatrix}$ row : 현재 상태(합=1)    column : 다음 상태    원소 : 확률
		- 상태 1) 오늘 맑음 $\to$ $p(\text{내일 맑음})=0.9$, $p(\text{내일 비})=0.1$ 
		- 상태 2) 오늘 비 $\to$ $p(\text{내일 맑음})=0.5$, $p(\text{내일 비})=0.5$ 
- $P^n$ 은 n일(단계) 다음의 확률 행렬, 이를 위해 대각화 사용 : $P^n=MD^nM^{-1}$
	- $\lambda=1\text{ or }0.4, M=\begin{pmatrix}1&1\\1&-5\end{pmatrix},D^n=\begin{pmatrix}1^n&0\\0&0.4^n\end{pmatrix}$
	- $P^\infty=M\begin{pmatrix}1&0\\0&0\end{pmatrix}M^{-1}=\begin{pmatrix}5/6&1/6\\5/6&1/6\end{pmatrix}$ : long term trasition matrix
- steady state distribution을 찾음 : $\pi=[\pi_1,\pi_2]$;
	- $\pi P=\pi$ 조건에서, : $0.9\pi_1+0.5\pi_2=\pi_1\implies\pi_1=5\pi_2$
	- $\pi_1+\pi_2=1$ 조건에서, : $\pi_1=5/6,\pi_2=1/6$;
		- 따라서 steady-state vector (장기 확률) : $\pi=[5/6,1/6]$
		- 5/6 확률로 맑음, 1/6 확률로 비
