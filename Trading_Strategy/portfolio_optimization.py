# 샤프 지수

# 샤프 지수(Shrpe Ratio) : 노벨 수상자인 윌리어 샤프가 창안한 리스크를 최소화하고 수익률은 최대화하는 포트폴리오를 찾아내는 이론
# 샤프 지수 : 측정된 위험 단위당 수익률을 계산한다는 점에서 수익률의 표준편차와 다름
# 샤프 지수 = 포트폴리오 예상 수익률 - 무위험률 / 수익률의 표준편차
# 샤프 지수는 계산의 편의를 고려해 무위험률을 0으로, 샤프 지수는 포트폴리오의 예상 수익률을 수익률의 표준편차로 나누어 계산

print()

# 포트폴리오 최적화

# 샤프 지수를 이용해 20,000개 포트폴리오 중 측정된 위험 단위당 수익이 제일 높은 포트폴리오 계산 가능

# 필요한 라이브러리 임포트
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Investar import Analyzer

# 2019년~2023년 4개 종목 종가를 데이터프레임으로 저장
mk = Analyzer.MarketDB()
stocks = ['삼성전자', 'SK하이닉스', '현대자동차', 'NAVER']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2019-01-01', '2023-12-31')['close']

# 연간 변동률과 연간 공분산 계산
daily_ret = df.pct_change()
annual_ret = daily_ret.mean() * 252
daily_cov = daily_ret.cov()
annual_cov = daily_cov * 252

# 포트폴리오 수익률, 리스크, 가중치, 샤프 지수를 저장할 리스트 생성
port_ret = []
port_risk = []
port_weights = []
sharpe_ratio = []

# 몬테카를로 시뮬레이션으로 20000개의 포트폴리오 생성 후 각 포트폴리오의 수익률, 리스크, 가중치, 샤프 지수 저장
for _ in range(20000):
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)

    returns = np.dot(weights, annual_ret)
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    port_ret.append(returns)
    port_risk.append(risk)
    port_weights.append(weights)
    sharpe_ratio.append(returns/risk)

# 포트폴리오 수익률, 리스크, 샤프 지수와 종목별 가중치를 추출하여 데이터프레임화하여 저장
portfolio = {'Returns': port_ret, 'Risk': port_risk, 'Sharpe': sharpe_ratio}
for i, s in enumerate(stocks):
    portfolio[s] = [weight[i] for weight in port_weights]
df = pd.DataFrame(portfolio)
df = df[['Returns', 'Risk', 'Sharpe'] + [s for s in stocks]]

# 샤프 지수가 최대가 되는 포트폴리오와 리스크가 최소가 되는 포트폴리오 값을 각각 추출
max_sharpe = df.loc[df['Sharpe'] == df['Sharpe'].max()]
min_risk = df.loc[df['Risk'] == df['Risk'].min()]

# x축은 포트폴리오 리스크, y축은 포트폴리오 수익률, 점의 색은 샤프 지수로 하여 산점도 계산
df.plot.scatter(x='Risk', y='Returns', c='Sharpe', cmap='viridis', edgecolors='k', figsize=(11,7), grid=True)
# 샤프 지수가 최대가 되는 값은 별 모양으로 크게 강조
plt.scatter(x=max_sharpe['Risk'], y=max_sharpe['Returns'], c='r', marker='*', s=300)
# 리스크가 최소가 되는 값은 X 모양으로 크게 강조
plt.scatter(x=min_risk['Risk'], y=min_risk['Returns'], c='r', marker='X', s=200)
plt.title('Portfolio Optimization')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
plt.show()

# 산점도에서 리스크당 수익률이 가장 높은 포트폴리오는 별표로 표시된 포트폴리오
print(max_sharpe)
# 4년 간 약 27%의 변동률을 겪으며 17%의 수익을 안겼으며 SK 하이닉스의 비중이 가장 높음

# 산점도에서 가장 리스크가 적은 포트폴리오는 X자로 표시된 포트폴리오
print(min_risk)
# 4년 간 약 23%의 변동률을 겪으며 12%의 수익을 안겼으며 삼성전자의 비중이 가장 높음

print()