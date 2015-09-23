###9.23(수) python####
#상속 : 내가 부모로부터 상속받은것을 그대로 사용 / 변경 할수 있다 
#객체지향의 꽃인 다형성을 구현
#이즈아 관계 : 상속으로 구현(상속이라는 개념을 사용해서)
#오버라이딩 : 부모에 대한 기능 재정의



#테란클래스생성
#coding:cp949
from abc import ABCMeta, abstractmethod

class Terran(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass


class Tank(Terran):
    def __init__(self, name, demage):
        super().__init__(name)
        self.demage = demage

    def attack(self):
        print("탱크를 쏩니다")

class Marine(Terran):
    def __init__(self, name, hp):
        super().__init__(name)
        self.hp = hp

    def attack(self):
        print("총을 쏩니다")

  
def Attack(terran): #attack 이라는 것을 탱크와 마린에 각각 넣어야 되므로 terran으로 설계하면된다
    terran.attack()

    

t1 = Tank("tank", 0)                      #객체만들기
t2 = Marine("marine", 100)

tlist = [Tank("tank1", 1) , Tank("tank2", 50), Marine("marine1", 100), Marine("marine2", 120)]
for item in tlist:
    Attack(item)

Attack(t1)
Attack(t2)
    
#★★객체지향프로그래밍기법 4가지(추상화(클래스 잘만드는 것), 은닉화(감추는거), 캡슐화, 다형성(메시지 하나로, 
#명령 하나로 다양하게 움직이도록 한다))
#다형성을 알면 추상메소드가 존재하면 추상 class로 만들수 있다(추상메소드는 인스턴스를 만들수 없다)


#테란이라는 객체는 실질적으로 없다 그거로부터 파생되어진 tank같은 인스턴스가 존재
#공격이라는 메소드를 클래스에 넣고 싶다






#리스트로 파생되어진 클래스를 만들고싶다
class MyList(list):
    name = ""
    def __init__(self, name):
        super().__init__([])
        self.name = name

    def __str__(self): ##__이렇게 시작하는 것은 이미 클래스에서 함수로 사용하는것들)
        return self.name+":"+super().__str__()

list1 = MyList("greenjoa")
list1.append(10)
list1.append(50)
list1.append(60)
list1.append(80)
list1.append(100)
print(list1)
print(dir(list1))#dir: list의 기능을 확인할수 있는 함수

#리스트에서 name을 추가하고싶을때 C++에서는 연산자 재정의를 했다 파이썬도 마찬가지로 연산자 오버로딩
#연산자 오버로딩 : 기존에 있는 연산자가지고 내가만들 클래스한테도 먹히게끔 재정의 하는것!
#이항연산은 이항연산으로 정의를해야한다(막 하면 안됨)

#a1 + 10 , 10 + a1 두개 다 재정의 해주어야 한다