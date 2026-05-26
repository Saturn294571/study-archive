# Research Summary: LLM Economist++

작성일: 2026-05-11  
용도: 교수 컨택 첨부용 1페이지 research summary 초안. 최종본은 영어 1페이지로 변환한다.

## 1. Working Title

History Filtering for LLM-based In-Context Reinforcement Learning in Economic Simulation

## 2. One-sentence Summary

This project examines whether filtering past learning histories can reduce the computational cost of LLM-based in-context reinforcement learning while maintaining policy quality in a simplified economic simulation environment.

## 3. Background

LLM-based economic simulation has recently been proposed as a way to model decision-making agents that can reason in natural language and adapt their behavior through interaction histories. Unlike standard reinforcement learning, in-context reinforcement learning relies heavily on which past histories are included in the prompt. Therefore, history selection becomes an important design choice that affects both policy quality and computational cost.

## 4. Research Question

How does history filtering affect policy performance and computational efficiency in an LLM-based ICRL economic simulation?

More concretely:

- Does filtered history preserve near-optimal decision quality?
- Does it reduce prompt length and execution cost?
- What limitations appear when the economic environment is simplified?

## 5. Method

The project simplifies the original LLM Economist-style setting into a monopoly production environment.

Economic setup:

- Cobb-Douglas production function
- Linear demand function
- Profit maximization by a firm agent
- Fixed policy parameters from the government side
- Analytically computable optimal benchmark through first-order condition

ICRL setup:

- Baseline: the agent uses previous interaction histories in the prompt.
- LHF-style filtering: only selected high-performing histories are retained.
- Main comparison: policy performance, optimality recovery, prompt/token cost, and execution time.

## 6. Preliminary Results

In the current experiment, both baseline and filtered-history ICRL achieved near-optimal policy quality.

| Metric | Baseline | LHF |
|---|---:|---:|
| Profit mean | 68.9485 | 68.6464 |
| Profit std | 0.5621 | 0.4904 |
| Recovery ratio | 0.9955 | 0.9911 |

Interpretation:

- LHF slightly reduces average profit relative to the baseline.
- The absolute performance loss is small in the current simplified environment.
- The main benefit is computational: filtered history reduces prompt length and can reduce execution time.

## 7. Contribution

The current contribution should be stated modestly.

- It implements a history filtering mechanism in an LLM-based economic ICRL setting.
- It separates policy quality from computational efficiency as evaluation dimensions.
- It provides a small but concrete experimental bridge between LLM-agent simulation and computational economics.

Do not overclaim:

- This is not yet a general theory of LLM economic simulation.
- This does not prove robustness across market structures.
- This does not yet establish real-world policy validity.

## 8. Limitations

Main limitations:

- Simplified monopoly setting
- Static environment
- Limited number of seeds/experiments
- Simple top-k filtering rule
- No Cournot competition, dynamic shocks, heterogeneous agents, or multi-equilibrium setting yet

These limitations are useful for master's application strategy because they naturally define future research directions.

## 9. Future Research Directions

Strong directions:

1. Dynamic and multi-agent market environments
2. Robustness across parameter changes and random seeds
3. More principled history selection mechanisms
4. LLM/agent-based market behavior simulation
5. Connection to financial risk, market forecasting, and model uncertainty

Less stable direction:

- Simply adding more mechanisms without clarifying the research question.

## 10. Link to Master's Research

This project can be connected to Japanese master's applications in three ways.

Financial AI:

- LLM/agent systems for market behavior
- interpretable financial AI
- model uncertainty and decision support

Social Research AI:

- LLM/agent simulation of socio-economic decision making
- text-based social indicators
- computational social science

AI in Economics:

- computational economics
- in-context reinforcement learning
- mechanism design and simulation

## 11. Materials to Attach Later

- Paper PDF
- Shorter paper PDF
- GitHub repository
- One slide figure showing the ICRL loop
- Result table and graph

