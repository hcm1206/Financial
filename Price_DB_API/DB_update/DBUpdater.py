# 주식 시세를 매일 DB로 업데이트하기

# 주식 시세를 업데이트하는 클래스를 정의하여 외부에서도 사용할 수 있도록 API 구현

import pymysql
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import calendar
from threading import Timer

class DBUpdater:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        # 커낵션 객체를 통해 MariaDB 연결(한글 텍스트 처리를 위해 utf-8로 인코딩)
        self.conn = pymysql.connect(host='localhost', user='root', password='password', db='INVESTAR', charset='utf8')

        # 커서 객체를 생성하고 기업 정보와 일별 시세 테이블이 없으면 생성
        with self.conn.cursor() as curs:
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
                company VARCHAR(40),
                last_update DATE,
                PRIMARY KEY (code)
            )
            """
            curs.execute(sql)
            sql = """
            CREATE TABLE IF NOT EXISTS daily_price (
                code VARCHAR(20),
                date DATE,
                open BIGINT(20),
                high BIGINT(20),
                low BIGINT(20),
                close BIGINT(20),
                diff BIGINT(20),
                volume BIGINT(20),
                PRIMARY KEY(code, date)
            )
            """
            curs.execute(sql)
        # 커서 객체가 실행한 내용을 데이터베이스에 커밋
        self.conn.commit()
        # 주가코드를 저장할 빈 딕셔너리 생성
        self.codes = dict()
        # 기업 정보 업데이트
        self.update_comp_info()

    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close()

    def read_krx_code(self):
        """KRX로부터 상장기업 목록 파일을 읽어와서 데이터프레임으로 반환"""
        # 한국거래소 사이트의 상장법인목록 다운로드 URL
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType13'
        # URL에서 상장법인목록을 다운로드하여 데이터프레임으로 저장
        krx = pd.read_html(url, header=0)[0]
        # 데이터프레임 중 종목코드와 회사명만 추출
        krx = krx[['종목코드', '회사명']]
        # 데이터프레임의 종목코드와 회사명 칼럼을 영문으로 변경
        krx = krx.rename(columns={'종목코드':'code', '회사명':'company'})
        # 종목코드 형식을 6자리 숫자코드로 변경
        krx.code = krx.code.map('{:06d}'.format)
        # 처리 완료된 상장법인목록 데이터프레임 리턴
        return krx

    def update_comp_info(self):
        """종목코드를 company_info 테이블에 업데이트한 후 딕셔너리에 저장"""
        # DB에서 기업 정보 데이터를 추출하는 SQL문을 실행하여 데이터프레임으로 저장
        sql = "SELECT * FROM company_info"
        df = pd.read_sql(sql, self.conn)
        # 기업 정보 데이터프레임을 통해 주가코드 딕셔너리에 종목코드와 회사명을 저장
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]]=df['company'].values[idx]
        # 커서객체 생성
        with self.conn.cursor() as curs:
            # 기업 정보 테이블에서 가장 최근에 업데이트한 날짜를 추출
            sql = "SELECT max(last_update) FROM company_info"
            curs.execute(sql)
            rs = curs.fetchone()
            today = datetime.today().strftime('%Y-%m-%d')

            # 업데이트 기록이 없거나 최근 업데이트 날짜가 오늘이 아니라면
            if rs[0] == None or rs[0].strftime('%Y-%m-%d') < today:
                # krx로부터 상장법인목록 데이터프레임 확보
                krx = self.read_krx_code()
                # 각 상장법인 별로 기업코드, 회사명을 받아와 업데이트하고 최근 업데이트 날짜를 오늘로 기록
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    sql = f"REPLACE INTO company_info (code, company, last_update) VALUES ('{code}', '{company}', '{today}')"
                    curs.execute(sql)
                    self.codes[code] = company
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    # 업데이트 한 내용을 콘솔에 출력
                    print(f"[{tmnow}] {idx:04d} REPLACE INTO company_info VALUES ({code}, {company}, {today})")
                # 커서 객체가 실행한 내용을 데이터베이스에 커밋
                self.conn.commit()
                print('')

    def read_naver(self, code, company, pages_to_fetch):
        """네이버에서 주식 시세를 읽어서 데이터프레임으로 반환"""
        try:
            # 인수로 받아온 종목코드에 대해 네이버 금융에서 일별 시세의 마지막 페이지 수 확보
            url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
            html = requests.get(url, headers={'User-agent':'Mozilla/5.0'}).text
            bs = BeautifulSoup(html, 'lxml')
            pgrr = bs.find("td", class_='pgRR')
            if pgrr is None:
                return None
            s = str(pgrr.a['href']).split('=')
            lastpage = s[-1]
            df = pd.DataFrame()
            # 설정 파일에서 설정된 페이지 수와 마지막 페이지 수 중 작은 것을 선택
            pages = min(int(lastpage), pages_to_fetch)
            # 선택된 페이지 수 만큼 반복하며 일별 시세 페이지에서 시세 데이터를 받아와 데이터프레임에 저장
            for page in range(1, pages + 1):
                url = '{}&page={}'.format(url, page)
                req = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
                df = df.append(pd.read_html(req.text, header=0)[0])
                tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading...'.format(tmnow, company, code, page, pages), end='\r')
            # 시세 데이터 저장이 끝난 데이터프레임 가공
            df = df.rename(columns={'날짜':'date', '종가':'close', '전일비':'diff', '시가':'open', '고가':'high', '저가':'low', '거래량':'volume'})
            df['date'] = df['date'].replace('.', '-')
            df = df.dropna()
            df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)
            df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]
        # 네이버 금융으로부터 데이터를 가져와 데이터프레임으로 가공하는 과정에서 예외 발생 시 예외 출력
        except Exception as e:
           print('Exception occured :', str(e))
           return None
        # 최종 형태로 가공된 데이터프레임 리턴
        print(df)
        return df
    

    def replace_into_db(self, df, num, code, company):
        """네이버에서 읽은 주식 시세를 DB에 REPLACE"""
        # 커서 객체 생성하여 일별 시세 테이블을 업데이트 후 DB에 반영
        with self.conn.cursor() as curs:
            for r in df.itertuples():
                sql = f"REPLACE INTO daily_price VALUES ('{code}', '{r.date}', {r.open}, {r.high}, {r.low}, {r.close}, {r.diff}, {r.volume})"
                curs.execute(sql)
            self.conn.commit()
            print('[{}] #{:04d} {} ({}) : {} rows > REPLACE INTO daily_price [OK]'.format(datetime.now().strftime('%Y-%m-%d %H:%M'), num+1, company, code, len(df)))

    def update_daily_price(self, pages_to_fetch):
        """KRX 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트"""
        # 모든 종목코드에 대하여 read_naver() 메서드를 이용해 종목코드에 대한 일별 시세 데이터프레임을 확보한 후 replace_into_DB 메서드를 통해 DB에 저장
        for idx, code in enumerate(self.codes):
            df = self.read_naver(code, self.codes[code], pages_to_fetch)
            if df is None:
                continue
            self.replace_into_db(df, idx, code, self.codes[code])

    def execute_daily(self):
        """실행 즉시 및 매일 오후 5시에 daily_price 테이블 업데이트"""
        # 먼저 최신 상장 법인 목록을 DB에 업데이트
        self.update_comp_info()
        # config.json 파일에서 패치할 페이지 수를 추출
        try:
            with open('config.json', 'r') as in_file:
                config = json.load(in_file)
                pages_to_fetch = config['pages_to_fetch']
        # config.json 파일이 없다면 패치할 페이지 수를 100개로 설정한 후 config.json 파일을 생성하여 다음 실행부터 패치 페이지 수를 1로 설정하도록 작성
        except FileNotFoundError:
            with open('config.json', 'w') as out_file:
                pages_to_fetch = 100
                config = {'pages_to_fetch': 1}
                json.dump(config, out_file)
        # pages_to_fetch값으로 update_daily_price() 메서드 호출
        self.update_daily_price(pages_to_fetch)

        # 오늘 날짜 정보 객체 저장
        tmnow = datetime.now()
        # 오늘 날짜 기준 이번 달의 마지막 날짜 정보 객체 저장
        lastday = calendar.monthrange(tmnow.year, tmnow.month)[1]
        # 내일 날짜 계산하여 내일 날짜의 오후 5시 시각을 계산
        if tmnow.month == 12 and tmnow.day == lastday:
            tmnext = tmnow.replace(year=tmnow.year+1, month=1, day=1, hour=17, minute=0, second=0)
        elif tmnow.day == lastday:
            tmnext = tmnow.replace(month=tmnow.month+1, day=1, hour=17, minute=0, second=0)
        else:
            tmnext = tmnow.replace(day=tmnow.day+1, hour=17, minute=0, second=0)
        # 오늘 날짜와 내일 오후 5시 사이의 시간 차이 계산
        tmdiff = tmnext - tmnow
        secs = tmdiff.seconds

        # 타이머 객체 생성한 후 내일 오후 5시가 되면 execute_daily() 메서드가 실행되도록 설정
        t = Timer(secs, self.execute_daily)
        print("Waiting for next update ({}) ...".format(tmnext.strftime('%Y-%m-%d %H:%M')))
        t.start()

# 이 파일이 단독으로 실행되었다면 DBUpdater 객체를 생성하고 시세 업데이트 실행
if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.execute_daily()