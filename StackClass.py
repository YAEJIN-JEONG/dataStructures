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

def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty() :
                return False
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False

    return stack.isEmpty()

def myStackClass():
    s=Stack()
    print("Enter a command: pop, push, peek, size, empty, p(rint), m(atch), q(uit)")

    while True:
        c = input().split()
        command = c[0]
        if command == 'pop':
            print(s.pop())
        elif command == 'push':
            item=c[1]
            s.push(item)
        elif command == 'peek':
            print(s.peek())
        elif command == 'size':
            print(s.size())
        elif command == 'empty':
            print(s.isEmpty())
        elif command=='p':
            print(s)
        elif command=='m':
            filename = 'w5input.txt'
            infile = open(filename, "r")
            lines = infile.readlines();
            infile.close()
            for line in lines:
                rst=checkBrackets(line)
                if(rst==True):
                    print(line+"matched")
                else:
                    print(line+"not matched")
        elif command == 'q':
            return


myStackClass()
