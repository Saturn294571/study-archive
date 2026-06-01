# CV Draft for Japanese Master's Applications

작성일: 2026-05-11  
용도: 일본 석사 컨택/사전심사/출원용 CV 초안. 실제 제출 전에는 영문 1-2페이지 형식으로 정리한다.

## 0. Positioning Statement

Economics undergraduate with software/AI training, interested in applying machine learning, natural language processing, and agent-based simulation to financial and socio-economic systems.

한국어 설명:

경제학을 주전공으로 공부하며 경제·금융 시스템을 보는 도메인 감각을 쌓았고, 3학년 이후 소프트웨어/AI 쪽으로 연구 관심을 확장했다. 현재 포지션은 전통 경제학 연구자보다 `financial and socio-economic systems를 다루는 AI/ML researcher or engineer`에 가깝다.

### (상담용 : 왜 일본이어야 하는가?)
1. 상대적으로 괜찮은 석박사 연구환경
2. 한국보다 조기에 정부주도하 인공지능 산업 투자 시작
3. 다른 유학 후보(미국,유럽 등)와 비교시 물리적 거리 및 문화적 거리가 비교적 가까움
  - 각 후보별 탈락 이유
    - 미국 : 매우 높은 학업적 성취 기준, 박사 풀펀딩이 없다면 매우 높은 학업비&생활 물가
    - 유럽(독일) : 학업비는 미국보단 저렴. 하지만 마찬가지로 높은 학업적 기준,문화적 이질성, 일정기준 미달시 커리큘럼 자격 자체 박탈(fail 3번로 기억), 마냥 좋진 않은 독일 취업시장
4. 국공립 대학의 경우 저렴한 등록금 및 장학금제도
5. 일본에서의 석-박사간 크지 않은 임금격차
6. 상대적으로 괜찮은 학사/석사 취업 시장 상황

## 1. Basic Information

| 항목 | 내용 |
|---|---|
| Name | 노동주 (盧東柱; No Dong-ju) |
| University | Inha University |
| Major | Economics |
| Additional major/minor | Interdisciplinary major in Software Convergence Engineering (`連携専攻：ソフトウェア融合工学`, from 2024-2) |
| Enrollment date | 2021-03-02 |
| Current status | Undergraduate student, 4th year |
| Cumulative GPA | 4.18 / 4.50 |
| Credits earned | 136 |
| Expected graduation | 2027-March |
| Email | Ocean33@inha.edu |
| GitHub / Portfolio | https://github.com/Saturn294571 |
| Languages | Korean native, English TOEFL target 80-90+, Japanese JLPT target N2/N1 |

## 2. Education

### Undergraduate

- Major: Economics
- Additional academic focus: software, machine learning, data analysis
- Enrollment date: 2021-03-02
- Current cumulative GPA: 4.18/4.50
- Credits earned so far: 136
- Relevant coursework:
  - Economics: Microeconomics, Macroeconomics, History of Economics, The Analytic Study for Economic Problems, International Finance, Financial Economics, Economics of technology and innovation, Financial Investments, Global Economy, Economics of Social Security,Welfare Economics,Econometrics, Financial Econometrics
  - Quantitative methods: 	Mathematics for Economics, Statistics, Regression Analysis, Statisical Computing, Linear Algebra
  - Computing and data: Introduction to Computer Engineering, Data Structures, Algorithms, Computer Networks, Computer Systems, Database, Data Mining
  - Research training: Undergraduate Research Practice - AI General Research 3, Undergraduate Research Practice - AI General Research 4

## 3. Research Experience

### LLM Economist++: History Filtering for LLM-based In-Context Reinforcement Learning in an Economic Simulation

Status: undergraduate research / paper draft  
Keywords: LLM, in-context reinforcement learning, history filtering, economic simulation, agent-based modeling, computational efficiency

Summary:

- Implemented and evaluated a history selection mechanism inspired by Filtering Learning Histories within an LLM-based ICRL economic simulation framework.
- Built a simplified monopoly market environment with a Cobb-Douglas production function, demand function, and analytically computable optimal benchmark.
- Compared baseline ICRL and LHF-style filtered-history ICRL in terms of policy quality and computational cost.
- Found that LHF maintained near-optimal profit recovery while reducing prompt length and execution cost.

Key result draft:

| Metric | Baseline | LHF |
|---|---:|---:|
| Profit mean | 68.9485 | 68.6464 |
| Profit std | 0.5621 | 0.4904 |
| Recovery ratio | 0.9955 | 0.9911 |

Limitations to state honestly:

- Single or limited seed setting
- Simplified static monopoly environment
- Simple top-k history filtering rule
- Needs robustness checks across dynamic, multi-agent, and parameter-varied environments

## 4. Project Experience

### Selected Projects

#### Project Cassandra: 2025 Economics Academic Festival

Topic: "Why did the exchange rate surge despite strong exports in 2025?"  
Format: economics research project / festival paper / award-winning presentation

- Analyzed the 2025 Korean macroeconomic "export-exchange rate paradox" using a modified IS-LM-BP framework with OLS, VAR, and impulse response analysis.
- Built and used an AI-assisted research workflow for research design, data collection support, coding, visualization, and paper drafting.
- Produced a full paper and empirical figures based on monthly macroeconomic data (2015-2025), focusing on fiscal dominance and risk premium channels.
- Received an encouragement prize (`奨励賞`) in an on-campus AI-themed economics academic festival.

#### Festival Compass in Seoul: ML-based Recommendation Service

Topic: recommendation system for reducing tourism concentration in Seoul  
Format: club ML service contest project

- Developed the core recommendation model using TF-IDF and cosine similarity for culture/festival recommendation.
- Built and deployed a FastAPI backend service, connecting offline model artifacts with online API inference.
- Worked on backend and ML integration with Python, pandas, scikit-learn, FastAPI, SQLite, Docker, and Google Cloud Run.
- Designed a two-track recommendation logic combining similarity-based retrieval and less-visited district recommendation.

### Economic / Financial AI Project Candidates

These are not yet all completed outputs. Use only completed work in the final CV.

- Financial/economic sentiment analysis
- Financial time-series forecasting with transformer-based models
- Credit forecasting
- Graph-based modeling of asset markets
- LLM/agent-based market simulation

### Previous Activities

- On-campus AI-themed economics academic festival: encouragement prize (`奨励賞`), research paper and presentation completed
- Club ML service contest: recommendation service prototype built and deployed
- Undergraduate research assistant activity: detail TBD

## 5. Technical Skills

Draft categories:

- Programming: Python, TBD
- Data analysis: pandas, NumPy, statsmodels, scikit-learn, TBD
- Machine learning: supervised learning, time-series modeling, NLP, LLM API use, TBD
- Research tools: LaTeX/Markdown, Git/GitHub, Zotero or reference manager TBD
- Econometrics/statistics: regression, time-series, hypothesis testing, financial econometrics, TBD

## 6. Research Interests

Primary:

- Financial AI
- Socio-economic AI
- Computational economics
- LLM/agent-based simulation
- NLP for economic and social text data

Possible proposal titles:

- Interpretable Financial AI for Text-Market Data Fusion and Risk Forecasting
- LLM/Agent-based Simulation for Socio-economic Decision Making and Market Behavior
- Robust History Selection and Stabilization in LLM-based Economic Simulation

## 7. Admission Target Fit

Strong fit:

- NAIST Information Science: NLP, social computing, AI-oriented research
- Tsukuba Risk and Resilience Engineering: risk, resilience, engineering methods, social/financial systems
- Kobe KIMAP/Economics: financial AI and economics background
- Kyushu Economics: computational economics and multi-agent simulation
- Hitotsubashi/Shiga/Kyoto: social data science and social informatics

## 8. Missing Information Checklist

- TOEFL/JLPT scores or expected test dates
- Paper title/status
- Supervisor/lab name
- Exact contest/festival official names and dates
- Awards, presentations, scholarships
- Concrete technical stack used in LLM Economist++
