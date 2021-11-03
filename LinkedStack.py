class Node:
    def __init__ (self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack :
    def __init__( self ):
        self.top = None

    def isEmpty( self ):
        return self.top == None

    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def clear( self ):
        self.top = None

    def push( self, item ):
        n = Node(item, self.top)
        self.top = n

    def pop( self ):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def peek( self ):
        if not self.isEmpty():
            return self.top.data

    def print(self):
        node = self.top
        while not node == None :
            print(node.data, end=' ')
            node = node.link
        print()

def main():
    stack=LinkedStack()
    print("Enter a command: pop, push, peek, size, empty, p(rint), m(atch), q(uit)")
    while True:
        print("> ",end="")
        line = input().split()
        command = line[0]
        if command == 'push':
            item = line[1]
            stack.push(item)
        elif command == 'pop':
            print(stack.pop())
        elif command == 'peek':
            print(stack.peek())
        elif command == 'size':
            print(stack.size())
        elif command == 'empty':
            print(stack.isEmpty())
        elif command == 'p':
            stack.print()
        elif command == 'q':
            break
main()