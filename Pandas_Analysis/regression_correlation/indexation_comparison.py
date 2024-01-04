# 지수화 비교
# 지수화(indexation) : 현재 종가를 특정 시점의 종가로 나누어 변동률을 계산하는 것

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# 2000년 이후 다우존스 지수(^DJI)와 KOSPI(^KS11) 데이터 다운로드
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')


# 금일 다우존스 지수와 KOSPI 지수를 2000년 1월 4일 기준 지수로 나눈 후 100을 곱하여 2000년 1월 4일 종가 대비 오늘의 변동률 계산
d = (dow.Close / dow.Close.loc['2000-01-04']) * 100
k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
# 다우존스 변동률을 빨간색 점선으로 표시
plt.plot(d.index, d, 'r--', label='Dow Jones Industrial Average')
# KOSPI 변동률을 파란색 실선으로 표시
plt.plot(k.index, k, 'b', label='KOSPI')
plt.grid(True)
plt.legend(loc='best')
plt.show()

# 지수화 결과 지난 20여년 간 KOSPI의 상승률이 다우존스의 상승률과 엇비슷

print()