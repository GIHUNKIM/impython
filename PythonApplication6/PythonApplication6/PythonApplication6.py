#9.16(수) 파일다루기
#파일다루기 마치고 전체적인 과제2 나갈예정
#default 값은 r(read the file)
#파일은 반드시 open했으면 close를 해주어야 한다
#전체읽기 : ex) myFile.read() 
#라인단위 : readline() / 파일의 끝은 None으로 출력됨(none=false)
#★파일을 read했을경우 반드시 close 해주어라

#coding:cp949
#fileName = "greenjoa.txt"
#with open(fileName, "w+#기존파일은 없어지고 새로만들어진다") as myfile :   #with로 open시에는 따로 close안해도 된다 자동으로 닫힘
#    #myfile.write("20101111 홍길동\n")
#    #myfile.write("20101111 고길동\n")
#    #myfile.write("20101111 김길동\n")
#    #myfile.write("20101111 이길동\n")
#    content = myfile.Read()
#    print(content)                              #파일이 w+라 새로만들어져서 다 지워짐

#with open(fileName, "r") as myfile :  
#    content = myfile.read()                      #파일을 읽어온다
#    print(content)                  

#readlines사용 파일의 모든 내용을 리스트에 저장하기
#with open(fileName, "r") as myfile :  
#    content = myfile.readlines()
#    #for line in content:
#    for line in myfile:
#        print(line)
        
        
        
#프렌즈 대사 내용에 대해 주인공에 해당하는 내용만 가져오기                 
#fileName = "파일입출력예제1.txt"
#fileName2 = "Monica.txt"
#with open(fileName, "r") as myfile, open(fileName2, "w") as monica :   #readlines과 같음
#    for line in myfile:
##string의 함수중에서 분리해줄수 있는 함수(split)
#        (role, etc) = line.strip().split(":")  #strip 공백 없애는 함수, 자른후 앞은 role 뒤는 etc
#        #if role == "Monica" :
#        #    print(role, etc)
#        if( role == "Monica" ) :
#          monica.writelines(etc)
#          monica.writelines("\n")
#fileName = "Monica.txt"
#with open(fileName, "r") as myfile, open(fileName2, "w") as monica :  #파일을 하나 더 열어준다



#문장안에 : 하나가 아니라 여러개가 있을경우에
#filename = "파일입출력예제2.txt"
#filename2 = "Monica.txt"
#with open(filename, "r") as myfile, open(filename2, "w") as monica :
#    for line in myfile:
#        (role, etc) = line.strip().split(":",1)  
#        if( role == "Monica" ) :
#          monica.writelines(etc)
#          monica.writelines("\n")

#python.org  1.pypi  사용자들이 라이브러리 공유고있다  2. docs 3.43에 해당하는 거 쳐봐도 도움많이된다\
# doc 라이브러리에 들어가면 split에 해당하는 사항을 확인할수 있다
          

#나오는 주인공대사 롤만 리스트에 저장
#filename = "파일입출력예제2.txt"
#filename2 = "Monica.txt"
#roles = []
#with open(filename, "r") as myfile, open(filename2, "w") as monica :
#    for line in myfile:
#        (role, etc) = line.strip().split(":",1)  
#        roles.append(role)
#print(roles)
#메모리에서 사용하던 저장하던 데이터들을// 리스트를 그대로 파일에 저장했다가 읽었을떄 리스트 그대로 읽어내는것          
#이런 라이브러리가 있다

import pickle   #pickle 두가지 함수를 통해서 저장(dump)하고 읽어옴(load)
#읽고 쓰는 모드가 바이너리라서 b가 같이 쓰임 db,lb
filename = "파일입출력예제2.txt"
filename2 = "Monica.txt"

roles = []
with open(filename, "r") as myfile, open(filename2, "wb+") as monica :
    for line in myfile:
        (role, etc) = line.strip().split(":",1)  
        roles.append(role)
    pickle.dump(roles, monica)
    
with open(filename2, "rb") as monica :   #fristtype defrence
    result = pickle.load(monica)
    print(result)



    #csv파일 과제를 통해 알아볼것
    #엑셀에서 다른이름 저장하면서  csv형식으로 저장할것
    #엑셀은 엑셀파일 메모장은 ,로 구분되는 파일이 열린다
    