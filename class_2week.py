class Fourcal:
    def setdata(self, first, second):       #메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징
        self.first = first
        self.second = second

a=Fourcal()

a.setdata(4, 2)  #a.setdata(4, 2)처럼 호출하면 setdata 메서드의 첫 번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달되기 때문
print(a.first)
print(a.second)


b=Fourcal()
b.setdata(10,20)
print(b.first)
# a 객체의 first 값은 b 객체의 first 값에 영향받지 않고 원래 값을 유지하고 있음을 확인할 수 있다
# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지


#id 함수는 객체의 주소를 돌려주는 파이썬 내장 함수
print(id(a.first))
print(id(b.first))
#a 객체의 first 주소 값과 b 객체의 first 주소 값이 서로 다르므로 각각 다른 곳에 그 값이 저장된다는 것을 알 수 있음




class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first+self.second
    def mul(self):
        return  self.first*self.second

a=Fourcal()

a.setdata(20,30)
print(a.add())  #a.add() 메서드 호출 전에 a.setdata(4, 2) 가 먼저 호출되어 a.first = 4, a.second = 2 라고 이미 설정
print(a.mul())


# 위의 예제에서 setdata 메서드 수행하지 않고 다른 메서드 실행하면 오류
# 초깃값이 필요할 때 생성자(객체가 생성될 때 자동으로 호출되는 메서드를 의미)를 사용
class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first+self.second
    def mul(self):
        return  self.first*self.second
    def sub(self):
        return self.first-self.second

a=Fourcal(11,12)
print(a.mul())

# 클래스의 상속 : 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것 -> 클래스의 기능을 확장시킬 때 주로 사용
class MoreFourCal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
    def sub(self):
        if(self.second==0) : return '영은 넣지마세요'
        else: return self.first-self.second

a=MoreFourCal(6,5)
print("상속")
print(a.add())
print(a.pow())
print(a.sub())


b=MoreFourCal(50,0)
print(b.add())
print(b.sub())