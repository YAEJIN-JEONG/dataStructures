class BSTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BSTree:
    def __init__(self):
        self.root = None
        self.insertSuccess = None

    def insert(self,data):
        new_node = BSTNode(data)
        if self.root == None:
            self.root = new_node
        node = self.root
        while True:
            pre_node = node
            if node.item > new_node.item:
                node = node.left
                if node == None:
                    node = new_node
                    pre_node.left = node
            elif node.item < new_node.item:
                node = node.right
                if node == None:
                    node = new_node
                    pre_node.right = node
            else:
                return True
        return False

    def delete(self,data):
        parent=None
        curr=self.root
        while curr is not None:
            if data < curr.item:
                parent=curr
                curr=curr.left
            elif data > curr.item:
                parent=curr
                curr=curr.right
            else: break
        if curr is None:
            return False
        if curr.left is None:
            if parent is None:
                self.root=curr.right
            else:
                if data < parent.item:
                    parent.left=curr.right
                else:
                    parent.right=curr.right
        elif curr.right is None:
            if parent is None:
                self.root = curr.left
            else:
                if data < parent.item:
                    parent.left = curr.left
                else:
                    parent.right = curr.left
        else:
            parentMaxNode=curr
            maxNode=curr.left
            while maxNode.right is not None:
                parentMaxNode=maxNode
                maxNode=maxNode.right
            curr.item=maxNode.item
            if parentMaxNode.right is maxNode:
                parentMaxNode.right=maxNode.left
            else:
                parentMaxNode.left=maxNode.left
        return True

    def search(self,data):
        curr=self.root
        while curr is not None:
            if data < curr.item:
                curr=curr.left
            elif data>curr.item:
                curr=curr.right
            else:
                return True
        return False

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

def main():
    t = BSTree()
    print("Enter a command: i(nsert), s(earch), d(elete), p(rint), or q(uit)")
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
        elif command == 'q':
            return

main()
