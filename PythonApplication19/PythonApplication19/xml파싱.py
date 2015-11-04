# 11월 2일(월) 파이썬
#xml 문서를 파싱해보기로 하자
#html은 고정적인 태그를 쓰는 반면에 xml은 자유롭게 태그를 사용할수 있다



from bs4 import BeautifulSoup

f = open('text.xml')
xml = f.read()
soup = BeautifulSoup(xml)
for node in soup.findAll('node'):
    print("Node : "+node.string)
    print("Attr1 : "+node['attr1']) 

#파일 오픈할때 솔루션 탐색기에서 추가 기존항목으로 xml파일 만들기!

f = open('song.xml', encoding='utf-8')
xml = f.read()
soup = BeautifulSoup(xml)
for nodes in soup.test('song'):
    for node in nodes:
        print(node.string)


import re

f = open('alcohol.xml', encoding='utf-8')
xml = f.read()
soup = BeautifulSoup(xml,'html.parser')
if soup.alcohol('cate1') == "안주": 
 for nodes in soup.alcohol('cate1'):
    print('Cate 1:' + nodes['tt'])
    for node in nodes('cate2'):
        print('\tCate2 :' + node['tt'])
        for item in node('item'):
            print('\t\t' + item.string)


#카테고리중에서 안주에 해당하는것만 출력해보기


#과제가 있다 open api를 설정하여 그룹과제
# 반드시 github를 만들어서 공유할수 있도록 하라
# 이력이 남도록 해야 된다 / 주소는 교수님께 보낼수 있도록하라
#내가 원하는 데이터의 형태를 뽑아 내야된다....

#json 은 xml보다 경량화 되어있는데 자료표현
#크게 2가지 함수로 사용해서 파이썬 -> json : dumps()
#                           json -> 파이썬 : loads()


import json
data = {1:'a',2:'b'}
data2 = json.dumps(data)
data3 = json.loads(data2)
print(type(data2))
print(type(data3))


s= """
{
"name": "cybaek",
"detail" : {"last":"baek"},
"emails":["cybaek@xxx.com","cybaek@yyy.com"]
}
"""

data = json.loads(s)

print(data['detail']['last'])

#과제할떄 외부라이브러리 안되는경우가 있는데 형태가 다르거나 문의를 해서 해결할수 있도록 하라

#16쪽 : json에 해당하는것을 뷰티풀솝처럼 .누르면 해당하는것이 나오는것처럼 하고싶을때
#사용하기 편하게 프로그램을 조금 변경을 시켜줄수 있다
#jsonObject라는 클래스를 만들어 사용할수 있다.




class JsonObject:
    def __init__(self,d):   #dic정보를 넣어 d. 머시기로 사용할려고 생성자를 만들어준다(키와 vluse로 사용할려고)
        self.__dict__= d

data = json.loads(s,object_hook=JsonObject) 
    #클래스를 만들어서 object_hook을 써줘야 한다!!  

print(data.name)



#-----------------------------파싱 끝 
#html xml json 이들어오건 사용할수 있어야 한다
#다음주에 프로젝트 주제 발표..... 프로젝트 주제 뭘로 할지..(기간 4주) 마지막주 발표