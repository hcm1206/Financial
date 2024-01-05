# OHLC : Open-High-Low-Close, 시가-고가-저가-종가를 의미
# 캔들 차트는 OHLC에 해당하는 네 가지 가격을 이용하여 일정 기간의 가격 변동 표시
# 캔들 차트는 시가-고가-저가-종가를 이용하여 하루 동안의 가격 변동을 표시
# 시가보다 종가가 높으면 붉은 양봉으로 표시하고 고가와 저가를 실선으로 연결
# 시가보다 종가가 낮으면 푸른 음봉으로 표시하고 고가와 저가를 실선으로 연결

# OHLC 차트와 캔들 차트의 비교

# 미국에서 사용하는 OHLC 차트(바 차트)와 우리나라에서 사용하는 캔들 차트는 약간 상이
# 그러나 둘 다 OHLC를 기반으로 그리는 차트이므로 표현 방식만 다를 뿐 내용은 동일

print()

# 셀트리온 종가 차트

# 셀트리온의 최근 30개 종가 데이터를 이용하여 차트로 표시하는 코드

# 필요한 라이브러리 임포트
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

# 네이버 금융 셀트리온 일별 시세의 마지막 페이지 번호 추출
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')
pgrr = bs.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]

# 네이버 금융 셀트리온 일별 시세 페이지로부터 주가 정보 받아와 데이터프레임으로 저장
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
for page in range(1, int(last_page)+1):
    url = '{}&page={}'.format(sise_url, page)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    df = df.append(pd.read_html(html, header=0)[0])

# 데이터프레임 결측치 제거
df = df.dropna()
# 셀트리온 최근 30일의 시세 데이터만 추출
df = df.iloc[0:30]
# 셀트리온 시세 데이터를 날짜 순으로 정렬
df = df.sort_values(by='날짜')


# 그래프 제목 설정
plt.title('Celltrion (close)')
# x축 날짜 표시를 45도 회전하여 출력
plt.xticks(rotation=45)
# x축을 날짜로, y축을 셀트리온 종가 데이터로 하여 청록색 그래프로 표시
plt.plot(df['날짜'], df['종가'], 'co-')
# 그래프에 회색 점선 격자 추가
plt.grid(color='gray', linestyle='--')
plt.show()

# 종가 그래프로는 한 달 반 동안의 종가 흐름을 파악할 수 있으나, 일자별 변동폭을 파악하기 어려움

print()