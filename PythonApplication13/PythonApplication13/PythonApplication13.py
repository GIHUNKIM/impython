#10.7(수)

#내장함수는 import없이 자체 내장되어져있는 함수 사용
#반복해서 작성할수 있는 것은 list, string(문자열) ,dir 사용하는 왠만한 자료형들은 반복가능한 형들이다
#키보드제어시에는 chr()/ ord() 함수를 사용한다
#dir() : list 객체가 가지고있는 변수나 함수를 리스트형태로 보여줌
d = [1,2,3,4,5,6,7,8,9,10]

print(dir(d))

#enumerate : 시퀀스자료형을 입력으로 받아 객체를 반환함

#a = list(enumerate("greenjoa"))
#print(a)
#???어떻게 사용?

#filter 사용리스트하나 주고 리스트에서 짝수만 걸러내봐라
def positive(l):
    return l%2==0

print(list(filter(positive,[1,2,3,4,5,6,7,8,9,10])))


aa = 3
print(id(3))
print(id(aa))
#같은 id를 갖게된다 reference를 참조하므로
#isinstance  오브젝트가 클래스의 인스턴스인지 판단해준다


#lambda 익명의 함수를 만들때 사용 / 함수이름을 만들지 않아도되지만 기능은 필요하다
#lambda는 return 구문을 사용할수 없다
#이름이 필요없는 한줄짜리 함수가 필요하다고 할때 사용함.(filter에 적용시킬때 딱이다)
#빈번하게 사용되고 반복문이랑 연동되서 사용됨 익혀둘것!
print(list(filter(lambda x:x%2==0,d)))


#list는 새로운 list를 만들어주는 함수

a = [1,2,3]
b= list(a)
c= a
print(a)
print(b)
print(c)
print(id(a))
print(id(b))  #b는 *새로운* list를 만들어주어서 다른 레퍼런스에 지정됨
print(id(c)) #그냥 대입시에는 참조하는것으로 동일한 주소값

print(list(map(lambda x:x*2==10, d)))

#repr 는 문자열 형태로 돌려주는 함수로 eval함수의 입력으로 주로 쓰임
#str로 하면 오류가 발생한다
t = eval(repr('hi'.upper()))
print(t)

y= [51,42,3,4,5,6,72,9]
y.sort()
#sort 사용시 대입시키면 왜안되나..??
print(y)   #데이터 자체가 정렬이 되어서 나온다

#동일한 개수의 요소값을 묶어주는 역할
#만약 객수가 다를경우 같은곳까지만 묶어주는 역할을 수행한다 남은것은 출력하지않는다
print(list(zip([1,2,3],[4,5])))

from operator import itemgetter

#Quiz
data= {"홍길동":[80,70,60,92],
          "김길동":[24,35,18,10],
          "고길동":[10,20,8,5]}

#print(type(data))

#이것을 정렬해 보아라               dir공부....


print(sorted(data.items(),key=itemgetter(1),reverse=False))
print(sorted(data.items(),key=itemgetter(0),reverse=True))
#print(sorted(data.values()))

for i in data:
    data[i].sort()


print(data)     
#Quiz2 key값도 정렬시켜보아라