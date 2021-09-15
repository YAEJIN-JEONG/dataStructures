#구구단의 단을 입력 받아 역순으로 출력한다. 0이 입력되면 프로그램을 종료한다.
while True:
    dan=int(input("구구단의 단을 입력하세요:"))
    for n in range (9,0,-1) :
        if dan == 0:
            break
        print("%2d x %2d = "%(dan,n),dan*n)
