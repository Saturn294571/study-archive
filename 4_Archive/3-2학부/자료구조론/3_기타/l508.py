def fibonachi(x) :
    if x == 1 or x == 2 :
        return 1
    elif x < 1 :
        pass
    else :
        return fibonachi(x-1) + fibonachi(x-2)
    
def summation(x) : 
    if x == 1 :
        return 1
    else :
        return x + summation(x-1)

def fact(x) :
    if x == 1 :
        return 1
    else :
        return x * fact(x-1)

class BNode :
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
    
    def setLeft(self,item) :
        self.left = item

    def setRight(self,item) :
        self.right = item

class BinaryTree :
    def __init__(self,root) :
        self.root = root
    
    def preOrder(self,n):
        # function(n.item)
        print(n.item,end=' ')
        if n.left : self.preOrder(n.left)
        if n.right : self.preOrder(n.right)

    def inOrder(self,n):
        if n.left : self.inOrder(n.left)
        print(n.item,end=' ')
        if n.right : self.inOrder(n.right)
    
    def postOrder(self,n):
        if n.left : self.postOrder(n.left)
        if n.right : self.postOrder(n.right)
        print(n.item,end=' ')
class Bnode :
    def __init__(self,item):
        self.item = item
        self.right = None
        self.left = None
    
    def setRight(self,value) :
        self.right = value

    def setLeft(self,value) :
        self.left = value

a = Bnode('A'); b = Bnode('B'); c = Bnode('C'); d = Bnode('D'); e = Bnode('E'); f = Bnode('F'); g = Bnode('G'); h = Bnode('H'); i = Bnode('I'); j = Bnode('J'); k = Bnode('K')

a.setLeft(b); a.setRight(c)
b.setLeft(d); b.setRight(e)
c.setLeft(f); c.setRight(g)
d.setLeft(h)
e.setLeft(i); e.setRight(j)
g.setRight(k)

bt = BinaryTree(a)
bt.preOrder(a)
print()
bt.inOrder(a)
print()
bt.postOrder(a)
