class DNode:
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head is None
    def clear(self):
        self.head = None
    def addFront(self, item):
        newNode = DNode(item)
        if self.isEmpty():
            self.head = newNode
            self.head.prev = newNode
            self.head.next = newNode
        else:
            newNode.next = self.head.next
            self.head.next=newNode

    def addRear(self,item):
        newNode = DNode(item)
        if self.isEmpty():
            self.head = newNode
            self.head.prev = newNode
            self.head.next = newNode
        else:
            newNode.next = self.head
            self.head.next = newNode
            self.head = newNode

    def deleteFront(self):
        if not self.isEmpty():
            data = self.head.item
            count = self.size()
            if count == 1:
                self.head = None
            else:
                self.head.next.prev = self.head.prev
                self.head.prev.next = self.head.next
                self.head = self.head.next
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.head.item
            count = self.size()
            if count == 1:
                self.head = None
            else:
                self.head.prev.prev.next=self.head.prev.next
                self.head.prev.prev=self.head.prev
                self.head = self.head.next
            return data

    def size(self):
        if self.head is None:
            return 0
        count = 1
        tmp = self.head
        while tmp is not self.head.prev:
            count += 1
            tmp = tmp.next
        return count

    def peekFront(self):
        if not self.isEmpty():
            return self.head.item

    def peekRear(self):
        if not self.isEmpty():
            node=self.head.prev
            return node.item

    def print(self):
        node = self.head
        if self.head is not None:
            while True:
                print(node.item,end=' ')
                node = node.next
                if node == self.head:
                    break
        print()

    def revPrint(self):
        node=self.head.prev
        while node is not self.head.next:
            print(node.item,end='')
            node=node.prev
        print()

def main():
    dq = CircularDoublyLinkedList()
    print("Enter a command: af(addFront), df(deleteFront), pf(peekFront), s(size)")
    print("ar(addRear), dr(deleteRear), pr(peekRear), rp(reversePrint) or q(quit)")

    while True:
        print("> ", end="")
        line = input().split()
        command = line[0]
        if command == 'af':
            item = line[1]
            dq.addFront(item)
        elif command == 'df':
            print(dq.deleteFront())
        elif command == 'pf':
            print(dq.peekFront())
        elif command == 'ar':
            item = line[1]
            dq.addRear(item)
        elif command == 'dr':
            print(dq.deleteRear())
        elif command == 'pr':
            print(dq.peekRear())
        elif command == 'p':
            dq.print()
        elif command == 'rp':
            dq.revPrint()
        elif command == 's':
            print("size: ", dq.size())
        elif command == 'q':
            break


main()
