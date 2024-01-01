# 튜플은 다른 리스트나 내장함수도 원소로 보유 가능
myTuple = ('a', 'b', 'c', [10, 20, 30], abs, max)

# 인덱싱을 사용하여 4번째 원소인 리스트 출력
print(myTuple[3])

# 5번째 원소인 내장함수 abs()에 -100을 파라미터로 전달
print(myTuple[4](-100))

# 6번째 원소인 내장함수 max()에 리스트를 파라미터로 전달
print(myTuple[5](myTuple[3]))

# 튜플의 첫 번째 원소에 새로운 값을 대입하려 하면 '튜플 객체는 원소 할당(item assignment)를 지원하지 않는다'는 메시지와 함께 타입 에러 발생
# myTuple[0] = 'A' # 에러

print()