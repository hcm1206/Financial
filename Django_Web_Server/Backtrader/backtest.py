# 백테스트 : 특정 투자 전략을 실제로 시장에 적용해보기 전에 과거 데이터(historical data)를 사용해 해당 전략이 얼마나 효과적인지를 검증하는 데 사용
# 백테스트는 과거 데이터를 기반으로 테스트를 진행하기 때문에 백테스트의 결과가 미래에 동일하게 나온다는 보장이 없음
# 조금이라도 더 신뢰할 수 있는 결과를 얻으려면 최대한 긴 기간 동안 수집된 다량의 데이터를 이용해 검증

# 백테스트 소프트웨어의 기본 기능은 사용자가 입력한 초기 투자 금액을 과거의 지정된 기간 동안 사용자가 설정한 매매기법에 따라 운용했을 때 발생하는 최종 수익을 알려주는 것
# 백테스트 결과를 더 효율적으로 나타내기 위해서 여러 통계적 지표를 제공하기도 함
# CAGR(Compound Annual Growth Rates, 연평균 성장률)
# MDD(Maximum Drawdown, 최대 손실 낙폭)
# 상관계수(Coefficient of Correlation)
# 샤프지수(Sharpe Ratio)

# 백트레이더 라이브러리를 이용하여 백테스트 기능 구현
# www.backtrader.com