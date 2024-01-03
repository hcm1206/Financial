# 야후 파이낸스로 주식 시세 구하기

# 야후 파이낸스에서 제공하는 삼성전자와 마이크로소프트 주식 시세를 데이터프레임으로 받아서 분석

from pandas_datareader import data as pdr
import yfinance as yf

# 데이터를 빠르게 다운로드하기 위한 코드
yf.pdr_override()

# 삼성전자와 마이크로소프트 주식 시세 데이터 로드(2018년 5월 4일부터 현재까지)
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

# 삼성전자 데이터프레임의 맨 앞 10행 출력
print(sec.head(10))

# 주식 데이터가 OHLC와 더불어 거래량(Volume)과 수정 종가(Adj Close)도 표시
# 수정 종가 : 액면 분할 등으로 인해 주식 가격에 변동이 있을 경우 가격 변동 이전에 거래된 가격을 현재 주식 가격에 맞춰 수정하여 표시한 가격
# 액면 분할 이후에는 종가(Close)와 수정 종가(Adj Close)가 동일해야 함
# 그러나 야후 파이낸스에서는 국내 주식에 대한 액면 분할 처리가 제대로 되지 않아서 수정 종가가 잘못 나와 있으므로 종가(Close)만 사용

print()

# 마이크로소프트 데이터프레임에서 거래량 칼럼을 제거한 데이터프레임 생성 후 가장 뒤의 5행 출력
tmp_msft = msft.drop(columns='Volume')
print(msft.tail(5))

print()

# 데이터프레임의 구성을 확인하기 위해 인덱스 확인
print(sec.index)
# 삼성전자 데이터프레임은 인덱스가 datetime형으로 되어 있고 총 328개 존재

print()

# 데이터프레임의 칼럼들의 대한 정보 확인
print(sec.columns)

print()

# 삼성전자와 마이크로소프트의 종가 데이터를 이용하여 그래프 출력

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

import matplotlib.pyplot as plt

# x 좌표는 삼성전자 데이터프레임 날짜 인덱스
plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
# y 좌표는 삼성전자 데이터프레임의 종가(Close) 데이터
plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
# 적절한 위치에 범례 표시
plt.legend(loc='best')
plt.show()

# 50,000원 대의 삼성전자와 130달러 대의 마이크로소프트 주가를 한 번에 표시
# 수치 차이가 커서 마이크로소프트 주가는 거의 0에 가까운 직선처럼 표시

print()