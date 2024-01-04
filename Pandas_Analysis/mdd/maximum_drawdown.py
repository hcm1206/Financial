# MDD(Maximum Drawdown, 최대 손실 낙폭) : 특정 기간에 발생한 최고점에서 최저점까지의 가장 큰 손실
# 퀀트 투자에서는 수익률을 높이는 것보다 MDD를 낮추는 것이 더 낫다고 할 만큼 중요한 지표
# 특정 기간동안 최대한 얼마의 손실이 날 수 있는지를 나타냄
# MDD = (최저점 - 최고점) / 최고점

# KOSPI의 MDD

# KOSPI(Korea Composite Stock Price Index, 한국종합주가지수) : 1983년 발표
# KOSPI는 1980년 1월 4일에 상장된 모든 종목의 시가 총액을 기준 지수 100포인트로 집계
# KOSPI 지수 2500은 한국 증시가 1980년 당시보다 25배가 올랐음을 의미

# KOSPI는 1994년 1145.66 포인트에서 1998년 277.37포인트까지 4년 동안 75.8%가 하락했고 이 기간 MDD는 -75.8%
# 전체 주식 시장이 1/4 토막 난 것이 KOSPI 역사상 최대 손실 낙폭

print()

# 서브프라임 당시의 MDD

# 2004년부터 현재까지의 KOSPI 지수 데이터를 통해 KOSPI의 MDD 계산
# rolling() 함수는 시리즈에서 윈도우 크기에 해당하는 개수만큼 데이터를 추출하여 집계 함수에 해당하는 연산을 실시

# 필요한 라이브러리 임포트
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

# KOSPI 지수 심볼(^KS11)을 통해 KOSPI 지수 데이터 다운로드
kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')

# 산정 기간에 해당하는 window 값을 1년 개장일 어림값 252로 설정
window = 252
# KOSPI 종가 칼럼에서 1년(거래일 기준) 기간 단위로 최고치를 구하여 저장
peak = kospi['Adj Close'].rolling(window, min_periods=1).max()
# 최고치(peak) 현재 KOSPI 종가가 얼마나 하락했는지 계산하여 저장
drawdown = kospi['Adj Close']/peak - 1.0
# KOSPI 종가 하락율에서 1년 기간 단위로 최저치를 계산
max_dd = drawdown.rolling(window, min_periods=1).min()

# 그래프 크기 설정
plt.figure(figsize=(9, 7))
# 2행 1열 중 1행 그래프 설정
plt.subplot(211)
# KOSPI 종가 그래프 표시
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
# 2행 1열 중 2행 그래프 설정
plt.subplot(212)
# 종가 하락율 그래프 표시
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
# 1년 중 최대 종가 하락율 그래프 표시
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()

print()

# 서브프라임 금융 위기 당시였던 2008년 10월 24일에 KOSPI 지수가 10.57% 하락하면서 MDD가 -54.5% 기록

# 정확한 MDD 수치 계산
print(max_dd.min())

print()

# 인덱싱 조건을 통해 MDD를 기록한 기간 확인
print(max_dd[max_dd==-0.5453665130144085])

# 2008년 10월 24일부터 2009년 10월 22일까지 약 1년(252일) 동안 주어진 max_dd와 일치

print()