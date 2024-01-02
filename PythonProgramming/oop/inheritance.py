# 상속 : 클래스가 가지는 모든 속성과 메서드를 다른 클래스에게 물려주는 기법

# 부모 클래스 or 슈퍼 클래스 : 상속을 해주는 클래스
# 자식 클래스 or 서브 클래스 : 상속받는 클래스

# 다중 상속 : 여러 부모 클래스로부터 자식 클래스가 상속받는 것

# 클래스 A 정의
class A:
    # 메서드 A 정의
    def methodA(self):
        print("Calling A's methodA")
    # 메서드 정의
    def method(self):
        print("Calling A's method")

# 클래스 B 정의
class B:
    # 메서드 B 정의
    def methodB(self):
        print("Calling B's methodB")

# 클래스 A와 클래스 B로부터 다중상속하여 클래스 C 정의
class C(A, B):
    # 메서드 C 정의
    def methodC(self):
        print("Calling C's methodC")
    # 메서드 재정의(오버라이딩) : 문자열 출력 후 부모 클래스 메서드 호출
    def method(self):
        print("Calling C's overridden method")
        super().method()

# C 클래스 인스턴스 생성
c = C()
# C 객체에서 메서드 A 호출
c.methodA()
# C 객체에서 메서드 B 호출
c.methodB()
# C 객체에서 메서드 C 호출
c.methodC()
# C 객체에서 재정의(오버라이딩)된 메서드 호출
c.method()

print()

# 오버라이딩(overriding) : 자식 클래스에서 부모 클래스의 메서드 이름과 인수 형식과 동일하게 메서드를 재정의하는 것
# 오버로딩(overloading) : 메서드 이름이 같고 인수 형식이 다른 여러 메서드를 작성하는 것