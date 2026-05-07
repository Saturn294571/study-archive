# 금융계량 과제 프로젝트
- 핵심 아이디어 및 질문 : 문학적 외생충격(즉, 걸작의 탄생)은 문학산업(여기선 문학도서출판업)의 수요을 견인하는가? 
    - (즉, 다른 소비재에서 '공급부문의 충격이 시장에 어떤 영향을 미치는가?'를 변주)
    - 방법론
        1. 시간대별로 문학상의 수상 평론의 정도를 종합한 문화인덱스 시계열 산출
            - 즉, 어떤 시간선에서 더 풍부한 비평이 많을수록 문화인덱스 크게 상승. 소위, '문화 르네상스'로 명명
        2. 문화인덱스가 문학도서 시장에 판매량이 얼마나 영향을 미치는지, 유의미한 설명을 할 수 있느지 시계열 회귀분석
        3. (필요시) 어떤 요소가 풍부한 평론, 즉, '문화 르네상스'를 이끄는지 문학이론에서 조사


## 1. 선행조사
- Experts, Information, Reviews, and Coordination: Evidence on How Prizes Affect Sales : 프 공쿠르상 -> 판매 영향?; 걸작 권위가 판매 영향
    - 즉, 본 연구는 해당 연구의 문제의식을 같이하되, 개별 도서가 아닌 문학산업 전체의 영향을 분석
- Success in Books: A Big Data Approach to Bestsellers : 도서출판업 시장 구조 (시계열적)
- The Effect of Word of Mouth on Sales: Online Book Reviews : 온라인 도서 리뷰 -> 판매?


## 2. 코딩 (No Direct AI generation!)
- literary_index.py (or .ipynb)
    - scoring_vader(text)
    - (not at assignment)scoring_TF(text)
    - add_sentiment_col(df, text_col, scorer)
- timeseries_analyze.py (or .ipynb)


## 3. 보고서 및 발표
- 보고서(<=5p)
- 발표 (<=10m)
    - ppt
    - 스크립트 


1. 분석 대상: 북미 문학
- 대상 시장: 미국 문학도서출판업
- 기간: 근 10년 (15.01.01 ~ 25.12.31)
- 시간 단위: (api 콜에 따라 다르겠지만 가능하다면 일별)
- 소비/수요 변수: 미국 문학도서 매출액
- 문화인덱스 원천 데이터: 

2. 문화인덱스 계산 규칙:
- 텍스트 단위: 
- 감성분석 도구: VADAR
- 집계 단위:
- 리뷰량 처리 방식: 

3. 시계열 분석:
- 사용할 강의 방법론: 수강중
- 정상성 확인 방식: unit root test, time trend variable
- 기본 비교모형: ARMA 혹은 ARIMA OLS를 통해 R^2, t값 산출
- AI 도움 없이 직접 작성할 부분:
