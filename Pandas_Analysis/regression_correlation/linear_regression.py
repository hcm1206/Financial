# 사이파이 선형 회귀 분석

# 사이파이(Scipy)는 파이썬 기반 수학, 과학, 엔지니어링용 핵심 패키지 모음
# 사이파이는 넘파이 기반의 함수들과 수학적 알고리즘의 모음으로 넘파이, 맷플롯립(Matplotlib), 심파이(Sympy), 팬더스 등을 포함

print()

# 선형 회귀 분석

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

# 회귀 모델 : 연속적인 데이터 Y와 이 Y의 원인이 되는 X 간의 관계를 추정하는 관계식을 의미
# 실제 데이터 값에는 측정 상의 한계로 인한 잡음(noise)이 존재하므로 정확한 관계식을 표현하는 확률 변수인 오차항을 두게 됨

# 선형 회귀 모델(linear regression model) : 독립변수 X와 종속변수 Y의 관계가 1차식으로 나타나는 모델
# 회귀 함수(regression function) : 선형 회귀 모델에서의 Y의 기대치 

# 파이파이 패키지의 서브 패키지인 stats의 통계 함수를 이용하여 선형 회귀 모델 생성
from scipy import stats
regr = stats.linregress(df['DOW'], df['KOSPI'])
# 선형 회귀식 매개변수(기울기, 절편, r값(상관계수), p값, 표준편차) 출력
print(regr)

print()