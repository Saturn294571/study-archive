import matplotlib.pyplot as plt
import numpy as np

# H.W #2: 위 문제를 행렬연산으로 구하시오.

X = np.array([[1,1],
             [1,2],
             [1,3]])
Y = np.array([1,3,2])

# 𝛽 = (𝑋′𝑋)−1𝑋′𝑌
temp1 = np.linalg.inv(np.dot(X.T, X)) # (𝑋′𝑋)−1
temp2 =  np.dot(X.T, Y) # 𝑋′𝑌

beta = np.dot(temp1,temp2)
print('베타0, 베타1의 각각의 값은 : ',beta)

x_line = [i * 0.1 for i in range(41)]  # 0부터 4까지의 값
y_line = [beta[0] + beta[1] * x for x in x_line]

# 그래프
plt.figure(figsize=(6, 6))
plt.scatter([1,2,3], [1,3,2], color='red', label='Points')
plt.plot(x_line, y_line, color='blue', label='y = 1+ 0.5x')

# 축 라벨 및 제목
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('HW2 linear regression plot')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

def pact(x) :
    result = 1
    for i in range(x) :
        result *= X
    return result
