# 출력할 문자열이 저장된 딕셔너리 생성
crispr = {'EDIT' : 'Editas Medicine', 'NTLA' : 'Intellia Therapeutics', 'CRSP' : 'Intellia Therapeutics'}

# % 기호 방식
# % 기호 다음에 특정 문자를 사용하여 출력 형식을 지정
for x in crispr:
    print('%s : %s' % (x, crispr[x]))

print()

# {} 기호 방식
# {} 기호를 사용하여 format() 함수에 주어진 인수의 자료형에 맞게 자동으로 출력
for x in crispr:
    print('{} : {}'.format(x, crispr[x]))

print()

# f-strings 방식
# {} 안에 출력할 값과 포맷 형식을 지정하여 출력
for x in crispr:
    print(f'{x} : {crispr[x]}')

print()