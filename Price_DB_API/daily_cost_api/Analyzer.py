# 일별 시세 조회 API 구현

import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta
import re

class MarketDB:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 연결"""
        # MariaDB 접속하여 connect 객체 생성
        self.conn = pymysql.connect(host='localhost', user='root', password='password', db='INVESTAR', charset='utf8')
        # 종목코드 저장할 딕셔너리 생성
        self.codes = {}
        # 기업 정보를 불러오기 위해 메서드 호출하여 종목코드 딕셔너리 완성
        self.get_comp_info()

    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        # MariaDB 접속 해재 및 커넥션 객체 제거
        self.conn.close()

    def get_comp_info(self):
        """company_info 테이블에서 읽어와서 codes에 저장"""
        # DB 기업 정보 테이블로부터 종목코드와 기업명을 불러와 종목코드 딕셔너리에 저장
        sql = "SELECT * FROM company_info"
        krx = pd.read_sql(sql, self.conn)
        for idx in range(len(krx)):
            self.codes[krx['code'].values[idx]] = krx['company'].values[idx]

    def get_daily_price(self, code, start_date=None, end_date=None):
        """KRX 종목별 시세를 데이터프레임 형태로 변환
            - code          : KRX 종목코드('005930') 또는 상장기업명('삼성전자')
            - start_date    : 조회 시작일('2020-01-01'), 미입력 시 1년 전 오늘
            - end_date      : 조회 종료일('2020-12-31'), 미입력 시 오늘 날짜
        """
        # 시작 날짜 미입력 시
        if (start_date is None):
            # 오늘 날짜에서 1년 전 날짜를 계산하여 시작 날짜로 지정
            one_year_ago = datetime.today() - timedelta(days=365)
            start_date = one_year_ago.strftime('%Y-%m-%d')
            print("start_date is initialized to '{}'".format(start_date))
        else:
            # 시작 날짜를 정규표현식을 이용하여 연, 월, 일 분리
            start_lst = re.split('\D+', start_date)
            if (start_lst[0] == ''):
                start_lst = start_lst[1:]
            start_year = int(start_lst[0])
            start_month = int(start_lst[1])
            start_day = int(start_lst[2])
            # 입력된 연도가 유효하지 않다면 에러 발생
            if start_year < 1900 or start_year > 2200:
                print(f"ValueError: start year({start_year:d}) is wrong.")
                return
            # 입력된 월이 유효하지 않다면 에러 발생
            if start_month < 1 or start_month > 12:
                print(f"ValueError: start_moth({start_month:d}) is wrong.")
                return
            # 입력된 일이 유효하지 않다면 에러 발생
            if start_day < 1 or start_day > 31:
                print(f"ValueError: start_day({start_day:d}) is wrong.")
                return
            start_date = f"{start_year:04d}-{start_month:02d}-{start_day:02d}"
        # 마지막 날짜 미입력 시
        if (end_date is None):
            # 오늘 날짜를 마지막 날짜로 지정
            end_date = datetime.today().strftime('%Y-%m-%d')
            print("end_date is initialized to {}".format(end_date))
        else:
            # 마지막 날짜를 정규표현식을 이용하여 연, 월, 일 분리
            end_lst = re.split('\D+', end_date)
            if (end_lst[0] == ''):
                end_lst = end_lst[1:]
            end_year = int(end_lst[0])
            end_month = int(end_lst[1])
            end_day = int(end_lst[2])
            # 입력된 연도가 유효하지 않다면 에러 발생
            if end_year < 1900 or end_year > 2200:
                print(f"ValueError: start year({end_year:d}) is wrong.")
                return
            # 입력된 월이 유효하지 않다면 에러 발생
            if end_month < 1 or end_month > 12:
                print(f"ValueError: start_moth({end_month:d}) is wrong.")
                return
            # 입력된 일이 유효하지 않다면 에러 발생
            if end_day < 1 or end_day > 31:
                print(f"ValueError: start_day({end_day:d}) is wrong.")
                return
            end_date = f"{end_year:04d}-{end_month:02d}-{end_day:02d}"
        
        # 종목코드 딕셔너리의 키(종목코드)를 리스트로 저장
        codes_keys = list(self.codes.keys())
        # 종목코드 딕셔너리의 값(회사명)을 리스트로 저장
        codes_values = list(self.codes.values())
        # 입력된 코드가 딕셔너리에 종목코드로 존재한다면 그대로 진행
        if code in codes_keys:
            pass
        # 입력된 코드가 딕셔너리에 회사명으로 존재한다면 해당하는 종목코드로 코드를 변경
        elif code in codes_values:
            idx = codes_values.index(code)
            code = codes_keys[idx]
        # 입력된 코드가 존재하지 않다면 에러 발생
        else:
            print("ValueError: Code({}) doesn't exist.".format(code))

        # DB에서 입력된 종목코드에 대하여 시작일과 종료일까지의 일별 시세를 불러와 데이터프레임으로 출력
        sql = f"SELECT * FROM daily_price WHERE code = '{code}' and date >= '{start_date}' and date <= '{end_date}'"
        df = pd.read_sql(sql, self.conn)
        df.index = df['date']
        return df