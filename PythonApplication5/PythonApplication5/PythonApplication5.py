########Report 1-1 #############
###[과제 1-1] 반지름이 200인 원을 그리고, 거북이를 원을 따라 한 바퀴 움직이게 하시오.

#import turtle  
#wn = turtle.Screen() #거북이가 거주할수 있는 공간 작성
#wn.title("[Report 1-1]200913975 김기훈") # title 이름 변경

#t = turtle.Pen() #t는 turtle의 인스턴스
#t.shape("turtle") #커서모양 바꾸기 
#t.color("yellow")
#t.penup()
#t.setposition(0,-150)
#t.pendown()


#for step in range(2):
#    t.fillcolor(1,0,0)    #컬러바꾸기(r,g,b) 
#    t.begin_fill()    #면 채우기
#    t.circle(200)     #원그리기(반지름) 
#    t.end_fill()      #면 채우기
    
    
######Report 1-2 #############
#[과제 1-2] 원의 중앙(0,0)에 거북이를 위치시킨 후 원 안에서만 특정 값(Ex, 5) 만큼씩 직진하게
#한 후 원을 벗어나게 되면 랜덤하게 각도를 변경하여 다시 직진을 수행하도록 반복 수행하시오.
#즉 원의 테두리에 부딪히게 되면 방향전환하여 다시 직진을 수행토록 하시오.

import turtle
import random
import math

wn = turtle.Screen() #거북이가 거주할수 있는 공간 작성
wn.title("[Report 1-2]200913975 김기훈")

t = turtle.Pen()   
t.shape("turtle") #커서모양 바꾸기 
t.speed(30)
t.penup()
t.setposition(0,-190)
t.pendown()
t.fillcolor(1,0,0)    #컬러바꾸기(r,g,b) 
t.begin_fill()    #면 채우기
t.circle(200)     #원그리기(반지름) 
t.end_fill()   
t.penup()
t.setposition(0,0)
t.color("yellow")


while 1:
   for i in range(30):
        #t.goto(10,10)
        #t.towards(0,0)
        t.penup()
        t.forward(5)
        t.speed(1)                  #거북이 속도 조절
        p=t.position()
        x=p[0]
        y=p[1]
        if math.pow(x,2) + math.pow(y,2) >= 40000:
            t.left(random.randrange(1,170))
            

                  


        

          