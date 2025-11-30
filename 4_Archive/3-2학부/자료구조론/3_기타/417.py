class Stack : 
    def __init__(self) :
        self.s = []
    
    def is_empiy(self) :
        return True if self.s else False

    def push(self,element) :
        return self.s.append(element)

    def pop(self) :
        return self.s.pop()

    def delete(self) :
        self.s.pop()

    def peek(self) :
        return self.s[-1]
    
    def print(self) :
        return self.s

string = 'qwerasdf'

s = Stack()
for letter in string :
    s.push(letter)

print(s.peek())

def is_oper(item) :
    if item in ['+','-'] :
        return 1
    elif item in ['*','/'] :
        return 2
    elif item in ['(',')'] :
        return 0
    else : return -1

def is_num(s) :
    return True if type(s) in [int,float] else False

