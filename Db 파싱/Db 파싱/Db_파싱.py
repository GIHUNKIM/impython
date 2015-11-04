##11.4(수) 파이썬 DB
##파이썬은 자체적으로 SQLite3 라이브러리를 자체적으로 지원해준다
##import SQLite3 로 사용 서버급은 아니고 로컬에서 간단하게 정보저장용으로 사용
##웹서버 돌리는것을 할떄는 데이터베이스를(mySQL)로 사용해서 해야한다 (설치 및 계정 만들기는 알아서 해라)
##연결해주는 함수 connect
##row 클래스 정보 : 각각의 튜플에 해당하는 정보를 받을 수 있다

##데이터베이스 연결하는 방법
#import sqlite3
#con = sqlite3.connect("test.db") #connect로 데이터베이스 연결(로컬에 해당db만들어진다)
##해당 질의를 날릴때 cursor가 필요하다

##":memory:" 메모리에 해당하는 DB를 만들수 있다 영구적인것은 아니고 사라진다 디스크에 저장하는것보다 속도가 빠르다
##임시적으로 저장했다 사용할떄 필요

#cur = con.cursor() #커서객체 획득
##db에 각종 테이블 만들기

##sql = """create table
##    phonebook(name text, phonenum text);"""
##cur.execute(sql)

##sql='''create table if not exists   #존재하지 않을경우에만 생성하겠다
##phonebook(name text, phoneNum text);'''  

##drop table 했을시 기존에 있던것을 지우고 새로운 테이블을 만든다

##dropsql = """drop table if exists phonebook;"""
##cur.execute(dropsql)  #테이블을 지우는거

##sql = """create table
##    phonebook(name text, phonenum text);"""
##cur.execute(sql)
##------------------------------자료형----------------------------------------
##자료형 두개 혼합해서 사용해도된다 int 나 INTEGER 가능

###sql질의문 삽입하기
##insertsql='''insert into phonebook
##         values('greenjoa1','010-1111-2222');'''
##cur.execute(insertsql)


##레코드 조회
##삽입이 됬는지 안됬는지 확인하고싶을떄 select form 구문 사용
##fetchone() : 1개 조회, fechmany(2) : 2개의 레코드
##다른 프로그래밍에서는 move to 로 사용했지만 python은 지원하지않는다
##fetchone으로 사용한다
##cur.execute("select * from phoneBook;")
##for row in cur:
##    print(row)
##    print(row[0])##-----------------------------레코드 삽입-------------------------------##?를 통해서 객체를 넣어줄수 있다 (인자 전달 순서에 맞추어 시퀀스 객체 전달)##name = 'greenjoa2'##phoneNumber = '010-2222-2222'##insertsql = '''insert into phonebook values(?,?);'''##cur.execute(insertsql, (name, phoneNumber))##cur.execute("select * from phoneBook;")##print(cur.fetchall())##?는 불편하다 시퀀스의 순서를 기억하고있어야 되서 각 인자에다가 이름을 사용할 수 있다##values(:inputName, :inputNum); 이런식으로##name='greenjoa3'##phoneNumber='010-3333-3333'##insertsql='''insert into phonebook##    values(:inputName,:inputNum);'''##cur.execute(insertsql,{"inputNum":phoneNumber,"inputName":name})##cur.execute("select * from phoneBook;")##print(cur.fetchall())##삽입2##executemany 를 사용하면 리스트에 해당하는것을 한꺼번에 삽입할수 있다##insertsql='''insert into phonebook values(?,?);'''##datalist=(('greenjoa4','010-4444-4444'),
##('greenjoa5','010-5555-5555'))
##cur.executemany(insertsql, datalist)
##cur.execute("select * from phoneBook;")
##print(cur.fetchall())

##삽입3
##제너레이터 : 특정함수를 만들어서 사용할수 있다
##함수에서 값을 반환받을때 return을 사용하지만 return은 종료가 되므로 yield 를 사용해서 종료되지 않게
##def dataGenerator():
##    datalist=(('greenjoa6','010-6666-6666'),('greenjoa7','010-7777-7777'))
##    for item in datalist:
##        yield item
##cur.executemany(insertsql, dataGenerator())##cur.execute("select * from phoneBook;")##print(cur.fetchall())##레코드 조회 시 조건절은 where에 사용##sql구문 : 갱신 삭제 등 그대로 사용하면 된다##-------------트랜잭션---------------------##데이터베이스에서 논리적인 작업의 단위##A통장에서 100만원 출금 후 B에 입금까지 완료해야된다##출금후에 정전이 됬다 이작업은 어떻게 수행해야할까##돈이 증발하면 안되기때문에 트랜잭션 개념으로 만들어서##여러개의 작업을 하나의 단위로 처리해서 작업이 끝나야 반영하는 개념으로##출금하고 입금해서 완료되었으면 commit 정상적으로 안됬으면 rollback##Db에 반영을 할것인지 안할것인지 정할 수 있다##삽입하는거 다빼고 데이터베이스의 모든것을 가져와보기##cur.execute("select * from phoneBook;")##print(cur.fetchall())##여러가지 insert를 했는데 빈값이 나온다 데이터베이스에 반영이 안되어있다.....##con.commit()##insertsql='''insert into phonebook##            values('greenjoa10','010-1234-1234');'''##cur.execute(insertsql)##cur.execute("select * from phoneBook;")##print(cur.fetchall())# #자동으로 commit설정하는 것이 있다##con.isolation_level = None 이라고하면된다#con.isolation_level = None##======================================레코드정렬========================##order by로 정렬##cur.execute("select * from phoneBook order by name;")   #오름차순정렬###cur.execute("select * from phoneBook order by name desc;")#내림차순 정렬##cur.execute("select * from phoneBook;")##print(cur.fetchall())##insertsql='''insert into phonebook values('Green','1');'''##cur.execute(insertsql)##cur.execute("select * from phoneBook order by name desc;")##print(cur.fetchall())##정렬을 해줄수있는 ***기준****함수를 작성해서 사용할수 있다##예를 들어서 대소문자 구분없이 정렬하고 싶다#def OrderFunc(str1, str2):
#    s1 = str1.upper()
#    s2 = str2.upper()
#    return (s1 > s2) - (s1 < s2) # 앞이 클 경우 (음수), 같음(0), 뒤가 클 경우(양수)
#                                #아스키코드값으로 계산
#                                #tip) for문없이 비교할수 있는것은 order by에 의해서 실행이 되는것이다
#con.create_collation('myordering', OrderFunc) #함수를 사용할 키워드 , OrderFunc)  #2를 통해서 1로 정의를 하겠다
#cur.execute("select * from phoneBook order by name collate myordering;")
#print(cur.fetchall())




##------------------------------집계 함수---------------------------------------------
##예제2) name을 안 넣고 핸드폰만 집어넣겠다
##테이블에 속성지정을 해주어야 한다

#cur.execute("insert into phoneBook(phoneNum) values('99-9999-9999');")
#cur.execute("select * from phoneBook;")
#print(cur.fetchall()) 
##cur.execute("select count(*) from phoneBook;")
##print(cur.fetchone())   #[0]을 주면 속성에 해당하는 값만 뽑을 수 있다


#cur.execute("select count(name) from phoneBook;")
#print(cur.fetchone()[0]) #name을 지정해서 none값은 포함하지 않는다



#-----예제3) 이름 나이만 있는 user테이블 하나만 만들어봐라


import sqlite3
con = sqlite3.connect("test1.db") 

cur = con.cursor() #커서객체 획득

#sql = """create table
#    user(name text, age int);"""
#cur.execute(sql)

insertsql='''insert into user values(?,?);'''
datalist=(('김길동','22'),('홍길동','23'),('고길동','19'),('대동','40'))
cur.executemany(insertsql, datalist)
cur.execute("select * from user;")
print(cur.fetchall())


#max랑 min을 구해봐라
cur.execute("select max(age) from user;")print(cur.fetchall())#경량화이지만 join ,인덱스 하는것 다가능하다



#예제4-------------------전체 평균나이를 구하고 싶다 avereage함수는 없으므로 만들어서 사용해야한다
#생성자 하나 만들었고, 누적해서 합계를 구한후 나누면되지않나
#반드시 재정의해야되는함수는 ★★step()-values 값이 들어오는것(들어오면 단계마다 무엇을 하겠다)
#, finalize()- 반환할 값을 최종적으로 지정 반드시 들어가야 한다

#클래스 만든후 등록을 시켜주어야 한다
#create_aggregate로 등록을 시켜주어야한다e("avg"# 사용할 이름, 1#step에 들어가는 인자 갯수, Average#해당클래스) 

class Average:
    def __init__(self):
        self.sum = 0
        self.cnt = 0
    def step(self, value):
        self.sum += value
        self.cnt +=1
    def finalize(self):
        return self.sum/self.cnt
con1.create_aggregate("avg", 1, Average) # DB에 등록
cur1.execute("select avg(Age) from user;")


# 파이썬에서는 class로 넣으면되지만
#데이터베이스에다가 넣을때는 쪼개서 각각의 값들을 넣어놓게 되는데 불편하다
#내가 원하는 형태로 객체를 넣어서 질의문에 대한 결과도 내가 넣은 데이터 타입대로 받고싶다 시퀀스로 받는게 아니라


#다음시간 데이터베이스 하나 더한다..오늘 DB나가는것까지 연동시켜서 저장하는것까지 과제로 나올것이다...



#데이터베이스 갱신과 삭제하는 구문 별도로 공부할것!!!
