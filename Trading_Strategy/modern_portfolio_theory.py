# 현대 포트폴리오 이론

# 평균-분산 최적화(mean-variance optimization, MVO) : 예상 수익률과 리스크의 상관관계를 활용해 포트폴리오를 최적화하는 이론

print()

# 수익률의 표준 편차

# 수익률의 표준편차(standard deviation of returns) : 자산 가격이 평균값에서 벗어나는 정도, 즉 리스크(risk)를 측정하는 방법
# 주식시장에서의 리스크는 흔히 주가의 변동성을 의미
# 정규분포 그래프에서 예상 수익률은 평균값인 μ(뮤)로 나타내고, 리스크는 표준편차인 σ(시그마)로 나타냄

print()

# 효율적 투자선(Efficient Frontier) : 투자자가 인내할 수 있는 리스크 수준에서 최상의 기대수익률을 제공하는 포트폴리오들의 집합

# 효율적 투자선 그래프에서 X축은 리스크(표준편차)이고 Y축은 예상 수익률(평균)
# 파란색 점선으로 표시된 부분을 표휼적 투자선이라고 부르며 붉은 점들은 개별 포트폴리오를 나타냄
# 효율적 투자선 위에 위치한 포트폴리오는 주어진 리스크에서 최대 수익을 창출

print()

# 시총 상위 4 종목으로 효율적 투자선 구하기
# 현재 KOSPI 시가총액 1위부터 4위까지 해당하는 종목으로 포트폴리오를 구성한다고 가정했을 때, 효율적 투자선 구현

# 필요한 라이브러리 로드
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Investar import Analyzer

# MarketDB API를 통해 시총 상위 4종목의 2019년~2023년 종가 데이터를 받아와 데이터프레임에 저장
mk = Analyzer.MarketDB()
stocks = ['삼성전자', 'SK하이닉스', '현대자동차', 'NAVER']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2019-01-01', '2023-12-31')['close']
print(df)

print()

# 수익률 비교를 위해 일간 변동률이 필요하므로 시총 4종목의 일간 변동률을 계산
daily_ret = df.pct_change()
print(daily_ret)

print()

# 일간 변동률의 평균값을 구하여 주식 시장 개장일을 252일로 잡아 연간 변동률 계산
annual_ret = daily_ret.mean()
print(annual_ret)

print()

# 일간 변동률의 공분산을 구하여 일간 리스크 계산
daily_cov = daily_ret.cov()
print(daily_cov)

print()

# 일간 리스크에 252일을 곱하여 연간 공분산 계산
annual_cov = daily_cov * 252
print(annual_cov)

print()

# 시총 상위 4개 종목의 포트폴리오 수익률, 리스크, 종목 비중을 저장할 빈 리스트 생성
port_ret = []
port_risk = []
port_weights = []

print()

# 몬테카를로 시뮬레이션

# 몬테카를로 시뮬레이션(Monte Carlo simulation) : 매우 많은 난수를 이용해 함수의 값을 확률적으로 계산하는 것
# 시총 상위 4개 종목으로 구성된 포트폴리오를 난수를 이용해 각 종목의 비중을 다르게 하여 20,000개 생성

# 몬테카를로 시뮬레이션을 이용해 포트폴리오 20,000개를 생성한 후 각각의 포트폴리오별로 수익률, 리스크, 종목 비중을 데이터프레임으로 확보
for _ in range(20000):
    # 4개의 랜덤 실수값으로 구성된 가중치 배열 생성
    weights = np.random.random(len(stocks))
    # 4개 가중치의 총합이 1이 되도록 정규화
    weights /= np.sum(weights)

    # 각 중목별 가중치와 연간 수익률을 곱하여 해당 포트폴리오 전체 수익률 계산
    returns = np.dot(weights, annual_ret)
    # 종목별 연간 공분산(리스크)와 가중치를 곱한 후 이를 다시 가중치의 전치(T)로 곱하고 제곱근을 계산하여 해당 포트폴리오 전체 리스크(Risk) 확보
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    # 포트폴리오의 수익률, 리스크, 가중치를 리스트에 추가하여 저장
    port_ret.append(returns)
    port_risk.append(risk)
    port_weights.append(weights)

# 포트폴리오 딕셔너리 생성 후 각 포트폴리오의 수익률과 리스크 저장
portfolio = {'Returns': port_ret, 'Risk': port_risk}
# 포트폴리오 딕셔너리에 각 종목 별 가중치 저장
for i, s in enumerate(stocks):
    portfolio[s] = [weight[i] for weight in port_weights]
# 포트폴리오 딕셔너리를 데이터프레임으로 저장
df = pd.DataFrame(portfolio)
df = df[['Returns', 'Risk'] + [s for s in stocks]]

# 포트폴리오 데이터프레임의 리스크를 x축으로, 수익률을 y축으로 하여 산점도 출력
df.plot.scatter(x='Risk', y='Returns', figsize=(10, 7), grid=True)
plt.title('Efficient Frontier')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
plt.show()

print()



