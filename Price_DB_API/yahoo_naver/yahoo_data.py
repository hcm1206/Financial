# 야후 파이낸스 데이터의 문제점

# 야후 파이낸스 데이터를 이용해 삼성전자 종가, 수정종가, 거래량을 그래프로 그려 파악

# 필요한 라이브러리 임포트
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

# 2017년 1월 1일 이후 삼성전자 주가 데이터 로드
df = pdr.get_data_yahoo('005930.KS', '2017-01-01')

# 그래프 크기 설정
plt.figure(figsize=(9, 6))
# 2행 1열 영역 중 1행 1열로 설정
plt.subplot(2, 1, 1)
# 그래프 제목 설정
plt.title('Samsung Electronics (Yahoo Finance)')
# x축을 데이터프레임 인덱스(날짜), y축을 삼성전자 종가로 하여 청록색 실선으로 그래프 출력
plt.plot(df.index, df['Close'], 'c', label='Close')
# x축을 데이터프레임 인덱스(날짜), y축을 삼성전자 수정 종가로 하여 파란색 점선으로 그래프 출력
plt.plot(df.index, df['Adj Close'], 'b--', label='Adj Close')
# 적당한 위치에 그래프 범례 출력
plt.legend(loc='best')
# 2행 1열 영역 중 2행 1열로 설정
plt.subplot(2, 1, 2)
# x축을 데이터프레임 인덱스(날짜), y축을 삼성전자 거래량으로 하여 초록색 막대 그래프 출력
plt.bar(df.index, df['Volume'], color='g', label='Volume')
# 적당한 위치에 그래프 범례 출력
plt.legend(loc='best')
plt.show()

# 야후 파이낸스 데이터는 종가와 수정 종가가 정확하지 않을 수 있고, 한국 주식 종목의 일부 데이터가 비어있을 수 있는 문제점 존재

print()