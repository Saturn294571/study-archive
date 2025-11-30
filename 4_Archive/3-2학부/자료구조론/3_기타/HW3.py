# 희소행렬의 곱셈
import numpy as np
class Sparse_matrix :
    def __init__(self,m,n):
        self.s = [[m,n,0]]
        self.m = m
        self.n = n

    def append(self,i,j,value):
        self.s.append([i,j,value])
        self.s[0][2] += 1

    def shape(self):
        return self.s[0][:2]

    def get_value(self,i,j):
        for I in self.s[1:] :
            if I[:2] == [i,j] : 
                return I[2]
        return 0 # 찾는 값이 행렬에 없으면 0으로 가정

    def print(self):
        mat = np.zeros([self.m,self.n])
        for i in range(1,len(self.s)) :
            mat[self.s[i][0],self.s[i][1]] = self.s[i][2]
        print(mat)
    
    @staticmethod
    def dot(a,b) : # a * b -> (I*K) * (K*J)
        if type(a) == type(b) == Sparse_matrix :
            I = a.s[0][0]
            J = b.s[0][1]
            K = a.s[0][1]
            if K == b.s[0][0] : # K == K 인지 확인
                ab = Sparse_matrix(I, J)
                for i in range(I): 
                    for j in range(J):
                        result = 0
                        for k in range(K): # 실제 원소끼리 곱셈
                            ele_a = a.get_value(i,k) 
                            ele_b = b.get_value(k,j)
                            result += ele_a * ele_b
                        ab.append(i,j,result) # 여기서 원소 추가
                for i in ab.s : # 원소가 0일때 희소행렬에서 제거
                    if i[2] == 0:
                        ab.s.remove(i)
                        ab.s[0][2] -= 1
                return ab
            else :
                return 'dimention missmatch!'
        else :
            return 'not a matrix!'


a = Sparse_matrix(3,3)
a.append(0,0,1)
a.append(1,0,1)
a.append(1,1,2)
a.append(2,0,1)
a.append(2,1,2)
a.append(2,2,3)
a.print()
print()

b = Sparse_matrix(3,1)
b.append(0,0,-2)
b.append(1,0,1)
b.append(2,0,4)
b.print()
print()

ab = Sparse_matrix.dot(a,b)
ab.print()
print(ab.s)

c = Sparse_matrix(3,3)
c.append(1,2,3)
c.append(0,0,1)

ac = Sparse_matrix.dot(a,c)
ac.print()