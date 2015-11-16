#11.16(월) python 플라스크
#플라스크 : 마이크로 웹 프레임 워크(빠르게 간단하게 웹서버를 만드는 프레임 워크)
#프로젝트별로 가상환경 만들어서 프로젝트를 생성해줄수 있는 virtualenv 라이브러리가 있다.
#1.virtualenv 설치하기
#2. 가상환경 만들기  c:\myWeb> virtualenv myenv
##3. c:\myWeb\myenv\scripts\activate.bat bat 파일 실행
#가상디렉토리에서 실행하면 라이브러리가 이폴더 안에 설치가 된다.

#비쥬얼베이직에서 사용을 하려면 기존 python34로 되어있어서 가상디렉토리로 바꿔줘야한다

#장고보다는 플라스크쪽으로 사용자들이 많아지는 추세이다(가볍기 때문에)


#flask 도  3.4 계열에서는 아직 안정화 되있다 2.버전은 완벽한것이 3.대는 아직 완벽하지 않지만 보완하고 있는 중이다
#python –m pip install flask 설치하기 cmd창에


#-------------------------웹페이지 하나 만들기----------------------------------
#route : 경로지정 / 를 붙였을때 hello world 를 호출시키라는 뜻
# 특징 몇줄 안되는 소스로 웹서버를 돌릴수 있다.


#from flask import Flask

#app = Flask(__name__)

#@app.route('/profile/<username>')
#def get_profile(username):
#    return 'profile :' + username

#def hello_world(): 
#    return 'Hello World!' 

#if __name__ == '__main__': 
#    #app.debug =True
#    app.run(host='203.252.166.65', port=5000) 
    #run 할때 디버깅모드를 설정할수 있다 기본이 false인데 true하면 에러가 났을때 원인이되는것을 보여준다
    #디버그는 개발할때만 사용하고 실제 사용할때는 true로 쓰면 안된다.(베포하고나서)
    #app.debug=True #소스 변경과 디버거 제공 
    #app.run(host='***.***.***.***', port=****)  #웹에 호스트랑 포트를 지정해줄수 있다
    #포트번호 지정하지 않으면 기본 5000번이 루트로 지정된다




#flask 실행과정 
# 1 사용자들은 URL을 가지고 호출하며 
# 2. 서버에 접속하여 경로에 따른 함수매핑(decorator) 사용자에게 보여줄 view를 보여준다(hello world 함수)

#-------------라우팅------------------
#rout() 복잡한 URL을 쉽게 연결할수 있는 데코레이터 함수
#ex)@app.route('/hello')  http://localhost:5000/hello hello까지 해야 불러올수 있다




#------------동적라우팅--------------
#<변환타입: 변수> defalut는 문자열 ex)@app.route('/profile/<username>')기본 문자열
#<int:message_id>로 설정해서 int로 받겠다
#from flask import Flask, url_for

#app = Flask(__name__)

##@app.route('/profile/<username>')
##def get_profile(username):
##    return 'profile :' + username

#@app.route('/')
#def hello_world(): 
#    return 'Hello World!' 

#@app.route('/login')
#def login():
#    return 'login'

#if __name__ == '__main__': 
#    #app.debug =True
#    app.run(host='203.252.166.65', port=5000) 






#------------URL와 리디렉션-------------------
#Url 규칙은 아파치 웹서버나 동일한 형태로 하면 된다.
#아파치 서버에서 url 끝에 뒤에 슬래쉬(/)가 붙은 경우아 안붙은경우가 약간의 차이가 있었다
#플라스크에서는 /가 없이 입력해도 /가 포함된 URL을 만들어준다



#----------------url_for----------------
#지금은 호출되는 형태가 url정보를 가지고 특정함수를 호출하는 것이다
#그반대에 해당하는것..특정함수를 호출했을 떄 url정보를 만들어내야하는 경우가 종종있다 
#그때 사용하는것이 url_for 함수(import 시킨다)
#url_for : 특정함수를 호출하는 url을 반환해주는 함수
#-(함수명, 인자에 해당하는값(url로 전달되는 값)
#ex) url_for('get_profile', username='greenjoa') : url에 해당하는 정보를 반환
#with app.test_request_context():
#    print(url_for('get_profile', username='greenjoa'))
#app.test_request_context() 함수 : http요청을 test해보는 함수 



#-----------------로그인이라는 함수 하나 만들어보자-----------
#헬로월드호출했을 때 로그인으로 가게끔 만들어봐라
#특정 웹페이지에서 다른곳으로 경로를 이동시켜보자
from flask import Flask, url_for, redirect
app = Flask(__name__)

#@app.route('/profile/<username>')
#def get_profile(username):
#    return 'profile :' + username

@app.route('/hello')
def hello_world(): 
    return redirect(url_for('login'))  #함수 이름을 주어라
            #함수를 호출했을때 경로가 호출된다 url for
            # url_for('login') 내가한것
            

@app.route('/login')
def login():
    return 'login'

if __name__ == '__main__': 
    #app.debug =True
    app.run(host='203.252.166.65', port=5000) 




#------------request------------------------
#http 요청에 관한 정보를 담고 있는 전역객체
#크게 3가지 속성 사용
#method : http 메소드가 어떤 방식으로 요청됬는지 정보를 담고 있는다.(get,post등)
#args : get방식으로 전달된 정보를 알고싶을때
#form : post방식의 전달할떄 html 폼 참조할때
#3가지를 이용하여 참조를 할수 있다
#default는 get방식
#@app.route('/profile/', methods=['POST','GET'])
#def profile(username=None):
#error=None
#if request.method == 'POST':
#username = request.form['username']
#email = request.form['email']
#if not username and not email:
#return add_profile(request.form)
#else:
#error = 'Invalide username or email'
#return render_template('profile.html', error=error)




#----------------------------정적파일---------------
#웹페이지를 만들때 사용하게 되는 자바나 이미지 css는 정적파일이라고 한다
# 지정된 경로가 정해져 있다!(/static 디렉토리를 만들어주어야 한다)
#app하위폴더에 넣어 주어야한다 다른곳에 느면 안된다.

#예제 튜토리얼에 있는 css파일 긁어왔다 이걸 static(프로젝트 폴더안에 만들어준다)안에다가 만들어주어야 한다
#이 파일을 적용하는 방법은 html이 있어야 한다
