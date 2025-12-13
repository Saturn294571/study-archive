# 전산통계 기말고사 6시간 초단기 완성 전략

**목표:** 6시간 집중으로 합격 안정권 점수 확보. "출제 확실시되는 문제"를 최우선 공략.

> [!CRITICAL]
> **전략의 핵심:**
> 시간은 부족하고 범위는 넓습니다.
> **가장 배점이 크고 출제가 확실한 "Neural Network 손계산"부터 잡고 시작합니다.**
> 나머지는 개념 위주로 방어하여 점수를 획득합니다.

---

## 1. 6시간 타임테이블 (집중력 100% 기준)

| 교시 | 시간 (분) | 주제 | 핵심 목표 및 활동 |
| :--- | :--- | :--- | :--- |
| **1교시** | **0 ~ 90분**<br>(1h 30m) | **[최우선]**<br>Neural Network<br>손계산 | **"손으로 못 그리면 모르는 것이다" (교수님 강조)**<br>1. 입력(X) $\to$ 가중치(W) 곱합 $\to$ 활성화함수(Sigmoid) $\to$ 출력(Y) 과정 직접 계산.<br>2. 오차(Error) 구하기 및 역전파(Backpropagation) 논리(가중치 수정) 이해.<br>3. 강의노트 예제 3번 이상 반복 풀이. |
| **2교시** | **90 ~ 150분**<br>(1h) | Decision Tree<br>& Ensemble | **서술형/단답형 대비 개념 구분**<br>1. **Random Forest:** 배깅(Bagging), 독립적, "집단지성".<br>2. **Boosting:** 부스팅, 순차적, "오답노트/가중치".<br>3. **Pruning:** 가지치기 $\to$ **Overfitting 방지**. |
| **3교시** | **150 ~ 210분**<br>(1h) | SVM<br>& Kernel | **그림 문제 및 핵심 용어**<br>1. **Support Vector:** 경계선에 닿은 점들.<br>2. **Margin:** 최대화해야 할 목표.<br>3. **Kernel Trick:** XOR 같은 비선형 문제를 고차원으로 매핑해 해결. |
| **4교시** | **210 ~ 270분**<br>(1h) | Deep Learning<br>역사 & 개념 | **빈칸 채우기/OX 대비**<br>1. **Perceptron 한계:** XOR 문제 해결 불가 (Minsky).<br>2. **해결:** Hidden Layer + Backpropagation (Hinton).<br>3. 주요 용어: MLP, AI Winter, AlexNet 등 흐름 파악. |
| **5교시** | **270 ~ 360분**<br>(1h 30m) | **총정리**<br>& 시뮬레이션 | **실수 방지 및 굳히기**<br>1. **백지 복습:** Forward Pass 계산식 안 보고 써보기.<br>2. **키워드 매칭:** Bagging vs Boosting, Linear vs Non-linear.<br>3. 컨디션 조절: 아는 것만 다 맞춰도 합격이다. |

---

## 2. 핵심 출제 예상 포인트 (상세)

### A. Neural Networks & Deep Learning (출제 0순위)
*   **계산 연습 (필수):**
    *   `Net` = $\sum (Input \times Weight) + Bias$
    *   `Output` = $Sigmoid(Net) = \frac{1}{1 + e^{-Net}}$
    *   **Backpropagation:** 출력의 오차를 줄이는 방향으로, 역방향으로 전파되며 **가중치(Weight)를 업데이트**하는 알고리즘.
*   **XOR 문제:** 단일 Perceptron(선형 분리)으로는 해결 불가능하다는 것이 증명됨(Minsky). 이를 해결하기 위해 **Hidden Layer(은닉층)**가 도입됨.

### B. Decision Trees (의사결정나무)
*   **원리:** 질문을 통해 데이터를 분할하며 불순도(Impurity)를 낮춰가는 과정.
*   **불순도 지표:** 지니 지수(Gini Index), 엔트로피(Entropy). (공식 형태 눈에 익히기)
*   **Overfitting 방지:** 나무가 너무 깊어지면 과적합되므로 **가지치기(Pruning)**가 필수.

### C. Ensemble Methods (앙상블)
*   **Random Forest (Bagging):**
    *   여러 개의 독립적인 나무를 만듦 (Bootstrap Sampling).
    *   다수결 투표로 결정. **Overfitting에 강함.**
*   **Boosting (AdaBoost, Gradient Boosting):**
    *   이전 모델이 틀린 오차(Residual)에 집중하여 순차적으로 모델을 만듦.
    *   성능은 좋으나 Noise에 민감할 수 있음.

### D. Support Vector Machines (SVM)
*   **목표:** 두 클래스를 나누는 **초평면(Hyperplane)** 중 **마진(Margin)**이 가장 큰 것을 찾음.
*   **Kernel Trick:** 데이터를 고차원으로 보내 비선형 문제를 선형 문제로 바꿔서 품. (축구에서 수비수가 막으면 빈 공간으로 패스하듯이 차원을 이동).

---

## 3. 시험 직전 5분 체크리스트

1.  [ ] $Sigmoid$ 함수 식 $\frac{1}{1+e^{-x}}$ 기억나는가?
2.  [ ] **Forward Pass** 계산 순서(입력 $\to$ 은닉 $\to$ 출력) 머릿속에 그려지는가?
3.  [ ] **Bagging**은 "따로따로(병렬)", **Boosting**은 "이어달리기(순차)" 구분 가능한가?
4.  [ ] **SVM**은 **Margin**을 **최대화**하는 것임을 아는가?
5.  [ ] **XOR** 문제는 **Hidden Layer**가 있어야 풀린다는 사실을 아는가?
