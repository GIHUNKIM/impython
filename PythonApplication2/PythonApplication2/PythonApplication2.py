#a = input('종료할까요? : ')
#a = a.lower()
#print(a)

#data=['a','b','c',['abcd','efg']]
#print(data[0])
#print(data[-1])
#print(data[-1][1])

#a=[]
b=[1,2,3]
c=['life', 'is', 'too', 'short']
#d=[1,2,'life', 'is']
#e=[1,2,['life','is']]
#f=b+c
#print(b+c)
#print(b*3)
#print(f)

#guests=['a','b','c','d']

#guests[0]='greenjoa'
#guests[1]=['greenjoa1','greenjoa2'] #1에 리스트 삽입
#guests[1:2]=['greenjoa1','greenjoa2'] #1<=x<2 범위내에 해당 값 삽입
#print(guests)

#print(guests.index('c'))   #c가 존재 하지 않을때 에러 발생

#아이디값이 3개있는 리스트 작성(패스워드 넣기 insert로)
data=['greenjoa1','greenjoa2','greenjoa3']
data.insert(3,'password1')
data.insert(4,'password2')
data.insert(5,'password3')
#부가적인 정보 더추가하기 (이름,번호 등등)
data.insert(6,'name1')
data.insert(7,'name2')
data.insert(8,'name3')
data.insert(9,'number1')
data.insert(10,'number2')
data.insert(11,'number3')
#print(data[0:])

#data2=range(4) #<0,4> 뜻은 0,1,2,3 까지 데이터를 내보내겠다는 의미
#print(data2)

#for steps in data :
#    print(steps)
scores=[85,62,63,45,90]
print(scores.sort())  # 오름차순으로 정렬
#scores.reverse()     # 반대로 순서가 바뀐다

for steps in range(4) :
    print(data[steps])   #

#top5 리스트 만들어 보기
#sort , reverse , [0:5] 범위연산자 사용









