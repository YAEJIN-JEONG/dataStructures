MAX_SIZE = 3


class CircularQueue:
    def __init__(self):
        self.items = [None] * MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
        self.maxSize = MAX_SIZE

    def isEmpty(self):
        # return self.front == self.rear
        return self.count == 0

    def isFull(self):
        return self.front == (self.rear + 1) % self.maxSize

    def clear(self):
        self.front = 0
        self.rear = 0
        self.count = 0
        self.maxSize = MAX_SIZE

    def enqueue(self, item):
        if self.isFull():
            self.resize()

        self.rear = (self.rear + 1) % self.maxSize
        self.items[self.rear] = item
        self.count += 1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxSize
            self.count -= 1
            return self.items[self.front]

    def resize(self):
        newItems = [None] * 2 * self.maxSize
        scan = (self.front + 1) % self.maxSize
        for i in range(self.count):
            newItems[i + 1] = self.items[scan]
            scan = (scan + 1) % self.maxSize
        self.items = newItems
        self.front = 0
        self.rear = self.count
        self.maxSize = 2 * self.maxSize

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % self.maxSize]

    def size(self):
        return (self.rear - self.front + self.maxSize) % self.maxSize

    def print(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front + 1:self.rear + 1]
        elif self.front > self.rear:
            out = self.items[self.front + 1:self.maxSize] \
                  + self.items[0:self.rear + 1]
        print(out)


class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if self.isFull():
            self.resize()

        self.items[self.front] = item
        self.front = self.front - 1
        if self.front < 0:
            self.front = self.maxSize - 1
        self.count += 1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0:
                self.rear = self.maxSize - 1
            return item

    def getRear(self):
        return self.items[self.rear]


def checkPalindrome():
    dq = CircularDeque()
    f = open("p5input1.txt", "r")
    lines = f.readlines()
    for line in lines:
        for character in line.rstrip('\n'):
            dq.enqueue(character)
        check=True
        while(dq.size()>1 and check):
            front=dq.deleteFront().lower()
            rear=dq.deleteRear().lower()
            if front != rear:
                check=False
        if check == False:
            print(line+"==> not palindrome")
        else:
            print(line+"==> palindrome")
        dq.clear()
    f.close()

checkPalindrome()


