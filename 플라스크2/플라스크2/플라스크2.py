#11.18(수) 플라스크2
#기본적으로 사용해야되는 폴더가 2가지가 있는데
# 1번째는 static이 있어야 한다
# template을 사용하여 html문서를 만들어놔야하는데 template 디렉토리 안에다가 넣어주어야 한다

#폴더 2개, static아래 폴더 하나 추가후 스타일시트 만들어서 소스 작성후
#<link rel="stylesheet" href="{{ url_for('static',filename='css/style.css') }}" 불러다가 사용하면된다
#그래서 html 파일에다 적용해야 하므로 html파일이 필요하다


#template 사용하기 위해서는 템플릿 엔진이 필요하다
#구조 : 템플릿과 데이터 객체를 엔진으로 합쳐서 랜더링된 html파일을 만든다

#from flask import Flask,render_template

#app = Flask(__name__)

#@app.route('/')
#def hello():
#    return render_template('hello.html')

#if __name__ == '__main__':
#    app.debug = True
#    app.run(host ='203.252.166.65',port=5000)

# 스타일 시트를 적용하여 웹페이지 글자색등을 바꿀수가 있다
# html 값들을 넘겨주어서 동적으로다가 html 구문들을 만들어 줄 수 있다

# ex) hello.html', name=name  -> name 변수는 html 파일안에 있어야 한다 {{name}} 넘어오는값

# 경로 하나에 매핑함수 하나일 필요는 없다


#신사엔진을 통해 랜더링된 html 파일을 만들어준다
#---------------이름, 타이틀 넣어보기-----------------
#from flask import Flask,render_template

#app = Flask(__name__)

#@app.route('/hello/')
#@app.route('/hello/<name>')  #웹브라우저 접속시 이름을 줄수 있다
#def hello(name=None):
#    return render_template('hello.html', name = name)

#if __name__ == '__main__':
#    app.debug = True
#    app.run(host ='203.252.166.65',port=5000)



#-----------------템플릿 안에 if문등을 넣을수 있다-------------
#%사이에 해당하는 구문들을 넣을 수 있다
#{# #} : 주석
#{% %} : if문 , for 문 제어문
#템플릿 페이지 안에서 해야 한다
#if문예제
#--------템플릿--------
#<body>
#    {% if name %}
#        <h1>{{name}}</h1>
#    {% else %}
#        <h1>Hello World!</h1>
#    {% endif %}
#</body>

#for문
#--------템플릿--------
#<body>
#    <h1>Hello World!!!</h1>
#    {% for item in items %}         #items 를 랜더링 하면될것이다
#    <li><a href="{{item.href}}">{{item.caption}}</a></li> # href랑 cap 두가지이므로 dir객체를 넘겨주면 될것이다
    
#    {% endfor %}
#</body>



#from flask import Flask,render_template

#app = Flask(__name__)

##@app.route('/hello/')
##@app.route('/hello/<name>')  #웹브라우저 접속시 이름을 줄수 있다
#@app.route('/')
#def hello():
#    data=[dict(href='http://www.naver.com', caption = '네이버'), dict(href="http://www.google.com",caption="구글")]
#    return render_template('hello.html', items = data)

#if __name__ == '__main__':
#    app.debug = True
#    app.run(host ='203.252.166.65',port=5000)


#--------템플릿--------
 #<h1>Hello World!!!</h1>
 #   {% for item in items %}
 #   <li><a href="{{item.href}}">{{item.caption}}</a></li>
    
 #   {% endfor %}

#데이터가 여러개일경우에 data를 쓰면 너무 길어지므로 묶음 데이터를 보낼수 있다
#data = { 'title : 'hello' }해서 dict객체를 만들어준다
#data넘길때는 **data로 넘겨주면 된다
#----------묶음 데이터 넘기기-----------------

#--------템플릿--------
#<head>
#    <meta charset="utf-8" />
#    <title>{{title}}</title>
#    <link rel="stylesheet" href="{{ url_for('static',filename='css/stylesheet1.css') }}">
#</head>
#<body>
#    <h1>{{name}}</h1>
    
#</body>


#from flask import Flask,render_template

#app = Flask(__name__)


#@app.route('/')
#def hello():
#    data ={
#        'title' : 'Hello',
#        'name' : 'greenjoa',
#        }

#    return render_template('hello.html', **data)

#if __name__ == '__main__':
#    app.debug = True
#    app.run(host ='203.252.166.65',port=5000)




#----------------상속-----------------
#템플릿도 상속을 할 수 있다
# 바꾸고 싶은곳에다가 {% block 블록 이름 %} 요부분에 해당하는 부분을 재정의해주면된다
#부모를 만들어 놓고 바뀌는 부분에 해당하는 부분 body부분을 
#상속받는 코드는 extends 를 쓰면된다
#본인이름 출력해보기 상속받아서 


from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    

    return render_template('main.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host ='203.252.166.65',port=5000)

#플라스크 이용하여 서버를 사용할 수 있다.


#다음시간 DB연동하여 사용한다
#플라스크 튜토리얼 예제 : 게시판같은곳에 글남기는것 글에 해당하는 목록정보
