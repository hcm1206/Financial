# 패키지는 여러 모듈(.py 파일)을 특정 디렉터리에 모아놓은 것
# 패키지명 뒤에 '.'을 뭍이고 모듈명 사용

# 패키지에 포함된 모듈 로드 후 모듈의 자료형 출력
import urllib.request
print(urllib.request)

print()

# 패키지의 경로 속성
# 패키지는 특별한 형태의 모듈로, 모든 패키지를 모듈이라 할 수 있으나 모든 모듈이 패키지는 아님
# 모듈 중 경로 속성을 갖는 것들이 패키지

# urllib 패키지(모듈) 임포트
import urllib
# urllib의 타입은 모듈로 출력
print(type(urllib))
# urllib에는 경로 속성이 존재(패키지)
print(urllib.__path__)
# urllib이 속한 패키지는 urllib로 출력
print(urllib.__package__)

print()

# __name__ 속성
# __name__ 속성은 단독으로 실행될 경우 __main__ 문자열이 되고 임포트하여 실행될 경우 실제 모듈명이 됨

# 모듈 A 임포트하여 __name__(모듈명) 출력
import myPackage.moduleA

# 모듈 A의 함수 A 실행
myPackage.moduleA.functionA()

print()

# __pycache__ 디렉터리
# 모듈 임포트 시 현재 디렉터리 하위에 '__pycache__' 디렉터리가 생성되어 그 안에 .pyc(Compiled Python File) 파일이 자동 생성
# 한 번 컴파일한 모듈을 .pyc 파일로 캐시(cache)해놓고, 다음 번에 모듈을 임포트할 때 컴파일 작업 없이 바로 .pyc 파일을 사용함으로써 속도 향상

print()

# __init__.py 패키지 초기화 파일
# 디럭터리에서 __init__.py 파일이 존재하면 해당 디렉터리를 패키지로 인식

# myPackage 패키지의 모듈 A 모듈 임포트
import myPackage.moduleA
# 모듈 A를 임포트하여 실행 시 모듈 A의 메인 함수 내용이 실행되지 않음
myPackage.moduleA.main()

# 파이썬의 선
# this 임포트 시 파이썬의 선(The Zen of Python) 전문이 출력
import this