# str 문자열 클래스

# 문자열 출력
print("Hello, world!")
# 따옴표 상관없이 모두 str 클래스
print(type('Hello, world!'))
print(type("Hello, world!"))

print()

# 이스케이프 문자

# 이스케이프 문자로 인한 출력 오류
print('C\windows\System32\notepad.exe')
# raw string으로 출력하는 방법
print(r'C:\Windows\System32\notepad.exe')

# 따옴표를 이스케이프 문자를 이용하여 출력
print('\"It\'s not that I\'m so smart; it\'s just that I stay with problems longer.\" Albert Einstein')
# 따옴표 3개를 문자열 출력에 사용
print('''"It's not that I'm so smart; it's just that I stay with problems longer." Albert Einstein''')
# 여러 줄에 걸친 문자열을 따옴표 3개를 이용하여 출력
print('''Wake up, Neo...
The MAtrix has you...
Follow the white rabbit.''')

print()

# 인덱싱

# 문자열 생성
word = 'Python'
# 문자열 길이 출력
print(len(word))
# 각 문자열 인덱스 값 출력
print(word[0] + word[1] + word[2] + word[3] + word[4] + word[5])
# 각 문자열 음수 인덱스 값 출력
print(word[-6] + word[-5] + word[-4] + word[-3] + word[-2] + word[-1])

print()

# 슬라이싱

# 문자열 생성
word = 'Python'
# 0부터 6미만 인덱스의 문자열 부분 출력
print(word[0:6])
# 0번째 인덱스에 해당하는 문자(P)부터 표시
print(word[0:])
# 5번째 인덱스에 해당하는 문자(n)까지 표시
print(word[:6])
# -2번째 인덱스에 해당하는 문자(o)까지 표시
print(word[:-1])