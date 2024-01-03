# 일간 변동률 누적곱 구하기

# 종목별로 전체적인 변동률을 비교하기 위해 일간 변동률의 누적곱(Cumulative Product) 계산
# 일간 변동률 데이터 중 0이 존재할 경우 전체 누적곱의 계산 결과도 0이 되므로 이를 피하기 위해 일간 변동률에 100을 더하여 계산

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# 삼성전자 주식 시세 데이터 로드
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
# 삼성전자 주식 시세 일간 변동률 계산
sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
# 일간 변동률 첫 번째 값인 NaN을 0으로 변경
sec_dpc.iloc[0]
# 삼성전자의 일간 변동률 누적곱 계산
sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100

# 마이크로소프트 주식 시세 데이터 로드
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
# 마이크로소프트 주식 시세 일간 변동률 계산
msft_dpc = (msft['Close'] / msft['Close'].shift(1) -1)*100
# 일간 변동률 첫 번째 값인 NaN을 0으로 변경
msft_dpc.iloc[0] = 0
# 마이크로소프트의 일간 변동률 누적곱 계산
msft_dpc_cp = ((100+msft_dpc)/100).cumprod()*100-100

# 일간 변동률 누적곱을 그래프로 표현

import matplotlib.pyplot as plt
# 삼성전자 일간 변동률 누적곱을 파란색 실선으로 그래프에 표시
plt.plot(sec.index, sec_dpc_cp, 'b', label='Samsung Electronics')
# 마이크로소프트 일간 변동률 누적곱을 빨간색 실선으로 그래프에 표시
plt.plot(msft.index, msft_dpc_cp, 'r--', label='Microsoft')
# y축 라벨 설정
plt.ylabel('Change %')
# 그래프 격자 표시
plt.grid(True)
# 적절한 위치에 범례 표시
plt.legend(loc='best')
plt.show()