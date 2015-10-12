##10.12(월) 파이썬
##중간고사 월요일 (프로그램하는걸로 진도나가는데까지)
##강의자료와 과제(pdf로저장한것만)만 오픈해서 볼수있다!(Pdf만 볼수있다)


##외장함수
##사용시에는 반드시 import를 해야한다

##시스템명령 직접내릴수 있는 모듈이 os모듈
#import os
#import sys
##Q1)파이썬명령을 직접 프로그램에서 내려봐라..
##test.py라는 파일을 만들었을때 저파일을 실행시키는 구문을 만들어보자

#os.system("python test.py a b c")


##exit 는 예외처리때 except에 사용

#print(sys.path)\

##pickle은 파일저장할떄 사용해봤음(객체를 그대로 저장할수 있다)

#class student:
#    def __init__(self,name, age):
#        self.name = name
#        self.age = age
#    def show(self):
#        #show = self.name + self.age
#        print(self.name, " : " ,self.age)

#s1 = student('홍길동',19)
#s1.show()                #☆함수호출시 이렇게해야된다
#print(s1.show())
 
#import pickle              #★★★★★자기객체 시험문제로 나온다
#f = open("text.txt",'wb')
#pickle.dump(s1, f)
#f= open("text.txt",'rb')
#data = pickle.load(f)
#print(data)


##print(os.environ) #시스템에 등록한 변수들이 뜬다
##getcwd(): 현재 자신의 디렉토리 위치를 반환
#os.chdir('..')#.현재디렉토리 , ..부모디렉토리
#print(os.getcwd()) 
##현재디렉토리에서 부모 디렉토리로 가고싶을떄

##각종 프로그램들을 시스템명령으로 실행시킬수있다 2가지방법
## system, startfile

##os.rename으로 파일이름 바꾸는것뿐만아니라 dir입력시 경로로 이동시켜줌(리눅스의 move명령어랑 비슷)
##print(list(os.walk('..'))) #리스트로 반환하므로 list를 써서 출력받는다



##Q2
##현재디렉토리에서 sample이라고 하는 디렉토리를 만들고  
##하위 디렉토리까지 다포함해서 txt파일만 골라서
##썜플디렉토리에 txt를 복사하라

##os.mkdir('sample')   #이런 디레게토리가 있나?하는 함수가있으면 좋겠다
##os.rename('sample','.')

#a, b, c = list(os.walk('.')) #walk를 쓰면 3개로 출력받을수 있다 path, dir, file
#print(b)

#for i in b:
#    if(b[i] == '*.txt'):
#        os.rename(b[i],'sample')`
#import shutil #파일 복사하는 모듈

#os.path     #중간고사공부엄청열심히해야된다...
##os.path.commonprefix 공통되는 부분만 추출해주는 함수

#print(os.path.dirname('C:/python34/python.exe'))
#print(os.path.dirname('text.txt'))

##exists 을 가지고 아까 현재디렉토리에 simple디렉토리가 있는지 확인할떄 사용
## ~(틸다) : 사용자 홈디렉터리 나타낼때 

#print(os.path.expanduser('~\\python.exe')) #
##경로 표시시 /로 쓸때는 하나만 \쓸때는 \\두개로 표시를 해주어야한다

##os.path.join 사용시 절대경로가 중간에 나오면 다시연결한다


##print(os.path.splitext('C


def Assign2_():
    fileName = "201401.txt"
    checkOutList = []
    fieldList = []
    findList = []
    nlist =[] 

    with open(fileName, "r") as myFile:
    
        while True:
            content = myFile.readline()
            if not content:break

            nlist = content.split("|") # list로 분할
       
print(nlist)    