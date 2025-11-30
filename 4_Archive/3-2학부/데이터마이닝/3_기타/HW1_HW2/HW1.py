import matplotlib.pyplot as plt

# H.W #1: 아래의 x, y 값을 선형 회귀식을 구하고 아래와 같은 Plot을 그리시오.
x = [1,2,3]; y = [1,3,2]

mean_x = sum(x)/len(x); mean_y = sum(x)/len(y)

sum1 = 0
sum2 = 0
for i in range(3) :
    sum1 += (x[i] - mean_x) * (y[i] - mean_y)
    sum2 += (x[i] - mean_x) ** 2

beta_hat = sum1 / sum2
alpha_hat = mean_y - beta_hat * mean_x

print('알파햇의 값 :',alpha_hat,'베타햇의 값 :', beta_hat)

# 선형회귀식: Yi = 1 + 0.5xi
x_line = [i * 0.1 for i in range(41)]  # 0부터 4까지의 값
y_line = [alpha_hat + beta_hat * x for x in x_line]

# 그래프
plt.figure(figsize=(6, 6))
plt.scatter(x, y, color='red', label='Points')
plt.plot(x_line, y_line, color='blue', label='y = 1+ 0.5x')

# 축 라벨 및 제목
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('HW1 linear regression plot')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

