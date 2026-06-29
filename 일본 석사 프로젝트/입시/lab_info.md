# 일본 석사 연구실 후보 재평가: AI공학 x 금융·사회경제 시스템

작성일: 2026-05-03

## 0. 후보 평가 목적

이 문서는 연구실/대학 후보를 **행동 가능한 기준**으로 평가하기 위한 문서다. 지원자의 정체성을 고정하기보다, 각 후보가 다음 산출물과 연결되는지를 확인한다.

- Python/ML/통계/계량 기반 연구 또는 프로젝트 산출물
- 금융·경제·사회 데이터 분석 경험
- 텍스트 분석, 시계열, agent simulation, LLM 활용 연구 중 하나 이상의 구체적 결과물
- CV, 연구요약, 연구계획서, 컨택 메일에서 설명 가능한 연구 핏

후보 평가의 핵심 질문:

> 이 연구실에서 2년 안에 검증 가능한 연구 산출물과 취업/진학에 설명 가능한 기술 포트폴리오를 만들 수 있는가?

기존 LLM Economist++ / LLM 기반 경제 시뮬레이션 / ICRL 경험은 "경제학 논문 경험"으로만 설명하지 않는다. 컨택 및 CV에서는 **LLM/agent 기반 경제 시뮬레이션 구현, 실험 설계, 결과 해석 경험**으로 제한해 표현한다.

상담용 자기설명은 정체성 단정보다 다음의 사실 중심 문장으로 관리한다.

> 경제학 주전공과 소프트웨어 복수전공을 병행했고, 학부연구생 활동에서 LLM/agent/economic simulation 관련 연구를 수행했습니다.  
> 석사 연구실은 금융·경제·사회 문제를 ML/통계/AI 방법론으로 다루며, Python 기반 구현과 실험 결과를 만들 수 있는 곳을 우선적으로 검토하고 있습니다.  
> 경제학계 연구실과 정보/데이터사이언스계 연구실을 병행 조사하되, 각 연구실의 최근 논문과 실제 지도 가능 주제에 맞춰 연구계획을 조정하려 합니다.

### 0.1 2026-05-11 컨설팅 통합 메모

`admission_consulting_2026-05-11.md`의 후보 추천 판단은 이 문서로 통합한다. 핵심은 다음이다.

- 현재 지원전략은 전통 경제학 전형만이 아니라, 경제/금융/사회 문제를 ML·통계·AI로 다루는 연구실을 병행 탐색하는 방식으로 둔다.
- LLM Economist++ 경험은 "경제학 논문 경험"으로만 좁히지 말고, **LLM/agent 기반 경제 시뮬레이션을 구현하고 실험한 연구 경험**으로 설명한다.
- 후보 판단 기준은 "경제학적으로 유명한 연구실인가"보다 **2년 뒤 Python, ML, 데이터분석, 시계열, 텍스트분석, LLM/agent simulation 기반 포트폴리오를 만들 수 있는가**에 둔다.

지원축은 두 갈래로 관리한다.

| 지원축 | 핵심 후보 | 해석 |
|---|---|---|
| 정보계/DS계 메인 루트 | NAIST Social Computing/NLP, Tsukuba Risk, Hitotsubashi SDS, Shiga DS, Kyoto Social Informatics | 구현 포트폴리오와 데이터 기반 연구 산출물로 연결하기 쉬움 |
| 경제학계 안의 AI 친화 루트 | Kobe Iwatsubo/KIMAP, Kyushu Murao, Tohoku DSSR, Osaka Matsumura, Kobe Motegi 등 | 경제학 배경을 살리되 연구계획서에 AI 구현 요소를 명시해야 함 |

연구계획서는 모든 후보에게 하나의 만능 문장으로 보내지 말고, 다음 두 축 중 연구실별로 하나를 메인으로 조정한다.

| 연구계획 축 | 예시 문장 | 특히 맞는 후보 |
|---|---|---|
| Financial AI | financial text + market data fusion for interpretable risk forecasting | Kobe Iwatsubo, Tsukuba Risk, Hitotsubashi SDS, Shiga DS |
| Social/Economic AI Simulation | LLM/agent-based simulation for socio-economic decision making and market behavior | Kyushu Murao, NAIST Social Computing, Tohoku DSSR, Tsukuba Risk |

### 0.2 연구 아이디어 사용 규칙

`research_note.md`의 아이디어는 후보별 컨택에서 하나씩만 선택해 사용한다. 여러 아이디어를 동시에 제시하면 연구 핏이 흐려질 수 있다.

| 아이디어 | 컨택용 표현 | 적합 후보 | 주의점 |
|---|---|---|---|
| 비평이 문화소비를 이끌어내는가 | 문화/콘텐츠 비평 텍스트가 소비 행동에 미치는 영향을 텍스트 분석과 시계열/인과추론으로 분석 | Tohoku DSSR, Hitotsubashi SDS, Shiga DS, Kyoto Social Informatics | 금융AI 직접성은 약하므로 Social Research AI로 분류 |
| ICRL 불안정성 개선 | LLM-agent/economic simulation에서 history selection과 탐색 정보가 의사결정 안정성에 미치는 영향 검증 | NAIST Social Computing/NLP, Kyushu Murao, Tsukuba Risk | 단순 AdaGrad 적용으로 축소하지 말고 안정성/강건성 문제로 재정의 |
| Black-Scholes Diffusion | diffusion-based generative modeling을 금융 시나리오 생성, 옵션/리스크 분석의 탐색적 도구로 검토 | Kobe Iwatsubo, Tsukuba Risk, 금융공학/계량 후보 | 수학 난도가 높고 기존 확률과정과의 차별화가 필요하므로 서브 아이디어로 취급 |

## 1. 현재 초안에 남아 있던 문제점

1. **경제학과 소속 여부와 계량경제학 적합성을 너무 강하게 앵커로 사용했다.**  
   기존 표는 좋은 경제학/계량경제학 후보를 찾는 데는 유용하지만, AI 엔지니어 커리어에 필요한 구현 경험, 데이터 파이프라인, 모델링 포트폴리오, 실제 기업 수요와의 연결성은 별도 기준으로 보지 않았다.

2. **"계량경제학적으로 강함"과 "AI 커리어에 강함"을 구분하지 않았다.**  
   시계열, 베이지안, 금융계량은 좋은 연구 훈련이지만, 그것만으로는 AI 엔지니어 포지션에서 요구하는 Python/ML 구현, 실험 관리, 데이터 전처리, 모델 평가, MLOps적 사고가 자동으로 생기지 않는다.

3. **Financial AI와 Social Research AI가 한 표 안에 섞여 있었다.**  
   금융 시계열/리스크/신용예측과 텍스트마이닝/소비·문화·여론 분석/계산사회과학은 필요한 지도교수, 데이터, 평가 지표가 다르다. 단일 순위가 아니라 트랙별 후보군으로 관리해야 한다.

4. **LLM Economist++와의 직접 적합성에 너무 묶일 위험이 있었다.**  
   LLM 기반 경제 시뮬레이션은 좋은 출발점이지만, 일본 석사와 취업을 함께 보면 "LLM 경제 시뮬레이션만 하는 사람"보다 "금융·경제·사회 데이터를 AI/ML로 분석하고 구현할 수 있는 사람"으로 읽히는 편이 더 강하다.

5. **일본 기업 수요 근거가 평가표에 반영되지 않았다.**  
   IPA/METI/FSA 자료가 말하는 수요는 단순 예측 성능이 아니라 데이터사이언스, 데이터 엔지니어링, AI 활용, 데이터 관리, 설명가능성, 보안, 거버넌스, 실무 문제 해결이다.

6. **정보과학/데이터사이언스/사회정보학 후보가 부족했다.**  
   경제학 지도교수 상담용 문서에서는 경제학 후보를 설명 가능한 형태로 제시하되, 실제 지원 포트폴리오에서는 정보계·데이터사이언스계 후보를 "추가 후보"가 아니라 공동 메인 후보로 다뤄야 한다.

7. **지원자의 실제 학업 정체성을 과소반영했다.**  
   기존 문서는 "경제학 기반 지원자가 AI/ML 쪽으로 넓히는 전략"에 가까웠다. 그러나 실제 정체성은 경제학 훈련을 가진 AI공학 지향 지원자다. 따라서 순수 계량경제학 후보는 더 냉정하게 보고, AI/NLP/DS/사회정보학 후보의 우선순위를 높여야 한다.

## 2. 일본 수요 근거의 해석

- IPA `DX動向2025-AI時代のデジタル人材育成`은 일본 기업의 DX 인재 부족과 실천형 학습/PBL의 중요성을 강조한다. 특히 일본 기업에서 DX를 추진할 인재 부족이 매우 크다는 점은 AI/데이터 포트폴리오의 취업 신호가 강하다는 근거가 된다.
- METI `Society 5.0時代のデジタル人材育成` 보고서는 스킬 기반 인재 육성, 비즈니스·엔지니어링·디지털 리터러시의 결합을 강조한다.
- METI/IPA `デジタルスキル標準 ver.2.0`은 AX(AI Transformation) 확산에 따라 데이터 활용과 데이터 매니지먼트 역할을 더 중요하게 본다.
- FSA `AI Discussion Paper Version 1.1`은 금융권 AI에서 건전한 활용, 리스크 관리, 거버넌스, 규제 적용 명확화가 중요하다는 방향을 제시한다.

해석: 지원 전략은 "경제학 연구실 지원"이 아니라 **경제·금융·사회 문제에 AI/ML을 적용하는 AI공학 지향 연구자/실무형 분석가 포지셔닝**이어야 한다.

## 3. 수정된 평가 기준

각 후보는 다음 6개 축을 5점 만점으로 본다. 단, 모든 항목을 균등하게 해석하지 않는다. 현재 정체성 기준에서는 AI공학 신호가 가장 중요하다.

| 평가축 | 의미 |
|---|---|
| AI 엔지니어 적합성 | Python/ML 구현, 데이터 전처리, 모델 실험, 대규모 데이터, NLP/LLM/시계열 모델 구현 경험으로 이어지는가 |
| AI 리서처 적합성 | ML/AI/통계/계량 방법론 자체의 연구 novelty, 논문 작성, 실험 설계 훈련으로 이어지는가 |
| Financial AI 적합성 | 금융 시계열, 금융 텍스트, 신용예측, 리스크, 시장미시구조, XAI/거버넌스와 연결되는가 |
| Social Research AI 적합성 | 사회·경제 텍스트, 여론/소비/문화 데이터, 계산사회과학, agent-based simulation과 연결되는가 |
| 일본 기업 수요 연결성 | 일본 DX/AI 인재 수요, 금융AI, 데이터 관리, 설명가능성, 실무 문제 해결과 연결되는가 |
| 입시 현실성 | 석사 입시 경로, 영어/일본어 요건, 연구계획서 방어 가능성, 지도 가능성, 경쟁 난도를 종합 |

가중 해석:

- AI 엔지니어 적합성: 최상위 기준
- AI 리서처 적합성: 최상위 기준
- Financial AI / Social Research AI / Economy Simulation 적합성: 도메인 방향을 결정하는 기준
- 일본 기업 수요 연결성: 취업·DX 적합성을 보는 기준
- 입시 현실성: 전략 배치 기준
- 경제학적 정통성: 보조 기준

주의: 입시 현실성은 중요하지만 보조지표다. 입시가 쉬워도 AI공학 신호가 약하면 좋은 선택이 아니다. 반대로 입시 현실성이 낮아도 AI공학 정체성을 강하게 만들어주는 후보는 상향 카드로 남길 가치가 있다.

## 4. 트랙별 후보 재정렬

### A. Financial AI

가장 직접적으로 "금융 데이터를 AI/ML로 분석하는 사람"이라는 포트폴리오를 만들 수 있는 트랙.

1. Kobe University - Kentaro Iwatsubo  
   금융, 국제금융, 딥러닝 기반 자산가격 예측, Python 기반 머신러닝 석사지도 사례가 있어 Financial AI 메인 후보로 가장 강하다.
2. Osaka University OSIPP - Mamiko Yamashita  
   금융계량, 리스크 관리, 예측. AI 구현은 연구계획서에서 보강해야 하지만 금융AI 주제와 잘 맞는다.
3. Hokkaido University - Ryuta Sakemoto  
   asset pricing, risk management, 금융기관 quantitative analyst 경력. 금융 실무 연결성이 좋다.
4. University of Tsukuba - Risk and Resilience Engineering  
   금융 리스크, 고빈도 데이터, 정보보안, NLP, computational social science, social simulation이 한 프로그램 안에 공존한다. 금융AI/리스크AI/거버넌스 축으로 추가 조사 가치가 크다.
5. Hitotsubashi University - Jouchi Nakajima  
   시계열, Bayesian statistics, macro/finance empirical analysis, big data. 금융AI보다는 금융 시계열 방법론 후보.
6. Kobe University - Kaiji Motegi / Kyushu University - Taro Takimoto  
   시계열·인과·금융/거시 데이터 방법론 백업 후보.

### B. Social Research AI

사회·경제 텍스트, 문화/소비/여론 데이터, 계산사회과학, 행동 변화 분석 포트폴리오를 만들기 좋은 트랙.

1. NAIST - Social Computing Lab / NLP Lab  
   소셜미디어, Web 텍스트, NLP, 계산사회학, 사회문제 분석, AI 사회실장/신뢰성. Social Research AI 후보로 매우 강하다.
2. Hitotsubashi University - Graduate School of Social Data Science  
   사회과학과 데이터사이언스의 결합, 통계·컴퓨터과학·AI·윤리·PBL을 명시한다. 단, 석사 입시 정보는 일본어 중심일 수 있어 추가 확인 필요.
3. Kyoto University - Graduate School of Informatics, Social Informatics Course  
   사회와 정보기술의 관계, 정보시스템 설계/분석, PBL. 사회정보학 기반으로 안정적이다.
4. Osaka University - Naohiro Matsumura  
   data mining, text mining, behavior change. 문화/소비/행동 데이터 분석과 연결 가능하다.
5. Tohoku University - DSSR / Takuya Ishihara  
   고차원 대규모 데이터, 서비스 산업, 사회경제 문제 해결, 경제·경영과 데이터사이언스의 융합.
6. Keio University SFC - Graduate School of Media and Governance / Cyber Informatics  
   기술과 사회문제 해결의 결합, 프로젝트 기반 성격. 경제학 지도교수 상담 이후 정보계 확장 후보로 검토.

### C. AI in Economics / Economy Simulation

기존 LLM Economist++ 경험과 가장 자연스럽게 이어지는 트랙. 다만 "LLM 경제 시뮬레이션만"이 아니라 ML/agent/data science 구현 중심으로 표현해야 한다.

1. Kyushu University - Tetsushi Murao  
   computational economics, machine learning, multi-agent deep reinforcement learning, computational social science, market competition. 기존 연구와 새 AI 커리어 포지션을 잇는 핵심 후보.
2. Tohoku University - DSSR / Takuya Ishihara  
   경제·경영 기반 데이터사이언스, 고차원 데이터, 서비스 산업, 사회경제 문제 해결.
3. University of Tsukuba - Risk and Resilience Engineering  
   social simulation, agent technology, data mining, NLP, financial risk management 관련 교원이 있어 agent-based social/economic simulation으로 확장 가능.
4. Hokkaido University - Yoske Igarashi  
   수리모델링과 컴퓨터 시뮬레이션을 경제·사회 문제에 적용한다는 설명이 현재 포지션과 잘 맞는다.
5. Kyoto University - Social Informatics / UTokyo IST - Social ICT  
   경제학과 직접 매칭은 약하지만, 사회 시스템을 정보기술로 분석/설계하는 방향에서는 강하다.

### D. Backup: Econometrics / Time-series methods

AI 커리어의 메인 트랙은 아니지만, 금융AI·경제AI의 방법론 기반을 제공하는 백업 트랙.

1. Kobe University - Kaiji Motegi  
   time series, mixed frequency data, Granger causality, financial/macro time series.
2. Hitotsubashi University - Jouchi Nakajima  
   Bayesian time series, policy evaluation, big data, macro/finance empirical analysis.
3. Kobe University - Naoya Sueishi  
   high-dimensional data, dimension reduction, econometrics, R/Python.
4. Kyushu University - Taro Takimoto  
   causal analysis in time series, applied macroeconometrics.
5. Hokkaido University - Yoshihide Kakizawa  
   time series/statistical theory. AI/실무 연결성은 연구계획서에서 보강해야 한다.
6. Nagoya University G30 Economics and Business Administration  
   영어 프로그램과 입시 경로 장점. 다만 개별 AI/ML 지도교수 매칭을 별도 확인해야 한다.

## 5. 후보별 점수표

점수는 2026-05-03 기준 공식 페이지와 현재 확보한 정보 기반의 1차 평가다. 개별 교수의 최근 3년 논문, 석사지도 가능성, 입시 요건을 확인하면 변동될 수 있다.

중요: 이 표는 "합격 가능성 순위"가 아니라 **AI공학 커리어 정체성과의 거리 측정표**다. 따라서 입시 현실성이 높아도 AI 엔지니어/AI 리서처 점수가 낮으면 메인 후보가 되기 어렵고, 입시 현실성이 낮아도 AI공학 신호가 강하면 상향 후보로 유지할 가치가 있다.

| 후보 | 주 트랙 | AI 엔지니어 | AI 리서처 | Financial AI | Social Research AI | 일본 기업 수요 | 입시 현실성 | 1차 판단 |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Kobe - Kentaro Iwatsubo | Financial AI | 4.0 | 3.5 | 5.0 | 2.0 | 4.5 | 3.0 | 금융AI 메인 후보. Python/ML/자산가격 예측 포트폴리오에 강함. |
| Kyushu - Tetsushi Murao | Economy Simulation / Social AI | 4.5 | 4.5 | 3.0 | 4.5 | 4.5 | 3.5 | AI+경제+multi-agent를 잇는 최상위 후보. |
| Tohoku - DSSR / Takuya Ishihara | Social/Econ Data Science | 4.0 | 4.0 | 3.0 | 4.5 | 4.5 | 3.5 | 경제 데이터사이언스와 사회문제 해결에 강함. |
| Osaka - Naohiro Matsumura | Social Research AI | 3.5 | 3.5 | 2.5 | 4.5 | 4.0 | 3.0 | 텍스트/행동변화/문화·소비 분석 후보. |
| Kobe - Kaiji Motegi | Backup methods | 2.5 | 3.5 | 3.5 | 2.5 | 3.5 | 3.0 | 시계열 방법론 백업. AI 포트폴리오는 별도 설계 필요. |
| Kyushu - Taro Takimoto | Backup methods | 2.5 | 3.5 | 3.5 | 2.5 | 3.5 | 3.5 | 인과/시계열 기반 백업. 금융AI보다 계량 안정성. |
| Hokkaido - Ryuta Sakemoto | Financial AI | 2.5 | 3.0 | 4.5 | 2.0 | 4.0 | 3.0 | 금융 리스크/자산가격 실무 연결성 좋음. |
| Osaka OSIPP - Mamiko Yamashita | Financial AI | 2.5 | 3.5 | 4.5 | 2.0 | 4.0 | 3.0 | 금융계량·리스크·예측 후보. ML 구현을 계획서에서 보강. |
| Kobe - Naoya Sueishi | Backup methods | 3.0 | 4.0 | 2.5 | 2.5 | 3.5 | 3.0 | 고차원 데이터/차원축소. ML 방법론 기초 후보. |
| Nagoya G30 Economics and Business Administration | Backup / English route | 2.5 | 2.5 | 3.0 | 3.0 | 3.0 | 4.0 | 영어 프로그램 장점. AI 지도교수 매칭 확인 필요. |
| Hokkaido - Yoske Igarashi | Economy Simulation | 2.5 | 3.0 | 2.0 | 4.0 | 3.5 | 3.0 | 경제·사회 시뮬레이션 방향. AI 구현은 직접 설계 필요. |
| Hitotsubashi - Jouchi Nakajima | Financial time-series methods | 2.5 | 4.0 | 4.0 | 3.0 | 3.5 | 2.0 | 매우 강한 시계열/베이지안 후보. 입시·지도경로 확인 우선. |
| Hokkaido - Yoshihide Kakizawa | Backup methods | 2.0 | 3.0 | 3.0 | 2.0 | 3.0 | 3.0 | 순수 시계열/통계 백업. AI 커리어 직접성은 약함. |
| Hitotsubashi - Graduate School of Social Data Science | Social Research AI | 4.5 | 4.0 | 3.5 | 5.0 | 5.0 | 2.5 | 사회과학+AI+PBL 조합. 석사 입시/언어 확인 필요. |
| Shiga University - Graduate School of Data Science | Data Science / Social AI | 4.5 | 3.5 | 3.0 | 4.0 | 5.0 | 3.5 | 실무형 DS 포트폴리오에 강함. 금융/경제 도메인은 직접 설계. |
| NAIST - Social Computing / NLP | Social Research AI | 4.5 | 4.5 | 2.5 | 5.0 | 4.5 | 3.0 | NLP/소셜텍스트/계산사회과학 최상위 추가 후보. |
| Kyoto - Informatics / Social Informatics | Social Research AI | 4.0 | 4.0 | 2.5 | 4.5 | 4.5 | 2.5 | 사회정보학 기반. 경제학 상담 후 정보계 확장 후보. |
| Tsukuba - Risk and Resilience Engineering | Financial/Social AI | 4.0 | 3.5 | 4.0 | 4.0 | 4.5 | 3.0 | 리스크, 보안, 금융, 사회시뮬레이션이 만나는 실전형 후보. |
| UTokyo - IST / Social ICT / AI Center | AI Research / Social ICT | 5.0 | 5.0 | 3.0 | 4.0 | 5.0 | 1.5 | AI 커리어는 최강급이나 입시 난도와 전공시험 리스크 큼. |
| Science Tokyo - Computing / DSAI | AI Engineering / AI Research | 4.5 | 4.5 | 2.5 | 3.0 | 5.0 | 2.0 | AI/DS 자체는 강함. 금융·사회경제 도메인 매칭 확인 필요. |
| Keio SFC - Media and Governance / Cyber Informatics | Social implementation | 4.0 | 3.5 | 2.0 | 4.5 | 4.5 | 3.0 | 프로젝트 기반 사회실장 후보. 사립/연구주제 매칭 확인 필요. |

## 6. 전략적 해석

### 정체성 기준 결론

현재 포지션은 "경제학 석사 지원자"가 아니라 **경제학 도메인을 이해하는 AI공학 지향 지원자**다. 그러므로 경제학계 후보는 더 이상 자동 메인이 아니다. 메인 후보는 AI/ML 구현, 논문형 실험, 데이터 기반 프로젝트, NLP/LLM/시계열/agent simulation 포트폴리오가 실제로 쌓이는 곳이어야 한다.

### 최우선군: AI공학 커리어 포트폴리오가 자연스럽게 쌓이는 후보

- NAIST - Social Computing / NLP
- Hitotsubashi - Social Data Science
- Tsukuba - Risk and Resilience Engineering
- Shiga - Graduate School of Data Science
- Kyushu - Tetsushi Murao
- Tohoku - DSSR / Takuya Ishihara
- Kobe - Kentaro Iwatsubo

해석: 상담용으로는 경제학계 후보를 먼저 보여줄 수 있지만, 실제 지원전략에서는 정보계/데이터사이언스계 후보를 뒤로 미루면 안 된다.

### 경제학계 안에서 비교적 강한 메인 후보

- Kyushu - Tetsushi Murao: AI+경제+multi-agent 조합이 가장 자연스럽다.
- Tohoku - DSSR / Takuya Ishihara: 경제·경영 데이터사이언스와 사회경제 문제 해결에 강하다.
- Kobe - Kentaro Iwatsubo: Financial AI 포트폴리오를 만들기 좋다.
- Osaka - Naohiro Matsumura: Social Research AI와 텍스트마이닝 방향에서 의미 있다.

### 조심해야 할 후보군

전통 계량/금융계량/시계열 후보는 연구 훈련 자체는 좋지만, AI공학 정체성을 자동으로 강화하지 않는다. 이 후보들을 선택하려면 연구계획서 안에 Python 구현, ML baseline, 딥러닝/Transformer, NLP/LLM, model comparison, explainability, drift detection 같은 요소를 명시적으로 넣어야 한다.

### 금융AI 메인으로 갈 때

Kobe Iwatsubo와 Tsukuba Risk and Resilience를 핵심 후보로 두고, Shiga DS/Hitotsubashi SDS에서 금융 데이터 프로젝트를 설계할 수 있는지도 본다. Osaka OSIPP Yamashita / Hokkaido Sakemoto / Hitotsubashi Nakajima는 금융 도메인은 강하지만, AI공학 포트폴리오는 연구계획서에서 별도로 설계해야 한다.

연구계획서 키워드:

- financial time-series forecasting
- financial text + market data fusion
- interpretable financial AI
- risk management and model uncertainty
- data/concept drift in financial markets

### 사회AI 메인으로 갈 때

NAIST Social Computing / Hitotsubashi SDS / Kyoto Social Informatics / Tohoku DSSR를 중심으로 본다. Osaka Matsumura는 경제학계 안에서 텍스트/행동변화 분석으로 연결 가능한 후보로 둔다.

연구계획서 키워드:

- socio-economic text analysis
- social indicators from text data
- consumer/cultural data analytics
- computational social science
- agent-based social simulation
- trustworthy AI for social systems

### 경제AI/시뮬레이션 메인으로 갈 때

Kyushu Murao를 가장 강한 앵커로 두고, Tohoku DSSR / Tsukuba Risk and Resilience / Hokkaido Igarashi를 확장 후보로 둔다.

연구계획서 키워드:

- computational economics with machine learning
- multi-agent simulation of markets
- LLM/agent-based economic modeling
- policy and market simulation
- machine learning for decision-making and market competition

### 계량/시계열 백업으로 갈 때

Kobe Motegi, Hitotsubashi Nakajima, Kobe Sueishi, Kyushu Takimoto, Hokkaido Kakizawa는 방법론 훈련 후보로 둔다. 다만 이 트랙은 AI 엔지니어 포트폴리오가 자동으로 생기지 않으므로, 연구계획서 안에 반드시 Python 구현, 금융 데이터, 텍스트 데이터, ML baseline, model comparison을 넣어야 한다.

## 7. 내일 지도교수 상담에서 말할 5문장

1. "저는 경제학을 주전공으로 공부하면서 경제 시스템을 보는 사고방식을 익혔지만, 3학년 이후에는 소프트웨어 복수전공과 학부연구생 활동을 통해 인공지능 공학 쪽으로 연구 관심이 이동했습니다."
2. "현재 연구 경험도 LLM, agent, ICRL, 경제 시뮬레이션처럼 AI 방법론을 경제 문제에 적용하는 방향에 가깝습니다."
3. "그래서 석사 연구실은 전통 경제학 주제 자체보다, AI/ML을 금융·사회경제 시스템에 적용할 수 있는 곳을 우선적으로 보고 싶습니다."
4. "다만 제 강점은 경제학 배경을 버리는 것이 아니라, AI 모델을 실제 경제·금융·사회 문제에 적용할 수 있는 도메인 이해력으로 가져가는 것이라고 생각합니다."
5. "이런 관점에서 경제학계 연구실과 정보/데이터사이언스계 연구실을 병행 탐색하는 것이 적절한지 조언을 구하고 싶습니다."

## 8. 상담 후 추가 조사해야 할 정보계/AI계열 후보군 방향

1. **정보과학/정보공학 대학원**
   - UTokyo IST, Kyoto Informatics, Science Tokyo Computing, NAIST Information Science.
   - 확인할 것: 전공시험 난도, 영어 입시 여부, 연구실 사전 컨택 필요성, 지도교수의 금융/사회 데이터 수용성.

2. **데이터사이언스 대학원**
   - Hitotsubashi Social Data Science, Shiga Data Science, Yokohama City Data Science, Tsukuba systems/data-related programs.
   - 확인할 것: 석사 입시 언어, PBL/기업 공동연구 가능성, 금융/사회경제 주제 허용성.

3. **AI/NLP/ML 연구실**
   - NAIST NLP/Social Computing, Kyoto Social Informatics, Tsukuba AI/Information Systems, UTokyo Creative Informatics.
   - 확인할 것: 일본어 텍스트 분석, 금융 뉴스/공시 분석, LLM 정보추출 주제 수용 가능성.

4. **금융공학/수리정보/리스크공학**
   - Tsukuba Risk and Resilience, Kyushu Economic Engineering, Osaka OSIPP financial econometrics, Hokkaido finance/risk.
   - 확인할 것: 금융 시계열 Transformer, XAI, model risk, concept drift 같은 AI 주제를 얼마나 자연스럽게 넣을 수 있는지.

5. **계산사회과학/사회정보학**
   - Kyushu Murao, NAIST Social Computing, Kyoto Social Informatics, Hitotsubashi SDS, Keio SFC.
   - 확인할 것: agent-based simulation, social media/text mining, 사회지표화, 행동 변화 분석의 지도 가능성.

## 9. 다음 액션

1. 상담 전에는 자기 정체성을 먼저 정리한다: **경제학적 사고를 가진 AI공학 지향 지원자**.
2. 상담에서 경제학계 후보 3개를 설명 가능한 앵커로 둔다: **Kyushu Murao / Kobe Iwatsubo / Tohoku DSSR**.
3. 동시에 정보계/데이터사이언스계 후보를 "추가 옵션"이 아니라 실제 메인 지원군으로 병행해도 되는지 묻는다: **NAIST / Hitotsubashi SDS / Tsukuba / Shiga / Kyoto Informatics**.
4. 상담 후에는 후보를 두 문서로 분리한다.
   - 교수 상담용: 경제학 기반 AI/ML 응용 연구실 후보
   - 실제 지원전략용: AI/ML/DS 중심 연구실 + 금융·사회경제 도메인 적용 후보
5. 각 후보에 대해 최근 3년 논문 3개, 석사 지도 가능성, 입시 언어, 컨택 필요 여부를 확인한다.
6. 연구계획서 초안은 3개 버전으로 만든다.
   - Financial AI 버전
   - Social Research AI 버전
   - AI in Economics / Economy Simulation 버전

## 10. 참고한 공식/준공식 출처

- IPA, `DX動向2025-AI時代のデジタル人材育成`: https://www.ipa.go.jp/digital/chousa/discussion-paper/dx2025_digital_talent_ai_era.html
- METI, `Society5.0時代のデジタル人材育成に関する検討会` 보고서: https://www.meti.go.jp/press/2025/05/20250523005/20250523005.html
- METI, `デジタルスキル標準 ver.2.0`: https://www.meti.go.jp/press/2026/04/20260416002/20260416002.html
- FSA, `AI Discussion Paper Version 1.1`: https://www.fsa.go.jp/en/news/2026/20260303/aidp.html
- Kobe University, Kentaro Iwatsubo: https://www.econ.kobe-u.ac.jp/en/staff/2179
- Kyushu University, Tetsushi Murao: https://hyoka.ofc.kyushu-u.ac.jp/html/100017841_en.html
- Kyushu University, Graduate School of Economics staff list: https://www.econ.kyushu-u.ac.jp/english/staff/
- Tohoku University DSSR: https://www2.econ.tohoku.ac.jp/~DSSR/en.outline.html
- Kobe University, Kaiji Motegi: https://www.econ.kobe-u.ac.jp/en/staff/5613/
- Kobe University, Naoya Sueishi: https://www.econ.kobe-u.ac.jp/en/staff/5408
- Osaka University OSIPP, Mamiko Yamashita: https://www.osipp.osaka-u.ac.jp/ja/osipp-faculty/yamashita-mamiko/
- Hitotsubashi University, Jouchi Nakajima: https://www.ier.hit-u.ac.jp/English/faculty/nakajima.html
- Hokkaido University, Ryuta Sakemoto: https://rebn.econ.hokudai.ac.jp/en/members/researchers
- Hokkaido University faculty list: https://www.econ.hokudai.ac.jp/en/archives/professors/saito-hisamitsu
- Osaka University Shikake Lab / Naohiro Matsumura: https://mtmr.jp/en/
- Nagoya University G30 Economics and Business Administration: https://admissions.g30.nagoya-u.ac.jp/graduate/business/
- Hitotsubashi University Social Data Science: https://www.sds.hit-u.ac.jp/en/aboutus/
- Shiga University Graduate School of Data Science: https://www.ds.shiga-u.ac.jp/graduate/
- NAIST Social Computing Lab: https://sociocom.naist.jp/
- NAIST NLP Lab: https://nlp.naist.jp/en/
- Kyoto University Social Informatics: https://www.soc.i.kyoto-u.ac.jp/en/
- University of Tsukuba Risk and Resilience Engineering: https://www.risk.tsukuba.ac.jp/en/
- University of Tokyo IST: https://www.i.u-tokyo.ac.jp/index_e.shtml
- Science Tokyo DSAI Center: https://www.dsai.titech.ac.jp/en/about/
- Keio SFC Graduate School of Media and Governance: https://www.sfc.keio.ac.jp/gsmg/en/about/
