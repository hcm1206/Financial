# 팬더스 시리즈 자료구조를 활용하기 위한 팬더스(pandas) 라이브러리 임포트
import pandas as pd

# 시리즈 생성

# 리스트로 시리즈 생성
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
print(s)

print()

# 시리즈의 인덱스 변경
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
# 인덱스명 설정
s.index.name = 'MY_IDX'
print(s)

print()

# 시리즈명 설정
s.name = 'MY_SERIES'
print(s)

# 데이터 추가
# 대괄호 []를 이용해서 인덱스 레이블과 인덱스에 해당하는 값을 한 번에 지정하여 시리즈에 값 추가
s[5.9] = 5.5
s[6.8] = 6.7
s[8.0] = 4.2

# =================== 이하 pandas 2.0 미만 버전에서만 동작 ===========================
# # 새로운 시리즈를 생성해서 append() 메서드로 데이터 추가 가능
# # 해당 방법의 경우 기존에 설정했던 시리즈명과 인덱스명이 사라짐

# # 추가할 ser 시리즈 생성
# ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
# # 기존 s 시리즈에 신규 ser 시리즈 추가
# s = s.append(ser)
# print(s)

# =================== 이상 pandas 2.0 미만 버전에서만 동작 ===========================

print()

# 데이터 인덱싱

# 시리즈의 마지막 데이터 인덱스 확인
print(s.index[-1])
# 시리즈의 마지막 데이터 확인
print(s.values[-1])
# 로케이션 인덱서(인덱스 값을 이용하여 데이터 접근)
print(s.loc[8.0])
# 인티저 로케이션 인덱서(위치를 나타내는 정수 인덱스 값을 이용하여 데이터 접근)
print(s.iloc[-1])
# values는 결괏값이 복수 개일 때 배열로 반환
print(s.values[:])
# iloc은 결괏값이 복수 개일 때 시리즈로 반환
print(s.iloc[:])

print()

# 데이터 삭제

# drop() 메서드에 원소의 인덱스 값을 인수로 넘겨서 해당 인덱스의 데이터 삭제
print(s.drop(8.0))
# 시리즈의 마지막 인덱스에 해당하는 데이터 삭제
print(s.drop(s.index[-1]))

# 마지막 원소를 삭제한 결과를 시리즈에 반영
s = s.drop(8.0)
print(s)

print()

# 시리즈 정보 보기

# 원소 개수, 평균, 표준편차, 최솟값, 제1 사분위수, 제2 사분위수(중앙값), 제3 사분위수, 최댓값 출력
print(s.describe())

print()

# 시리즈 출력하기

import pandas as pd

# 시리즈 생성 후 값 추가
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2])
# 시리즈에 인덱스 추가
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8, 5.9, 6.8, 8.0])
# 시리즈 인덱스명 설정
s.index.name = 'MY_IDX'
# 시리즈 이름 설정
s.name = 'MY_SERIES'

import matplotlib.pyplot as plt

# 그래프 제목 설정
plt.title("ELLIOTT_WAVE")
# 시리즈를 bs--(푸른 사각형과 점선) 형태로 출력
plt.plot(s, 'bs--')
# x축의 눈금값을 s 시리즈의 인덱스값으로 설정
plt.xticks(s.index)
# y축의 눈금값을 s 시리즈의 데이터값으로 설정
plt.yticks(s.values)
# 그래프에 격자 표시
plt.grid(True)
# 그래프 출력
plt.show()

print()