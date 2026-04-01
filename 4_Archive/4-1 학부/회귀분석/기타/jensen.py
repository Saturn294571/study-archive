import numpy as np
import matplotlib.pyplot as plt

# 1. 볼록 함수 정의 (예시: f(x) = x^2)
def convex_function(x):
    return x**2

# 2. X축상의 두 점 정의
x1 = 1.0
x2 = 4.0

# 3. 가중치 람다 (lambda) 정의 (0과 1 사이의 임의의 값)
# 젠센 부등식에서 E[X] = lambda*x1 + (1-lambda)*x2
lambda_val = 0.4
x_star = lambda_val * x1 + (1 - lambda_val) * x2  # E[X] = x*

# 4. Y값 계산
f_x1 = convex_function(x1)
f_x2 = convex_function(x2)
f_x_star = convex_function(x_star)

# 5. 현(Secant line) 위의 값 (E[f(X)])
E_f_x = lambda_val * f_x1 + (1 - lambda_val) * f_x2

# 6. 플롯 데이터 생성 (x축 범위)
x_vals = np.linspace(0, 5, 100)
f_vals = convex_function(x_vals)

# 7. 그래프 생성
fig, ax = plt.subplots(figsize=(8, 6))

# 볼록 함수 곡선 (검은색)
ax.plot(x_vals, f_vals, 'k-', label='$f(x) = x^2$')

# x1, x2 위치 (수직선)
ax.vlines([x1, x2], 0, [f_x1, f_x2], color='gray', linestyle='--')

# 현(Secant line) (보라색 수평선)
ax.hlines(E_f_x, x1, x2, color='purple', linestyle='-')

# 점 x1, x2, x* (x축)
ax.plot([x1, x2, x_star], [0, 0, 0], 'k.', markersize=8)
ax.text(x1 - 0.2, -0.5, '$x_1$', fontsize=14)
ax.text(x2 - 0.2, -0.5, '$x_2$', fontsize=14)
ax.text(x_star - 0.2, -1.5, '$x^*$', color='red', fontsize=14)

# 함수 값 f(x1), f(x2)
ax.plot([x1, x2], [f_x1, f_x2], 'o', color='purple', markersize=6)
ax.text(x1 - 1, f_x1, '$f(x_1)$', fontsize=12)
ax.text(x2 + 0.1, f_x2, '$f(x_2)$', fontsize=12)

# 현 위의 값 (E[f(X)])
ax.plot(x_star, E_f_x, 'o', color='purple', markersize=6)
ax.text(x_star + 0.1, E_f_x + 0.5, '$E[f(X)]$', color='purple', fontsize=12)

# 함수 값 f(x*) (f[E(X)])
ax.plot(x_star, f_x_star, 'o', color='red', markersize=6)
ax.vlines(x_star, f_x_star, E_f_x, color='red', linestyle='--') # Jensen 부등식 화살표

# 플롯 제목 및 레이블
ax.set_title('Convex Function and Jensen\'s Inequality', fontsize=16)
ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$f(x)$', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(-2, convex_function(x2) + 2)
ax.set_xlim(-0.5, 5.5)

plt.show()

