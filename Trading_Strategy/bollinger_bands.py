# 볼린저 밴드 구하기

# 볼린저 밴드 : 주가의 20일 이동 평균선을 기준으로 상대적인 고점을 나타내는 상단 밴드와 상대적인 저점을 나타내는 하단 밴드로 구성
# 주가가 상단 밴드 근처에 있을수록 상대적인 고점에, 주가가 하단 밴드 근처에 있을수록 상대적인 저점에 있다고 판단 가능
# 상단 밴드와 하단 밴드의 사이의 폭은 표준편차와 특정 상수의 곱으로 나타낼 수 있음
# 밴드폭이 좁을수록 주가 변동성이 작고, 밴드폭이 넓을수록 변동성이 크다는 것을 의미

# 표준 볼린저 밴드 공식
# 상단 볼린저 밴드 = 중간 볼린저 밴드 + (2 × 표준편차)
# 중간 볼린저 밴드 = 종가의 20일 이동평균
# 하단 볼린저 밴드 = 중간 볼린저 밴드 - (2 × 표준편차)

# 네이버 종가 데이터를 이용하여 볼린저 밴드 구현

# 필요한 라이브러리 임포트
import matplotlib.pyplot as plt
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일부터의 네이버 일별 주가를 받아와 데이터프레임으로 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('NAVER', '2023-01-02')

# 각 날짜의 이전 20일의 종가 평균을 계산하여 중간 볼린저 밴드로 저장
df['MA20'] = df['close'].rolling(window=20).mean()
# 각 날짜의 이전 20일의 종가 표준편차를 계산하여 저장
df['stddev'] = df['close'].rolling(window=20).std()
# 각 날짜의 중간 볼린저 밴드에 표준편차를 2배한 값을 더하여 상단 볼린저 밴드로 저장
df['upper'] = df['MA20'] + (df['stddev'] * 2)
# 각 날짜의 중간 볼린저 밴드에 표준편차를 2배한 값을 빼서 하단 볼린저 밴드로 저장
df['lower'] = df['MA20'] - (df['stddev'] * 2)
# 첫 20일은 볼린저 밴드를 계산하지 못하므로 제거하고 21번째(20행) 데이터부터 사용
df = df[19:]

# 그래프 크기 설정
plt.figure(figsize=(9, 5))
# 날짜별 종가를 파란색 실선으로 그래프에 표시
plt.plot(df.index, df['close'], color='#0000ff', label='Close')
# 날짜별 상단 볼린저 밴드를 빨간색 점선으로 표시
plt.plot(df.index, df['upper'], 'r--', label='Upper band')
# 날짜별 중간 볼린저 밴드를 검은색 점선으로 표시
plt.plot(df.index, df['MA20'], 'k--', label='Moving average 20')
# 날짜별 하단 볼린저 밴드를 청록색 점선으로 표시
plt.plot(df.index, df['lower'], 'c--', label='Lower band')
# 날짜별 상단 볼린저 밴드와 하단 볼린저 밴드의 사이를 회색으로 채움
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
# 그래프의 적당한 위치에 범례 표시
plt.legend(loc='best')
# 그래프 타이틀 설정
plt.title('NAVER Bollinger Band (20 day, 2 std)')
# 그래프 출력
plt.show()

# 통계학에서는 평균값에서 ±2×표준편차 이내에 표본값 95.4%가 존재하므로 주가가 볼린저 밴드 내부에 존재할 확률도 95.4%

print()

# 볼린저 밴드 지표 I : %b

# 주가가 볼린저 밴드 어디에 위치하는지를 나타내는 지표가 %b
# %b값은 종가가 상단 밴드에 걸쳐 있을 때 1.0이 되고 중간에 걸쳐 있을 때 0.5가 되며 하단에 걸쳐있을 때 0.0
# %b는 상한선이나 하한선이 없으므로 종가가 상단 밴드보다 위에 있으면 1.0을 넘게 되고 종가가 하단 밴드 아래에 있으면 0보다 작은 수가 됨
# %b 산출 공식 : %b = 종가 - 하단 볼린저 밴드 / 상단 볼린저 밴드 - 하단 볼린저 밴드

# 볼린저 밴드 차트에 %b를 추가하여 볼린저 밴드의 변화에 따른 %b값 변화 확인

# 필요한 라이브러리 임포트
import matplotlib.pyplot as plt
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일부터 네이버 일별 주가를 받아와 데이터프레임으로 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('NAVER', '2023-01-02')

# 날짜별 볼린저 밴드 계산
df['MA20'] = df['close'].rolling(window=20).mean()
df['stddev'] = df['close'].rolling(window=20).std()
df['upper'] = df['MA20'] + (df['stddev'] * 2)
df['lower'] = df['MA20'] - (df['stddev'] * 2)
# %b 지표 계산하여 데이터프레임에 저장
df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower'])
df = df[19:]

# 그래스 크기 설정
plt.figure(figsize=(9, 8))
# 2행 1열로 구성된 그래프 중 1행 1열 그래프 설정
plt.subplot(2, 1, 1)
# 종가, 상단 볼린저 밴드, 중간 볼린저 밴드, 하단 볼린저 밴드와 볼린저 밴드 범위를 그래프로 표시
plt.plot(df.index, df['close'], color='#0000ff', label='Close')
plt.plot(df.index, df['upper'], 'r--', label = 'Upper band')
plt.plot(df.index, df['MA20'], 'k--', label='Moving average 20')
plt.plot(df.index, df['lower'], 'c--', label='Lower band')
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
plt.title('NAVER Bollinger Band(20 day, 2 std)')
plt.legend()

# 2행 1열로 구성된 그래프 중 2행 1열 그래프 설정
plt.subplot(2, 1, 2)
# 날짜별 %b 지수를 파란색 실선으로 그래프에 표시
plt.plot(df.index, df['PB'], color='b', label='%B')
# 그래프에 격자 표시
plt.grid(True)
# 그래프의 적당한 위치에 범례 표시
plt.legend(loc='best')
# 그래프 출력
plt.show()

# %b는 현재 주가가 하단 볼린저 밴드, 중간 볼린저 밴드, 상단 볼린저 밴드를 기준으로 어디쯤에 있는지를 수치로 나타낸 것
# %b의 그래프는 실제 주가의 흐름과 유사한 모양으로 표시

print()

# 볼린저 밴드 지표 II : 밴드폭

# 밴드폭(BandWidth) : 상단 볼린저 밴드와 하단 볼린저 밴드 사이의 폭
# 밴드폭은 스퀴즈를 확인하는 데 유용한 지표
# 스퀴즈(squeeze) : 변동성이 극히 낮은 수준까지 떨어져 곧이어 변동성 증가가 발생할 것으로 예상되는 상황
# 볼린저의 저술에 따르면 밴드폭이 6개월 저점을 기록하는 것을 보고 스퀴즈를 파악할 수 있다고 함

# 밴드폭 산출 공식 : 밴드폭 = 상단 볼린저 밴드 - 하단 볼린저 밴드 / 중간 볼린저 밴드

# 밴드폭의 또 다른 중요한 역할은 강력한 추세의 시작과 마지막을 포착하는 것
# 강력한 추세는 스퀴즈로부터 시작되는데 변동성이 커지면서 밴드폭 수치가 급격히 높아짐
# 이 때 밴드폭이 넓어지면서 추세의 반대쪽에 있는 밴드는 추세 반대 방향으로 향함

# 2023년 1월 2일 이후 네이버 볼린저 밴드와 밴드폭 확인

# 필요한 라이브러리 임포트
import matplotlib.pyplot as plt
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일부터 네이버 일별 주가를 받아와 데이터프레임으로 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('NAVER', '2023-01-02')

# 날짜별 볼린저 밴드 계산
df['MA20'] = df['close'].rolling(window=20).mean()
df['stddev'] = df['close'].rolling(window=20).std()
df['upper'] = df['MA20'] + (df['stddev'] * 2)
df['lower'] = df['MA20'] - (df['stddev'] * 2)
# 밴드폭 계산하여 데이터프레임에 저장
df['bandwidth'] = (df['upper'] - df['lower']) / df['MA20'] * 100
df = df[19:]

# 그래프 크기 설정
plt.figure(figsize=(9, 8))
# 2행 1열로 구성된 그래프 중 1행 1열 그래프 설정
plt.subplot(2, 1, 1)
# 종가, 상단 볼린저 밴드, 중간 볼린저 밴드, 하단 볼린저 밴드와 볼린저 밴드 범위를 그래프로 표시
plt.plot(df.index, df['close'], color='#0000ff', label='Close')
plt.plot(df.index, df['upper'], 'r--', label='Upper band')
plt.plot(df.index, df['MA20'], 'k--', label='Moving average 20')
plt.plot(df.index, df['lower'], 'c--', label='Lower band')
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
plt.title('NAVER Bollinger Band(20 day, 2 std)')
plt.legend(loc='best')

# 2행 1열로 구성된 그래프 중 2행 1열 그래프 설정
plt.subplot(2, 1, 2)
# 날짜별 밴드폭을 마젠타색 실선으로 그래프에 표시
plt.plot(df.index, df['bandwidth'], color='m', label='BandWidth')
# 그래프에 격자 표시
plt.grid(True)
# 적당한 위치에 그래프 범례 표시
plt.legend(loc='best')
# 그래프 출력
plt.show()