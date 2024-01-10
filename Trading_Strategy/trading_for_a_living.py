# 심리투자 법칙

# 성공적인 매매를 위한 세 가지 요소인 3M을 강조
# 정신(Mind) : 시장 노이즈에 휩쓸리지 않도록 해주는 원칙
# 기법(Method) : 시장 지표를 활용해 주가를 분석하고 이를 매매에 활용하는 기법
# 자금(Money) : 리스크를 거래의 일부로 포함시키는 자금 관리

print()

# 시장 지표

# 시장 지표(market indicator)는 크게 세 가지로 구분

# 추세(trend) 지표 : 이동평균, MACD 같이 시장의 흐름을 나타내는 지표
# 시장이 움직일 때는 잘 맞지만 시장이 횡보할 때 잘못된 신호 전송 가능

# 오실레이터(oscillator) : 스토캐스틱이나 RSI처럼 과거 일정 기간의 가격 범위 안에서 현재 가격의 상대적인 위치를 나타내는 지표
# 오실레이터는 횡보장에서 전환점을 포착하는데 적합하지만 가격보다 앞서 변하는 경향이 존재

# 기타 지표들은 강세장과 약세장에 따른 강도를 예측

# 시장지표의 분류

# 추세
# 발생 시점 : 동행 또는 후행
# 지표 : 이동평균(Moving Averages), 이동평균 수렴확산(MACD), MACD 히스토그램, 방향성 시스템(the Directional System),
# 거래량 균형 지표(On-Balance Volume, OBV), 누적분산 지표(Accumulation/Distribution, AD)

# 오실레이터
# 발생 시점 : 선행 또는 동행
# 지표 : 스토캐스틱(Stochastic), 변화율(Rate of Change), 평활화된 변화율(Smoothed RoC), 모멘텀(Momentum),
# 상대강도지수(Relative Strength Index, RSI), 엘더레이(Elder-ray), 강도지수(the Force Index), 윌리엄스(Williams %R),
# 상대가격변동폭(the Commodity Channel Index)

# 기타 지표
# 발생 시점 : 선행 또는 동행
# 지표 : 신고점-신저점 지수(New High-New Low Index), 풋-콜 비율(the Put-Call Ratio), 상승하락 지수(the Advance/Decline Index, A/D),
# 트레이더 지수(the Trader's Index, TRIN)

print()

# 단순 이동평균

# 단순 이동평균(simple moving averages, SMA) : 일정 기간 동안의 가격을 모두 더한 뒤 이를 가격 개수로 나누어 평균값을 구한 것
# 이동평균 값들을 선으로 이으면 이동평균선이 되며 이동평균선 진행 방향을 보면 전반적인 가격 흐름을 예측 가능
# 이동평균은 가장 오래된 가격이 제외되고 새로운 가격이 추가되면서 값이 달라짐
# 단순 이동 평균은 오래된 가격의 변동과 최근 가격의 변동을 동일하게 반영하므로 최근 가격의 변동이 왜곡될 가능성이 있음

print()

# 지수 이동평균

# 지수 이동평균(exponential moving averages, EMA) : 최근의 데이터에 가중치를 부여해 단순 이동평균에 비해서 최근의 데이터 변동을 잘 반영하도록 설계

# 지수 이동평균의 장점
# 최근 거래일에 더 많은 가중치를 주므로 최근 가격의 변동을 더 잘 나타냄
# 오래된 지수 이동평균 데이터가 천천히 사라지므로 오래된 데이터가 빠져나갈 때 지수 이동평균이 급등락하지 않음

# 지수 이동평균선이 오르면 추세가 상승하고 있음을 나타내므로 매수 측에서 매매해야 함
# 지수 이동평균선이 내리고 있다면 매도 측에서 매매하는 것이 좋음

print()

# 이동평균 수렴확산(MACD)

# 이동평균 수렴확산(Moving Average Convergence Divergence, MACD) : 세 가지 지수 평균선을 이용해 개발

# MACD 차트에서는 두 선으로 표시되는데, 하나는 MACD선(실선)이고 다른 하나는 신호선(점선)으로, 이 두 선의 교차점에서 매매 신호가 발생
# MACD선 : 종가의 12일 지수 이동평균선에서 26일 지수 이동평균선을 뺀 것으로 가격 변화에 상대적으로 빨리 반응
# 신호선 : MACD선의 9일 지수 이동평균을 구한 선으로 MACD선을 평활화시킨 것이기 때문에 변화에 상대적으로 늦게 반응

# 빠른 MACD선이 늦은 신호선을 상향 돌파하는 것은 매수세가 시장을 주도한다는 뜻이므로 매수적 관점에서 대응
# 빠른 MACD선이 늦은 신호선을 하향 돌파할 때는 매도 관점에서 대응

print()

# MACD 히스토그램

# MACD 히스토그램(MACD Histogram) : 원래의 MACD보다 매수와 매도 상태를 더 잘 표현
# 단순히 매수와 매도의 비중을 표시할 뿐이 아니라 강해지고 있는지 약해지고 있는지를 보여줌

# MACD 히스토그램의 기울기를 확인하는 것은 히스토그램이 중심선(0) 위에 있는지 아니면 아래에 있는지 확인하는 것보다 중요
# 현재 봉이 이전 봉보다 높다면 기울기는 올라가고 있으므로 매수
# 최고의 매수 신호는 MACD 히스토그램이 중심선 아래에 있고, 기울기가 상향 반전하고 있을 때 발생

# MACD 히스토그램과 가격과의 다이버전스는 일 년에 몇 번만 일어나며 기술적 분석에서 가장 강력한 신호
# 가격이 신저점까지 낮아졌으나 MACD 히스토그램이 저점에서 상승하기 시작했다면 강세 다이버전스(bullish divergence)가 형성됨을 의미
# 가격이 신저점을 갱신하면서 MACD 히스토그램도 낮아지고 있다면 단순 하향추세 신호

print()

# 스토캐스틱

# 스토캐스틱(Stochastic) : 지난 n일 동안의 거래 범위에서 현재 가격 위치를 백분율로 표시
# 14일 스토캐스틱이 70이면 지난 14일간 거래에서 최저점과 최고점 사이 70%에 위치해 있다는 의미
# 일반적으로 80 이상은 과매수 상태를 나타내고 20 이하는 과매도 상태를 의미

# 스토캐스틱은 두 선으로 이루어져 있으며 빠른 선은 %K, 느린 선은 %D
# 일반적으로 %K의 기간은 14일로 설정
# 느린선 %D는 빠른 선 %K를 평활화해 확보

# 스토캐스틱은 시장이 박스권에서 움직일 때는 잘 작동하지만 시장이 추세에 들어갈 때는 잘 작동하지 않음
# 시장이 상승 추세에 들어가면 스토캐스틱은 일찍 과매수 상태로 판단해서 매도 신호를 보내지만 시장은 계속 상승 가능
# 반대로 시장이 하락 추세에 들어가면 스토캐스틱은 일찍 과매도 상태로 판단해서 매수 신호를 보내지만 시장은 계속 하락 가능

# 스토캐스틱은 장기 추세 추종형 지표와 겨합하여 사용

print()