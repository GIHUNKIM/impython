#coding:cp949


def printData(data, level=0):
    for item in data:
        if isinstance(item, list):
            printData(item, level+1)
        else:
            for i in range(level):
                print("\t",end="") # \t는 탭출력 , end=""는 줄바꿈
            print(item) #실제로 출력되는 부분은 이부분임 이전에 for문을 사용하여 출력을 해준다