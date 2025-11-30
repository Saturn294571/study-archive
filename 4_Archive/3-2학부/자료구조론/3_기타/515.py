from l508 import *

class MaxHeap():
    def __init__(self):
        self.x = [None]

    def _exchange(self,i,j):   # _ 로 시작하는 메소드는 히든 메소드를 의미한다.
        # x[i] > x[j] 가 되도록 자리를 바꾼다.
        if self.x[i] < self.x[j]:
            self.x[i],self.x[j] =  self.x[j],self.x[i]

    def push(self, item):
        self.x.append(item)   # 마지막 위치에 push
        cIndex = len(self.x) - 1
        pIndex = cIndex // 2
        while pIndex >= 1:
            self._exchange(pIndex, cIndex)
            cIndex = pIndex
            pIndex = cIndex // 2

    def pop(self):
        item = self.x[1]
        n = len(self.x) - 1
        self.x[1], self.x[n] = self.x[n], self.x[1]
        self.x = self.x[:-1]
        self.heapify()
        return item

    def _child(self, pIndex):
        n = len(self.x)
        leftIndex = pIndex * 2
        rightIndex = pIndex * 2 + 1
        if rightIndex <= n-1:
            return leftIndex, rightIndex
        elif leftIndex == n-1:
            return leftIndex, None
        else:
            return None, None

    def heapify(self):
        pIndex = 1
        lastIndex = len(self.x) - 1
        while pIndex < len(self.x):
            left, right = self._child(pIndex)
            if left != None and right == None :
                self._exchange(pIndex, left)
            elif left != None and right != None:
                if self.x[left] < self.x[right]:
                    self._exchange(pIndex, right)
                else:
                    self._exchange(pIndex, left)
            pIndex += 1

    def print(self):
        print(self.x)

'=============================================='

h = MaxHeap()
for i in range(1,9):
    h.push(i)
print(h.x)
for i in range(8):
    print(h.pop())   # heap sort

class MaxHeap():
    def __init__(self):
        self.x = [None]

    def _exchange(self,i,j):   # _ 로 시작하는 메소드는 히든 메소드를 의미한다.
        # x[i] > x[j] 가 되도록 자리를 바꾼다.
        if self.x[i] < self.x[j]:
            self.x[i],self.x[j] =  self.x[j],self.x[i]

    def push(self, item):
        self.x.append(item)   # 마지막 위치에 push
        cIndex = len(self.x) - 1
        pIndex = cIndex // 2
        while pIndex >= 1:
            self._exchange(pIndex, cIndex)
            cIndex = pIndex
            pIndex = cIndex // 2

    def pop(self):
        item = self.x[1]
        n = len(self.x) - 1
        self.x[1], self.x[n] = self.x[n], self.x[1]
        self.x = self.x[:-1]
        self.heapify()
        return item

    def _child(self, pIndex):
        n = len(self.x)
        leftIndex = pIndex * 2
        rightIndex = pIndex * 2 + 1
        if rightIndex <= n-1:
            return leftIndex, rightIndex
        elif leftIndex == n-1:
            return leftIndex, None
        else:
            return None, None

    def heapify(self):
        pIndex = 1
        lastIndex = len(self.x) - 1
        while pIndex < len(self.x):
            left, right = self._child(pIndex)
            if left != None and right == None :
                self._exchange(pIndex, left)
            elif left != None and right != None:
                if self.x[left] < self.x[right]:
                    self._exchange(pIndex, right)
                else:
                    self._exchange(pIndex, left)
            pIndex += 1

    def print(self):
        print(self.x)

h = MaxHeap()
for i in range(1,9):
    h.push(i)
print(h.x)
for i in range(8):
    print(h.pop())   # heap sort

'====================================='

class BST(BinaryTree) :
    def aa(self) :
        pass