####9.21(월) python 클래스######
'''클래스 : 데이터와 함수를 결합한 사용자 정의
##def 함수정의 sum(self, a,b) 클래스의 멤버 함수 에는 첫번째 인스턴스를 self(자바,C++= this 와 같은개념)로 넣어야 한다
 함수 호출할때 주소값이 넘어가는 것이다 =selt(인스턴스 객체를 나타낸다 그 객체의 해당되는 주소값을 넘겨준다)
함수사용하는 목적 : 중복을 방지하기 위해서(코드 중복을 막기위해서) , self를 빼면 오류가 날것이다


함수호출
bound에서는 self를 명시해주지 않아도 된다
unbound 아직 결정되어지지 않은 객체의 sum함수 사용 / 반드시 self를 넣어서 인스턴스 객체를 넘겨주어야한다
2가지 동일한 형태의 호출이다


생성자 함수 : _init_함수 / 보통 속성 초기화하는 용도로 많이 사용한다, 속성은 공유되지 않는다
init만들때도 제일먼저 self라는 값이 들어간다 그뒤에 속성 
this에서는 멤버들을 속한 멤버만 access를 했는데 self는 상관없이 멤버를 엑세스 할수 있다
java에서는 클래스 변수에 static를 붙여주었다
*클래스변수는 인스턴스가 없어도 엑세스 가능하지만 함수에서의 인스턴스는 인스턴스가 있어야지만 엑세스 할수있다
클래스 밖에서도 객체를 생성할수 있다(특정객체만 호출할수 있는 객체도 생성 가능)


class Movie:
    title = ""
    director = ""
    def __init__(self, title, director):   #__로 시작하는것은 시스템에 있는 함수를 사용하겠다는 것
        self.title = title
        self.director = director

            
    def showInfo(self):
        print(self.title +" " + self.director)


#movie 객체 2개 만들어보기

movie1= Movie("베테랑","김길동")
movie1.showInfo()
movie2 =Movie("암살","고길동")
movie2.showInfo()


#1번째 객체에는 주인공이라는 속성을 넣어봐라

movie1.actor = "유아인"

#생성자도 호출가능 ex) movie.__init__(m1,"암") 
'''


#class Movie:
#    '''영화 클래스입니다'''
#    title = "암살"
#    director = "최동훈"
#    def __init__(self, title, director):   
#        self.title = title
#        self.director = director
             
#    def showInfo(self):
#        print(self.title +" " + self.director)

#m1 = Movie("베테랑", "류승완")
#print(m1.title)             #값을 변경시키지 않으면 class값그래도 사용을 하지만 값을 변경을 하면 베테랑이라는 값을 갖게된다

##클래스에 있는 title값을 변경하고 싶다 그떄 사용하는 속성이 __class__이다!
#print(m1.__doc__)#클래스에 주석처리를 해주면 해당하는 정보를 한번씩 확인하도록 해줄수 있다






#소멸자#

#class Movie:
#    '''영화 클래스입니다'''
#    title = "암살"
#    director = "최동훈"
#    def __init__(self, title, director):   
#        self.title = title
#        self.director = director
#        print(self.title + "생성자 호출")

#    def __del__(self):
#        print(self.title+ "소멸자 호출")
                 
#    def showInfo(self):
#        print(self.title +" " + self.director)

#m1 = Movie("베테랑1", "류승완1")
#m2 = Movie("베테랑2", "류승완2")
#m3 = Movie("베테랑3", "류승완3")
#m4 = Movie("베테랑4", "류승완4")

#print(type(m4))
#m4 = m3                                                              #모든 대입연산은 얉은 복사이다.
#print(id(m4))
#print(id(m3))
#m4.showInfo()



#static method#
#self만 뺀다고 static이 되는것이 아니다
# @ : 데코레이터를 사용하여 method를 정의하는데 사용하고 있다 아래다가 메소드를 정의한다
#class method : 클래스 변수에 해당하는 것을 엑세스 할수 있다 (인스턴스를 통하지 않고)
#self를 뺀 함수를 만들 수 있다 객체를 없이 ☆인스턴스를 만들지 않고 멤버를 엑세스 할떄 사용한다(static, class Method)
# STATIC: 클래스에 해당하는 정보가 전달이 안됨(
# CLASS:클래스는 클래스정보가 전달이되므로 멤버를 엑세스 할수 있다



#카운트를 해보자
class Movie:
    '''영화 클래스입니다'''
    count = 0                            #만들어질때마다 +가 되어야 한다
    title = "암살"
    director = "최동훈"
    def __init__(self, title, director):   
        self.title = title
        self.director = director
        Movie.count+=1
        print(self.title + "생성자 호출")

    def __del__(self):
        print(self.title + "소멸자 호출")
                 
    def showInfo(self):
        print(self.title +" " + self.director)

    @staticmethod
    def showCount1():
        print(Movie.count)          #class에 해당하는 명을 명확하게 알아야 한다
    
    @classmethod
    def showCount2(cls):             #클래스에 해당하는 정보를 
        print(cls.count)







m1 = Movie("a" , "b")
m2 = Movie("c" , "d")
m3 = Movie("e" , "f")
m4 = Movie("g" , "h")
m5 = Movie("i" , "j")

Movie.showCount2
Movie.showCount1

print(m1.count)
print(m2.count)
#내것을 증가시키는 것이 아니라 클래스에 있는것을 증가시켜라    Movie.count+=1

#self가 있어서 인스턴스를 통해 확인해야되지만 확인하지않고 함수를 추가시켜서 카운터 하고싶다
    
        






#엑셀 라이브러리는 압축 풀고 인스톨 해서 사용해라

