from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

# 종목 코드를 입력받아 해당 종목의 가격, 변동률, 종목명을 반환하는 함수
def get_data(symbol):
    # 네이버 금융에서 입력받은 종목코드에 대한 주가 페이지 URL 설정
    url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(symbol)
    # 설정된 URL에 대해 GET 요청으로 웹 크롤링
    html = requests.get(url, headers={'User-agent':'Mozilla/5.0'}).text
    # 크롤링한 HTML에 대하여 뷰티풀 수프 객체 생성
    soup = BeautifulSoup(html, 'lxml', from_encoding='euc-kr')
    # id가 _nowVal인 <strong> 태그를 찾아 해당 종목에 대한 현재 가격 추출
    cur_price = soup.find('strong', id='_nowVal')
    # id가 _rate인 <strong> 태그를 찾아 해당 종목에 대한 현재 변동률 추출
    cur_rate = soup.find('strong', id='_rate')
    # <title> 태그를 찾아 해당 태그의 문자열 추출
    stock = soup.find('title')
    # <title> 태그의 문자열에서 콜론(:) 문자를 기준으로 첫 번째 문자열(종목명)을 구한 후 문자열 좌우 공백문자 제거
    stock_name = stock.text.split(':')[0].strip()
    # 입력된 종목에 대한 가격, 변동률, 종목명 리턴
    return cur_price.text, cur_rate.text.strip(), stock_name

# 인자를 받는 메인 뷰 정의
def main_view(request):
    # GET 요청의 인자를 딕셔너리로 받아오기
    querydict = request.GET.copy()
    # 딕셔너리를 리스트로 변환
    mylist = querydict.lists()
    # 종목별 각종 요소들을 저장할 빈 2차원 리스트 생성
    rows = []
    # 계좌 잔고를 저장할 변수 생성
    total = 0

    # 인자로 입력된 종목 별로 반복
    for x in mylist:
        # 종목의 종목코드에서 get_data() 함수를 통해 가격, 변동률, 종목명 추출
        cur_price, cur_rate, stock_name = get_data(x[0])
        # 현재 가격에서 쉼표 제거
        price = cur_price.replace(',', '')
        # 입력된 종목의 주식수에서 쉼표 제거 후 숫자형으로 변환
        stock_count = format(int(x[1][0]), ',')
        # 가격과 주식수를 숫자형으로 변환 후 곱하여 해당 종목에 대한 총 평가금액 계산
        sum = int(price) * int(x[1][0])
        # 계산된 종목 총 평가금액을 쉼표를 넣은 문자열로 변환하여 별도의 변수로 저장
        stock_sum = format(sum, ',')
        # 종목명, 종목코드, 현재가, 주식수, 변동률, 종목의 총 평가금액을 리스트에 담은 후 row 2차원 리스트의 원소로 추가
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate, stock_sum])
        # 총 평가 금액에 현재 종목 총 평가 금액을 추가하여 계산
        total = total + int(price) * int(x[1][0])

    # 총 평가 금액에 쉼표를 추가하여 문자열로 변환
    total_amount = format(total, ',')
    # 장고 탬플릿 인자로 보내기 위해 종목별 요소가 저장된 2차원 리스트와 총 평가금액을 딕셔너리로 저장
    values = {'rows' : rows, 'total' : total_amount}
    # 인숫값에 해당하는 values 딕셔너리를 넘겨주면서 탬플릿 파일을 표시하도록 렌더 함수를 호출하며 리턴
    return render(request, 'balance.html', values)