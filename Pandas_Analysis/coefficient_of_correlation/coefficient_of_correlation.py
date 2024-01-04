# 다우존스 지수와 KOSPI 지수 다운로드하여 데이터프레임 생성
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

import pandas as pd

df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

# 상관계수(Coefficient) : 독립변수와 종속변수 사이의 상관관계의 정도를 나타내는 수치
# 상관계수 r은 항상 -1 <= r <= 1 범위
# 양의 상관관계가 가장 강한 값을 1, 음의 상관관계가 가장 강한 값을 -1, 상관관계가 없을 때는 0으로 표현

print()

# 데이터프레임으로 상관계수 구하기

# 데이터프레임의 상관계수 계산
print(df.corr())

print()

# 시리즈로 상관계수 구하기

# 인수로 상관계수를 구할 다른 시리즈 객체를 입력하여 시리즈의 상관계수 계산
df['DOW'].corr(df['KOSPI'])

print()

# 결정계수 구하기
# 결정계수(R-squared) : 관측된 데이터에서 추정한 회귀선이 실제로 데이터를 어느 정도 설명하는지를 나타내는 계수
# 두 변수의 상관관계 정도를 나타내는 상관계수(R value)를 제곱한 값

# 다우존스 지수와 KOSPI 지수의 상관계수 계산
r_value = df['DOW'].corr(df['KOSPI'])
print(r_value)
# 다우존스 지수와 KOSPI 지수의 결정계수 계산
r_squared = r_value ** 2
print(r_squared)

# 결정계수가 1이면 모든 표본 관측치가 추정된 회귀선 안에만 있다는 의미로 추정된 회귀선이 변수 간의 관계를 완벽히 설명
# 결정계수가 0이면 추정된 회귀선이 변수 사이의 관계를 전혀 설명하지 못한다는 의미

print()

# 다우존스 지수와 KOSPI의 회귀 분석
# 다우존스 지수와 KOSPI의 선형회귀 모델을 생성한 뒤 회귀선을 그려서 분석

from scipy import stats
import matplotlib.pyplot as plt

# 다우존스 지수와 KOSPI 지수의 데이터프레임 생성 및 결측치 처리
df = pd.DataFrame({'X': dow['Close'], 'Y': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

# 다우존스 지수와 KOSPI 지수의 선형회귀 모델 생성 및 회귀선 계산
regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}'

# 다우존스 지수와 KOSPI 지수의 산점도와 회귀선을 그래프에 표현
plt.figure(figsize=(7,7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['DOW x KOSPI', regr_line])
plt.title(f'DOW x KOSPI (R = {regr.rvalue:.2f})')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()

print()

# 미국 국채와 KOSPI의 상관관계 분석

# 미국 국채와 KOSPI 데이터 다운로드
tlt = pdr.get_data_yahoo('TLT', '2002-07-30')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

# 미국 국채와 KOSPI의 데이터프레임 생성 및 결측치 처리
df = pd.DataFrame({'X': tlt['Close'], 'Y': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

# 미국 국채와 KOSPI의 선형회귀 모델 생성 및 회귀선 계산
regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}'

# 미국 국채와 KOSPI의 산점도와 회귀선을 그래프에 표현
plt.figure(figsize=(7,7))
plt.plot(df.X, df.Y, 'xg')
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['TLT x KOSPI', regr_line])
plt.title(f'DTLT x KOSPI (R = {regr.rvalue:.2f})')
plt.xlabel('iShares Barclays 20+ Yr Treas.Bond (TLT)')
plt.ylabel('KOSPI')
plt.show()

# 미국 국채와 KOSPI 지수의 상관계수는 다우존스 지수와 KOSPI 지수의 상관계수보다 약간 낮음
# 큰 차이는 아니지만 국내 주식에 투자하고 있을 경우 다우존스 지수에 분산 투자하는 것보다 미국 채권에 분산 투자하는 것이 리스크 완화에 도움

print()

# 상관계수에 따른 리스크 완화

# 현대 포트폴리오 이론(modern portfolio theory, MPT) : 상관관계가 낮은 자산을 대상으로 분산 투자하면 위험을 감소할 수 있다는 이론
# 주식과 채권이 상관관계가 낮은 대표적인 예

# 상관계수 +1.0 : 리스크 완화 효과가 없음
# 상관계수 +0.5 : 중간 정도의 리스크 완화 효과가 있음
# 상관계수 0 : 상당한 리스크 완화 효과가 있음
# 상관계수 -0.5 : 대부분의 리스크를 제거
# 상관계수 -1.0 : 모든 리스크 제거

# 파이썬에서 표시되는 상관관계 출력 확인

# 임의의 정수로 시리즈 1 생성
s1 = pd.Series([+10, -20, +30, -40, +50])
# 시리즈 1과 변동비율과 부호가 같지만 값은 다른 시리즈 2 생성
s2 = pd.Series([+1, -2, +3, -4, +5])
# 시리즈 1과 절댓값은 같지만 부호가 다른 시리즈 3 생성
s3 = pd.Series([-10, +20, -30, +40, -50])
# 시리즈 3개를 포함하는 데이터프레임 생성
df = pd.DataFrame({'S1': s1, 'S2': s2, 'S3': s3})
print(df)

print()

# 각 시리즈의 상관관계 확인
print(df.corr())
# 시리즈 1과 시리즈 2처럼 변동 비율이 같고 부호가 같을 경우 상관관계가 1로 표시
# 시리즈 1과 시리즈 3 또는 시리즈 2와 시리즈 3처럼 변동 비율이 같지만 부호가 반대일 경우 상관관계가 1로 표시

print()