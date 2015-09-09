
##9.9(수) dictionary

##-key value 값을 쌍으로 갖으며,key는 중복되면 안된다, key는 변할수 없는 값으로 해야한다
##key에 리스트를 쓸수 없다

##( : 튜플, 터플
##[ : 리스트
##{ : dictionary


##차이점
## a.get('name') : 값이 없을때 None 반환
## a['name'] : 값이 없을 떄 오류 발생


##해당 key가 있는지 조사 : 'name' in a
##(in 연산)
##ex) if 'name ' in a 
##    ture 를 사용할수 있다


##set : 순서가 중요하지 않다
##set으로 부터 리스트도 만들 수 있다


##★자료형들 다시한번 복습!(눈여겨 봐야됨)
##a={'name' : 'pey', 'phone' : '0119993323', 'birth':'1118'}
##b= a.keys()
##print(b)

##c= list(a.keys())  
##리스트 반환
##print(c)

##d=a.values()
##print(d)

##b= a.items()
##print(b)


##영화 별점 데이터 실습
##dic안에 또 다른 dic 이 들어갈수 있다
#dic = {
#       "홍길동" : {"베테랑" :5.6, "암살" : 4.5}, 
#       "고길동" : {"베테랑" :7.6, "암살" : 9.5},
#       "김길동" : {"베테랑" :3.6, "암살" : 5.1}
#       }

#print(dic["홍길동"]) #홍길동이 영화평점 준것

#print(dic.get("홍길동").get("암살")) #홍길동이 암살에서의 평점을 보고싶을때1
#print(dic["홍길동"]["암살"])#홍길동이 암살에서의 평점을 보고싶을때2



##조건문

#answer=input("Would tou like express shipping?")
#a=answer.lower()                    #소문자나 대문자를 다 인식할수 있게끔
#if a == "yes":
        
#    print("That will be an extra $10")
#    #if 문 안에서 in이라는 연산자도 사용할 수 있다
#    #if문 들여쓰기에 주의할것




##a = [(1,2),(3,4),(5,6)]
##for (first, last) in a:
##    print(first+last)


##구구단(?다시짜보기)
#for i in range(2,10):
#    for j in range(1,10):
                
#        print("%d * %d = %d\n" %(i,j,i*j),end="")               #★★ 문자열 복습!!
#        #print(i*j, end="")
#    print('')


#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)


import turtle
for steps in ['red','blue','green','black']:
    turtle.colormode(steps)
    turtle.forward(100)
    turtle.right(90)
 #라이브러리가 풍부해서 파이썬의 장점이다 

#과제.../다음 시간 모듈(함수 만들고 라이브러리로 만들어 배포하는것까지) 파일 입출력까지 . 추가 과제)
       #모듈 끝난 후 클래스


