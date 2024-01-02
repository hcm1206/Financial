# 들여쓰기

# 파이썬에서 함수 작성 시 예약어 def를 사용하며 반드시 들여쓰기를 포함
# 들여쓰기(indentation)는 탭 문자나 스페이스 문자를 조합하여 사용
# 코드 레벨에 맞게 들여쓰기를 하지 않으면 에러 발생

print()

# 연평균 성장률(CAGR) 계산
# CAGR(Compound Annual Growth Rates) : '복합 연평균 성장률' 또는 '연복리 수익률'
# CAGR은 1년 동안 얼마 만큼씩 증가하는지를 나타내는 값
# 주로 투자 수익률을 표시하는데 사용되지만 판매수량이나 사용자 증가율 등을 나타낼 때도 사용

# CAFR 계산 함수(처음 값, 마지막 값, 처음 값과 마지막 값 사이 연(year) 수)
def getCAGR(first, last, years):
    return (last/first)**(1/years) - 1

# 삼성전자는 1998년 4월 27일 65,300원이던 주가가 액면 분할 직전인 2018년 4월 27일 2,669,000원이 되기까지 정확이 20년 동안 4,087%로 상승
cagr = getCAGR(65300, 2669000, 20)
print("SEC CAGR : {:.2%}".format(cagr))
# 연평균 성장률 계산 결과는 20.38%

print()

# None 반환값
# 함수를 정의할 때 반환값 미지정 시 None 반환

# 반환값 없는 함수
def func1():
    pass

# 아무것도 반환하지 않는 함수
def func2():
    return

# None을 반환하는 함수
def func3():
    return None

# 모두 None을 반환하는 함수
print(func1()); print(func2()); print(func3())

print()

# None 타입 출력
print(type(None))

# 함수의 None 반환 여부 출력
print(func1() == None)
print(func1() is None)

print()

# 함수, 프로시저, 메서드
# 일부 프로그래밍 언어에서는 결괏값을 반환하는 것을 함수로, 결괏값을 반환하지 않는 것을 프로시저(procedure)로 구분
# 파이썬에서는 클래스에 속하지 않는 함수를 함수로, 클래스에 속하는 함수로르 메서드(method)로 구분해서 사용

print()

# 여러 결괏값 반환
# 파이썬은 함수에서 여러 결괏값을 튜플 형태로 한번에 반환 가능

# 문자열, 리스트, 함수를 튜플 형태로 반환하는 함수
def myFunc():
    var1 = 'a'
    var2 = [1, 2, 3]
    var3 = max
    return var1, var2, var3

print(myFunc())

# 람다
# 람다(lambda)는 이름 없는 간단한 함수를 만들 때 사용

# 람다를 통해 천 단위 숫자에 쉼표 삽입
insertComma = lambda x : format(x, ',')
print(insertComma(1234567890))

print()

# 내장 함수 리스트
# 파이썬의 내장 함수명이나 내장 클래스명을 변수명으로 사용하면 문법 오류가 발생하지는 않지만 해당 내장 객체 호출 불가

# abs 변수 선언 후 abs() 함수 호출 시 에러 발생
abs = 1
# abs(-100) # 에러 발생

print()