# ---스택 자료구조 순차리스트----------------------
class SL_Stack :
    def __init__(self) :
        self.stack = []

    def push(self,item): # 삽입 연산
        self.stack.append(item)

    def peek(self): # top 항목 접근
        if len(self.stack) != 0:
            return self.stack[-1]

    def pop(self): # 삭제 연산
        if len(self.stack) != 0:
            item = self.stack.pop(-1)      
            return item


my_stack = SL_Stack(); print('--------------------------순차리스트 스택----------------------------')

my_stack.push('apple')
my_stack.push('orange')
my_stack.push('cherry')

print('사과, 오렌지, 체리  push 후:\t', end='')
print(my_stack.stack, '\t<- top')
print('top 항목: ', end='')
print(my_stack.peek())

my_stack.push('pear')
print('배 push 후:\t\t', end='')      
print(my_stack.stack, '\t<- top')
my_stack.pop()              
my_stack.push('grape')
print('pop(), 포도 push 후:\t', end='')
print(my_stack.stack, '\t<- top')


# ---스택 자료구조 연결리스트----------------------
class LL_Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    class __Node: # Node 클래스  
        def __init__(self, item, link): # Node 생성자    
            self.item = item          
            self.next = link       

    def push(self,item): # push 연산
        self.top = self.__Node(item, self.top)  
        self.size += 1

    def peek(self): # peek 연산
        if self.size != 0:
            return self.top.item

    def pop(self): # pop 연산
        if self.size != 0:
            top_item = self.top.item
            self.top = self.top.next
            self.size -= 1
            return top_item  

    def print_stack(self): # 스택 출력
        print('top ->\t', end='')
        p = self.top
        while p:
            if p.next != None:
                print(p.item, '-> ', end='')
            else:
                print(p.item, end='')
            p = p.next
        print()


my_stack = LL_Stack(); print('--------------------------연결리스트 스택----------------------------')

my_stack.push('apple')
my_stack.push('orange')
my_stack.push('cherry')      

print('사과, 오렌지, 체리  push 후:\t', end='')
my_stack.print_stack()
print('top 항목: ', end='')
print(my_stack.peek())     

my_stack.push('pear')
print('배 push 후:\t\t', end='')
my_stack.print_stack()

my_stack.pop()
my_stack.push('grape')
print('pop(), 포도 push 후:\t', end='')
my_stack.print_stack()

 
# ---큐 자료구조 연결리스트------------------------
class LL_Queue :
    def __init__(self):
        self.size = 0
        self.front = self.rear = None

    class __Node:
        def __init__(self, item, n): # Node 생성자
            self.item = item
            self.next = n

    def enqueue(self,item): # 삽입 연산
        new_node = self.__Node(item, None)
        if self.size == 0:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self): # 삭제 연산
        if self.size != 0:
            fitem = self.front.item
            self.front = self.front.next
            self.size -= 1
            if self.size == 0:
                self.rear = None
            return fitem

    def print_q(self): # 큐 출력
        p = self.front
        print('front: ', end='')
        while p:
            if p.next != None:
                print(p.item, '->   ', end='')
            else:
                print(p.item, end = '')
            p = p.next
        print('  : rear')


my_queue = LL_Queue(); print('--------------------------연결리스트 큐----------------------------')

my_queue.enqueue('apple')
my_queue.enqueue('orange')
my_queue.enqueue('cherry')
my_queue.enqueue('pear')

print('사과, 오렌지, 체리, 배 삽입 후: \t', end='')
my_queue.print_q()

my_queue.dequeue()
print('remove한 후:\t\t', end='')
my_queue.print_q()

my_queue.dequeue()
print('remove한 후:\t\t', end='')
my_queue.print_q()

my_queue.enqueue('grape')
print('포도 삽입 후:\t\t', end='')
my_queue.print_q()