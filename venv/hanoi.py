# 하노이 탑을 구현한다. 원판의 수를 입력 받아 0가 될 때까지 진행하며 원판의 이동과 이동 횟수를 출력한다.
def hanoi_tower(n,fr,tmp,to):
    if(n==1):
        print("원판 1 : %s --> %s"%(fr,to))
    else:
        hanoi_tower(n-1,fr,to,tmp)
        print("원판 %d : %s --> %s"%(n,fr,to))
        hanoi_tower(n-1,tmp,fr,to)


while True:
    num = int(input("원판의 수를 입력하세요:"))
    rst=1
    if num == 0:
        break
    for i in range(1,num+1):
        rst=rst*2
    hanoi_tower(num,'A','B','C')
    print()
    print("이동 횟수 :"+str(rst-1))
    print()

