# 산점도 분석

# 산점도(Scatter plot) : 독립변수 x와 종속변수 y의 상관관계를 확인할 때 쓰는 그래프
# 미국 시장과 국내 시장의 상관관계를 알아보고자 x를 다우존스 지수로, y를 KOSPI 지수로 하는 산점도 구현

# 필요한 라이브러리 임포트
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# 2000년 이후 다우존스 지수(^DJI)와 KOSPI(^KS11) 데이터 다운로드
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

# 다우존스 지수 데이터 개수와 KOSPI 지수 데이터 개수를 출력 (데이터 개수가 다름)
print(len(dow)); print(len(kospi))
# 데이터 개수가 다르기 때문에 산점도 출력에 오류 발생
# pls.scatter(dow, kospi, marker='.)

import pandas as pd

# 다우존스 지수 종가 칼럼과 KOSPI 지수 종가 칼럼을 합쳐서 데이터프레임 생성
# 데이터프레임에서 한쪽에 데이터가 없으면 값이 없다는 의미의 NaN을 자동으로 할당
df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
print(df)

# 데이터프레임에 NaN이 포함되어 있어도 산점도 출력에 오류 발생
# plt.scatter(*df['DOW'], df['KOSPI'], marker='.')

# 데이터프레임에 포함된 NaN값을 뒤에 있는 값으로 NaN 위치를 덮어씌워 채움
df = df.fillna(method='bfill')
print(df)

# 데이터프레임의 마지막 행에 존재하는 NaN을 제거하기 위해 NaN 앞에 있는 값으로 NaN 값을 덮어씌움
df = df.fillna(method='ffill')
print(df)

import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))
# x축은 다우존스 지수, y축은 KOSPI 지수로 하고 작은 원(.) 모양으로 산점도 출력
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()

# 산점도에서 점의 분포가 y = x인 직선 형태에 가까울수록 직접적인 관계가 있다고 볼 수 있음
# 다우존스의 지수와 KOSPI 지수는 어느 정도 영향을 미치긴 하지만 그리 강하지는 않음

print()