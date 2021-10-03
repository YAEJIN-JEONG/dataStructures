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
        print(self.items[pos])
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

def mylist():
    s = ArrayList()
    print("Enter a command: i(nsert), d(elete), e(mpty), g(etEntry), c(lear), a(dd)")
    print("remove, search, f(ind), r(eplace), s(ort), m(erge), p(rint):")
    while True:
        c=input().split()
        command=c[0]
        if command=='a':
            elem=c[1]
            s.add(elem)
        elif command=='i':
            pos=int(c[1])
            elem=c[2]
            s.insert(pos,elem)
        elif command == 'p':
            s.print()
        elif command == 'e':
            s.isEmpty()
        elif command == 'g':
            pos=int(c[1])
            s.getEntry(pos)
        elif command=='remove':
            elem=c[1]
            s.remove(elem)
        elif command=='search':
            item=c[1]
            s.search(item)
        elif command=='s':
            s.sort()
        elif command=='dup':
            s.dup()
        elif command=='r':
            pos = int(c[1])
            elem = c[2]
            s.replace(pos, elem)
        elif command=='m':
            mlst=[]
            j = 1
            for j in range(len(c)-1) :
                mlst.append(c[j+1])
            lst=mlst
            s.merge(lst)
        elif command == 'q':
            return

mylist()


