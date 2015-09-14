######함수######
##def sum_and_mul(a, b):
##    return a+b, a*b



##answer=sum_and_mul(10,30)
##sum, mul =sum_and_mul(10,30)
##print(sum, mul)        #(40, 300) 으로 튜플로 반환된다
##변수로 반환받고 싶을 시에는 변수로 두개를 넣어주면된다


a=1  #전역변수
def vartest(a):
    a = a + 1 #지역변수

    vertest(a)
print(a)

#예제1 
#리스트안에 리스트


#유니코드로 안하고 기존 cp949로 저장된다
#coding:cp949 인코딩모드를 cp949로 한글쓸려고하면 UTF 
#파이썬3에서는 자동으로 utf 지만 저장은 자동적으로 cp949임으로 여기서 쓰는 모드를 cp949로 바꾸자(저장할때도 cp949이므로)

#def printData(data):
#    for item in data:
#        if isinstance(item, list):
#            for items in item:
#                print(items)
#        print(item)


#data = ["홍길동",["베테랑","암살"], 
#        "고길동",["베테랑","암살"], 
#        "김길동",["베테랑","암살"]]



#암살 베테랑에 해당되는것을 item 별로 출력하라
# if 사용하라
      #if isinstance(item, list):
      #      for items in item:
      #          print(items)




# 애니메이션영화를 리스트를 안에 별도로 리스트를 만들고 싶을때
#data = ["홍길동",["베테랑",["류승완","황정민","유아인"],"암살"], 
#        "고길동",["베테랑","암살"], 
#        "김길동",["베테랑","암살"]]

#★????☆리스트안에 리스트가 몇개인지 모를때 어떻게 해야되는지.. 패턴이 반복된다(=재귀함수)

#def printData(data):
#    for item in data:
#        if isinstance(item, list):
#            #for items in item: 반복문을 쓰지말고 재귀함수 사용
#            printData(item)
#        else:
#            print(item)
        


#첫번째 리스트면 홍길동, 레벨별로 나누어서 출력하고 싶다.재귀호출 될때매다 출력하는것을 탭되어 출력할때(인자하나를 넣어주면된다)

#def printData(data, level=0):
#    for item in data:
#        if isinstance(item, list):
#            printData(item, level+1)
#        else:
#            for i in range(level):
#                print("\t",end="") # \t는 탭출력 , end=""는 줄바꿈
#            print(item) #실제로 출력되는 부분은 이부분임 이전에 for문을 사용하여 출력을 해준다
#printData(data)



#import printData    #프린터데이터안에 있는 모듈을 호출하겠다
#data = ["홍길동",["베테랑",["류승완","황정민","유아인"],"암살"], 
#        "고길동",["베테랑","암살"], 
#        "김길동",["베테랑","암살"]]    
#printData.printData(data)  #모듈이름.함수이름

import os   #os라는 라이브러리 사용       
#이 함수가 무엇인지 모를때 help() 함수를 호출  ex)help(os.mkdir)

print(os.getcwd())   #getcwd : 현재 작업 디렉토리에 해당되는 위치 
#os.mkdir("sample")
os.chdir(".//sample")
print(os.getcwd())
#os.system("dir\\w")
os.system("python setup.py sdist")
#os.system("python setup.py install")


