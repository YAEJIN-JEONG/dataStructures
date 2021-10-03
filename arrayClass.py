class Bag:
    def __init__(self):
        self.items = []

    def contains(self, e):
        if e in self.items:
            return True
        else:
            return False

    def insert(self, e):
        self.items.append(e)

    def remove(self, e):
        self.items.remove(e)

    def count(self):
        return len(self.items)


myBag = Bag()
myBag.insert("휴대폰")
myBag.insert("지갑")
myBag.insert("손수건")
myBag.insert('빗')
myBag.insert('연필')
print("가방속 물건: ", myBag.items)

myBag.insert('빗')
myBag.remove('손수건')
myBag.insert('자료 구조 책')
print("가방속 물건: ", myBag.items)
print("가방속 물건 갯수: %d" % myBag.count())
print("가방속 지갑 유무: %s" % myBag.contains('지갑'))
print("가방속 손수건 유무: %s" % myBag.contains('손수건'))
