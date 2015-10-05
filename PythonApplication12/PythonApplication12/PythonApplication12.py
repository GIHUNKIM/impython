#10.5 (월)  다음주 월요일(6시 보강예정)
#[class 다중상속]
#클래스 (생성자 ,소멸자)
#생성자 : __init__ 이고 self 가 들어간다 (나에대한 정보를 주어야지 해당정보를 참조 할수 있다.) this 를 생각해라(내주소에 해당하는 값이 넘어간다(명시적으로))
#super : 부모클래스의 객체를 반환해주는 함수  / 호출된 자리에 객체가 들어간다 
#객체를 통한 멤버 호출시에는 self를 안넣고/ 클래스를 통한 객체를 호출시 self를 넣는다


#**arg 인자의 갯수를 모를떄 사용

class A():
    def __init__(self, a):
        self.a = a
    def show(self):
        print('show:',self.a)

class B(A):            #super 호출시에는 A가 2개일때 1번만 A를 호출하게 된다. 따라서 A가 한번 실행되어 a가 나오게 된다
    def __init__(self, b, **arg):
        super().__init__(**arg)
        self.b = b
    def show(self):
        print('show:',self.b)
        super().show()

class C(A):
    def __init__(self, c, **arg):
        super().__init__(**arg)
        self.c = c
    def show(self):
        print('show:', self.c)
        super().show()

class D(B,C):
    def __init__(self, d, **arg):
        super().__init__(**arg)
        self.d = d
    def show(self):
        print('show:',self.d)
        super().show()

data = D(a=1,b=2,c=3,d=4)
data.show()


#[private variables]
#파이썬에서는 기본적인 접근제어가 public 이다
#private 앞에 __을 사용하여 private variables란 개념으로 지원함

#오버라이딩 할때 완전히 동일해야되는데 가능하지만
#인자개수가 다르므로 오버로딩한것인데 이렇게되면 부모에 대한 정보를 호출하지 못함





class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

#private copy of original update() method
    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
    

data= MappingSubclass([1,2,3,4])
print(data.items_list)
data.update([1,2,3],[2,5,6])
print(data.items_list)



#[예외처리]
#


import sys
number1 = float(input("enter a number: "))
number2 = float(input("enter a number: "))
try:
    result = number1/number2
    print(result)
except ZeroDivisionError  as e:           # 해당 에러 발생시 여기로 이동
    print(e)                             # as 뒤에는 에러 내용
    print("The answer is infinity")
except:
    error = sys.exc_info()[0]    #sys.exc_info() 현재 발생한 예외정보를 튜플로 반환
    print(error)
    #print(sys.exc_info()) #오류에 해당하는 정보 출력
    sys.exit()   #finally까지 다 수행하고 종료를 한다

finally:
    print("Done")

