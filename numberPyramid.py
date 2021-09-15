# 숫자 피라미드의 높이를 입력 받아 다음과 같이 출력되도록 한다.
# 0가 입력되면 프로그램을 종료한다.
while True :
    height = int(input("숫자를 입력하세요:"))
    if height == 0:
        break
    for i in range(height):
        print(" "*(2*(height-i)-1),end=" ")
        for j in range(i+1) :
            print(2*j+1,end=" ")
        for j in range(i,0,-1):
            print(2*j-1,end=" ")
        print()