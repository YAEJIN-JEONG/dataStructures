# 파일 “input.txt”에 있는 연, 월, 일로 주어진 날짜를 읽어 출력하고 가장 오래된 날짜와 가장 늦은 날짜를 출력하도록 한다.
# 문제를 해결하기 위해 Date 클래스를 다음과 같이 정의하고 멤버 함수를 구현한다.
# 실행하기 위함 함수 main()은 주어진 파일을 읽어 날짜를 리스트에 저장한다.
# 날짜를 모두 읽은 후 리스트에 저장된 날짜를 출력하고 findMinMax() 함수 사용하여 리스트에 있는 날짜에서 가장 오래된 날짜와 가장 늦은 날짜를 출력한다.
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __gt__(self, rhs):
        return self.year > rhs.year

    def __lt__(self, rhs):
        return self.year < rhs.year

    def __str__(self):
        return "{}/{}/{}".format(self.year, self.month, self.day)


def findMinMax(lst):
    min = lst[0]
    max = lst[0]
    for i in range(1, len(lst)):
        if max < lst[i]: max = lst[i]
        if min > lst[i]: min = lst[i]
    return min, max


def main():
    inFile = open("C:/Users/N20036/Desktop/input.txt", 'r')
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()]
        lst.append(Date(date[0], date[1], date[2]))
    for i in range(len(lst)):
        print(lst[i])
    min, max = findMinMax(lst)
    print()
    print("earlist date:", min)
    print("latest date:", max)
    inFile.close()

main()
