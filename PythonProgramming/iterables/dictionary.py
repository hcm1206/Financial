# 유전자 가위 기술(CRISPR)로 각광을 받는 미국 대표 기업들을 딕셔너리로 표현
crispr = {'EDIT' : 'Editas Medicine', 'NTLA' : 'Intellia Therapeutics'}

# 순서가 없으므로 시퀀스 자료형들처럼 인덱스로 값에 접근 불가
# 인터프리터는 딕셔너리를 키로 처리하기 때문에 인덱스로 접근 시 키 에러 발생
# print(crispr[1]) # 에러
print(crispr['NTLA'])

# 키와 값을 함께 지정하여 딕셔러니에 원소 추가
crispr['CRSP'] = 'CRISPR Therapeutics'
print(crispr)

# CRSP 종목을 추가한 딕셔너리 원소 개수는 3개
print(len(crispr))

print()

