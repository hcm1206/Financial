# RSI_SMA를 이용한 백테스트

# 매매 주문에 대한 처리 결과를 상세히 출력하도록 보완
# 21일 단순 이동 평균에 대한 RSI_SMA를 지표로 하여 엔씨소프트 주가에 대한 백테스트 수행
# RSI_SMA : 커틀러 RSI라고도 하며 상승분화 하락분을 계산할 때 지수 이동 평균 대신 단순 이동 평균 이용

# bt.indicators 패키지는 Accdecoscillator, ATR, Bollinger, CCI, Crossover, Deviation, DirectionalMove,
# DMA, Ichimoku, MACD, Momentum, Sma, Stochastic, Williams, WMA 등 대부분의 지표를 모듈로 제공

# RSI_SMA를 지표로 하고 처리 결과 출력 부분을 보완한 엔씨소프트 백테스트 결과 출력

# 필요한 라이브러리 임포트
import backtrader as bt
from datetime import datetime
import yfinance as yf

# bt.Strategy 클래스를 상속받아 새로운 전략 클래스 생성
class MyStrategy(bt.Strategy):
    # 클래스 생성자 정의
    def __init__(self):
        # 입력받은 주가 데이터에서 종가 정보 추출
        self.dataclose = self.datas[0].close
        # 주문 상태 객체를 저장할 변수 선언
        self.order = None
        # 거래 금액 객체를 저장할 변수 선언
        self.buyprice = None
        # 거래 수수료 객체를 저장할 변수 선언
        self.buycomm = None
        # 이전 21일을 기준으로 종가에 대한 RSI_SMA 지표를 계산하여 객체로 저장
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=21)

    # 매 주문 상태를 입력받아 거래 정보를 로그로 출력하는 메서드 정의
    def notify_order(self, order):
        # 주문 상태가 제출(Submiited) 또는 승인(Accepted)일 때 아무것도 실행하지 않음
        if order.status in [order.Submitted, order.Accepted]:
            return
        # 주문 상태가 완료(Completed)일 때
        if order.status in [order.Completed]:
            # 매수라면
            if order.isbuy():
                # 매수 시 주가, 수량, 수수료, 매수 수행 후 자산을 계산하여 로그로 출력
                self.log(f"BUY  : 주가 {order.executed.price:,.0f}, \
                         수량 {order.executed.size:,.0f}, \
                         수수료 {order.executed.comm:,.0f}, \
                         자산 {cerebro.broker.getvalue():,.0f}")
                # 주문 수행 후 가격 계산
                self.buyprice = order.executed.price
                # 주문 수행 후 수수료 계산
                self.buycomm = order.executed.comm
            # 매도라면
            else:
                # 매도 시 주가, 수량, 수수료, 매도 수행 후 자산을 계산하여 로그로 출력
                self.log(f"SELL : 주가 {order.executed.price:,.0f}, \
                         수량 {order.executed.size:,.0f}, \
                         수수료 {order.executed.comm:,.0f}, \
                         자산 {cerebro.broker.getvalue():,.0f}")
            # 주문 수행 후 그래프 설정
            self.bar_executed = len(self)
        # 주문 상태가 취소(Cancled)일 때
        elif order.status in [order.Canceled]:
            # 주문이 취소되었음을 로그로 출력
            self.log('ORDER CANCELD')
        # 주문 상태가 마진(Margin)일 때
        elif order.status in [order.Margin]:
            # 주문 마진을 로그로 출력
            self.log('ORDER MARGIN')
        # 주문 상태가 거절(Rejected)일 때
        elif order.status in [order.Rejected]:
            # 주문이 거절되었음을 로그로 출력
            self.log('ORDER REJECTED')
        # 주문 정보를 로그로 출력한 후 주문 객체 변수를 비움
        self.order = None
    
    # 데이터와 지표(indicator)를 만족시키는 주기마다 호출되는 next() 메서드 정의
    def next(self):
        # 현재 시장에 참여하고 있지 않을 때(매도 상태일 때)
        if not self.position:
            # RSI 수치가 30 미만이라면
            if self.rsi < 30:
                # 매수 주문
                self.order = self.buy()
        # 현재 시장에 참여하고 있을 때(매수 상태일 때)
        else:
            # RSI 수치가 70 미만이라면
            if self.rsi > 70:
                # 매도 주문
                self.order = self.sell()

    # 텍스트 메시지와 데이터프레임(기본값 None)을 인수로 받아 해당 날짜와 거래 내역 로그를 출력하는 메서드 정의
    def log(self, txt, dt=None):
        # dt에 데이터에 지정된 날짜 저장
        dt = self.datas[0].datetime.date(0)
        # 거래 날짜와 함께 거래 내역 로그를 출력
        print(f'[{dt.isoformat()}] {txt}')

# 데이터를 취합하여 백테스트 또는 라이브 트레이딩을 수행하는 Cerebro 객체 생성
cerebro = bt.Cerebro()
# Cerebro 객체에 정의한 전략 클래스 추가
cerebro.addstrategy(MyStrategy)
# 야후파이낸스에서 2020년~2023년 엔씨소프트 주가를 팬더스 데이터프레임으로 받아와 취합
data = bt.feeds.PandasData(dataname=yf.download('036570.KS', '2020-01-01', '2023-12-31', auto_adjust=True))
# 취합된 데이터를 Cerebro 객체에 추가
cerebro.adddata(data)
# 초가 투자 자금 1,000만원 설정
cerebro.broker.setcash(10000000)
# 수수료를 0.14%로 설정
# (주식 매도 시 0.25%가 증권거래세로, 주식 매수와 매도 시 약 0.015%를 증권거래수수료로 차감한다고 가정하여 매수/매도 시 0.28%, 거래 1번 당 0.14% 수수료로 책정)
cerebro.broker.setcommission(commission=0.0014)
# 매매 주문을 적용할 주식수를 퍼센트화하여 수수료를 차감한 90%로 설정
cerebro.addsizer(bt.sizers.PercentSizer, percents=90)

# 초기 포트폴리오 금액(자금) 출력
print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
# 설정된 주식 데이터, 자금, 전략으로 백테스트 수행
cerebro.run()
# 백테스트 수행 후 최종 포트폴리오 금액(자금) 설정
print(f'Final Portfolio Value   : {cerebro.broker.getvalue():,.0f} KRW')
# 백테스트 결과를 차트로 출력
cerebro.plot(style='candlestick')

# 백테스트 실행 결과

# 제일 위의 그래프는 자산 가치를 나타내는 파란 선과 현금을 나타내는 빨간 선으로 구성
# 우측 상단에 빨간 박스로 표시된 부분은 포트폴리오에서 남은 최종 현금을 의미

# 두 번째 그래프는 매매(매수/매도) 결과에 대한 수익 금액을 표시
# 파란 원은 수익을 나타내고 빨간 원은 손실을 나타냄
# 원의 높이가 수익 또는 손실의 크기

# 세 번째 그래프는 엔씨소프트의 주가 흐름을 캔들스틱으로 쇼피
# 매수 시점을 연두색 삼각형으로, 매도 시점을 빨간색 삼각형으로 표시

# 네 번째 그래프에서는 주가 흐름에 따른 상대적 강도 지수의 단순 이동 평균(RSI SMA) 표시