#11.9(월) DB 파싱 2
#제안서 발표를 한다... 제안서 뭐쓸것인지 주제 알려주기 바란다.
#삭제,업데이트도 한번씩 해봐야한다..

#------------------------------사용자정의 자료형-------------------------------
# 클래스 객체에서 SQLite3 입력 가능한 자료형으로 변환
#def PointAdapter(point):#cur1.execute("select p from test")     p타입은 포인터이므로 포인터 객체를 반환한다
#자주사용하는 데이터들은 adapter함수 만들어서 사용하면 된다.(데이터가 저장되는것은 아니지만 객체가 저장되는것 처럼 사용할수 있다)
#print(cur1.fetchone())  




#-----------------------------로그인기능---------------------------------
#웹서버를 개발하면 기본으로 들어간다
#회원가입 등록하는 기능하나와 로그인하는 기능
#회원가입시 아이디 중복체크 기능


#schema.sql

#drop table if exists user;
#create table user(
#user_no integer primary key autoincrement 순번은 자동으로
#userid string not null,
#username string not null,
#userpw string not null
#);


#q1 회원가입만들기 

import sqlite3 as sqlite
from werkzeug import check_password_hash, generate_password_hash

def init_db():
    db = sqlite.connect("test.db")
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
        db.commit() #db 저장하는것
        db.close() #db닫아주는것
    #cur = con.cursor()


 #db객체를 얻어야 하기 때문에 함수 하나를 만들자
def get_db():
    db = sqlite.connect("test.db")
    return db


def register():
    print("****회원 가입 ****\n")
    print("user id : ", end="")
    userid = input()
    db = get_db() #아이디 중복 체크 만들기.
    cur= db.cursor()
    cur.execute("select * from user where userid=?",[userid]) # 조건문을 써서 가지고 온다
    if(cur.fetchone() != None):
        print("아이디가 존재합니다.")
        return   #아이디 체크확인했으니 이제 db에 넣는 작업하기

    #무조건 insert하면 안되고 이 아이디가 존재하는지 여부를 체크 해야된다.
    



    #그룹프로젝트는 진행할때 github 만들어서 사용할것...



     
    #내가 생각한것
    #insertsql = '''insert into user values('ab','홍길동','123456')'''
    #cur.execute(insertsql)
    #cur.execute("select * from user;")
    #print(cur.fetchall())

    print("user name : ",  end="")
    username = input()
    print("user passwd: ", end="")
    userpasswd = input()

    sql = "insert into user(userid, username, userpw) values(?,?,?)"
    cur.execute(sql, [userid, username, generate_password_hash(userpasswd)])
    db.commit()  #안없어지게 하기 위해 꼭 저장을 해주어야 한다!!
    
    cur.execute("select * from user;")
    print(cur.fetchall())
    db.close()#디비를 마지막에 닫아준다


#my code


#def login():
#    print("**** 로그인 ****\n")
#    print("user id : ", end="")
#    userid = input()
#    db = get_db() #아이디 중복 체크 만들기.
#    cur= db.cursor()
#    cur.execute("select * from user where userid=?",[userid]) # 조건문을 써서 가지고 온다
#    if(cur.fetchone() != None):
#        print("user passwd : ",  end="")
#        username = input()
#        db = get_db() #아이디 중복 체크 만들기.
#        cur= db.cursor()
#        cur.execute("select * from user where userpw=?",[userpw]) # 조건문을 써서 가지고 온다
#        if(cur.fetchone() != None):
#         print("로그인 성공")





def login():
    print("**** 로그인 ****\n")
    print("user id : ", end="")
    userid = input()
    print("user passwd : ",  end="")
    userpasswd = input()

    db = get_db() #아이디 중복 체크 만들기.
    cur= db.cursor()
    cur.execute("select * from user where userid=?",[userid])
    temp = cur.fetchone()
    if(temp == None):
        print("아이디가 존재합니다.")
        return
    elif check_password_hash(temp[3], userpasswd):
        print("로그인 성공")
        return
    else : 
        prnt("비밀번호 체크요함")
        return

register()
login()





#------------------비밀번호 암호화------------------------
#파이썬에서도 암호화 시켜주는 해쉬함수를 제공해주고 있다
#벡자이크에서 제공하는 해시함수 이용
#
# 입력된 비밀번호를 해시값으로 변환
# generate_password_hash(userpw) 입력받은 userpw를 줘서#from werkzeug import check_password_hash, generate_password_hash




#--------------Mysql 연동----------
#python –m pip install pymysql  설치
#계정정보를 등록시킨후에 가지고 있는 아이디를 쳐야지만 접근 할수있다
#con = mysql.connect(host='127.0.0.1',
# user='greenjoa', passwd=‘1234',db='my_db', charset='utf8') #한글사용할때 깨지는 현상이 있으므로 charset을 지정해주면된다
#원격에서 접속하는 것이기때문에 DB입력정보가 많다
#cursor = con.cursor()