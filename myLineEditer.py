class ArrayList:

    def __init__(self):
        self.items = []

    def add(self, elem):
        self.items.append(elem)

    def remove(self, elem):
        for i in range(self.size()):
            if self.items[i] == elem:
                self.items.remove(elem)
                return print(elem, " removed")
        return print('No such element')

    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos):
        return self.items.pop(pos)

    def isEmpty(self):
        if self.size() == 0:
            print("True")
        else:
            print("False")

    def getEntry(self, pos):
        return self.items[pos]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def find(self, item):
        return self.items.index(item)

    def replace(self, pos, elem):
        self.items[pos] = elem

    def sort(self):
        self.items.sort()

    def merge(self, lst):
        self.items.extend(lst)

    def print(self, msg="ArrayList"):
        print(msg, self.size(), self.items)

    def search(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return print(item, ' found')
        return print('No such element')

    def dup(self):
        new_list = []
        for i in self.items:
            if i not in new_list:
                new_list.append(i)
        self.items = new_list


def myLineEditor():
    list = ArrayList()
    filename = 'input.txt'
    infile = open(filename, "r")
    lines = infile.readlines()
    for line in lines:
        list.insert(list.size(), line.rstrip('\n'))
    infile.close()
    for line in range(list.size()):
        print('%d> ' % (line + 1), end='')
        print(list.getEntry(line))
    while True:
        c = input().split()
        command = c[0]
        if command == 'i':
            pos = int(c[1])-1
            while True:
                s=input()
                if s =='*':
                    break
                else:
                    elem = s
                list.insert(pos, elem)
                pos=pos+1
        elif command == 'd':
            p1 = int(c[1])-1
            p2 = int(c[2])
            for i in range(p1,p2):
                dnum=p1
                list.delete(dnum)
                dnum=dnum+1
        elif command == 'r':
            pos = int(c[1])-1
            str = input()
            list.replace(pos, str)
        elif command == 'p':
            for line in range(list.size()):
                print('%d> ' % (line + 1), end='')
                print(list.getEntry(line))
        elif command == 'q':
            return

myLineEditor()
