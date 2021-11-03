MAX_SIZE = 3
class CircularQueue :
    def __init__( self ) :
        self.items = [None] * MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count=0
        self.maxSize=MAX_SIZE

    def isEmpty( self ) :
        #return self.front == self.rear
        return self.count==0
    def isFull( self ) :
        return self.front == (self.rear+1)%self.maxSize
    def clear( self ) :
        self.front = 0
        self.rear = 0
        self.count=0
        self.maxSize=MAX_SIZE

    def enqueue( self, item ):
        if self.isFull():
            self.resize()

        self.rear = (self.rear+1)% self.maxSize
        self.items[self.rear] = item
        self.count+=1

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front+1)% self.maxSize
            self.count-=1
            return self.items[self.front]

    def resize(self):
        newItems=[None]*2*self.maxSize
        scan=(self.front+1)%self.maxSize
        for i in range(self.count):
            newItems[i+1]=self.items[scan]
            scan=(scan+1)%self.maxSize
        self.items=newItems
        self.front=0
        self.rear=self.count
        self.maxSize=2*self.maxSize

    def peek( self ):
        if not self.isEmpty():
            return self.items[(self.front + 1) % self.maxSize]

    def size( self ) :
       return (self.rear - self.front + self.maxSize) % self.maxSize

    def print( self ):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        elif self.front>self.rear:
            out = self.items[self.front+1:self.maxSize] \
                + self.items[0:self.rear+1]
        print(out)

def myqueue():
    q = CircularQueue()
    print("Enter a command: e(nqueue), d(nqueue), peek, s(ize), p(rint), or q(uit)")
    while True:
        c=input().split()
        command=c[0]
        if command=='e':
            item=c[1]
            q.enqueue(item)
        elif command=='d':
            print(q.dequeue())
        elif command == 'p':
            q.print()
        elif command == 's':
            print('size: ',q.size())
        elif command == 'peek':
            print(q.peek())
        elif command == 'q':
            return

myqueue()

