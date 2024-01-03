# 딕셔너리를 이용한 데이터프레임 생성

import pandas as pd

# KOSPI 지수와 KOSDAQ 지수를 이용한 데이터프레임 생성
df = pd.DataFrame({'KOSPI' : [1915, 1961, 2026, 2467, 2041],
                   'KOSDAQ': [542, 682, 631, 798, 675]})
print(df)

print()

# 데이터프레임에 각 연도를 인덱스로 추가
df = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 2467, 2041],
                   'KOSDAQ': [542, 682, 631, 798, 675]},
                   index=[2014, 2015, 2016, 2017, 2018])
print(df)

print()

# 데이터프레임 객체에 포함된 데이터의 전체적인 모습 확인
# 원소의 개수, 평균, 표준편차, 최솟값, 제1 사분위수, 제2 사분위수(중앙값), 제3 사분위수, 최댓값 출력
print(df.describe())

print()

# 데이터프레임의 인덱스 정보, 칼럼 정보, 메모리 사용량 등 확인
df.info()

print()

# 시리즈를 이용한 데이터프레임 생성

# KOSPI 지수에 대한 시리즈 생성
kospi = pd.Series([1915, 1962, 2026, 2467, 2041],
                  index=[2014, 2015, 2016, 2017, 2018], name='KOSPI')
print(kospi)

print()

# KOSDAQ 지수에 대한 시리즈 생성
kosdaq = pd.Series([542, 682, 631, 798, 675],
                   index=[2014, 2015, 2016, 2017, 2018], name='KOSDAQ')
print(kosdaq)

print()

# 생성된 두 시리즈를 딕셔너리 형태로 구성하여 데이터프레임의 생성자로 넘겨 데이터프레임 생성
df = pd.DataFrame({kospi.name: kospi, kosdaq.name: kosdaq})
print(df)

print()

# 리스트를 이용한 데이터프레임 생성

# 데이터프레임 컬럼명 리스트 설정
columns = ['KOSPI', 'KOSDAQ']
# 데이터프레임 인덱스 리스트 설정
index = [2014, 2015, 2016, 2017, 2018]
# 데이터프레임의 실제 데이터를 담을 빈 리스트 설정
rows = []
# 각 행에 해당하는 데이터들을 리스트로 각각 추가
rows.append([1915, 542])
rows.append([1961, 682])
rows.append([2026, 632])
rows.append([2467, 798])
rows.append([2041, 675])
# 데이터프레임의 생성자에 데이터, 컬럼명, 인덱스를 생성자로 넘겨 데이터프레임 생성
df = pd.DataFrame(rows, columns=columns, index=index)

print()

# 데이터프레임 순회 처리

# 인덱스를 사용하여 데이터 프레임 순회
for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])

print()

# itertuples() 메서드를 이용해 데이터프레임의 각 행을 이름있는 튜플로 반환하며 순회
for row in df.itertuples(name='KRX'):
    print(row)

print()

# itertupe() 메서드를 이용해 순회 및 각 튜플의 값을 분리하여 출력
for row in df.itertuples():
    print(row[0], row[1], row[2])

print()

# iterrows() 메서드를 이용한 순회
# 데이터프레임의 각 행을 인덱스와 시리즈의 조합으로 반환하며, itertuples() 메서드보다는 느림
for idx, row in df.iterrows():
    print(idx, row[0], row[1])

print()