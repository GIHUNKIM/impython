#10.14(수)
# 중간고사 이후 정규표현식 진행
#시험은 월요일날 진행 (PDF파일로 가지고 온것만 열수있다)
#프린트 및 책 사용 가능

#정규표현식 : 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어(자바나  c++에서도 지원)
#각 언어마다 정규표현식을 사용하게해주는 모듈이 있다.
#반복메타문자
# *(아스트리크)  ex) ab라는 문자가 0회이상 반복
# + 꼭 1번이상은 반복되어야 한다 ex) ab+c : abc, abbc
# ? 0회 또는 1회를 의미 ex) ab?c : ac, abc
# {m} m회 반복  / {m, n} m회부터 n회까지


#매칭 메타 문자
# . : 줄바꿈을 제외한 모든 문자와 매치 만약 줄바꿈을 표현하고 싶을때 DOTALL 옵션을 주면 줄바꿈도 대체가능하다
# ^ : 문자열의 시작과 매치 Multiline 모드에서는 /
#[]기호는 문자의 집합을 나타낸다
# ^ : 시작에서 매치 , $ : 끝에서 매치
# | : or을 의미
# () : 정규식에 찾고자 하는게 여러개이면 ()로 묶어주면된다(하나의 그룹으로 된다)


#이스케이프 기호

#정규식을 표현하는 모듈 re모듈( import re)로 사용
#re.compile(정규식(패턴을 넣는다))
#re.IGNORECASE : 대소문자 구분안하겠다
#\\\\ : \를 2번표현하고 싶을떄 이렇게 써야되지만 앞에 r을 붙이면 2번만 쓰면됨 . r\\
#match는 딱맞아야되는것만 찾아주고 search는 포함된것 다찾아줌

#re객체에 패턴을 만들어놓게되면 re.match('ab*','abbbb')는 매치에서밖에 못쓰지만 객체를 만들면 여러곳에서 사용가능

#search
#string의 전역에서 일치하는 부분을 찾아 매치 오브젝트로반환  //#group은 인덱스가 1부터 시작함


import re
#pattern = re.compile("d")
#result = pattern.search("dog")
#print(result)                      #span 0에서 매치가 되었다  match object로 반환한다
#result = pattern.search("dog",1)
#print(result)
##r에서 공백사용하고 싶을때 r" " 이렇게 or \ 이렇게

#pattern = re.compile("o")
#result1 = pattern.search("dog")
#print(result1.group())
#result = pattern.search("dog",1)
#print(result1.group())

#플래그

#str = """Sample1.
#        Sample2.
#        Sample3. """

##p = re.compile('^.*',re.S) #패턴을 처음부터 뒤에는 아무거나 들어갈수 있다 라고 만드
##result3 = p.search(str)
##print(result3.group())


##마지막 문장만 추출하고 싶을떄
#p = re.compile('.*$') #패턴을 처음부터 뒤에는 아무거나 들어갈수 있다 라고 만드
#result3 = p.search(str)
#print(result3.group())

#pattern = re.compile("\s*[a-zA-Z]+\s+(\d+)+\s+([a-zA-Z]+)\s*");#%%%정규식객체 추출하는거 많이사용한다
#result = pattern.match(str)

#p = re.compile("o[gh]") #og나 oh에 해당되는 것을 찾는다
#re = p.fullmatch("dog")
#print(re)
#re = p.fullmatch("ogre")
#print(re)
#re = p.fullmatch("doggie",1,3)  #span범위가 1,3이면 1,2에 해당되는것만 찾는다
#print(re)


#p2 = re.compile("\W+")
#re2 = p2.split('words, words, words.')
#pritn(re2)
#re2 = p2.split('words, words, words.',1)
#pritn(re2)

pe = re.compile("x*")
ree = pe.split('axbc')
print(ree)

pattern = re.compile("x")
result = pattern.split('axbc')
print(result)
result = re.sub(r'\W','','a:b:c, d.')

#정규식 배운이후에 html에 대한 파싱ᄁk지 배울것이다

str= '<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*?)">', str)   #옵션없이 매칭을 하게되면 탐욕적인 매칭이되서 끝에있는 > 까지 찾아줌으로 최소매칭을 해야된다
print(result.group(1))                     #그래서 뒤에다가 ?(최소매칭)를 붙여주면된다


#Q1 str에 해당되는게 주민등록 번호인데 주민등록 번호 포맷이 맞는지 맞다 하면 잘라내라
#123456-123456

str = "123456-1234567"
#pattern = re.compile((\d{1,6})+r'-'+(\d{1,7}))
#정규식\d{6}-\d{7} or (\d{6})-(\d{7})
#result = pattern.match(pattern.split("-")
#match를 쓰면 자릿수가 바뀌었을 때 안나오므로 fullmatch를 사용해야된다
result = pattern.fullmatch(str)
print(result)


