class Stack :
    def __init__(self) :
        self.s = []
    
    def append(self,value) :
        self.s.append(value)
    
    def pop(self) :
        if self.s:
            return self.s.pop()
        else :
            return None

    def size_(self) :
        return len(self.s)
    
    def is_empty(self) :
        return True if self.s else False

    def peek(self) :
        return self.s[-1]

class Queue :
    def __init__(self) :
        self.s = []
    
    def push(self,value) :
        self.s.append(value)
    
    def pop(self) :
        if self.s:
            return self.s.pop(0)
        else :
            return None

    def size_(self) :
        return len(self.s)
    
    def is_empty(self) :
        return True if self.s else False

    def peek(self) :
        return self.s[-1]

aaa = Stack()
aaa.append(1)
aaa.append(2)
aaa.append(3)
aaa.pop()
print(aaa.s)

bbb = Queue()
bbb.push(1)
bbb.push(2)
bbb.push(3)
bbb.pop()
print(bbb.s)