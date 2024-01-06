# 파이마이에스큐엘로 버전 정보 확인하기

# 마리아DB 설치 및 세팅 완료 후 
# 파이썬 프로그램 내부에서 마리아디비를 사용하기 위해 파이마이에스큐엘 라이브러리 필요

# 커밋(commit) : 데이터베이스에서 변경된 내역을 영구적으로 확정하는 것
# 파이마이에스큐엘의 connection 객체의 autocommit 속성은 기본적으로 False
# connection.commit() 함수를 호출해야 실제로 데이터베이스에 반영

# 파이마이에스큐엘을 통해 마리아 DB에 연결

import pymysql

# 포트, DB, 사용자, 패스워드 등의 인수를 넘기어 마리아 DB에 접속하기 위한 커넥션 객체 생성
connection = pymysql.connect(host='localhost', port=3306, db='INVESTAR', user='root', passwd='password', autocommit=True)

# DB를 조작하기 위한 커서 객체 생성
cursor = connection.cursor()
# MariaDB 버전을 반환하는 SELECT SQL문 실행
cursor.execute("SELECT VERSION();")
# 커서 객체 실행 결과를 튜플로 받아옴
result = cursor.fetchone()

# 실행 결과 출력
print("MariaDB version : {}".format(result))

# MariaDB 연결 종료
connection.close()

print()