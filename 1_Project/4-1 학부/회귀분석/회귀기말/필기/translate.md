
### Cell Means Model & Perfect Multicollinearity

* **Model with Intercept and All Group Indicators:**
    * $Y_i = (\mathbf{1}, E_1, E_2, E_3) (\beta_0, \mu_1, \mu_2, \mu_3)' + \epsilon_i$
* **Design Matrix ($X$) Analysis:**
    * $$
    X = 
    \begin{pmatrix} 1 & 1 & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots \\ 1 & 0 & 1 & 0 \\ \vdots & \vdots & \vdots & \vdots \\ 1 & 0 & 0 & 1 \\ \vdots & \vdots & \vdots & \vdots \end{pmatrix}
    $$
* **Problem: Linear Dependence (Multicollinearity):**
    * The first column ($\mathbf{1}$) is the sum of the group indicator columns ($E_1 + E_2 + E_3$).
    * $\mathbf{1} = E_1 + E_2 + E_3$
    * **Consequence:** Columns are linearly dependent $\rightarrow$ $X'X$ is singular (not invertible) $\rightarrow$ $\beta$ estimation is impossible (식별 불가).

#### Cell Means Model (Solution)

* **Refined Model (Remove Intercept):**
    * $Y = (E_1, E_2, E_3) \beta + \epsilon$
    * $$ Y = (E_1, E_2, E_3) \begin{pmatrix} \mu_1 \\ \mu_2 \\ \mu_3 \end{pmatrix} + \epsilon $$
* **Properties:**
    * Columns $E_1, E_2, E_3$ are linearly independent.
    * Estimation is possible.
* **Hypothesis Testing:**
    * $H_0: \beta_1 = \beta_2 = \beta_3$ (All group means are equal).
    * $H_1:$ Not all $\beta_j$ are equal (At least one pair differs).
