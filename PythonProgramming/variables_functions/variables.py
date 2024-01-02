# 전역 변수와 지역 변수

# 전역 변수(global variable) : 함수 밖에서 선언되며 코드 전반에 걸쳐서 유효
# 지역 변수(local variable) : 함수 안에서 선언되며 해당 함수 내부에서만 유효

print()

# 내장 객체와 자료형

# type() 함수 : 변수형을 확인할 수 있는 내장 함수(built-in functions)
# 내장 클래스(built-in classes) : 정수(int), 실수(float), 문자열(str)

# 정수형 클래스
i = 3
print(type(i))
# 실수형 클래스
f = 1.0
print(type(f))
# 정수형과 실수형의 계산 결과는 실수형으로 처리
var = i * f
print('{} : {}'.format(var, type(var)))

print()

# 제한 없는 정수형

# 파이썬은 정수형(int 클래스) 크기에 제한이 없기 때문에 10의 100승을 나타내는 구골 같이 큰 수도 처리 가능
googol = 10 ** 100 # == pow(10, 100)
print(type(googol))
print(googol)

print()

# dir() 함수

# 인수 없는 dir() : 현재 파이썬 환경에서 사용 가능한 객체가 표시
# 인수 있는 dir() : 인수 객체가 갖고 있는 함수와 변수를 리스트 형태로 출력
s = 'string'
print(type(s))
print(dir(s))

print()

# 예약어
# 예약어 : 파이썬에서 변수명으로 사용할 수 없는 단어

# 예약어 출력
help('keywords')

print()