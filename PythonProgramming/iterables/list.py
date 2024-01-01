# 리스트 생성
ls = ['one', 'two', 'three', 4, 5, 6]

# 인덱스를 통한 리스트 원소 접근
print(ls[0])
print(ls[-1])

print()

# 리스트를 원소로 갖는 리스트
L = [[1, 2], [3, 4]]

# 중첩 리스트의 원소 접근
print(L[0])
print(L[1])

print()

# 인덱스를 여러 번 사용하여 중첩 리스트 내부 원소 접근
print(L[0][0])
print(L[0][1])
print(L[1][0])
print(L[1][1])

print()

# 덧셈 연산자를 이용하여 리스트 뒤에 리스트 추가
print(L + L)

print()

# 곱셈 연산자를 이용하여 리스트를 반복하여 표시
print(L * 3)

print()

# split() 함수
# 인수로 주어진 문자열을 구별자로 사용하여 분리
# 구별자 미지정 시 공백 문자를 기준으로 분리
# 분리된 문자열은 리스트로 반환

myList = 'Thoughts become things'.split()
print(type(myList))
print(myList)

print()

# join() 함수
# 인수로 주어진 리스트를 하나의 문자열로 결합

# 원소들을 공백 문자로 연결하여 문자열 하나로 생성
print(myList)
print(' '.join(myList))

print()

# sort() 함수
# 리스트를 직접 정렬하고 None을 반환
# 리스트에서만 사용 가능
li = [2, 5, 3, 1, 4]
li.sort()
print(li)

print()

# sorted() 함수
# 리스트 뿐만 아니라 문자열, 튜플, 딕셔너리 등 반복 가능한 자료형에 모두 사용 가능
# 기본 리스트를 복사해서 새로 만들어 반환하므로 sort() 함수보다 느리며 기존 리스트에 영향 없음
li = [4, 3, 1, 2, 5]
print(sorted(li))
print(li)

print()

# append() 함수
# append() 함수는 넘겨받은 인수의 자료형에 상관없이 리스트 뒤에 그대로 추가

L = [1, 2]
L.append([3, 4])
print(L)

print()

# extend() 함수
# extend() 함수는 넘겨받은 인수가 반복 자료형일 경우, 반복 자료형 내부의 각 원소를 추가
L = [1, 2]
L.extend([3, 4])
print(L)

print()

# 구분자 변경하기

# 날짜 문자열을 구분자 '/'를 기준으로 리스트로 분리 후 다시 문자열로 합치면서 구분자 '-'로 연결
print('-'.join('2012/01/04'.split('/')))
# 문자열에서 특정 문자를 변경하는 replace() 함수를 사용하여 동일한 동작 가능
print('2012/01/04'.replace('/', '-'))

print()

# 천 단위 숫자를 쉼표로 구분하기

# split() 함수와 join() 함수를 이용하여 천 단위로 구분된 숫자에서 쉼표를 제거
print(''.join('1,234,567,890'.split(',')))
# replace() 함수를 이용하여 동일한 동작
print('1,234,567,890'.replace(',', ''))
# format() 함수를 이용하여 숫자를 천 단위마다 쉼표로 분리해 문자열 형태로 표시
print(format(1234567890, ','))

print()

# 리스트 복사

# 리스트는 문자열과 같이 인덱싱과 슬라이싱이 가능하며 len() 함수를 비롯한 여러 내장 함수 사용 가능
# [:]를 사용하면 리스트 복사 가능
myList = ['Thoughts', 'become', 'things.']
newList = myList[:]
print(newList)

# [:]를 이용하여 리스트를 복사한 경우 새로운 리스트를 변경하더라도 기존 리스트는 변경되지 않음(얕은 복사)
newList[-1] = 'actions'
print(newList)
print(myList)

print()

# 리스트 내포
# 내포(comprehension) 기능을 통해 리스트, 딕셔너리, 셋 같은 열거형 객체의 전체 또는 일부 원소를 변경하여 새로운 열거형 객체 생성 가능

# for 반복문을 사용해서 리스트의 모든 원소에 대하여 제곱 계산
nums = [1, 2, 3, 4, 5]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

# 리스트 내포를 이용하여 리스트의 모든 원소에 대하여 제곱 계산
nums = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in nums]
print(squares)

# 리스트에서 조건에 맞는 원소만 골라서 가공한 뒤 새로운 리스트로 생성할 때 편리하게 사용 가능
# 결과가 짝수일 때만 원소로 저장
nums = [1, 2, 3, 4, 5]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

print()