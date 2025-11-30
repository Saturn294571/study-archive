#PRIM
import sys

N = 7  # 그래프 정점 수
s = 0  # 시작 정점
g = [None for x in range(N+1)]

g[0] = [(1, 9), (2, 10)]
g[1] = [(0, 9), (3, 10), (4, 5), (6, 3)]
g[2] = [(0, 10), (3, 9), (4, 7), (5, 2)]
g[3] = [(1, 10), (2, 9), (5, 4), (6, 8)]
g[4] = [(1, 5),  (2, 7), (6, 1)]
g[5] = [(2, 2),  (3, 4), (6, 6)]
g[6] = [(1, 3),  (3, 8), (4, 1), (5, 6)]


visited = [False for x in range(N+1)]  # 초기화
D = [sys.maxsize for x in range(N+1)]  # D[i]를 최댓값으로 초기화
D[s] = 0
previous = [None for x in range(N+1)]  # 최소신장트리 간선 추출위해
previous[s] = s
 
for k in range(N):    
    m = -1
    min_value = sys.maxsize

    for j in range(N): # 방문안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j          
    
    visited[m] = True  

    for w, wt in g[m]: # m에 인접한 방문 안된 각 정점의 D의 원소 갱신          
        if not visited[w]:  
            if wt < D[w]:            
                D[w] = wt  # D 원소 갱신
                previous[w] = m
 

print('최소신장트리: ', end='')
mst_cost = 0

for i in range(1,N):
    print('(%d, %d)'% (i, previous[i]), end='')
    mst_cost += D[i]
print('\n최소신장트리 가중치: ', mst_cost)