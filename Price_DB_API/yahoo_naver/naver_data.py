# 네이버 금융 데이터로 시세 데이터베이스 구축하기

# 네이버 금융 데이터를 이용해 삼성전자 주식 데이터를 그래프로 그려 파악

# 필요 라이브러리 로드(Investar 패키지는 직접 구현)
import matplotlib.pyplot as plt
from Investar import Analyzer # 현재 미구현

# 시세 객체 로드 후 삼성전자의 2017년 7월 10일부터 2018년 6월 30일까지의 주식 데이터 로드
mk = Analyzer.MarketDB()
df = mk.get_daily_price('005930', '2017-07-10', '2018-06-30')

# 그래프 크기 설정
plt.figure(figsize=(9, 6))
# 2행 1열 영역 중 1행 1열로 설정
plt.subplot(2, 1, 1)
# 그래프 제목 설정
plt.title('Samsung Electronics (Investar Data)')
# x축을 데이터프레임 인덱스(날짜), y축을 삼성전자 종가로 하여 청록색 실선으로 그래프 출력
plt.plot(df.index, df['Close'], 'c', label='Close')
# 적당한 위치에 그래프 범례 출력
plt.legend(loc='best')
# 2행 1열 영역 중 2행 1열 설정
plt.subplot(2, 1, 2)
# x축을 데이터프레임 인덱스(날짜), y축을 삼성전자 거래량으로 하여 초록색 막대 그래프 출력
plt.bar(df.index, df['Volume'], color='g', label='Volume')
# 적당한 위치에 그래프 범례 출력
plt.legend(loc='best')
plt.show()

# 삼성전자가 2018년 5월 초에 액면 분할을 시행했기 때문에 액면 분할 이후의 거래량이 액면 분할 이전 거래량보다 월등하게 많음

print()