# 삼중창 매매 시스템 : 추세 추종과 역추세 매매법을 함께 사용하며, 세 단계의 창(Screen)을 거쳐 더 정확한 매매 시점을 찾도록 구성

# 같은 시장이더라도 지표들이 내는 신호들이 다를 수 있음
# 삼중창 매매 시스템은 한 가지 지표만 사용했을 때의 단점을 보완하고자 추세 추종형 지표와 오실레이터를 적절히 결합해 사용

# 주식 시장의 중요한 딜레마 중 하나는 시간의 관점에 따라 주가 차트가 오를 수도 있고 내릴 수도 있다는 점
# 그렇기 때문에 삼중창은 서로 다른 시간 단위에서 신호를 비교함으로써 정확한 매매 시점을 파악하도록 개발

print()

# 첫 번째 창 - 시장 조류

# 트레이더에게는 매수, 매도, 관망 세 가지 선택지가 주어짐
# 삼중창의 첫 번째 창(First Screen)을 이용하면 이 중 한 선택지를 제거 가능
# 시장이 상승 추세인지 하락 추세인지 판단해 상승 추세에서는 매수하거나 관망하고, 하락 추세에서는 매도하거나 관망

# 삼중창의 첫 번째 창은 시장 조류(Market Tide) 즉 장기 차트를 분석하는 것
# 트레이더는 자신이 매매하는 시간 단위보다 한 단계 긴 단위 차트를 이용해 분석

# 삼중창 매매 시스템의 첫 번째 창 구현

# 필요한 라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일 이후의 엔씨소프트 일별 주가를 받아와 데이터프레임으로 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('엔씨소프트', '2023-01-02')

# 종가의 12주 지수 이동평균 계산
ema60 = df.close.ewm(span=60).mean()
# 종가의 26주 지수 이동평균 계산
ema130 = df.close.ewm(span=130).mean()
# MACD선(이동평균 수렴확산) 계산
macd = ema60 - ema130
# 신호선(MACD의 9주 지수 이동평균) 계산
signal = macd.ewm(span=45).mean()
# MACD 히스토그램 계산
macdhist = macd - signal

# 26주 지수 이동평균, 12주 지수 이동평균, MACD선, 신호선, MACD 히스토그램을 갖는 데이터프레임을 생성하고 결측치 제거
df = df.assign(ema130=ema130, ema60=ema60, macd=macd, signal=signal, macdhist=macdhist).dropna()
# 날짜형 인덱스를 숫자형으로 변환
df['number'] = df.index.map(mdates.date2num)
# 데이터 프레임 중 날짜(숫자형), 시가, 고가, 저가, 종가를 추출하여 ohlc 데이터프레임으로 저장
ohlc = df[['number', 'open', 'high', 'low', 'close']]

# 차트 크기 설정
plt.figure(figsize=(9, 7))
# 2행 1열로 구성된 차트에서 1행 1열 차트 설정
p1 = plt.subplot(2, 1, 1)
# 차트 타이틀 설정
plt.title('Triple Screen Trading - First Screen (NCSOFT)')
# 차트에 격자 표시
plt.grid(True)
# ohlc 데이터프레임의 일자, 시가, 고가, 저가, 종가 값을 이용하여 캔들 차트 구현
candlestick_ohlc(p1, ohlc.values, width=.6, colorup='red', colordown='blue')
# 차트 날짜 형식을 4자리 연도, 2자리 월로 설정
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# 날짜별 26주 지수 이동평균을 청록색 실선으로 차트에 표시
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
# 적당한 위치에 차트 범례 표시
plt.legend(loc='best')

# 2행 1열로 구성된 차트에서 2행 1열 차트 설정
p2 = plt.subplot(2, 1, 2)
# 차트에 격자 표시
plt.grid(True)
# 차트 날짜 형식을 4자리 연도, 2자리 월로 설정
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# 날짜별 MACD 히스토그램을 마젠타색 막대 그래프로 표시
plt.bar(df.number, df['macdhist'], color='m', label='MACD-Hist')
# 날짜별 MACD선을 파란색 실선으로 차트에 표시
plt.plot(df.number, df['macd'], color='b', label='MACD')
# 날짜별 신호선을 초록색 점선으로 차트에 표시
plt.plot(df.number, df['signal'], 'g--', label='MACD-Signal')
# 적당한 위치에 차트 범례 표시
plt.legend(loc='best')
# 차트 출력
plt.show()

# 시장의 장기 추세를 분석하기 위해서 26주 지수 이동평균에 해당하는 EMA 130 그래프와 주간 MACD 히스토그램을 함께 표시
# 삼중창 매매 시스템의 첫 번째 창에서는 EMA 130 그래프가 오르고 있을 때에만 시장에 참여하면 됨

print()

# 두 번째 창 - 시장 파도

# 두 번째 창에서는 첫 번째 창의 추세 방향과 역행하는 파도(market wave)를 파악하는 데 오실레이터를 활용
# 오실레이터는 시장이 하락할 때 매수 기회를 제공하고, 시장이 상승할 때 매도 기회를 제공
# 즉, 주봉 추세가 상승하고 있을 때 일봉 추세가 하락하면 매수 기회로 봄

# 삼중창 매매 시스템의 두 번쨰 창 구현

# 필요한 라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일 이후의 엔씨소프트 일별 주가를 받아와 데이터프레임으로 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('엔씨소프트', '2023-01-02')

# 종가의 12주 지수 이동평균 계산
ema60 = df.close.ewm(span=60).mean()
# 종가의 26주 지수 이동평균 계산
ema130 = df.close.ewm(span=130).mean()
# 종가의 MACD선(이동평균 수렴확산) 계산
macd = ema60 - ema130
# 신호선(MACD의 9주 지수 이동평균) 계산
signal = macd.ewm(span=45).mean()
# MACD 히스토그램 계산
macdhist = macd - signal

# 26주 지수 이동평균, 12주 지수 이동평균, MACD선, 신호선, MACD 히스토그램을 갖는 데이터프레임을 생성하고 결측치 제거
df = df.assign(ema130=ema130, ema60=ema60, macd=macd, signal=signal, macdhist=macdhist).dropna()
# 날짜형 인덱스를 숫자형으로 변환
df['number'] = df.index.map(mdates.date2num)
# 데이터프레임 중 날짜(숫자형), 시가, 고가, 저가, 종가를 추출하여 ohlc 데이터프레임으로 저장
ohlc = df[['number', 'open', 'high', 'low', 'close']]

# 각 날짜별 지난 14일(없다면 최소 1일)동안의 고가 최댓값 계산
ndays_high = df.high.rolling(window=14, min_periods=1).max()
# 각 날짜별 지난 14일(없다면 최소 1일)동안의 저가 최솟값 계산
ndays_low = df.low.rolling(window=14, min_periods=1).min()
# 빠른선 %K 계산
fast_k = (df.close - ndays_low) / (ndays_high - ndays_low) * 100
# 지난 3일 동안의 %K의 평균을 통해 느린선 %D 계산
slow_d = fast_k.rolling(window=3).mean()
# %K와 %D를 갖는 데이터프레임을 생성하고 결측치 제거
df = df.assign(fast_k=fast_k, slow_d=slow_d).dropna()

# 차트 크기 설정
plt.figure(figsize=(9, 7))
# 2행 1열로 구성된 차트에서 1행 1열 차트 설정
p1 = plt.subplot(2, 1, 1)
# 차트 타이틀 설정
plt.title('Triple Screen Trading - Second Screen (NCSOFT)')
# 차트 격자 표시
plt.grid(True)
# ohlc 데이터프레임의 일자, 시가, 고가, 저가, 종가 값을 이용하여 캔들 차트 구현
candlestick_ohlc(p1, ohlc.values, width=.6, colorup='red', colordown='blue')
# 차트 날짜 형식을 4자리 연도, 2자리 월로 설정
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# 날짜별 26주 지수 이동평균을 청록색 실선으로 차트에 표시
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
# 차트 범례 표시
plt.legend(loc='best')

# 2행 1열로 구성된 차트에서 2행 1열 차트 설정
p1 = plt.subplot(2, 1, 2)
# 차트 격자 표시
plt.grid(True)
# 차트 날짜 형식을 4자리 연도, 2자리 월로 설정
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# 날짜별 빠른 선 %K를 청록색 실선으로 차트에 표시
plt.plot(df.number, df['fast_k'], color='c', label='%K')
# 날짜별 느린 선 %D를 검은색 실선으로 차트에 표시
plt.plot(df.number, df['slow_d'], color='k', label='%D')
# y축 눈금을 0, 20, 80, 100으로 설정하여 스토캐스틱의 기준선을 나타냄
plt.yticks([0, 20, 80, 100])
# 적당한 위치에 차트 범례 표시
plt.legend(loc='best')
# 차트 출력
plt.show()

# 상단 차트는 130일 지수 이동평균 그래프, 하단 차트는 스토캐스틱 그래프를 구현
# 스토캐스틱에는 빠른 선인 %K와 느린 선인 %D가 존재
# %K 대신 느린 %D를 사용할 경우 더 적은 신호를 만들어내기 때문에 그만큼 더 확실한 신호로 파악 가능

# 삼중창 매매 시스템의 두 번째 창에서
# 130일 지수 이동 평균이 상승하고 있을 때 스토캐스틱이 30 아래로 내려가면 매수 기회로 판단 가능
# 130일 지수 이동 평균이 하락하고 있을 때 스토캐스틱이 70 위로 올라가면 매도 기회로 판단 가능

print()

# 세 번째 창 - 진입 기술

# 세 번째 창은 첫 번째 창과 두 번째 창이 동시에 매매 신호를 냈을 때 진입 시점을 찾아내는 기법(Entry Technique)만 존재
# 주간 추세가 상승하면 추적 매수 스톱(Trailing buy stop) 기법을 사용해 가격 변동에 따라 주문 수준을 수정
# 하락 추세에서는 추적 매도 스톱(Trailing sell stop) 기법을 사용해 가격 변동에 따라 주문 수준을 수정

# 추적 매수 스톱 : 주간 추세가 상승하고 있을 때, 일간 오실레이터가 하락하면서 매수 신호가 발생하면 전일 고점보다 한 틱 위에서 매수 주문을 내는 것
# 주간 추세대로 가격이 계속 상승해 전일 고점을 돌파하는 순간(Intraday Breakout) 매수 주문이 체결
# 매수 주문이 체결되면 전일의 저가나 그 전일의 저가 중 낮은 가격보다 한 틱 아래에 매도 주문을 걸어 놓음으로써 손실을 막을 수 있음

# 만약 가격이 하락한다면 매수 스톱은 체결되지 않을 것
# 매수 주문이 체결되지 않으면 다시 전일 고점 1틱 위까지 매수 주문의 수준을 낮추도록 함
# 주간 추세가 반대 방향으로 움직이거나 매수 신호가 취소될 때까지 매일 매수 스톱을 낮추면서 주문을 걸어 놓음

# 진입 시점을 찾아내는 기법
# 주간 추세 상승, 일간 오실레이터 상승 : 관망
# 주간 추세 상승, 일간 오실레이터 하락 : 매수(주문 : 추적 매수 스톱)
# 주간 추세 하락, 일간 오실레이터 하락 : 관망
# 주간 추세 하락, 일간 오실레이터 상승 : 매도(주문 : 추적 매도 스톱)

print()

# 전체 소스 코드

# 삼중창 매매 기법의 전체 소스 코드
# 두 번째 창에 일간 오실레이터로 스토캐스틱의 %D 사용
# 기준 포인트로 80, 20을 사용해 더 확실한 신호를 추적

# 필요한 라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from Investar import Analyzer

# MarketDB API를 이용하여 2023년 1월 2일 이후의 엔씨소프트 일별 주간를 받아와 데이터프레임에 저장
mk = Analyzer.MarketDB()
df = mk.get_daily_price('엔씨소프트', '2023-01-02')

# 종가의 12주 지수 이동평균 계산
ema60 = df.close.ewm(span=60).mean()
# 종가의 26주 지수 이동평균 계산
ema130 = df.close.ewm(span=130).mean()
# 종가의 MACD선(이동평균 수렴확산) 계산
macd = ema60 - ema130
# 신호선(MACD의 9주 지수 이동평균) 계산
signal - macd.ewm(span=45).mean()
# MACD 히스토그램 계산
macdhist = macd - signal
# 26주 지수 이동평균, 12주 지수 이동평균, MACD선, 신호선, MACD 히스토그램을 갖는 데이터프레임을 생성하고 결측치 제거
df = df.assign(ema130=ema130, ema60=ema60, macd=macd, signal=signal, macdhist=macdhist).dropna()
# 날짜형 인덱스를 숫자형으로 변환
df['number'] = df.index.map(mdates.date2num)
# 데이터프레임 중 날짜(숫자형), 시가, 고가, 저가, 종가를 추출하여 ohlc 데이터프레임으로 저장
ohlc = df[['number', 'open', 'high', 'low', 'close']]

# 각 날짜별 지난 14일(없다면 최소 1일)동안의 고가 최댓값 계산
ndays_high = df.high.rolling(window=14, min_periods=1).max()
# 각 날짜별 지난 14일(없다면 최소 1일)동안의 저가 최솟값 계산
ndays_low = df.low.rolling(window=14, min_periods=1).min()

# 빠른 선 %K 계산
fast_k = (df.close - ndays_low) / (ndays_high - ndays_low) * 100
# 지난 3일 동안의 %K의 평균을 통해 느린 선 %D 계산
slow_d = fast_k.rolling(window=3).mean()
# %K와 %D를 갖는 데이터프레임을 생성하고 결측치 제거
df = df.assign(fast_k=fast_k, slow_d=slow_d).dropna()

# 차트 크기 설정
plt.figure(figsize=(9, 9))
# 3행 1열로 구성된 차트에서 1행 1열 차트 설정
p1 = plt.subplot(3, 1, 1)
# 차트 타이틀 설정
plt.title('Triple Screen Trading (NCSOFT)')
# 차트 격자 표시
plt.grid(True)
# ohlc 데이터프레임의 일자, 시가, 고가, 저가, 종가 값을 이용하여 캔들 차트 구현
candlestick_ohlc(p1, ohlc.values, width=.6, colorup='red', colordown='blue')
# 차트 날짜 형식을 4자리 연도, 2자리 월로 설정
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# 날짜별 26주 지수 이동평균을 청록선 실선으로 차트에 표시
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
# 각 날짜별 반복
for i in range(1, len(df.close)):
    # 전날에 비해 130일(26주) 이동 지수평균이 상승하고 %D가 20 아래로 떨어지면
    if df.ema130.values[i-1] < df.ema130.values[i] and df.slow_d.values[i-1] >= 20 and df.slow_d.values[i] < 20:
        # 차트에서 해당 날짜 위치에 빨간색 상향 삼각형 표시(매수 신호)
        plt.plot(df.number.values[i], 250000, 'r^')
    # 전날에 비해 130일(26주) 이동 지수평균이 하락하고 %D가 80 위로 상승하면
    elif df.ema130.values[i-1] > df.ema130.values[i] and df.slow_d.values[i-1] <= 80 and df.slow_d.values[i] > 80:
        # 차트에서 해당 날짜 위치에 파란색 하향 삼각형 표시(매도 신호)
        plt.plot(df.number.values[i], 250000, 'bv')
# 적당한 위치에 차트 범례 표시
plt.legend(loc='best')

# 3행 1열로 구성된 차트에서 2행 1열 차트 설정
p2 = plt.subplot(3, 1, 2)
# 차트 격자 표시
plt.grid(True)
# 차트 날짜 형식을 4자리 연도, 2자리 월로 설정
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# 날짜별 MACD 히스토그램을 마젠타색 막대 그래프로 표시
plt.bar(df.number, df['macdhist'], color='m', label='MACD-Hist')
# 날짜별 MACD선을 파란색 실선으로 차트에 표시
plt.plot(df.number, df['macd'], color='b', label='MACD')
# 날짜별 신호선을 초록색 점선으로 차트에 표시
plt.plot(df.number, df['signal'], 'g--', label='MACD-Signal')
# 적당한 위치에 차트 범례 표시
plt.legend(loc='best')

# 3행 1열로 구성된 차트에서 3행 1열 차트 설정
p3 = plt.subplot(3, 1, 3)
# 차트 격자 표시
plt.grid(True)
# 차트 날짜 형식을 4자리 연도, 2자리 월로 설정
p3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
# 날짜별 빠른 선 %K를 청록색 실선으로 표시
plt.plot(df.number, df['fast_k'], color='c', label='%K')
# 날짜별 느린 선 %D를 검은색 실선으로 표시
plt.plot(df.number, df['slow_d'], color='k', label='%D')
# y축 눈금을 0, 20, 80, 100으로 설정하여 스토캐스틱의 기준선을 나타냄
plt.yticks([0, 20, 80, 100])
# 적당한 위치에 차트 범례 표시
plt.legend(loc='best')
# 차트 출력
plt.show()

print()