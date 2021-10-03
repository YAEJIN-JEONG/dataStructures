class Set:
    def __init__(self):
        self.items = []

    def __eq__(self, setB):
        return type(self) == type(setB) and self.items == setB.items

    def insert(self, elem):
        if elem not in self.items:
            self.items.append(elem)

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC

    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC

    def isSubstring(self, setB):
        for item in setB.items:
            if item not in self.items:
                return False
            break
        return True

    def isProperSubstring(self, setB):
        if self.isSubstring(setB):
            if len(self.items) != len(setB.items):
                return True
        return False

    def size(self):
        return len(self.items)

    def print(self, msg):
        print(msg, self.items)


def test(setA, setB):
    setA.print('Set A:')
    setB.print('Set B:')
    if setA == setB:
        print("A equal B : True")
    else:
        print("A equal B : False")
    print('A subset B: ', setA.isSubstring(setB))
    print("A proper subset B: ", setA.isProperSubstring(setB))
    setA.union(setB).print('A union B: ')
    setA.intersect(setB).print('A intersect B: ')
    setA.difference(setB).print('A difference B: ')
    print()


def main():
    setA = Set()
    setA.insert(2)
    setA.insert(3)
    setA.insert(4)

    setB = Set()
    setB.insert(2)
    setB.insert(3)
    setB.insert(4)

    setC = Set()
    setC.insert(2)
    setC.insert(3)
    setC.insert(4)
    setC.insert(4)

    test(setA, setB)
    test(setA, setC)
    test(setC, setA)


main()
