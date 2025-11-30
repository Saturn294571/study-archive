class Queue:
    def __init__(self):
        self.q = []
    def isEmpty(self):
        return len(self.q) == 0
    def enQueue(self, item):
        self.q.append(item)
    def deQueue(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.q.pop(0)
    def peek(self):
        return self.q[0]
    
class BinaryTree:
    def __init__(self):
        self.t = [None]
        self.size = len(self.t)

    def append(self, item):
        self.t.append(item)
        self.size += 1

    def getChild(self, item):
        idx = self.t.index(item)
        leftChildIdx = idx * 2
        rightChildIdx = leftChildIdx + 1

        if leftChildIdx >= self.size:
            return None
        elif rightChildIdx >= self.size:
            return self.t[leftChildIdx], None
        else:
            return self.t[leftChildIdx], self.t[rightChildIdx]

    def getParent(self, item):
        if item in self.t:
            idx = self.t.index(item)
            return self.t[idx // 2]
        

def get_item(item):
    q = []
    item_list = []
    item_tmp = item
    while True:
        childs = tree.getChild(item_tmp)
        if childs[0] : 
            q.append(childs[0])
        if childs[1] : 
            q.append(childs[1])

        _tmp = q.pop()
        if not tree.getChild(_tmp) : 
            item_list.append(_tmp)
        else:
            item_tmp = _tmp
        if not q:
            break
    return item_list

tree = BinaryTree()
tree.append("음료")
tree.append("사이다")
tree.append("콜라")
tree.append("일반사이다")
tree.append("제로칼로리사이다")
tree.append("일반콜라")
tree.append("제로콜라")
tree.append("칠성")
tree.append("스프라이트")
tree.append("나랑드")
tree.append("부르르")
tree.append("코카콜라")
tree.append("펩시콜라")
tree.append("코카콜라제로")
tree.append("펩시제로슈거")

print(get_item('콜라'))

