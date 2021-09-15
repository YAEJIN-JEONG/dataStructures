# 구구단의 단을 입력 받아 2단부터 입력 받은 단까지 수평으로 출력한다.
# 0이 입력되면 프로그램을 종료한다.
while True :
    dan = int(input("구구단의 단을 입력하세요:"))
    if dan == 0:
        break
    for i in range(1, 10):
        for j in range(2,dan+1) :
            print("%2d x %2d = " % (j, i), j * i,end="\t")
        print()
