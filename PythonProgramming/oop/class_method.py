# 클래스 변수와 인스턴스 변수
# 클래스 변수(class variable) : 클래스 내부에 존재하면서 메서드 밖에 정의된 변수, 클래스의 모든 인스턴스는 클래스 변수를 공유
# 인스턴스 변수(instance variable) : 메서드 내부에서 정의되며 변수명 앞에 self가 붙으며 해당 인스턴스에서만 사용 가능한 변수

# 클래스 메서드
# 클래스 메서드 : 클래스 내부에 정의된 함수

# __init__ 생성자
# __init__ 함수 : 클래스 인스턴스가 생성될 떄 자동으로 호출되는 메서드로서 생성자(constructor)라고 함

# __del__ 소멸자
# __del__ 함수 : 인스턴스가 메모리에서 제거될 때 자동으로 호출되는 함수로서 소멸자(descructor)라고 함

# 나스탁주식 클래스 정의
class NasdaqStock: 
    # 독스트링
    """Class for NASDAQ stocks"""
    # 클래스 변수 정의
    count = 0
    # 클래스 생성자 정의
    def __init__(self, symbol, price):
        # 독스트링
        """Constructor for NasdaqStock"""
        # 인스턴스 변수
        self.symbol = symbol
        # 인스턴스 변수
        self.price = price
        # 클래스 변수 1 증가
        NasdaqStock.count += 1
        # 생성자 호출과 인스턴스 변수와 클래스 변수 출력
        print('Calling __init__({}, {:.2f}) > count: {}'.format(self.symbol, self.price, NasdaqStock.count))

    # 클래스 소멸자 정의
    def __del__(self):
        # 독스트링
        """Destructor for NasdaqStock"""
        # 소멸자 호출 출력
        print('Calling __del__{}'.format(self))

# 구글 나스닥주식 인스턴스 생성
gg = NasdaqStock('GOOG', 1154.05)
# 구글 인스턴스 제거
del(gg)
# 마이크로소프트 나스닥주식 인스턴스 생성
ms = NasdaqStock('MSFT', 102.44)
# 마이크로소프트 인스턴스 제거
del(ms)
# 아마존 나스닥주식 인스턴스 생성
amz = NasdaqStock('AMZN', 1746.00)
# 아마존 인스턴스 제거
del(amz)

print()

# __doc__ 독스트링
# 독스트링(docstring) : 클래스나 메서드를 설명하는문자열
# 클래스나 메서드명 바로 아랫 줄에 위치
# help() 함수에서 클래스나 메서드 설명을 출력하는 데 사용