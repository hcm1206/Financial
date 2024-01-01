# if 조건문

# 상대강도지수(relative strength index, RSI)
# 시장이나 개별 주식이 과매수 상태인지 또는 과매도 상태인지를 판단하는데 도움을 주는 자료
# 상대강도지수가 70을 초과하면 과매수 상태, 30 미만이면 과매도 상태로 판단

rsi = 80
if rsi > 70:
    print('RSI', rsi, 'means overbought.')
elif rsi < 30:
    print('RSI', rsi, 'means oversold.')
else:
    print('...')

print()

# for 반복문

# 리스트를 이용한 반복문
for i in [1, 3, 5]:
    print(i)

print()

# range(시작값, 멈춤값, 증가값) 함수를 이용한 반복문
for i in range(1, 7, 2): 
    print(i)

print()

# enumerate(반복자료형, 인덱스 시작값) 함수를 이용한 반복문
FAANG = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']
for idx, symbol in enumerate(FAANG, 1):
    print(idx, symbol)

print()

# while 반복문
i = 1
while i < 7:
    print(i)
    i += 2

print()

# continue문 : 조건이 맞으면 나머지 코드를 실행하지 말고 다음 반복을 이어서 수행하라는 의미
# break문 : 코드 실행을 중단하고 가장 근접한 for, while문을 벗어나라는 의미

# while else와 for else문
# while과 for 반복문에 else 문을 같이 쓰면 반복을 종료하고 특정 문장 실행 가능
# 단, break문에 의해서 종료되면 실행되지 않음
i = 0
while i >= 0:
    i += 1
    if (i % 2) == 0:
        continue
    if i > 5:
        break
    print(i)
else:
    print('Condition is false.')

print()

# try except 예외 처리

# 0으로 나누기 연산 예외 처리를 통해 프로그램 종료 방지
try:
    1/0
except Exception as e:
    print('Exception occured :', str(e))

print()