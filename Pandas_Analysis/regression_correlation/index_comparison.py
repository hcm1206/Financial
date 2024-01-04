# 회귀 분석은 데이터의 상관관계를 분석하는 데 쓰이는 통계 분석 방법

# KOSPI와 다우존스 지수 비교

# 필요한 라이브러리 임포트
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# 2000년 이후 다우존스 지수(^DJI)와 KOSPI(^KS11) 데이터 다운로드
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
# 다우존스 지수를 빨간색 점선으로 표시
plt.plot(dow.index, dow.Close, 'r--', label='Dow Jones Industrial')
# KOSPI 지수를 파란색 실선으로 표시
plt.plot(kospi.index, kospi.Close, 'b', label='KOSPI')
plt.grid()
plt.legend(loc='best')
plt.show()

# 지수 기준값이 다르므로 어느 지수가 더 좋은 성과를 냈는지 알아보기 어려움