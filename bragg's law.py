import numpy as np

def Bragg(d,T) :
    y = (2* d*10**3)/ T
    return y

while True:
    
    print("움직인 거리(=몇번 돌리셨는지) 입력해 주세요! ")
    d = int(input())
    print("무늬가 몇번 바뀌었는지 횟수를 입력해주세요! ")
    N= int(input())
    lamda = Bragg(d,N)
    lamda0 = 632.8
    error = abs(((lamda0 - lamda)/(lamda0))*100)

    print("원래 주어진 파장값 ={0}nm , 우리가 실험으로 얻은 파장값 ={1}nm".format(lamda0,lamda))
    print("에러값은 {0}% 입니다.".format(error))
    print("다시 하실려면  1을 입력해 주시고 종료하고 싶으면 아무 숫자키를 입력해 주세요")
    e = int(input())
    
    if e != 1:
        break
    
    
