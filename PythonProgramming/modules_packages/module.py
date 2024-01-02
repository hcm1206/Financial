# help() 함수
# 표준 라이브러리 : 별도의 설치 없이 import 명령으로 바로 불러와서 사용 가능
# 외부 라이브러리 : 사용자가 직접 설치한 후 import 명령으로 불러와야 사용 가능

# 현재 PC에 설치된 모듈 목록 확인
# help('modules') # 너무 길어서 주석 처리

# 모듈 사용법 확인
# time 모듈 사용법 확인
# help('modules time') # 너무 길어서 주석처리

# 모듈명에 대한 상세 설명 표시
# datetime 모듈명에 대한 상세 설명 표시
# help('datetime') # 무시무시하게 길어서 주석처리

print()

# import
# 파이썬 모듈은 변수, 함수, 클래스를 포함할 수 있으며 import 예약어를 사용해 다른 모듈에 정의된 변수, 함수, 클래스 등을 사용 가능

# keyword 모듈을 임포트하여 파이썬 예약어 확인
import keyword
print(keyword.kwlist)

print()

# __file__ 속성
# 임포트한 모듈이나 패키지의 실제 파일 위치 확인
print(keyword.__file__)

print()

# from ~ import ~
# from 예약어 사용 시 실행 과정에서 from 다음에 지정한 패키지명이나 모듈명 생략 가능

# 'import 모듈명' 형식으로 calendar 모듈 임포트 시의 month() 메서드 호출
import calendar
print(calendar.month(2020, 1))

# 'from 모듈명 import 메서드명' 형식으로 임포트 시의 month() 메서드 호출
from calendar import month
print(month(2020, 1))

print()

# import ~ as ~
# as 예약어 사용 시 이름이 긴 모듈명을 프로그래머가 원하는 별칭으로 줄여서 사용 가능

# as와 from 미사용 시의 datetime 모듈 임포트
import datetime
print(datetime.datetime.now())

# as와 from 사용 시의 datetime 모듈 임포트
from datetime import datetime as dt
print(dt.now())

print()