##10.28(수) 
##다음주 월요일 퀴즈 실시
## 요청하는 웹사이트로 부터 문서를 받을 수 있다(자바 일수도 있고 json일수도 있다 , xml 일수도 있다
## 정규식을 잘사용하면 정규식을 가지고 다 찾아낼수 있고 파싱을 할수 있다 ( 라이브러리가 있다)
## BeautifulSoup 이라는 라이브러리가 있다
##HTML과 XML 을 파싱하는 라이브러리 (디폴트가 아니라 별도로 설치를 해야한다)
## 인스톨 설치시 pip install beautiful 리눅스에서 pip가 wum(얌)이라는 것으로 설치 했었다


##프로젝트 주제선정시 외부라이브러리를 가져다가 사용할텐데 현재는 2.7버전위주의 라이브러리가 많지만
##잘 찾아보면 3 라이브러리가 있다


#from bs4 import BeautifulSoup
#import bs4

#html_doc= """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#"""

#soup = BeautifulSoup(html_doc, "html.parser")  #뷰티풀솝이라는 객체를 만들어야 한다 (앞에는 파싱해야할 문서, 두번째는 파서종류(넣주지않으면 html.parser(기본파서))
#print(soup.prettify())   #prettify : 예쁘게 출력해줘라
#print(soup.a.prettify())




##원하는 태그부터 시작할수 있다  soup.title
#import re
#p = re.compile(r"<title>(.+)</title>")
#a = p.search(html_doc)

#print(a.group(1))
## 태그안에 다른 태그가 없을 경우 string속성으로 태그 내용을 얻을 수 있다
## soup.title.string

##print(soup.p)
#print(soup.a['href'])
#print(soup.a['href'])

##모든 태그 목록 반환
#print(soup('a',{'class' : 'sister'}))#태그 중에서 조건에 해당되는 것만 가져올수 도 있다
#print(soup('a',{'id' : 'link3'}))    # 조건식을 만들 수 있다

##부모에 해당하는 정보 출력 : parent

#print(soup('a')[0].parent)




#find : 처음만나는것 해당 태그를 반환한다
#soup.find_all(id='link3') 태그의 속성별로 출력할수 있다

#soup.find_all(class_='sister') 조건사용할때 class_= 로 해야한다

#print(soup.find_all(class_='story'))
#print(soup.find_all(class_='id'))




#웹툰에해당하는 목록가져오기



from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
import urllib
import webbrowser

url= "http://comic.naver.com/webtoon/list.nhn?titleId=626907"

data = urlopen(url)
#webdata = data.read().decode("utf-8")
#print(webdata)  #데이터 읽어주는 역할

soup = BeautifulSoup(data, 'html.parser')

cartoons = soup.find_all('td',{'class':'title'})

for i in range(len(cartoons)):
    title = cartoons[i].find('a').string
    ref = cartoons[i].find('a')['href']
    tempurl= urljoin(url, ref)
    print(title, " " , tempurl)
    #webbrowser.open_new(tempurl) #웹브라우저에 창이 뜬다
#print(soup.prettify()) 여기서는 prettify 가 안된다

##웹브라우저 열고싶을떄 webbrowser.open_new(tempurl)
#원하는것만 파싱해서 데이터를 가지고 올수도 있다



#웹에 해당하는것을 크롤링 하는것을 가지고 오고 싶다
#다이닝코드에 해당하는것도 데이터가 필요하다 크롤링 :다 수집해다가 파싱해서 링크가 있는 부분을 찾아가서 계속 도는것 
#Crawler class 기본적인 내용이지만 나중에는 DB에 저장해서 분석도 하는것까지 확장시켜보자




class crawler:
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpage= set()
            for page in pages:
                try:
                    c = urllib.request.urlopen(page)
                except:
                    print("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), from_encoding="utf-8")
                print('Found %s' % page)
            links = soup('a')
            for link in links:
                if('href' in dict(link.attrs)):
                    url = urllib.parse.urljoin(page, link['href'])
                    if url.find("'")!=-1 : continue
                    url = url.split("#")[0]
                    if url[0:4]=='http':
                            newpage.add(url)
            pages = newpage


pagelist = ['http://www.naver.com']
crawler = crawler()
print(crawler.crawl(pagelist)) #db에 파싱하는것까지 해본다