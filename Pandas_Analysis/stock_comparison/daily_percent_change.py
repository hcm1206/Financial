from pandas_datareader import data as pdr
import yfinance as yf

# 데이터를 빠르게 다운로드하기 위한 코드
yf.pdr_override()

# 삼성전자와 마이크로소프트 주식 시세 데이터 로드(2018년 5월 4일부터 현재까지)
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

# 일간 변동률로 주가 비교하기
# 일간 변동률(daily percent change)을 구하면 가격이 다른 두 주가의 수익률 비교 가능

# 종가 칼럼인 sec['Close']의 자료형 확인 (종가 칼럼은 시리즈)
print(type(sec['Close']))

print()

# 삼성전자 종가 칼럼 데이터 확인
print(sec['Close'])

print()

# shift() 함수를 이용해 이전 거래일의 종가 확인
print(sec['Close'].shift(1))

print()

# 당일 종가 데이터와 이전 거래일의 종가 데이터를 이용하여 일간 변동률 계산
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
print(sec_dpc.head())

print()

# 첫 번째 일간 변동률의 값이 NaN이므로 향후 계산을 위해 0으로 변경
sec_dpc.iloc[0] = 0
print(sec_dpc.head())

print()

# 주가 일간 변동률 히스토그램

# 히스토그램(histogram) : 도수 분포(frequency distribution)을 나타내는 그래프로서, 데이터값들에 대한 구간별 빈도수를 막대 형태로 표현
# 빈스(bins) : 히스토그램의 구간 수
# 빈스에 따라 그래프 모양이 달라지므로 관측한 데이터 특성을 잘 보여주도록 빈스값 지정

# 삼성전자 주식 종가의 일간 변동률을 18개 구간으로 나누어 빈도수를 표시한 히스토그램으로 출력
import matplotlib.pyplot as plt
plt.hist(sec_dpc, bins=18)
plt.grid(True)
plt.show()

# 출력 결과를 보면 삼성전자 일간 변동률 분포가 0 bin을 기준으로 좌우 대칭에 가까운 정규분포 형태와 비슷
# 급첨 분포(leptokurtic distribution) : 주가 수익률은 정규분포보다 중앙 부분이 더 뾰족한 편
# 팻 테일(fat tail) : 주가 수익률 분포의 양쪽 꼬리는 정규분포보다 더 두터운 편

# 주가 수익률이 급첨 분포를 나타낸다는 것은 정규분포와 비교했을 때 주가의 움직임이 대부분 매우 작은 범위 안에서 발생한다는 것을 의미
# 두꺼운 꼬리를 가리키는 팻 테일은 그래프틔 좌우 극단 부분에 해당하는 아주 큰 가격 변동이 정규분포보다 더 많이 발생한다는 의미

print()

# 삼성전자 일간 변동률의 평균과 표준편차 확인
print(sec_dpc.describe())

print()