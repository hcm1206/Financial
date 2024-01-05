# 신버전으로 캔들 차트 그리기
# 새로 출시된 mplfinance 패키지를 이용해 캔들 차트를 더 쉽게 구현 가능
# OHLC 데이터 칼럼과 날짜 시간 인덱스(DatetimeIndex)를 포함한 데이터프레임만 있으면 수동으로 처리했던 데이터 변환 작업을 자동화

# 필요한 라이브러리 임포트
import pandas as pd
import requests
from bs4 import BeautifulSoup
# 신형 mplfinance 라이브러리 사용
import mplfinance as mpf

# 맨 뒤 페이지 숫자 확인
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
# 한글 칼럼명을 함수가 인식할 수 있도록 영문 칼럼명으로 변경
df = df.rename(columns={'날짜':'Date', '시가':'Open', '고가':'High', '저가':'Low', '종가':'Close', '거래량':'Volume'})
# 날짜 기준으로 오름차순 정렬
df = df.sort_values(by='Date')
# Date 칼럼을 DatetimeIndex형으로 변경한 후 데이터프레임의 인덱스로 설정
df.index = pd.to_datetime(df.Date)
# 시가, 고가, 저가, 종가, 거래량 칼럼만 갖도록 데이터프레임 구조 변경
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# 가공한 시세 데이터프레임을 인수로 넘겨 캔들 차트 형태로 출력
mpf.plot(df, title='Celltrion candle chart', type='candle')

print()

# 시세 데이터를 미국식 OHLC 차트로 변경(type 미지정시 기본적으로 ohlc 차트로 설정)
mpf.plot(df, title='Celltrion ohlc chart', type='ohlc')

print()

# 캔들 색상 변경, 거래량 표시, 이동평균선 출력 요소가 포함된 캔들 차트 구현

# mpf.plot() 함수에 저장할 인수 딕셔너리 정의
kwargs = dict(title='Celltrion customized chart', type='candle', mav=(2, 4, 6), volume=True, ylabel='ohlc candles')
# 상승은 빨간색, 하락은 파란색으로 지정하고 관련 색상은 이를 따르도록 마켓색상 설정
mc = mpf.make_marketcolors(up='r', down='b', inherit=True)
# 설정한 마켓색상을 인수로 넘겨 스타일 객체 생성
s = mpf.make_mpf_style(marketcolors=mc)
# 시세 데이터를 인수 딕셔너리와 스타일 객체에서 정의된 설정에 따라 캔들 차트 출력
mpf.plot(df, **kwargs, style=s)