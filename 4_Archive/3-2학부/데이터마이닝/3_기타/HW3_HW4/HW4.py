import numpy as np
X = np.array([[1],
              [2],
              [3],
              [4],
              [5],
              [6]])
y = np.array([[0],
              [0],
              [0],
              [1],
              [1],
              [1]])

alpha = 0.1 # 학습률(learning rate)
repeat_count = 2000


b = 0.0
w = 0.0

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 학습
final_cost = None # 최종 cost 기록

for i in range(repeat_count):

    z = w * X + b # zi = w*xi + b

    cost = -np.sum(y * np.log(sigmoid(z)) + (1 - y) * np.log(1 - sigmoid(z)))
    final_cost = cost

    db = -np.sum(y - sigmoid(z)) # dcost/db
    dw = -np.sum((y - sigmoid(z)) * X) # dcost/dw


    b = b - alpha * db
    w = w - alpha * dw

print(f"최종 cost : {final_cost}")
print(f"최종 편향 b: {b}")
print(f"최종 가중치 w: {w}")
