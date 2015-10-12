#10.12(월) 보충수업 파이썬

#glob 해당 디렉토리내의 파일들을 읽어서 반환(find구문처럼 사용)
#다음시간은 정규식

import os
import glob

os.chdir('C:/python34')
print(glob.glob(os.path.abspath('.'+'\\*.exe')))

#예제 무슨파일인가? traverse라는 함수 순차적으로 호출 ,모두 트리형태로 출력해주는함수

#ndir = nfile = 0
#def traverse(dir, depth):
#    global ndir, nfile
#    for obj in glob.glob(dir + '/*'):
#           if depth ==0:
#               prefix = '|--'
#           else:
#               prefix = '|' + '' *depth + '|--'
#           if os.path.isdir(obj):
#               ndir += 1
#               print(prefix + os.path.basename(obj))
#               traverse(obj, depth+1)
#           elif os.path.isfile(obj):
#                nfile += 1
#                print(prefix + os.path.basename(obj))
#           else:
#                print(prefix+'unknown object:',obj)
#if __name__=='__main__':
#     traverse('..',0)
#     print('\n',ndir,'directories,',nfile,'files')

#tempfile 잠깐쓸때 사용 기본모드는 'w+b'

import tempfile
with tempfile.TemporaryFile('w+',delete=False) as fp:
    fp.write('Hello world!')
    fp.seek(0)
    data = fp.read()
    print(data)

#print(os.rename('fp.name','asd.name'))
print(os.path.exists('fp.name'))   #''은 문자열로 바뀐다
print(os.path.isfile(fp.name))  #delete가 false이므로 true가 나옴

            
#time 중 sleep함수는 : 몇초동안 멈춰준다

#★★★★★시간값을 원하는 형태로 출력할줄 알아야된다!!
import time

time1 = time.ctime(1234567)
t = time.strptime(time1)
t2= time.time()
print(time1)
print(t)
print(t2)

#calender 달력볼수있는 함수   weekday(제일많이사용) :해당하는 날짜의 요일을 숫자로 반환 monthrange을 많이사용
import calendar

print(calendar.weekday(2015,10,12))
print(calendar.monthrange(2015,10))  #해당하는 달의 1일이 무슨요일이고 몇일까지 있는지

#random 잘사용할줄알아야되고 잘사용함 
#정수난수 발생시에는 나머지연산자 %를 사용한다
#choice:입력받은 리스트에서 무작위로 하나를 선택, 
#suffle:무작위로 섞어주는 함수
#sample(a,b) a에 들어가있는 값중에서 b개 선택

#1부터 100까지의 숫자중에서 20개 뽑고싶을떄
#for 문돌리지 않고 random.sample(range(100),20)을 하게되면됨

import random
print(random.sample(range(100),20))

#Q1)100개의 숫자중 10개를 뽑고 섞어서 하나 선택해봐라
a=random.sample(range(100),10)
random.shuffle(a)
print(random.choice(a))


#Q2) 똑같은확률이 아니라 특정리스트는 만들고싶다
# 각 칼라마다 각각의 가중치가 있는데 리스트를 만들어서 샘플링(초이스)하고 싶다

nlist = [('red',3),('blue',1),('green',4),('yellow',2)]
datalist =[]
for val, cnt in nlist:
    for i in range(cnt):
        datalist.append(val)

print(datalist)

import random
weighted_choices = [('red',3),('blue',1),('green',4),('yellow',2)]
population = [val for val, cnt in weighted_choices for in range(cnt)] #for문을 한번쓰고 싶을떄


#중간고사 시험범위는 웹브라우저까지
#중간고사 이후에는 외부 라이브러리를 가져다가 응용위주로 하겠다(project준비까지)
#os쪽 리눅스 셀프로그램작성했던..??