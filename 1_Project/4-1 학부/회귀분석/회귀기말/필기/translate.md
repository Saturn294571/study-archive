
### AIC (Akaike Information Criterion) Derivation

* **Likelihood Function of $\beta$ ($L(\beta)$):**
    * Model: $Y_i = x_i'\beta + \epsilon_i, \quad \epsilon_i \sim iid \ N(0, \sigma^2), \quad i=1, 2, \dots, n$
    * $x_i' = [1, x_{i1}, \dots, x_{ip}]$
    * $L(\beta) = (2\pi\sigma^2)^{-\frac{n}{2}} \exp\left\{-\frac{1}{2\sigma^2} \sum_{i=1}^n \epsilon_i^2\right\} = (2\pi\sigma^2)^{-\frac{n}{2}} \exp\left\{-\frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - x_i'\beta)^2\right\}$

* **Log-Likelihood:**
    * $\log L(\beta) = -\frac{n}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - x_i'\beta)^2$

#### AIC Calculation ($AIC(M(A))$)

* **Definition:**
    * $AIC(M(A)) = -2 \log L(\hat{\beta}) + 2|A|$
    * $= n \log(2\pi\sigma^2) + \frac{1}{\sigma^2} \sum_{i=1}^n (y_i - x_i'\beta_A)^2 + 2|A|$
    * (Here, $\beta_A$ is defined as $\beta_i$ if $i \in A$, and $0$ if $i \notin A$)

* **Approximation using MLE ($\hat{\sigma}^2$):**
    * If $\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^n (y_i - x_i'\hat{\beta}_A)^2$,
    * $AIC(M(A)) = n \log(2\pi\hat{\sigma}^2) + \frac{1}{\hat{\sigma}^2} \sum_{i=1}^n (y_i - x_i'\hat{\beta}_A)^2 + 2|A|$
    * Since $\sum (y_i - x_i'\hat{\beta}_A)^2 = n\hat{\sigma}^2$, the second term simplifies:
    * $= n \log(2\pi\hat{\sigma}^2) + \frac{1}{\hat{\sigma}^2} (n\hat{\sigma}^2) + 2|A|$
    * $= n \log(2\pi\hat{\sigma}^2) + n + 2|A|$
