# 셋은 중복을 허용하지 않으므로 원소를 중복해서 생성해도 해당 원소는 하나만 존재
s = {'A', 'P', 'P', 'L', 'E'}
print(s)

print()

# 셋은 생성한 순서대로 원소가 저장되지 않음
mySet = {'B', 6, 1, 2}
print(mySet)

print()

# 셋 내부에 특정 원소가 존재하는지 검사
if 'B' in mySet:
    print("'B' exists in", mySet)

print()

# 셋의 원소들은 인덱싱이 불가능하지만 원소들의 교집합, 합집합, 차집합 계산 가능
# 셋 2개(setA, setB) 생성
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}

# setA와 setB의 교집합
print(setA & setB)
# setA와 setB의 합집합
print(setA | setB)
# setA에서 setB의 차집합
print(setA - setB)
# setB에서 setA의 차집합
print(setB - setA)

print()

# 교집합, 합집합, 차집합을 함수로 계산 가능

# setA와 setB의 교집합
print(setA.intersection(setB))
# setA와 setB의 합집합
print(setA.union(setB))
# setA에서 setB의 차집합
print(setA.difference(setB))
# setB에서 setA의 차집합
print(setB.difference(setB))

print()

# 셋은 리터럴로 원소가 없는 상태에서 생성 불가

# 빈 리스트 생성
ls = []
ls = list()
# 빈 딕셔너리 생성
d = {}
d = dict()
# 빈 튜플 생성
t = ()
t = tuple()
# 빈 셋 생성
s = set()

print()

# 중복 없는 셋의 특징을 이용하여 리스트에서 중복 원소 제거 가능
ls = [1, 3, 5, 2, 2, 3, 4, 2, 1, 1, 1, 5]
print(list(set(ls)))

print()