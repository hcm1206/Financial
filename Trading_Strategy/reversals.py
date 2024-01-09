# 볼린저 밴드를 이용한 반전 매매기법

# 볼린저 밴드를 이용한 반전(Reversals) 매매기법 : 주가가 반전하는 지점을 찾아내 매수 또는 매도하는 기법
# 주가가 하단 밴드를 여러 차례 태그하는 과정에서 강세 지표가 발생하면 매수
# 주가가 상단 밴드를 여러 차례 태그하는 과정에서 약세 지표가 발생하면 매도

# 매수 : 주가가 하단 밴드 부근에서 W형 패턴을 나타내고, 강세 지표가 확증할 때 매수(%b가 0.05보다 작고 II%가 0보다 크면 매수)
# 매도 : 상단 밴드 부근에서 일련의 주가 태그가 일어나며, 약세 지표가 확증할 때 매도(%b가 0.95보다 크고 II%가 0보다 작으면 매도)

# 일중 강도
# 일중 강도(intraday intensity, II) : 거래 범위에서 종가의 위치를 토대로 주식 종목의 자금 흐름을 설명
# II는 장이 끝나는 지점에서 트레이더들의 움직임을 나타냄
# 종가가 거래 범위 천정권체어 형성되면 1, 중간에서 형성되면 0, 바닥권에서 형성되면 -1
# 일중 강도율(intraday intensity %, II%) : 21일 기간 동안의 II 합을 21일 기간 동안의 거래량 합으로 나누어 표준화한 것

# 일중 강도 = (2 × 종가 - 고가 - 저가) / (고가 - 저가) × 거래량
# 일중 강도율 = 일중강도의 21일 합 / 거래량의 21일 합 × 100

# SK 하이닉스 일별 시세를 이용해 일중 강도율을 출력

# 필요한 라이브러리 임포트
import matplotlib.pyplot as plt
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일 이후의 SK하이닉스 일별 주가를 받아와 데이터프레임에 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('SK하이닉스', '2023-01-02')

# 각 날짜별 이전 20일의 중간 볼린저 밴드 계산
df['MA20'] = df['close'].rolling(window=20).mean()
# 각 날짜별 이전 20일의 종가 표준편차 계산
df['stddev'] = df['close'].rolling(window=20).std()
# 각 날짜별 이전 20일의 상단 볼린저 밴드 계산
df['upper'] = df['MA20'] + (df['stddev'] * 2)
# 각 날짜별 이전 20일의 하단 볼린저 밴드 계산
df['lower'] = df['MA20'] - (df['stddev'] * 2)
# 각 날짜별 이전 20일의 %b 수치 계산
df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower'])

# 각 날짜별 일중 강도 계산
df['II'] = (2 * df['close'] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']
# 각 날짜별 이전 21일의 일중 강도율 계산
df['IIP21'] = df['II'].rolling(window=21).sum() / df['volume'].rolling(window=21).sum()*100
# 데이터프레임 결측치 제거
df = df.dropna()

# 그래프 크기 설정
plt.figure(figsize=(9, 9))
# 3행 1열로 구성된 그래프 중 1행 1열 그래프 설정
plt.subplot(3, 1, 1)
# 그래프 타이틀 설정
plt.title('SK Hynix Bollinger Band(20 day, 2 std) - Reversals')
# 날짜별 종가를 파란색 실선으로 그래프에 표시
plt.plot(df.index, df['close'], 'b', label='Close')
# 날짜별 상단 볼린저 밴드를 빨간색 점선으로 그래프에 표시
plt.plot(df.index, df['upper'], 'r--', label='Upper band')
# 날짜별 중간 볼린저 밴드를 검은색 점선으로 그래프에 표시
plt.plot(df.index, df['MA20'], 'k--', label='Movin average 20')
# 날짜별 하단 볼린저 밴드를 청록색 점선으로 그래프에 표시
plt.plot(df.index, df['lower'], 'c--', label='Lower band')
# 날짜별 볼린저 밴드 범위를 회색으로 채움
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
# 적당한 위치에 그래프 범례 표시
plt.legend(loc='best')

# 3행 1열로 구성된 그래프 중 2행 1열 그래프 설정
plt.subplot(3, 1, 2)
# 날짜별 %b 수치를 파란색 실선으로 그래프에 표시
plt.plot(df.index, df['PB'], 'b', label='%b')
# 그래프에 격자 표시
plt.grid(True)
# 적당한 위치에 그래프 범례 표시
plt.legend(loc='best')

# 3행 1열로 구성된 그래프 중 3행 1열 그래프 설정
plt.subplot(3, 1, 3)
# 날짜별 일중 강도율을 초록색 막대 그래프로 표시
plt.bar(df.index, df['IIP21'], color='g', label='II% 21day')
# 그래프에 격자 표시
plt.grid(True)
# 적당한 위치에 그래프 범례 표시
plt.legend(loc='best')
# 그래프 출력
plt.show()

# 세 번째 차트에 표시된 일중 강도율은 기관 블록 거래자의 활동을 추적할 목적으로 만들어진 지표
# 존 볼린저는 일중 강도율을 볼린저 밴드를 확증하는 도구로 사용
# 주가가 하단 볼린저 밴드에 닿을 때 일중 강도율이 +이면 매수
# 주가가 상단 볼린저 밴드에 닿을 때 일중 강도율이 -이면 매도

print()

# 반전 매매 구현

# SK하이닉스의 일별 시세를 이용해 볼린저 밴드의 반전 매매기법 구현

# 필요한 라이브러리 임포트
import matplotlib.pyplot as plt
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일 이후의 SK하이닉스 일별 주가를 받아와 데이터프레임에 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('SK하이닉스', '2023-01-02')

# 각 날짜별 이전 20일의 중간 볼린저 밴드 계산
df['MA20'] = df['close'].rolling(window=20).mean()
# 각 날짜별 이전 20일의 종가 표준편차 계산
df['stddev'] = df['close'].rolling(window=20).std()
# 각 날짜별 이전 20일의 상단 볼린저 밴드 계산
df['upper'] = df['MA20'] + (df['stddev'] * 2)
# 각 날짜별 이전 20일의 하단 볼린저 밴드 계산
df['lower'] = df['MA20'] - (df['stddev'] * 2)
# 각 날짜별 이전 20일의 %b 수치 계산
df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower'])

# 각 날짜별 일중 강도 계산
df['II'] = (2 * df['close'] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']
# 각 날짜별 이전 21일의 일중 강도율 계산
df['IIP21'] = df['II'].rolling(window=21).sum()/df['volume'].rolling(window=21).sum()*100
# 데이터프레임 결측치 제거
df = df.dropna()

# 그래프 크기 설정
plt.figure(figsize=(9, 9))
# 3행 1열로 구성된 그래프 중 1행 1열 그래프 설정
plt.subplot(3, 1, 1)
# 그래프 타이틀 설정
plt.title('SK Hynix Bollinger Band(20 day, 2 std) - Reversals')
# 날짜별 종가를 마젠타색 실선으로 그래프에 표시
plt.plot(df.index, df['close'], 'm', label='Close')
# 날짜별 상단 볼린저 밴드를 빨간색 점선으로 그래프에 표시
plt.plot(df.index, df['upper'], 'r--', label='Upper band')
# 날짜별 중간 볼린저 밴드를 검은색 점선으로 그래프에 표시
plt.plot(df.index, df['MA20'], 'k--', label='Moving average 20')
# 날짜별 하단 볼린저 밴드를 청록색 점선으로 그래프에 표시
plt.plot(df.index, df['lower'], 'c--', label='Lover band')
# 날짜별 볼린저 밴드 범위를 회색으로 채움
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
# 날짜 별로 반복
for i in range(0, len(df.close)):
    # 해당 날짜의 %b 수치가 0.05 미만이고 일중 강도율이 양수이면
    if df.PB.values[i] < 0.05 and df.IIP21.values[i] > 0:
        # 해당 날짜의 종가 위치에 빨간색 상향 삼각형 표시
        plt.plot(df.index.values[i], df.close.values[i], 'r^')
    # 해당 날짜의 %b 수치가 0.95 초과이고 일중 강도율이 음수이면
    elif df.PB.values[i] > 0.95 and df.IIP21.values[i] < 0:
        # 해당 날짜의 종가 위치에 파란색 하향 삼각형 표시
        plt.plot(df.index.values[i], df.close.values[i], 'bv')
# 적당한 위치에 그래프 범례 표시
plt.legend(loc='best')

# 3행 1열로 구성된 그래프 중 2행 1열 그래프 설정
plt.subplot(3, 1, 2)
# 날짜별 %b 수치를 파란색 실선으로 그래프에 표시
plt.plot(df.index, df['PB'], 'b', label='%b')
# 그래프에 격자 표시
plt.grid(True)
# 적당한 위치에 그래프 범례 표시
plt.legend(loc='best')

# 3행 1열로 구성된 그래프 중 3행 1열 그래프 설정
plt.subplot(3, 1, 3)
# 날짜별 일중 강도율을 초록색 막대 그래프로 표시
plt.bar(df.index, df['IIP21'], color='g', label='II% 21day')
# 날짜 별로 반복
for i in range(0, len(df.close)):
    # 해당 날짜의 %b 수치가 0.05 미만이고 일중 강도율이 양수이면
    if df.PB.values[i] < 0.05 and df.IIP21.values[i] > 0:
        # 그래프에서 해당 날짜 위치에 빨간색 상향 삼각형 표시
        plt.plot(df.index.values[i], 0, 'r^')
    # 해당 날짜의 %b 수치가 0.95 초과이고 일중 강도율이 음수이면
    elif df.PB.values[i] > 0.95 and df.IIP21.values[i] < 0:
        # 그래프에서 해당 날자 위치에 파란색 하향 삼각형 표시
        plt.plot(df.index.values[i], 0, 'bv')
# 그래프에 격자 표시
plt.grid(True)
# 적당한 위치에 그래프 범례 표시
plt.legend(loc='best')
# 그래프 출력
plt.show()

print()