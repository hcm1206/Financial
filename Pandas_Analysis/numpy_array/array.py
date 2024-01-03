# 배열을 사용하기 위한 넘파이(numpy) 라이브러리 임포트
import numpy as np

# 배열 생성

# 2차원 리스트를 이용해 2차원 넘파이 배열 생성
A = np.array([[1, 2], [3, 4]])
print(A)

print()

# 배열 정보 보기

# 넘파이 배열의 클래스(자료형) 확인
print(type(A))
# 배열 차원 확인
print(A.ndim)
# 배열 크기 확인
print(A.shape)
# 배열의 원소 자료형 확인
print(A.dtype)
# 배열의 원소별 최댓값, 평균값, 최솟값, 합계 계산
print(A.max(), A.mean(), A.min(), A.sum())

print()

# 배열의 접근

# 배열 요소는 대괄호로 접근하며, 인덱싱과 슬라이싱 활용
print(A[0]); print(A[1])
# 배열 원소 접근법 1 : A[행 인덱스][열 인덱스]
print(A[0][0], A[0][1]); print(A[1][0], A[1][1])
# 배열 원소 접근법 2 : A[행 인덱스, 열 인덱스]
print(A[0, 0], A[0, 1]); print(A[1, 0], A[1, 1])
# 조건에 맞는 원소들만 인덱싱(A 배열 원소 중 1보다 큰 것만 출력)
print(A[A>1])

print()

# 배열 형태 바꾸기

# 전치(transpose) : 배열의 요소 위치를 주대각선(왼쪽 위→오른쪽 아래를 잇는 선)을 기준으로 뒤바꾸는 것
# A 배열 전치
print(A)
print(A.T)
print(A.transpose())

# 평탄화 : 다차원 배열을 1차원 배열 형태로 변환
print(A)
print(A.flatten())

print()

# 배열의 연산
# 같은 크기의 행렬끼리 사칙 연산 가능
# 원소별(element -wise) 연산 : 두 행렬에서 같은 위치에 있는 원소끼리 연산하는 것

print(A)
# 덧셈 연산
print(A + A)
print(np.add(A, A))
# 뺄셈 연산
print(A - A)
print(np.subtract(A, A))
# 곱셈 연산
print(A * A)
print(np.multiply(A, A))
# 나눗셈 연산
print(A / A)
print(np.divide(A, A))

print()

# 브로드캐스팅
# 브로드캐스팅(broadcasting) : 행렬 크기가 달라도 연산이 가능하도록 작은 행렬을 확장해주는 넘파이 기능

# 2×2 크기 행렬 A와 1×2 크기 행렬 B를 브로드캐스팅을 이용하여 곱하기 연산 수행
print(A)
B = np.array([10, 100])
print(A * B)

print()

# 내적 구하기
# 행렬 A가 m × k 행렬이고 행렬 B가 k × n 행렬일 때 행렬 A와 행렬 B를 곱한 행렬 C는 m × n 크기 행렬
# 행렬 A의 i행과 행렬 B의 j열의 내적(inner product) : 행렬 C의 i행 j열에 해당하는 원소

# 내적 곱은 크기가 같은 행 벡터와 열 벡터에 대해 정의되지만 넘파이에서는 1차원 배열끼리 내적 곱 계산 가능
# 1차원 배열끼리 내적 곱 계산 시 앞에 오는 배열을 행 벡터, 뒤에 오는 배열을 열 벡터로 가정
# 1차원 벡터끼리의 내적 계산
print(B.dot(B))
print(np.dot(B, B))

# 2차원 행렬끼리의 내적 계산(2 × 2 크기 행렬 A, 2 × 1 크기 행렬 B)
print(A.dot(B))
print(np.dot(A, B))

print()