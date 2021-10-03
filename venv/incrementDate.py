# 다음과 같이 파일 “input2.txt”에는 한 줄에 기준 날짜와 날짜 수가 주어진다.
# 기준 날짜에서 날짜 수만큼 진행한 후의 날짜를 출력한다.
# 하루를 증가시키는 멤버 함수 increment()를 구현하여 사용한다.
# 필요하면 보조 멤버 함수를 추가하여 사용한다.
class Date:
    def __init__(self, year, month, day,add):
        self.year = year
        self.month = month
        self.day = day
        self.add = add
    def __str__(self):
        return "{}/{}/{}       {}일 후 ==>".format(self.year, self.month, self.day, self.add)
    def __add__(self, other):
        return self.day+other.add

def lastDayOfTheMonth(self):
    if self.month == 1:
        self.lastDayOfTheMonth().day = 31
    if self.month == 3:
        self.lastDayOfTheMonth().day = 31
    if self.month == 5:
        self.lastDayOfTheMonth().day = 31
    if self.month == 7:
        self.lastDayOfTheMonth().day = 31
    if self.month == 8:
        self.lastDayOfTheMonth().day = 31
    if self.month == 10:
        self.lastDayOfTheMonth().day = 31
    if self.month == 12:
        self.lastDayOfTheMonth().day = 31
    if self.month == 4:
        self.lastDayOfTheMonth().day = 30
    if self.month == 6:
        self.lastDayOfTheMonth().day = 30
    if self.month == 9:
        self.lastDayOfTheMonth().day = 30
    if self.month == 11:
        self.lastDayOfTheMonth().day = 30
    if self.month == 2:
        if ((self.year % 4 == 0) and (self.year % 100 != 0)) or (self.year % 400 == 0):
            self.lastDayOfTheMonth().day = 29
        else:
            self.lastDayOfTheMonth().day = 28

def increment(self):
    if self.day == self.lastDayOfTheMonth():
        self.day = 1
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
    else:
        self.day += 1
    return self.day+self.add

def main():
    inFile = open("C:/Users/N20036/Desktop/input2.txt", 'r')
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()]
        lst.append(Date(date[0], date[1], date[2],date[3]))

    for i in range(len(lst)):
        self=increment(lst[i])
        print(lst[i]+self)
    inFile.close()

main()
