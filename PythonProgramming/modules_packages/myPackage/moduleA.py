# 모듈 A 파일

# 모듈 A의 함수 A
def functionA():
    print('FUNCTION_A')

# 모듈 실행 시 name 속성 출력
print('MODULE_A :', __name__)

# 메인 함수 정의
def main():
    print('MAIN_A :', __name__)

# 모듈이 단독으로 실행되었을 경우 name 속성은 main 문자열로 변경
    
# 현재 모듈이 단독 실행되었다면 메인 함수 실행
if __name__ == '__main__':
    main()
