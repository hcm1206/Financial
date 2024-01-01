# 파이썬 프로그램 성능 측정 라이브러리 로드
import timeit

# 순회 속도 비교
# 0~9999 정수 1만개를 원소로 갖는 각 반복 자료형을 생성하여 원소 순회 동작 1000회 반복하여 걸린 시간 계산

# 원소 순회 코드 설정
iteration_test = """
for i in itr:
    pass
"""
# 10000개 원소 리스트의 순회를 1000번 반복한 시간 계산하여 출력
print(timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000))
# 10000개 원소 튜플의 순회를 1000번 반복한 시간 계산하여 출력
print(timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=1000))
# 10000개 원소 셋의 순회를 1000번 반복한 시간 계산하여 출력
print(timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=1000))

# 순회 속도에 큰 차이는 없음

print()

# 검색 속도 비교
# 0~9999 사이의 임의 난수 생성 후 0~9999 정수 1만개로 구성된 각 반복 자료형에 존재하는지 검색

# 원소 검색 코드 설정
search_test = """
import random
x = random.randint(0, len(itr)-1)
if x in itr:
    pass
"""

# 10000개 원소 셋의 검색을 1000번 반복한 시간 계산하여 출력
print(timeit.timeit(search_test, setup='itr = set(range(10000))', number=1000))
# 10000개 원소 리스트의 검색을 1000번 반복한 시간 계산하여 출력
print(timeit.timeit(search_test, setup='itr = list(range(10000))', number=1000))
# 10000개 원소 튜플의 검색을 1000번 반복한 시간 계산하여 출력
print(timeit.timeit(search_test, setup='itr = tuple(range(10000))', number=1000))

# 난수 검색 작업을 1000번씩 반복 수행한 결과 셋이 가장 성능이 빠름

print()