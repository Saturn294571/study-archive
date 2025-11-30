class Node:
    def __init__(self, item = None):
        self.item = item
        self.link = None

class LinkedList:
    def __init__(self):
        self.root = Node()

    def append(self, item):
        newNode = Node(item)
        curNode = self.root
        if self.root.item == None:
            self.root = newNode
        else:
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode

    def insert(self, k, item):
        newNode = Node(item)
        curNode = self.root
        if k == 0:
            _tmp = self.root
            self.root = newNode
            newNode.link = _tmp
        elif k > 0:
            for i in range(k-1):
                curNode = curNode.link
            _tmp = curNode.link
            curNode.link = newNode
            newNode.link = _tmp

    def delete(self, item):
        curNode = self.root
        k = self.find(item)
        if k == 0:
            self.root = self.root.link
        elif k > 0:
            for i in range(k-1):
                curNode = curNode.link
            curNode.link = curNode.link.link


    def find(self, item):
        curNode = self.root
        idx = 0
        while curNode.link != None:
            if curNode.item == item:
                return idx
            else:
                curNode = curNode.link
                idx += 1
        if curNode.item == item:
            return idx
        return -1

    def pprint(self):
        curNode = self.root
        while curNode.link != None:
            print(curNode.item)
            curNode = curNode.link
        print(curNode.item)
