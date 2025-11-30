class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.link = None

# LinkedList Class: Linked List에 노드를 추가(append)하고 노드를 찾는(get) 메소드가 있다.
class LinkedList:
    def __init__(self):
        self.root = Node()
        self.cnt = 0
    # 리스트 마지막에 노드를 삽입한다.
    def append(self, key, value):
        # 추가할 새 노드를 만든다.
        newNode = Node(key, value)
        # 현위치를 루트로 지정하고 노드를 추가한다.
        curNode = self.root
        # 현 위치가 비어 있으면 현 위치에 삽입
        if curNode.key == None:
            self.root = newNode
            self.cnt += 1
        # 현 위치가 비어 있지 않으면 다음 노드로 옮기는 작업을 마지막 노드가 나타날 때 까지 반복한다.
        # 마지막 노드를 만나면 마지막 노드 다음에 새 노드를 삽입한다.
        else:
            while curNode.link != None:
                self.cnt += 1
                curNode = curNode.link
            curNode.link = newNode
        return self.cnt

    def get(self, key):
        cnt = 0
        curNode = self.root
        if curNode.key == key:
            return curNode.value, cnt
        else:
            while curNode.link != None:
                curNode = curNode.link
                cnt += 1
                if curNode.key == key:
                    return curNode.value, cnt
            return None

# 100 보다 작은 소수

def get_prime(x):
    def isprime(x): # 이 함수가 내부에서만 쓰일 경우
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    for x in range(100, 2, -1):
        if isprime(x) == True:
            return x

print(get_prime(100))

class ChainHash:
    def __init__(self, k): # k: number of keys
        # 데이터 수의 3배를 기준으로 소수 리턴한다.
        self.m = self.get_prime(3 * k)
        self.h = [None] * self.m  # [None, None, ...], self.m개 만든다.

    def get_prime(self, x):
        def isprime(x):
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True

        for i in range(x, 2, -1):
            if isprime(i) == True:
                return i

    def insert(self, key, item):
        idx = key % self.m
        #print(key, idx)
        if self.h[idx] == None:
            self.h[idx] = LinkedList()
            self.h[idx].append(key, item)
        else:
            print(key, idx,  "충돌")
            curNode = self.h[idx].root
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = Node(key, item)

    def get(self, key):
        idx = key % self.m
        xList = self.h[idx]
        return xList.get(key)
    
print('=====================================')
x = [25, 37, 18, 55, 22, 35, 50, 63] # keys, value = [a25, a37, a18, ...]

h = ChainHash(len(x))
for key in x:
    h.insert(key, 'a'+str(key)) #25,37,18,55,22,35,50,63 -(23로 나눈 나머지)> 2,14,18,9,22,12,4,17

for key in x:
    print(key, h.get(key))
# -> 충돌이 하나도 없음
print('=====================================')
y = [26, 38, 19, 56, 23, 36, 51, 64]
for val in y:
    h.insert(val, 'a'+str(val))

for key in y:
    print(key, h.get(key))

print('=====================================')
class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(-1)
        else:
            return None

    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None

    def isEmpty(self):
        if len(self.s) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.s)

    def print(self):
        print(self.s)