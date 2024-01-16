# 상대적 강도 지수

# 상대적 강도 지수(relative strength index, RSI) : 가격의 움직임의 강도를 백분율로 나타내어 언제 추세가 전환될지 예측하는데 유용
# RS = N일간의 상승폭 평균/N일간의 하락폭 평균
# RSI = 100 - (100 / (1 + RS))
# 일반적으로 RSI가 70 이상일 때 과매수(overbought) 구간으로 보고 매도 시점으로 해석
# RSI가 30 이하일 때 과매도(oversold) 구간으로 보고 매수 시점으로 해석

# 백트레이더 라이브러리를 이용하여 엔씨소프트 종가 정보를 취합한 후 천만 원의 초기 투자 금액으로 RSI 지표에 따라 매매했을 때의 백테스트 결과를 출력

# 필요한 라이브러리 임포트
from datetime import datetime
import backtrader as bt
import yfinance as yf

# bt.Strategy 클래스를 상속받아 새로운 전략 클래스 생성
class MyStrategy(bt.Strategy):
    # 클래스 생성자 정의
    def __init__(self):
        # 데이터의 종가를 지표로 사용하는 RSI 객체 생성
        self.rsi = bt.indicators.RSI(self.data.close)

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
            # RSI 수치가 70 이상이라면
            if self.rsi > 70:
                # 매도 주문
                self.order = self.sell()

# 데이터를 취합하여 백테스트 또는 라이브 트레이딩을 수행하는 Cerebro 객체 생성
cerebro = bt.Cerebro()
# Cerebro 객체에 정의한 전략 클래스 추가
cerebro.addstrategy(MyStrategy)
# 야후파이낸스에서 2020년~2023년 엔씨소프트 주가를 팬더스 데이터프레임으로 받아와 취합
data = bt.feeds.PandasData(dataname=yf.download('036570.KS', '2020-01-01', '2023-12-31', auto_adjust=True))
# 취합된 데이터를 Cerebro 객체에 추가
cerebro.adddata(data)
# 초기 투자 자금 1,000만원 설정
cerebro.broker.setcash(10000000)
# 주식 매매 단위를 30주로 설정
cerebro.addsizer(bt.sizers.SizerFix, stake=30)

# 초기 포트폴리오 금액(자금) 출력
print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
# 설정된 주식 데이터, 자금, 전략으로 백테스트 수행
cerebro.run()
# 백테스트 수행 후 최종 포트폴리오 금액(자금) 출력
print(f'Final Portfolio Value   : {cerebro.broker.getvalue():,.0f} KRW')
# 백테스트 결과를 차트로 출력
cerebro.plot()

# 출력된 그래프에서 연두색 상향 삼각형은 RSI 전락에 따른 매수 시점, 빨간색 하향 삼각형은 매도 시점을 의미