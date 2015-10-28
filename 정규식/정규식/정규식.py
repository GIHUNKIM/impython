#10.26(월) Python
# 다다음주에 그룹과제가 나간다(open API 사용하는것) : 프로젝트 주제와 관련된것 선정할것
# 프로젝트 주제 선정할것 !
#<복습내용>
#re.compile 을 하게되면 다른곳에서 사용할수 있게 할수 있다


#<정규표현식2>

#findall : 만족하는 모든것을 찾아서 반환시켜주는 함수

import re

#str = """Window
#Unix
#Linux
#Solaris"""
#p = re.compile('^.+',re.S)                            #^ : 처음시작하는것
##print(p.findall(str))
#result = p.search(str)
#print(result) 
##search 와 findall 이 해당함수에 따라 약간씩 적용이 다르다



#그룹에 해당하는 이름을 줄수 있다
#m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
#print(m.group('first_name'))
## 그룹이름으로 자기가 원하는것을 출력 할 수 있다
#print(m.groups())


#m = re.match(r"(\d+)\b(\d+)?" ,"24 23 45")
#print(m.groups())
#print(m.groups(0))   

#m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)","Malcolm Reynolds")
#print(m.groupdict()) # dic 형태로 출력된다


p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

#: 앞에 것만 나오게 하고 싶을 때  (?=:)
#p = re.compile(".+(?=:)")



#현재 디렉토리를 C: 디렉토리로 옮겨봐라 : import os
import os

os.chdir('C:\\')
#현재디렉토리에 있는것 중에서 현재 디렉토리에 있는 파일 찾아오는것 : import glob
import glob       #glob.glob 을 하면 현재 디렉토리에 있는 모든것을 반환을 한다
glob.glob('C:\\')
#??????????????????????????
p = re.compile('.*[.](?!bat$|exe$).*$')



#Lookbehind
# 패턴에 만족하는것 뒤에것만 반환을 한다
p = re.compile("(?<=abc)def")
m = p.search("abcdef")
mm = re.search('(?<=-)\w+','spam-egg')
print(mm.group())


#인덱스 위치가 m다음인지 그위치인지 확인할것! (start에서)
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
print(m.start())  #7이라는값
print(m.end())#18 g에 해당되는 인덱스까지 감
result = email[:m.start()] + email[m.end():]
print(result)



# %r 이라는 포멧팅 문자열은 repr()로(문자열은 문자열인데 바로 실행할수 있는 문자열일떄))
# %s : str()을 사용하여 변환할수 있다

#포커만들기

def displaymatch(match):
 if match is None:
  return None
 return '<Match: %r, groups=%r>' % (match.group(), match.groups())

valid = re.compile(r"^[a2-9tjqk]{5}$")
print(displaymatch(valid.match("akt5q")))



#string 에서 사용했던 split 함수도 정규식에서 사용하고 있다
text = """Ross: McFluff: 834.345.1254: 155 Elm Street
Ronald: Heathmore: 892.345.3428 436: Finley Avenue
Frank: Burger: 925.541.7625 662: South Dogwood Way
Heather: Albrecht: 548.326.4584 919: Park Place"""
entries = re.split("\n", text)
result = [re.split(":?", entry, 4) for entry in entries]
print(result)




#웹으로 데이터를 다운로드 받아서 내가 원하는 것만 찾아내는 작업을 하고싶을때도 있을것이다
#웹에 해당하는 문서를 다운로드받을때 사용할수 있는 라이브러리 Urllib
#몇가지 모드들이 포함되어있다 url 문서 오픈하고 읽을 수 있는 
#Urllib.request : open해당 해당문서를 가지고 올수 있게 하는라이브러리
#함수는 urlopen()을 사용하면 해당 정보를 가져올수 있다
#import urllib.request
#with urllib.request.urlopen('http://www.python.org/'#가지고 오고싶은 해당주소) as f:
# print(f.read())       #읽어올때는 read 함수 사용
# print(f.read(300)) #300 byte
# print(f.read(300).decode("utf-8")) #encoding mode utf-8

#읽어와서 타이틀만 뽑아내봐라
import urllib.request
with urllib.request.urlopen('http://www.naver.com/') as f:
    a = f.read().decode("utf-8")
    p = re.compile(r"(^/<title/>).*(/<//title/>$)")
    m = p.search(a)
    #d = p.group(1)
    print(m)



 #다음주에 퀴즈한번본다.....
