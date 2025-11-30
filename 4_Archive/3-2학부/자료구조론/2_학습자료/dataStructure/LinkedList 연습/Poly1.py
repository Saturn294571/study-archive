class Poly1:
    def __init__(self, coef):
        self.coef = coef
    
    def getMaxOrder(self):
        return len(self.coef)-1

    @classmethod
    def add(cls, p, q):
        coef = []
        if p.getMaxOrder() > q.getMaxOrder():  
            for i in range(q.getMaxOrder()+1):
                coef.append(p.coef[i] + q.coef[i])
            for i in range(q.getMaxOrder()+1, p.getMaxOrder()+1):
                coef.append(p.coef[i])
        else:
            for i in range(p.getMaxOrder()+1):
                coef.append(p.coef[i] + q.coef[i])
            for i in range(p.getMaxOrder()+1, q.getMaxOrder()+1):
                coef.append(q.coef[i])    
        return Poly1(coef)

p = Poly1([3,0,3,0,4])
q = Poly1([1,2,4,3])

print(Poly1.add(p, q).coef)