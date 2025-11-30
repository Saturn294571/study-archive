# method 1 : 1차원 배열로 더하기
pol1 = [3,0,3,0,4]
pol2 = [1,2,4,3]

p = q = None
if len(pol1) >= len(pol2) :
    p = pol1; q = pol2 # 두 다항식의 최고 차항이 p>=q로 가정
else :
    p = pol2; q = pol1
while len(p) != len(q) : # 다항식의 차수를 맞춤
    q.append(0)

r = []
for i in range(len(pol1)) :
    r.append(p[i] + q[i])

print(r)
# ans = ''
# for i in range(len(r)-1,-1,-1) :
#     ans += f'{r[i]}x^{i} + '
# print(ans[:-6])

# method 2 : 2차원 배열로 더하기
pol1 = [[4,4],[3,2],[3,0]] # [계수,차수]
pol2 = [[3,3],[4,2],[2,1],[1,0]]

p = q = None
if pol1[0][1] >= pol2[0][1] : # 차수가 p >= q 임을 가정 
    p = pol1; q = pol2
else :
    p = pol2; q = pol1

i1 = i2 = 0 # 각항을 비교할 2개의 인덱스
r = []
for i in range(p[0][1]+1) : # 최대 차수 + 1만큼 반복하며 각 항의 차수를 비교
# while p[i1][1] != 0 and q[i2][1] != 0 : # 두 다항식의 항의 계수가 0차 아닐때 까지
    if p[i1][1] == q[i2][1] : # 현재 항이 동일한 차수일 때
        r.append([p[i1] + q[i2]])
    elif p[i1][1] > q[i2][1] : # p의 항이 차수가 더 클때
        pass
    else : # q의 항이 차수가 더 클때
        pass

# 두 다항식의 상수항을 더하기
r.append()
# method 3 : 연결리스트 + 2차원 배열

# method 3
class Node:
        def __init__(self,item=None,link=None):
            self.item = item
            self.link = link

class LinkedList:
    def __init__(self):
        self.root = None
        self.n = 0

    def append(self, item):
        newNode = Node(item)
        if self.root == None:
            self.root = newNode
        else:
            curNode = self.root
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode
        self.n += 1

    def insert(self, idx, item):
        newNode = Node(item)
        if idx == 0:
            newNode.link = self.root.link
            self.root = newNode
        elif idx <= self.n - 1:
            curNode = self.root
            for i in range(idx-1):
                curNode = curNode.link
            newNode.link = curNode.link
            curNode.link = newNode
        else:
            print('index Error')
        self.n += 1

    def find(self, item):
        curNode = self.root
        idx = 0
        while curNode.link != None:
            if curNode.item == item:
                return idx
            curNode = curNode.link
            idx += 1
        if curNode.item == item:
              return idx
        return -1

    def delete(self, item):
        idx = self.find(item)
        curNode = self.root
        if idx == 0:
            self.root = self.root.link
        elif idx > 0:
            for i in range(idx-1):
                curNode = curNode.link
            curNode.link = curNode.link.link
        if idx >= 0:
            self.n -= 1
        return idx

    def print(self):
        curNode = self.root
        while curNode.link != None:
            print(curNode.item, end = ' -> ')
            curNode = curNode.link
        print(curNode.item)

class Poly3:
    def __init__(self):
        self.coef = LinkedList()
        self.maxOrder = 0

    def append(self, coef, order):
        self.coef.append([coef, order])

    def isEmpty(self):
        if self.coef.n == 0:
            return True
        else:
            return False

    def pop(self):
        item = self.coef.root.item
        self.coef.root = self.coef.root.link
        self.coef.n -= 1
        return item

    def peek(self):
        return self.coef.root.item[1]

    @staticmethod
    def add(p, q):
        r = Poly3()
        while p.isEmpty() == False and q.isEmpty() == False:
            if p.peek() > q.peek():
                tmp = p.pop()
                r.append(tmp[0], tmp[1])
            elif p.peek() == q.peek():
                tmp1 = p.pop()
                tmp2 = q.pop()
                r.append(tmp1[0]+tmp2[0], tmp1[1])
            else:
                tmp = q.pop()
                r.append(tmp[0], tmp[1])
        return r

p = Poly3()
p.append(4,4)
p.append(3,2)
p.append(3,0)
p.coef.print()

q = Poly3()
q.append(3,3)
q.append(4,2)
q.append(2,1)
q.append(1,0)
q.coef.print()

r = Poly3.add(p, q)
r.coef.print()

a = 8
b = a
a = 9
print()