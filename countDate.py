class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return "{}/{}/{}       {}/{}/{}==>".format(self.year, self.month, self.day, self.year, self.month, self.day)

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
    return self

def main():
    inFile = open("C:/Users/N20036/Desktop/input2.txt", 'r')
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()]
        lst.append(Date(date[0], date[1], date[2],date[3],date[4],date[5]))

    for i in range(len(lst)):
        print(lst[i])
    inFile.close()

main()