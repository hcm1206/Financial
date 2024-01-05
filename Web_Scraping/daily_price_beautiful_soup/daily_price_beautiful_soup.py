# 맨 뒤 페이지 숫자 구하기

# 뷰티풀 수프를 이용하여 네이버 금융에서 셀트리온의 맨 뒤 페이지 숫자 확인

from bs4 import BeautifulSoup
import requests
# 네이버 금융 셀트리온 일별 시세 첫 페이지 URL
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
# 셀트리온 URL에 대해 브라우저 정보를 헤더에 추가하여 html 요청
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
# html에 대하여 'lxml' 파싱 방식으로 뷰티풀 수프 객체 생성
bs = BeautifulSoup(html, 'lxml')
# 뷰티풀 수프 객체 중 'pgRR' 클래스의 td 태그를 검색
pgrr = bs.find('td', class_='pgRR')
# pgRR 클래스 td 태그의 링크(href) 속성값 출력
print(pgrr.a['href'])

print()

# pgRR의 전체 텍스트를 계층적으로 확인
print(pgrr.prettify())
# 태그를 제외한 텍스트 부분만 확인
print(pgrr.text)

# 문자열을 리스트로 분리한 후 리스트의 마지막 원소를 통해 셀트리온 일별 시세의 전체 페이지 수 확인
s = str(pgrr.a['href']).split('=')
last_page = s[-1]
print(last_page)

print()

# 전체 페이지 불러오기
# 셀트리온 일별 시세의 첫 페이지부터 마지막 페이지까지 차례대로 반복하면서 일별 시세 조회

import pandas as pd

# 일별 시세를 저장할 빈 데이터프레임 생성
df = pd.DataFrame()
# 셀트리온 일별 시세를 받아올 네이버 금융 URL
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

# 셀트리온 일별 시세 첫 페이지부터 마지막 페이지까지 반복
for page in range(1, int(last_page)+1):
    # 페이지 번호를 URL에 추가하여 URL 완성
    url = '{}&page={}'.format(sise_url, page)
    # URL에 대하여 웹 페이지 HTML 요청
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    # 데이터 프레임에 HTML에 저장된 시세 데이터 추가
    df = df.append(pd.read_html(html, header=0)[0])
# 데이터프레임 결측치 제거
df = df.dropna()
print(df)

# 2005년 7월 19일부터 오늘까지 일별 시세 출력

print()