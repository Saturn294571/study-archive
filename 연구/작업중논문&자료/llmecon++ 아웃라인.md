# 0. 요약
- 
# 1. 서론
- _정책시뮬의 필요성 대두_
	- 최근 인공지능 분야의 발전은 정부의 의사 결정 및 정책 분석을 지원하는 데 점점 더 많이 활용된다. AI 시스템은 방대한 데이터 처리, 패턴 식별, 예측 생성에 따라 정책 입안자들이 위험을 예측, 정책 대안을 평가, 자원 배분 개선을 할 수 있도록 지원한다.
- _LLM econ : LLM 기반 경제 시뮬 등장_
	- 그러나, 기존 의사결정 및 예측에 주로 사용되는 Agent-based 모델은 agent behavior rule이 고정되어있고, 인간 의사결정 과정에 대한 표현이 제한적이라는 한계점을 가진다. 
	- 이러한 한계점에 대해 \<LLM Economist: Large Population Models and Mechanism Design in Multi-Agent Generative Simulacra\>(이하 LLM Economist)는 'In Context-Reinforcement Learning(ICRL) 방식을 통한 LLM 기반 정책 시뮬레이션' 이라는 측면에서 자연어 기반 추론 과정, 상황 기반 행동 생성, 동적인 전략 수립이라는 해결책을 제안하였다.
- _LLM econ의 구조(ICRL)과 history 문제_
	- 하지만 ICRL은 전통적 강화학습과는 달리, 명시적인 가치함수 추정이나 파라미터 갱신 없이 과거의 상호작용 기록(history)을 프롬프트로 제공하여 정책을 개선한다는 점에서 본질적으로 “어떤 history를 어떻게 제공할 것 인가”에 크게 의존하는 바이다.
- _LHF와 본 논문의 기여_ 
	- 본 연구는 LLM 기반 ICRL 프레임워크에서 history selection 메커니즘이 정책 성능과 계산 복잡도에 어떠한 영향을 미치는지 경제학적 환경 하에서 분석한다. 특히, 기존 LLM Economist 구조를 기반으로, 과거 학습 기록 중 성과가 우수한 사례만을 선별하여 프롬프트에 포함하는 Filtering Learning Histories(LHF) 기법을 구현하고, 그 효과를 비교 실험을 통해 평가하였다.
	- 본 연구의 기여는 다음과 같다. 첫째, LLM 기반 ICRL에서 history selection을 명시적으로 분리·구현하고, 그 효과를 경제학적 모형 위에서 실증적으로 분석하였다. 둘째, 계산 복잡도 측면에서 History filtering의 실질적 이점을 정량적으로 제시하였다.
# 2. 배경 및 문제 정의
- _LLM Economist에 대하여_
	- 어떠한 문제상황을 다루고 있는지
		- 선행 연구 LLM Economist는 계층적 의사결정 구조가 존재하는 전략적 환경에서 경제 정책을 설계, 평가하기 위해 에이전트 기반 모델링을 활용하는 프레임워크를 제시했다. 
	- 어떻게 그걸 해결했는지
		- 하위 수준에선, 미 인구 조사 데이터에 맞춰 보정된 인구 통계에서 추출한 '인물 조건부 프롬프트'로 구현된 'Bounded-rational worker' 에이전트들이 맥락 내(in-context) 학습된 텍스트 기반 효용 함수를 극대화 하기 위해 노동 공급량을 선택한다.
		- 상위 수준에선, 기획자 에이전트가 ICRL을 활용하여 미 연방 세율 구간에 기반한 분할 선형 한계세율표를 제시한다.
	- 왜 그게 필요한지
		- 이러한 구조는 경제 시뮬라크라(Simulacra)에게 이질적 효용의 최적화, 인구 통계학적 현실성, 자연어로 표현된 메커니즘 디자인의 세 측면으로 하여금 신뢰 가능한 재정실험의 요소를 부여한다. 
- _경제학적 환경 정의_
	- 한편, LLM Economist++에서는 선행연구에서의 복합적인 가정 상황을 피하고, 경제학적으로 직관적이고 친화적인 독점적 시장구조 하의 생산물 시장을 상정했다. 또한 First-order conditions(FOC)하 해석적 최적값과의 비교가 가 용이하도록 정부-기업 경제주체간 상호작용을 다음과 같이 축소하였다.
	- 본디 선행연구 LLM Economist가 정부-기업 에이전트 간 스택켈버그 게임임을 상정하였으나, 본 연구에서의 정부 에이전트는 어떠한 목표 없이 고정된 세율($\tau$)와 규제 변수($\rho$)만을 가진다. 또한, 에이전트의 조건부 합리성을 고려한 선행연구와는 달리, 본 연구에선 완전 합리성을 따른다고 가정한다. 따라서 실질적인 ICRL 프레임워크 내에서의 상황은 ICRL을 통한 단일 기업 에이전트의 오목한 목적함수에 대한 노동 공급($L$)최적화 문제에 가깝다. 
	- 이 요건에 따라 콥-더글라스 생산함수(2.1), 수요함수(2.2), 이윤함수(2.3)를 상정하였다.
		- $Q = A_0K_0^{\alpha} L^{1-\alpha}$ (2.1)
		- $P=a-bQ$ (2.2)
		- $\pi(L) = P(Q)Q - wL - \tau Q$ (2.3)
	- 각 파라미터값은 극댓값 계산시 미분에서의 편의를 위해 다음과 같이 임의로 가정하였다. 
		- $A_0=1,\ K_0=1,\ \alpha=0.33,\ a=10,\ b=0.1,\ w=1,\ \tau=0.2$ (2.4)
	- _선행연구의 Saez 해법에 해당하는 공급량에 대한 미분으로 계산하는 경제학적 관행에 따라, FOC 조건
		- $\pi\left(Q\right)=\left(a-bQ-\tau\right)Q-wQ^{1/\left(1-\alpha\right)}\quad(\because (2.1))$ (2.5)
		- $\frac{d\pi}{dQ}=a-2bQ-\tau-w\frac{1}{1-\alpha}Q^\frac{\alpha}{1-\alpha}=0$ (2.6)
		- $\therefore L_M\approx74.79, \ \pi(L_M)\approx69.26$

# 3. LHF 기법과 방법론 
- Filtering Learning History
- \<Filtering Learning Histories Enhances In-Context Reinforcement Learning\>
	- 어떠한 문제상황을 다루고 있는지
	- 어떻게 그걸 해결했는지
	- 왜 그게 필요한지
-  LLM Economist++ 구조
	- LLM Economist++ 프레임워크의 전반적인 구조도는 <Figure 1>을 따른다. 먼저, (2.1)에서 정의한 독점적 시장의 상황을 가정하고 과 정부의 고정된 정책변수들($\tau$, $\rho$)을 가정한다. 먼저 주어진 정책변수 수준과 과거 의사결정 과정을 담은 

# 4. 실험
-  _Baseline(No LHF) 및 LHF(k=5)의 실험 환경_
	- 실험조건 중 공통적인 조건은 타우 = 0.2, Histroy window = 20, Max timestep = 50으로 공통 설정하였다. 단, LHF 개선후의 경우 관련 파라미터는 k_best_hist=5로 설정하였다.
	- 또한 유의할 점으로, Max timestep의 경우 엄밀한 이론적 도출의 결과가 아닌 일종의 경험법칙(Rules of Thumb)으로서 <Graph 1>에 따른 양상에서 Timestep 증가에 따른 유의미한 Profit 향상이나, Prompt tokens의 증가 양상이 없을 것으로 기대하고 정한 임의적인 수이다.

-  _실험결과_
	- <Graph 1>과 <Table 1>에 따르면, 본 실험에서 Baseline과 LHF의 평균 이윤은 각각 이론적 최적값 대비 약 99.55%와 99.11% 수준을 기록하였다. 이를 optimality gap 관점에서 보면, LHF는 Baseline 대비 소폭 증가한 갭을 보이지만, 그 절대 규모는 최적값 대비 1% 미만에 머문다. 즉, 본 정규화된 독점 환경에서는 LHF 도입으로 인한 평균 정책 품질의 저하는 제한적인 수준으로 관찰된다.
	- 반면 계산 효율 측면에서는 LHF가 프롬프트 길이를 유의미하게 감소시켜 평균 입력 토큰 수를 크게 절감하였으며, 이에 따라 전체 실행 시간 역시 상당 폭 단축되었다. 이는 history filtering이 정책 품질을 거의 유지하면서 계산 자원 요구를 완화할 수 있음을 시사한다. 
- _LHF의 토큰 감소 원리_
	- LLM Economist의 구조는 construct initial history+LHF(T_env_step) → Policy making(T_prompt_build) → Action()이에 따르면 전체적인 ICRL 프레임워크의 소요 시간은 다음과 같이 추론된다. 
		- $T_{\mathrm{total}}\approx\sum_{t=1}^{T}\left(T_{\mathrm{prompt\_build}}+T_{\mathrm{LLM\_inference}}+T_{\mathrm{env\_step}}\right)$ (4.1)
	- 이때, $T_\text{LLM\_inference}$가 Transformer의 self-attention 메커니즘으로 인해 토큰 수에 따른 Big-O notation은 다음에 근사된다.
		- $T_{\mathrm{inference}}\propto O\left(n_{\mathrm{tokens}}^2\right)\quad\left(\mathrm{attention}\right)$ (4.2)

|                | Baseline | LHF     |
| -------------- | -------- | ------- |
| profit mean    | 68.9485  | 68.6464 |
| profit std     | 0.5621   | 0.4904  |
| recovery ratio | 0.9955   | 0.9911  |

# 5. 논의점과 향후 과제

1)한계점
단일시드, 정적환경, 독점, 단순 top-k 룰 
2)향후 과제
- 향후 과제로는 실험단계에서 가설로 제시하였던 'LHF 기법이 '
- 쿠르노 과점
- 동태적 환경
- 다중균형 환경
