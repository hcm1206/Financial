# 듀얼 모멘텀 투자

# 모멘텀(Momentum) : 물리학 용어로 '물체를 움직이는 힘'을 의미
# 주식 시장에서 모멘텀은 한 번 움직이기 시작한 주식 가격이 계속 그 방향으로 나아가려는 성질을 가리킴


# 모멘텀 현상

# 모멘텀 현상은 행동재무학에서 일컫는 군집 행동, 정박 효과, 확증 편향, 처분 효과 등의 행동 편향(action bias)에 의해서 발생한다고 알려짐
# 최근 주가 움직임이 미래에도 이어질 것이라고 믿는 확증 편향에 사로잡힌 투자자들이 최근 상승주에 더 투자하기 때문에 모멘텀이 이어진다는 것
# 이러한 편향들로 인해 정보에 대한 과소평가 혹은 과대평가가 생겨나게 되며 이는 가격의 비효율성으로 이어져 투자자들의 비이성적 행동을 낳게 됨

# 군집 행동(herding) : 다수 그룹의 행동을 따라하는 경향
# 정박 효과(anchoring) : 정보를 처음 제공받은 시점에 지나치게 의존하는 경향
# 확증 편향(confirmation bias) : 본인의 믿음과 반대되는 정보를 무시하는 경향
# 처분 효과(disposition effect) : 수익이 난 주식을 금방 팔고, 손해 본 주식을 계속 보유하는 경향


# 듀얼 모멘텀 투자
# 1800년대 초반부터 모멘텀에 대한 수많은 학술 연구가 이루어진 덕분에 모멘텀 투자 전략이 거의 모든 자산 유형에 유효하다는 사실이 밝혀짐
# 최근 6~12개월 동안의 상대적으로 수익률이 높은 종목을 매수하는 상대적 모멘텀 전략이 나름대로 일리가 있어 보이지만
# 반면에 이미 수익이 난 종목을 매수하기 때문에 소위 상투를 잡게 될 위험성이 커짐
# 이에 대한 해결책이 절대적 모멘텀 전략으로 상승장에서만 투자하고 하락장에서는 미국 단기 국채나 현금으로 갈아타는 전략

# 게리 안토니치의 듀얼 모멘텀 투자(Dual Momentum Investing) : 상대 강도가 센 주식 종목들에 투자하는 상대적 모멘텀 전략과
# 과거 6~12개월의 수익이 단기 국채 수익률을 능가하는 강세장에서만 투자하는 절대적 모멘텀 전략을 하나로 합친 듀얼 전략

# 절대 모멘텀 자체는 상승장에서 투자하고 하락장에서 쉬어가는 매우 단순한 전략
# 절대 모멘텀을 상대 모멘텀과 함께 사용함으로써 상대 모멘텀만 사용했을 때보다 MDD를 줄일 뿐만 아니라 더 높은 수익률 달성 가능

# 듀얼 모멘텀 클래스 구현

# 필요한 라이브러리 임포트
import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta
from Investar import Analyzer

# 듀얼 모멘텀 클래스 정의
class DualMomentum:
    def __init__(self):
        """생성자: KRX 종목코드(codes)를 구하기 위한 MarketDB 객체 생성"""
        # MarketDB API를 이용하여 종목코드를 구하기 위한 데이터프레임 생성
        self.mk = Analyzer.MarketDB()
    
    # 상대 모멘텀
        
    # 상대 모멘텀(Relative) : 특정 기간 동안 상대적으로 수익률이 좋았던 n개 종목을 구하는 것
        
    def get_rltv_momentum(self, start_date, end_date, stock_count):
        """특정 기간 동안 수익률이 제일 높았던 stock_count 개의 종목들 (상대 모멘텀)
            - start_date    : 상대 모멘텀을 구할 시작일자 ('2020-01-01)
            - end_date      : 상대 모멘텀을 구할 종료일자 ('2020-12-31)
            - stock_count   : 상대 모멘텀을 구할 종목수
        """
        # 커넥션 객체를 생성하여 MariaDB에 연결
        connection = pymysql.connect(host='localhost', port=3306, db='INVESTAR', user='root', passwd='password', autocommit=True)
        # 커서 객체 생성
        cursor = connection.cursor()

        # 입력된 시작 날짜까지의 날짜 중 유효한 시작 날짜를 찾아서 추출
        sql = f"select max(date) from daily_price where date <= '{start_date}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        # 유효한 시작 날짜가 없으면 에러 발생
        if (result[0] is None):
            print("start_date : {} -> returned None".format(sql))
            return
        # 조회된 거래일을 적절한 포맷 문자열로 변환해 사용자가 입력한 조회 시작 일자 변수에 반영
        start_date = result[0].strftime('%Y-%m-%d')

        # 입력된 마지막 날짜까지의 날짜 중 유효한 마지막 날짜를 찾아서 추출
        sql = f"select max(date) from daily_price where date <= '{end_date}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        # 유효한 마지막 날짜가 없으면 에러 발생
        if (result[0] is None):
            print("end_date : {} -> returned None".format(sql))
            return
        # 조회된 거래일을 적절한 포맷 문자열로 변환해 사용자가 입력한 조회 종료 날짜 변수에 반영
        end_date = result[0].strftime('%Y-%m-%d')

        # 종목별 수익률 계산
        # 상대 모멘텀은 종목별 수익률을 계산하는 것
        # 시작자와 종료일자에 해당하는 종가를 DB에서 조회해 종목별 수익률 계산

        # 2차원 리스트 데이터를 저장할 빈 리스트 생성
        rows = []
        # 칼럼명 설정
        columns = ['code', 'company', 'old_price', 'new_price', 'returns']
        # 각 종목코드 별로 반복
        for _, code in enumerate(self.mk.codes):
            # 현재 종목 코드와 시작 날짜에 해당하는 종가 추출
            sql = f"select close from daily_price where code='{code}' and date='{start_date}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            # 추출된 값이 없다면 다음 종목코드로 넘어감
            if (result is None):
                continue
            # 시작 날짜에 해당하는 가격을 조회
            old_price = int(result[0])
            # 현재 종목 코드와 종료 날짜에 해당하는 종가 추출
            sql = f"select close from daily_price where code='{code}' and date='{end_date}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            # 추출된 값이 없다면 다음 종목코드로 넘어감
            if (result is None):
                continue
            # 종료 날짜에 해당하는 가격을 조회
            new_price = int(result[0])
            # 현재 종목에 대한 수익률 계산
            returns = (new_price / old_price - 1) * 100
            # 2차원 리스트에 종목 코드, 종목명, 구 가격, 신 가격, 수익률을 하나의 행으로 추가
            rows.append([code, self.mk.codes[code], old_price, new_price, returns])

        # 상대 모멘텀 데이터프레임 생성
        # 2차원 리스트에 종목별 수익을 저장했다면 이를 다시 데이터프레임으로 변환해서 수익률(returns)이 높은 순서로 출력
        
        # 완성된 2차원 리스트를 미리 설정한 컬럼명을 반영하여 상대 모멘텀 데이터프레임으로 저장
        df = pd.DataFrame(rows, columns=columns)
        # 상대 모멘텀 데이터프레임 중 종목 코드, 종목명, 구 가격, 신 가격, 수익률 칼럼만 갖도록 구조 수정
        df = df[['code', 'company', 'old_price', 'new_price', 'returns']]
        # 상대 모멘텀 데이터프레임을 수익률(returns) 칼럼을 기준으로 내림차순으로 정렬
        df = df.sort_values(by='returns', ascending=False)
        # 인수로 입력받은 종목수만큼의 상위 종목만 남김
        df = df.head(stock_count)
        # 상대 모멘텀 데이터프레임의 인덱스를 수익률 순위로 변경
        df.index = pd.Index(range(stock_count))

        # 커낵션 객체 종료
        connection.close()
        # 구한 상대 모멘텀 수익률의 평균을 계산
        print(f"\nRelative momentum ({start_date} ~ {end_date}) : {df['returns'].mean():.2f}% \n")
        # 상대 모멘텀 데이터프레임 리턴
        return df
    
    # 절대 모멘텀

    # 절대 모멘텀(Absolute Momentum) : 자산의 가치가 상승하고 있을 때만 투자하고 그렇지 않을 때는 단기 국채를 매수하거나 현금을 보유하는 전략
    
    def get_abs_momentum(self, rltv_momentum, start_date, end_date):
        """특정 기간 동안 상대 모멘텀에 투자했을 때의 평균 수익률 (절대 모멘텀)
            - rltv_momentum : get_rltv_momentum() 함수의 리턴값 (상대 모멘텀)
            - start_date    : 절대 모멘텀을 구할 매수일 ('2020-01-01')
            - end_date      : 절대 모멘텀을 구할 매도일 ('2020-12-31')
        """
        # 인수로 받은 상대 모멘텀 데이터프레임 rltv_momentum에서 종목 칼럼(code)을 추출해 종목 리스트(stocklist)를 생성
        stockList = list(rltv_momentum['code'])

        # 커낵션 객체를 이용하여 MariaDB에 연결
        connection = pymysql.connect(host='localhost', port=3306, db='INVESTAR', user='root', passwd='password', autocommit=True)
        # 커서 객체 생성
        cursor = connection.cursor()

        # 입력된 시작 날짜까지의 날짜 중 유효한 시작 날짜를 찾아서 추출
        sql = f"select max(date) from daily_price where date <= '{start_date}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        # 유효한 시작 날짜가 없으면 에러 발생
        if (result[0] is None):
            print("{} -> returned None".format(sql))
            return
        # 조회된 거래일을 적절한 포맷 문자열로 변환해 사용자가 입력한 조회 시작 날짜 변수에 반영
        start_date = result[0].strftime('%Y-%m-%d')
        
        # 입력된 종료 날짜까지의 날짜 중 유효한 종료 날짜를 찾아서 추출
        sql = f"select max(date) from daily_price where date <= '{end_date}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        # 유효한 종료 날짜가 없으면 에러 발생
        if (result[0] is None):
            print(" {} -> returned None".format(sql))
            return
        # 조회된 거래일을 적절한 포맷 문자열로 변환해 사용자가 입력한 조회 종료 날짜 변수에 반영
        end_date = result[0].strftime('%Y-%m-%d')

        # 2차원 리스트 데이터를 저장할 빈 리스트 생성
        rows = []
        # 칼럼명 설정
        columns = ['code', 'company', 'old_price', 'new_price', 'returns']
        # 상대 모멘텀에 저장된 종목코드 별로 반복
        for _, code in enumerate(stockList):
            # 현재 종목 코드와 시작 날짜에 해당하는 종가 추출
            sql = f"select close from daily_price where code='{code}' and date='{start_date}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            # 추출된 값이 없다면 다음 종목으로 넘어감
            if (result is None):
                continue
            # 시작 날짜에 해당하는 가격을 조회
            old_price = int(result[0])
            # 현재 종목 코드와 종료 날짜에 해당하는 종가 추출
            sql = f"select close from daily_price where code='{code}' and date='{end_date}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            # 추출된 값이 없다면 다음 종목으로 넘어감
            if (result is None):
                continue
            # 종료 날짜에 해당하는 가격을 조회
            new_price = int(result[0])
            # 현재 종목에 대한 수익률 계산
            returns = (new_price / old_price - 1) * 100
            # 2차원 리스트에 종목 코드, 종목명, 구 가격, 신 가격, 수익률을 하나의 행으로 추가
            rows.append([code, self.mk.codes[code], old_price, new_price, returns])
        
        # 완성된 2차원 리스트를 미리 설정한 칼럼명을 반영하여 절대 모멘텀 데이터프레임으로 저장
        df = pd.DataFrame(rows, columns=columns)
        # 절대 모멘텀 데이터프레임 중 종목 코드, 종목명, 구 가격, 신 가격, 수익률 칼럼만 갖도록 구조 수정
        df = df[['code', 'company', 'old_price', 'new_price', 'returns']]
        # 절대 모멘텀 데이터프레임을 수익률(returns) 칼럼을 기준으로 내림차순 정렬
        df = df.sort_values(by='returns', ascending=False)
        # 커넥션 객체 종료
        connection.close()
        # 절대 모멘텀 데이터프레임 출력
        print(df)
        # 구한 절대 모멘텀 데이터프레임의 수익률의 평균을 계산
        print(f"\nAbsolute momentum ({start_date} ~ {end_date}) : {df['returns'].mean():.2f}%")
        return