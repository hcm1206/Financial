# 볼린저 밴드 매매기법

# 밴드 태그(주가가 밴드에 닿는 현상)가 일어났다고 해서 그 자체로 매수 신호나 매도 신호가 되는 것은 아님

# %b는 볼린저 밴드 어디에 주가가 위치하는지를 나타내며 주가와 연계해 트레이딩 시스템을 구축할 때 필요한 핵심 수단
# 밴드폭은 밴드의 너비를 수치로 나타낸 것으로 추세의 시작과 끝을 포착하는 역할을 수행
# 변동성과 추세는 볼린저 밴드를 구축할 때 이미 반영되었으므로 이 두 가지를 주가의 움직임을 확증하는 근거로 삼으면 안 됨
# 확증에 활용할 지표들은 범주별로 하나씩 선택

# 범주별 기술적 지표
# 모멘텀 : 변화율, 스토캐스틱
# 추세 : 선형회귀, MACD
# 거래량 : 일중강도(II), 매집/분산(A/D), 현금흐름지표(MFI), 거래량가중 MACD
# 과매수/과매도 : CCI, RSI
# 심리 : 여론조사선, 풋-콜 비율

# 볼린저 밴드와 함께 주로 사용되는 지표는 거래량 지표

# 존 볼린저는 '변동성 돌파', '추세 추종', '반전'이라는 세 가지 매매 기법을 제시
# '변동성 돌파' 매매기법 : 주가가 상단 밴드를 상향 돌파할 때 매수하고 주가가 하단 밴드를 하향 이탈할 때 공매도하는 기법

print()

# 볼린저 밴드를 이용한 추세 추종 매매기법

# 추세 추종(Trend Following) : 상숭 추세에 매수하고 하락 추세에 매도하는 기법
# 상승 추세나 하락 추세의 시작을 단순히 %b 지표만 이용해서 주가가 볼린저 상/하단 밴드에 태그했는지 여부로만 판단하지 않음
# 현금흐름지표(MFI)나 이중강도(II) 같은 거래량 관련 지표를 함께 이용해서 확증이 이루어진 경우에만 매수/매도에 들어감

# 매수 : 주가가 상단 밴드에 접근하며, 지표가 강세를 확증할 때만 매수(%b가 0.8보다 크고, MFI가 80보다 클 때)
# 매도 : 주가가 하단 밴드에 접근하며, 지표가 약세를 확증할 때만 매도(%b가 0.2보다 작고, MFI가 20보다 클 때)

# MFI(현금흐름지표, Money Flow INdex)

# 주가를 나타낼 때 중심 가격(Typical Price)를 이용하면 트레이딩이 집중적으로 발생하는 주가 지점을 더 잘 나타낼 수 있음
# 중심 가격은 일정 기간의 고가, 저가, 종가를 합한 뒤에 3으로 나눈 값

# 현금 흐름(Money Flow) : 중심 가격에 거래량을 곱한 값
# MFI는 가격과 거래량을 동시에 분석하므로 상대적으로 신뢰도가 더 높음
# MFI는 상승일 동안의 현금 흐름의 합(긍정적 현금 흐름)과 하락일 동안의 현금 흐름의 합(부정적 현금 흐름)을 이용

# MFI = 100 - (100 ÷ (1 + 긍정적 현금 흐름/부정적 현금 흐름))
# 긍정적 현금 흐름 : 중심 가격이 전일보다 상승한 날드의 현금 흐름의 합
# 부정적 현금 흐름 : 중심 가격이 전일보다 하락한 날들의 현금 흐름의 합

# 추세 추종 매매 구현

# 네이버 종목의 일별 시세를 이용해 밴드의 추세 추종 매매기법 구현

# 필요한 라이브러리 임포트
import matplotlib.pyplot as plt
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일부터 네이버 일별 주가를 받아와 데이터프레임에 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('NAVER', '2023-01-02')

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
# 각 날짜별 중심 가격 계산
df['TP'] = (df['high'] + df['low'] + df['close']) / 3
# 각 날짜별 긍정적 현금 흐름을 저장할 컬럼 생성
df['PMF'] = 0
# 각 날짜별 부정적 현금 흐름을 저장할 컬럼 생성
df['NMF'] = 0
# 시작 날짜부터 마지막 앞 날짜까지 반복
for i in range(len(df.close)-1):
    # i번째 날의 중심 가격보다 그 다음 날의 중심 가격이 더 높으면
    if df.TP.values[i] < df.TP.values[i+1]:
        # 그 다음날의 긍정적 현금 흐름을 계산하여 해당 컬럼에 값 저장
        df.PMF.values[i+1] = df.TP.values[i+1] * df.volume.values[i+1]
        # 그 다음날의 부정적 현금 흐름은 0으로 설정
        df.NMF.values[i+1] = 0
    # i번째 날의 중심 가격보다 그 다음 날의 중심 가격이 더 낮으면
    else:
        # 그 다음날의 부정적 현금 흐름을 계산하여 해당 컬럼에 값 저장
        df.NMF.values[i+1] = df.TP.values[i+1] * df.volume.values[i+1]
        # 그 다음날의 긍정적 현금 흐름은 0으로 설정
        df.PMF.values[i+1] = 0
# 날짜별 이전 10일 동안의 긍정적 현금 흐름의 합을 10일 동안의 부정적 현금 흐름의 합으로 나눈 결과를 현금 흐를 비율 칼럼에 저장
df['MFR'] = df.PMF.rolling(window=10).sum() / df.NMF.rolling(window=10).sum()
# 날짜별 이전 10일의 현금 흐름 지수 계산하여 저장
df['MFI10'] = 100 - 100 / (1 + df['MFR'])
# 데이터프레임의 첫 20일은 제거
df = df[19:]

# 그래프 크기 설정
plt.figure(figsize=(9, 8))
# 2행 1열로 구성된 그래프 중 1행 1열 그래프 설정
plt.subplot(2, 1, 1)
# 그래프 타이틀 설정
plt.title('NAVER Bollinger Band(20 day, 2 std) - Trend Following')
# 날짜별 종가를 파란색 실선으로 그래프에 표시
plt.plot(df.index, df['close'], color='#0000ff', label='Close')
# 날짜별 상단 볼린저 밴드를 빨간색 점선으로 그래프에 표시
plt.plot(df.index, df['upper'], 'r--', label='Upper Band')
# 날짜별 중간 볼린저 밴드를 검은색 점선으로 그래프에 표시
plt.plot(df.index, df['MA20'], 'k--', label='Moving average 20')
# 날짜별 하단 볼린저 밴드를 청록색 점선으로 그래프에 표시
plt.plot(df.index, df['lower'], 'c--', label='Lower band')
# 날짜별 볼린저 밴드 범위를 회색으로 채움
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
# 날짜별로 반복
for i in range(len(df.close)):
    # 해당 날짜의 %b 수치가 0.8보다 크고 현금 흐름 지수가 80보다 크다면
    if df.PB.values[i] > 0.8 and df.MFI10.values[i] > 80:
        # 그래프에서 해당 날짜 종가 위치에 빨간색 상향 삼각형 표시
        plt.plot(df.index.values[i], df.close.values[i], 'r^')
    # 해당 날짜의 %b 수치가 0.2보다 작고 현금 흐름 지수가 20보다 작다면
    elif df.PB.values[i] < 0.2 and df.MFI10.values[i] < 20:
        # 그래프에서 해당 날짜 종가 위치에 파란색 하향 삼각형 표시
        plt.plot(df.index.values[i], df.close.values[i], 'bv')
# 적당한 위치에 그래므 범례 표시
plt.legend(loc='best')
# 2행 1열로 구성된 그래프 중 2행 1열 그래프 설정
plt.subplot(2, 1, 2)
# MFI의 범위와 비교할 수 있도록 각 날짜별 이전 20일의 %b 수치에 100을 곱하여 파란색 실선으로 그래프에 표시
plt.plot(df.index, df['PB'] * 100, 'b', label='%B × 100')
# 각 날짜별 이전 10일의 현금 흐름 지수를 초록색 점선으로 그래프에 표시
plt.plot(df.index, df['MFI10'], 'g--', label='MFI(10 day)')
# y축의 표시 범위 설정
plt.yticks([-20, 0, 20, 40, 60, 80, 100, 120])
# 날짜별로 반복
for i in range(len(df.close)):
    # 해당 날짜의 %b 수치가 0.8보다 크고 현금 흐름 지수가 80보다 크다면
    if df.PB.values[i] > 0.8 and df.MFI10.values[i] > 80:
        # 그래프에서 해당 날짜 위치에 빨간색 상향 삼각형 표시
        plt.plot(df.index.values[i], 0, 'r^')
    # 해당 날짜의 %b 수치가 0.2보다 작고 현금 흐름 지수가 20보다 작다면
    elif df.PB.values[i] < 0.2 and df.MFI10.values[i] < 20:
        # 그래프에서 해당 날짜 위치에 파란색 하향 삼각형 표시
        plt.plot(df.index.values[i], 0, 'bv')
# 그래프에 격자 표시
plt.grid(True)
# 적당한 위치에 그래프 범례 표시
plt.legend(loc='best')
# 그래프 출력
plt.show()

# 매수 조건은 %b가 0.8보다 크고 MFI가 80보다 클 때 붉은색 윗방향 삼각형으로 표시
# 매도 조건은 %b가 0.2보다 작고 MFI가 20보다 작을 때 파란색 아랫방향 삼각형으로 표시

print()