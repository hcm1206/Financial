# 클래스
# 클래스(class) : 객체를 생성하는 틀(template)
# 데이터 맴버(data member)라고도 불리는 속성(attribute)과 동작을 수행하는 메서드(method)로 구성

# 인스턴스화(instantiation) : 클래스로부터 객체를 생성하는 것
# 생성된 인스턴스가 가지고 있는 속성과 메서드는 . 표기법(dot notation)을 사용하여 접근 가능

# MyFirstClass 클래스 정의, . 표기법으로 clsVar 속성에 접근하고 clsMethod() 메서드를 호출하는 객체
class MyFirstClass:
    clsVar = 'The best way to predict the future is to invent it.'
    def clsMethod(self):
        print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')

# 인스턴스화
mfc = MyFirstClass()

# 클래스 변수에 접근
print(mfc.clsVar)

# 클래스 메서드 호출
mfc.clsMethod()

print()