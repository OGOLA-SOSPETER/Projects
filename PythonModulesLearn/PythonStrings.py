# Understanding the python strings
from random import randint
import numpy


class PythonStrings:
    def __init__(self):
        self.id = numpy.array(5)
        self.mylist = []

    def getList(self):
        for a in range(randint(10,30)):
            num = randint(100,1000)
            self.mylist.append(num)

    def addItemList(self):
        num = randint(100, 1000)
        self.mylist.insert((len(self.mylist)), num)
        return self.mylist

    def deleteItemList(self):
        self.mylist.__delitem__(-1)

    def sortList(self):
        return self.mylist.sort()

    def printList(self):
        print(self.mylist)
        # [print(self.mylist[i]) for i in range(len(self.mylist))]


py1 = PythonStrings()
py1.getList()
py1.printList()
py1.addItemList()
py1.printList()
# py1.deleteItemList()
py1.sortList()
py1.printList()
