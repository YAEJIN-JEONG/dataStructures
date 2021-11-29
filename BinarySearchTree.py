class BSTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BSTree:
    def __init__(self):
        self.root = None
        self.insertSuccess=None
        self.deleteSuccess=None
    def insert(self,data):
        self.root=self.insert1(self.root,data)
        return self.insertSuccess
    def insert1(self,node,data):
        if node is None:
            node=BSTNode(data)
            self.insertSuccess=True
        elif data>node.item:
            node.right=self.insert1(node.right,data)
        elif data<node.item:
            node.left=self.insert1(node.left,data)
        else:
            self.insertSuccess=False
        return node
    def delete(self,data):
        self.root=self.delete1(self.root,data)
        return self.deleteSuccess
    def delete1(self,node,data):
        if node is None:
            self.deleteSuccess=False
        elif data>node.item:
            node.right=self.delete1(node.right,data)
        elif data<node.item:
            node.left=self.delete1(node.left,data)
        else:
            self.deleteSuccess=True
            if node.right is None:
                node=node.left
            elif node.left is None:
                node=node.right
            else:
                maxNode=node.left
                while maxNode.right is not None:
                    maxNode=maxNode.right
                node.item=maxNode.item
                node.left=self.delete1(node.left,maxNode.item)
        return node

    def search(self,data):
        return self.search1(self.root,data)

    def search1(self,node,data):
        if node is None:
            return False
        elif data>node.item:
            return self.search1(node.right,data)
        elif data<node.item:
            return self.search1(node.left,data)
        else:
            return True

    def print(self):
        self.print1(self.root,0)

    def print1(self,node,skip):
        if node is not None:
            self.print1(node.right,skip+10)
            for i in range(skip):
                print(" ",end=' ')
            print(node.item,end=' ')
            if node.left is not None:
                print(",L",end=' ')
            if node.right is not None:
                print(",R",end=' ')
            print()
            self.print1(node.left,skip+10)

    def inorder(self):
        self.inorder1(self.root)
        print()

    def inorder1(self,node):
        if node is not None:
            self.inorder1(node.left)
            print(node.item, end=' ')
            self.inorder1(node.right)

    def nodeCount(self):
        return self.nodeCount1(self.root)

    def nodeCount1(self,node):
        if node is None:
            return 0
        else:
            return 1 + self.nodeCount1(node.left) + self.nodeCount1(node.right)

    def checkFull(self):
        if not self.root:
            return True
        if self.left and self.right:
            return self.checkFull(self.left) and self.checkFull(self.right)
        else:
            return not self.left and not self.right

    def max(self):
        n=self.root
        while n is not None and n.right is not None:
            n = n.right
        return n.item

    def min(self):
        n=self.root
        while n is not None and n.left is not None:
            n = n.left
        return n.item

def main():
    t = BSTree()
    print("Enter a command: i(nsert), s(earch), d(elete), inorder(traversal),")
    print("nc(node count), min, max, full, path, p(rint), or q(uit)")
    while True:
        print("> ",end=' ')
        line = input().split()
        command = line[0]
        if command == 'i':
            item=int(line[1])
            if t.insert(item):
                print(item," is inserted")
            else:
                print("Not inserted: same data")
        elif command =='s':
            item = int(line[1])
            if t.search(item):
                print(item, " is found")
            else:
                print("No such item in the tree")
        elif command == 'd':
            item=int(line[1])
            if t.delete(item):
                print(item," is deleted")
            else:
                print("No such item in the tree")
        elif command == 'p':
            t.print()
        elif command =='inorder':
            t.inorder()
        elif command =='nc':
            print("node count =",t.nodeCount())
        elif command =='min':
            print("Min: ",t.min())
        elif command == 'max':
            print("Max: ",t.max())
        elif command == 'full':
            t.checkFull()
        elif command == 'path':
            t.path()
        elif command == 'q':
            return

main()
