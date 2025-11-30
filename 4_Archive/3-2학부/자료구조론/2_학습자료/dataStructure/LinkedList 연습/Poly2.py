class Poly2:
    def __init__(self, coef):
        self.coef = coef

    def getMaxOrder(self):
        return self.coef[0][1]

    def pop(self):
        return self.coef.pop(0)

    def peek(self):
        return self.coef[0]

    def getLength(self):
        return len(self.coef)

    @classmethod
    def add(cls, p, q):
        coef = []
        while p.getLength() > 0 and q.getLength() > 0:
            if p.peek()[1] > q.peek()[1]:
                coef.append(p.pop())
            elif p.peek()[1] < q.peek()[1]:
                coef.append(q.pop())
            else:
                _tmp1 = p.pop()
                _tmp2 = q.pop()
                coef.append((_tmp1[0]+_tmp2[0], _tmp1[1]))
        
        if p.getLength() > 0:
            for i in range(p.getLength()):
                coef.append(p.pop())
        else:
             for i in range(q.getLength()):
                coef.append(q.pop())           
        print(coef)

p = Poly2([(4,4), (3,2), (3,1)])
q = Poly2([(3,3), (4,2), (2,1), (1,0)])
Poly2.add(p, q)