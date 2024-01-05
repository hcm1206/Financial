# 셀트리온 캔들 차트

# 구 버전으로 캔들 차트 그리기
# 예전 방식대로 mpl_finance 패키지를 이용해 캔들 차트 구현

# 필요한 라이브러리 임포트
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
# 구형 mpl_finance 라이브러리 방식의 캔들 차트 함수
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime

# 페이지 맨 뒤 숫자 확인
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
pgrr = bs.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]

# 전체 페이지 로드
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
for page in range(1, int(last_page)+1):
    url = '{}&page={}'.format(sise_url, page)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = df.append(pd.read_html(html, header=0)[0])

# 차트 출력을 위해 데이터프레임 가공
df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by='날짜')
# 각 날짜 별로 반복
for idx in range(0, len(df)):
    # 날짜 칼럼의 %Y.%m.%d 형식 문자열을 datetime형으로 변환
    dt = datetime.strptime(df['날짜'].values[idx], '%Y.%m.%d').date()
    # datetime형을 다시 float형으로 변환
    df['날짜'].values[idx] = mdates.date2num(dt)
# 날짜, 시가, 고가, 저가, 종가 칼럼 별로 별도의 데이터프레임 생성
ohlc = df[['날짜', '시가', '고가', '저가', '종가']]

# 구 버전 라이브러리로 캔들 차트 구현

# 차트 크기 설정
plt.figure(figsize=(9, 6))
# 1행 1열 중 1행 1열에 차트 표시
ax = plt.subplot(1, 1, 1)
# 차트 제목 설정
plt.title('Celltrion (mpl_finance candle stick)')
# 날짜, 시가, 고가, 저가, 종가 데이터프레임을 통해 캔들 차트 표시
candlestick_ohlc(ax, ohlc.values, width=0.7, colorup='red', colordown='blue')
# x축에 표시되는 숫자로 된 날짜를 문자열로 변환하여 표시
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# x축 날짜 표시를 45도 회전시켜 출력
plt.xticks(rotation=45)
# 차트에 회색 점선 격자 표시
plt.grid(color='gray', linestyle='--')
plt.show()

# 캔들 차트를 이용하면 종가만 표시했을 때 보이지 않던 하룻 동안의 주가의 변동폭을 한 눈에 볼 수 있어 좋음
# 그러나 캔들 차트를 그리기 위한 구형 라이브러리 함수는 복잡한 과정이 많음

print()