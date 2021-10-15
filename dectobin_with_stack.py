class Stack :
    def __init__( self ):
        self.top = []

    def isEmpty( self ):
        return len(self.top) == 0

    def size( self ):
        return len(self.top)

    def clear( self ):
        self.top = []

    def push( self, item ):
        self.top.append(item)

    def pop( self ):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self ):
        return str(self.top[::-1])

def dectobin(decNum):
    s=Stack()
    n=decNum
    binNum=''
    if n == '-1':
        return
    else :
        while (n>=1):
            r=n%2
            n=n//2
            s.push(r)
        while s.size()>0:
            binNum+=str(s.pop())
        return binNum


while True:
    decNum=int(input("Enter a decimal number: "))
    rst = dectobin(decNum)
    print(decNum,"==>",rst)