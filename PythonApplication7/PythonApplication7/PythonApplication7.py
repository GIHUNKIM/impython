########Report 1-1 #############
###[과제 1-1] 반지름이 200인 원을 그리고, 거북이를 원을 따라 한 바퀴 움직이게 하시오.

import turtle  
wn = turtle.Screen() #거북이가 거주할수 있는 공간 작성
wn.title("[Report 1-1]200913975 김기훈") # title 이름 변경

t = turtle.Pen() #t는 turtle의 인스턴스
t.shape("turtle") #커서모양 바꾸기 
t.color("yellow")
t.penup()
t.setposition(0,-150)
t.pendown()


for step in range(2):
    t.fillcolor(1,0,0)    #컬러바꾸기(r,g,b) 
    t.begin_fill()    #면 채우기
    t.circle(200)     #원그리기(반지름) 
    t.end_fill()      #면 채우기
    