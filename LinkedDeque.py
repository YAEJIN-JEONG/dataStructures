class DNode:
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next

class LinkedDeque:
    def __init__(self):
        self.front = None
        self.rear=None

    def isEmpty(self):
        return self.front == None

    def clear(self):
        self.front = self.front = None

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if (self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if (self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.item
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.item
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data

    def peekFront(self):
        if not self.isEmpty():
            return self.front.item

    def peekRear(self):
        if not self.isEmpty():
            return self.rear.item

    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count

    def print(self):
        node = self.front
        while not node == None:
            print(node.item, end=' ')
            node = node.next
        print()

    def revPrint(self):
        node = self.rear
        while not node == None:
            print(node.item, end=' ')
            node = node.prev
        print()

def main():
    dq=LinkedDeque()
    print("Enter a command: af(addFront), df(deleteFront), pf(peekFront), s(size)")
    print("ar(addRear), dr(deleteRear), pr(peekRear), rp(reversePrint) or q(quit)")

    while True:
        print("> ",end="")
        line=input().split()
        command = line[0]
        if command == 'af':
            item=line[1]
            dq.addFront(item)
        elif command =='df':
            print(dq.deleteFront())
        elif command =='pf':
            print(dq.peekFront())
        elif command =='ar':
            item=line[1]
            dq.addRear(item)
        elif command =='dr':
            print(dq.deleteRear())
        elif command =='pr':
            print(dq.peekRear())
        elif command=='p':
            dq.print()
        elif command =='rp':
            dq.revPrint()
        elif command=='s':
            print("size: ",dq.size())
        elif command=='q':
            break
main()

