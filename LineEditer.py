class ArrayList:

    def __init__(self):
        self.items=[]

    def add(self,elem):
        self.items.append(elem)
    def remove(self,elem):
        for i in range(self.size()):
            if self.items[i] == elem:
                self.items.remove(elem)
                return print(elem," removed")
        return print('No such element')
    def insert(self,pos,elem):
        self.items.insert(pos,elem)
    def delete(self,pos):
        return self.items.pop(pos)
    def isEmpty(self):
        if self.size()==0:
            print("True")
        else:
            print("False")
    def getEntry(self,pos):
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items==[]
    def find(self,item):
        return self.items.index(item)
    def replace(self,pos,elem):
        self.items[pos]=elem
    def sort(self):
        self.items.sort()
    def merge(self,lst):
        self.items.extend(lst)
    def print(self,msg="ArrayList"):
        print(msg,self.size(),self.items)
    def search(self,item):
        for i in range(len(self.items)):
            if self.items[i]==item:
                return print(item,' found')
        return print('No such element')
    def dup(self):
        new_list = []
        for i in self.items:
            if i not in new_list:
                new_list.append(i)
        self.items = new_list

def myLineEditor() :
    myLine = ArrayList()
    infile=open("C:/Users/N20036/Desktop/lineEditerinput.txt", "r")
    lines = infile.readlines()
    for line in lines:
        myLine.insert(myLine.size(), line.rstrip('\n'))
    infile.close()
    for i in range(myLine.size()):
        print('%d> ' % (i + 1), end='')
        print(myLine.getEntry(i))
    while True :
        myinput = input().split()
        command=myinput[0]
        if command == 'i' :
            pos = int(myinput[1])
            elem=[]
            for pos in range(len(myinput)-1):
                if myinput[pos]=="*":
                    break
                else :
                    elem=myinput[pos]
            myLine.insert(pos,elem)

        elif command == 'd' :
            pos = int( input("  삭제행 번호: "))
            myLine.delete(pos)
        elif command == 'r' :
            pos = int( input("  변경행 번호: "))
            str = input("  변경행 내용: ")
            myLine.replace(pos, str)
        elif command == 'q' : return
        elif command == 'p' :
            for i in range(list.size()):
                print('%d> ' % (i + 1), end='')
                print(list.getEntry(i))
            print()
        elif command == 's' :
            outfile = open("C:/Users/N20036/Desktop/lineEditerinput.txt", "w")
            for i in range(myLine.size()) :
                outfile.write(myLine.getItem(i)+'\n')
            outfile.close()

myLineEditor()