import numpy as np
import copy
class Sparse_matris_linked_list :
    def __init__(self,m,n) : # m x n 행렬
        self.s = [[m,n,0]]
        self.m = m
        self.n = n
        pass

    def append(self,i,j,val):
        self.s.append([i,j,val])
        self.s[0][2] += 1
        pass

    def shape(self):
        return (self.s[0][0], self.s[0][1])

    def get_value(self,I,J):
        for i in self.s[1:] :
            if [i[0],i[1]] == [I,J] :
                return i[2]
        return 'there is no such value'
        

    def print(self) :
        mat = np.zeros([self.m,self.n])
        for i in range(1,len(self.s)) :
            mat[self.s[i][0],self.s[i][1]] = self.s[i][2]
        print(mat)

    @staticmethod
    def transpose(x) :
        xt = copy.deepcopy(x)
        for i in range(len(xt.s)) :
            xt.s[i][0],xt.s[i][1] = xt.s[i][1],xt.s[i][0]
        return xt
    
    # def add(x,y) :
        # if x.s[0][:2] == y.s[0][:2] :
        #     z = Sparse_matris_linked_list(x.s[0][0],x.s[0][1])
        #     for i in range(z.s[0][0]) :
        #         for j in range(z.s[0][1])
        #         pass
        # else :
        #     return 'dimension mismatch!'
        # pass

    def add(a,b) :
        c = copy.deepcopy(a)
        for i in range(1,len(b.s)):
            for j in range(1,len(a.s)):
                if b.s[i][0] == a.s[j][0] and b.s[i][1] == a.s[j][1] :
                    tmp= a.s[j][2] + b.s[j][2]
                    if tmp != 0:
                        c.s[j] = tmp
                    else:
                        c.s.pop(j)
                else:
                    c.s.append(b.s[i])
        return c

a = Sparse_matris_linked_list(3,3)

a.append(0,0,1)
a.append(1,0,1)
a.append(1,1,2)
a.append(2,0,1)
a.append(2,1,2)
a.append(2,2,3)

# a.print()

# print(a.shape())
# print(a.s)
# print(a.get_value(1,1))
at = Sparse_matris_linked_list.transpose(a)
# at.print()
# print(at.s)
c = Sparse_matris_linked_list.add(a,at)
print(c.print())