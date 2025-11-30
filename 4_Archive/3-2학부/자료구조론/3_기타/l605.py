def isCycle(u, n): # u: 기존 그래프, n: 연결을 원하는 간선
    idx1 = idx2 = -1
    n1 = n[0]
    n2 = n[1]
    for i in range(len(u)):
        if n1 in u[i]: # 연결을 원하는 간선과 기존 그래프 어디에 매치되는가?
            idx1 = i
        if n2 in u[i]:
            idx2 = i

    if idx1 == -1 and idx2 == -1: # [n1,n2] 이 기존 리스트에 없다면
        u.append([n1,n2])
        print(u)
        return False
    elif idx1 == -1:              # [n1,n2] 이 기존 리스트 중 한 곳에만 있다면
        u[idx2].append(n1)
        print(u)
        return False
    elif idx2 == -1:              # [n1,n2] 이 기존 리스트 중 한 곳에만 있다면
        u[idx1].append(n2)
        print(u)
        return False
    elif idx1 != idx2: # [n1,n2] 이 기존 리스트에 서로 다른 곳에 존재한다면
        d1 = u[idx1]  # [[0,1,2],[3,4]],[2,3]
        d2 = u[idx2]
        union = d1 + d2
        u.remove(d1)
        u.remove(d2)
        u.append(union) # 서로의 집합을 합침
        print(u)
        return False

    elif idx1 == idx2 and len(u[idx1]) > 2:# [n1,n2] 이 기존 리스트에 같은 곳에 존재한다면
        print(u)
        return True

u = [[0, 1, 2],[3, 4]]
print(isCycle(u, (2,3)))
u = [[0, 1, 2],[3, 4]]
print(isCycle(u, (0,2)))
u = [[0, 1, 2],[3, 4]]
print(isCycle(u, (1,5)))
u = [[0, 1, 2],[3, 4]]
print(isCycle(u, (4,6)))

print('=========================================')

class SpanningTree:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = set()
        self.union = [] # union-find 알고리즘에서 기존 엣지 리스트

        # 그래프의 노드를 구함
        for edge in graph:
            self.nodes.add(edge[0])
            self.nodes.add(edge[1])
        self.nNode = len(self.nodes)

    def isCycle(self, n1, n2):
        idx1 = idx2 = -1
        for i in range(len(self.union)):
            if n1 in self.union[i]:
                idx1 = i
            if n2 in self.union[i]:
                idx2 = i

        if idx1 == -1 and idx2 == -1:
            self.union.append([n1, n2])
            return False
        elif idx1 == -1:
            self.union[idx2].append(n1)
            return False
        elif idx2 == -1:
            self.union[idx1].append(n2)
            return False
        elif idx1 != idx2:
            d1 = self.union[idx1]
            d2 = self.union[idx2]
            union = d1 + d2
            self.union.remove(d1)
            self.union.remove(d2)
            self.union.append(union)
            return False
        elif idx1 == idx2 and len(self.union[idx1]) > 2:
            print(self.union[idx1])
            return True
        else:
            return False

    def kruskal(self):
        self.graph.sort(key = lambda t: t[2]) # 그래프를 2번째 원소기준으로 소트한다.
        tree = []  # 최소비용신장트리를 담을 리스트를 만든다.
        nedges = 0 # nedges == self.nNode - 1이면 알고리즘이 끝난다.
        i = 0
        while nedges < self.nNode - 1:
            if self.isCycle(self.graph[i][0],self.graph[i][1]) == False:
                tree.append(self.graph[i])
                nedges += 1
            else:
                print("싸이클 발견",self.graph[i] )
            i += 1

        return tree

g = [(0,1,9),(0,2,10),(1,3,10),(1,4,5),(1,6,3),(2,3,9),(2,4,7),(2,5,2),(3,5,4),(3,6,8),(4,6,1),(5,6,6)]
t = SpanningTree(g)
print(t.kruskal())

print('=====================================')
# 경로 그래프를 만든다.
graph = (['start','A', 6],['start','B', 2], ['A', 'finish', 1], ['B', 'finish', 5], ['B', 'A', 3])
graph
'''
노드 집합을 만든다.
노드 집합에서 노드를 꺼내 방문하기 시작한다. 방문한 노드는 visits로 옮긴다.
nodes에 있는 모든 노드가 visits로 이동하면 알고리즘이 끝난다.
'''
nodes = set()
for node in graph:
    nodes.add(node[0])
    nodes.add(node[1])
nodes
aaa = float("inf")
type(aaa), aaa

# 방문한 노드를 기록하기 위한 집합을 만든다.
visits = set()

# 각 노드는 출발점과의 거리와 최적경로를 만족하는 부모노드를 지정해야 한다.
# 처음에는 최적경로를 모르므로 모든 노드와 거리는 무한대로 설정하고 각 노드의 부모노드는 "모름"으로 설정한다.

cost = {}

for node in nodes:
    cost[node] = [float("inf"), None]  # [노드까지 가는 비용, 부모노드]

# 시작과 끝 노드를 정의한다.
start = 'start'
end = 'end'

# 시작노드의 거리는 0으로 설정한다.
curNode = start
cost[curNode][0] = 0

print(cost)

# curNode에서 갈 수 있는 노드를 반환하는 함수다.
# 'start'에서 갈 수 있는 노드는 'A', 'B' 다.

def _neighbor(curNode):
    # curNode에 연결된 이웃노드를 리스트로 리턴한다.
    neighbor = {}
    for node in graph:
        if node[0] == curNode:
            neighbor[node[1]] = node[2]
        elif node[1] == curNode:
            neighbor[node[0]] = node[2]
    return neighbor

neighbors = _neighbor(curNode)
neighbors

# 그래프에서 노드 n1, n2의 가중값을 리턴한다.
def _getWeight(n1, n2):
    for node in graph:
        if (node[0] == n1 and node[1] == n2) or (node[0] == n2 and node[1] == n1):
            return node[2]
    return None

# curNode를 방문처리한다.
visits.add(curNode)
nodes.remove(curNode)   # 안 가본 노드

# 모든 이웃에 대해 현재 노드를 통해 이웃노드에 접근하는 cost가 더 작을 경우, cost 값을 갱신하고 부모노드를 변경한다.
# 'A': [6, 'start'] 는 'A'에 'start'를 통해 접근할 경우, cost가 6이란 의미다.
# 만약, 'A'에 다른 노드를 통해 접근할 때 더 작은 cost가 있다면 갱신한다.
# curNode에서 갈 수 있는 모든 이웃에 대해
# curNode를 통해 node로 가는 비용은 curNode까지 오는 비용 + curNode에서 node 까지 가는 비용이므로
# cost[curNode][0] + _getWeight(curNode,node)가 된다.
# 이 비용이 현재시점에서 알고있는 node 비용보다 작다면 node의 비용과 parent 노드를 curNode를 통해 가는 것으로 갱신한다.
# 초기 cost는 {'start': [0, None], 'B': [inf, None], 'A': [inf, None], 'finish': [inf, None]} 이다.
# 현재 노드의 이웃노드를 하나씩 꺼낸다.

# curNode : start
for node in neighbors:
    if cost[curNode][0] + _getWeight(curNode,node) < cost[node][0]:
        print(curNode)
        cost[node][0] = cost[curNode][0] + _getWeight(curNode, node)
        cost[node][1] = curNode

print(curNode, nodes)
print(cost)

# 딕셔너리 필터는 nodes에서 cost가 최소인 노드를 찾아 리턴한다.
# cost 중에 현재 노드에서 이동가능한 노드만 cost가 갱신 되어 있으므로 최소노드는 이동 가능한 노드 중에만 선택된다.
def dicFilter(cost, nodes):
    import sys
    mini = sys.maxsize       # 컴퓨터가 기억할 수 있는 최대값
    for key, value in cost.items():
        if key in nodes:
            if value[0] < mini:
                mini = value[0]
                curNode = key
    return curNode

print(cost, nodes)
curNode = dicFilter(cost, nodes)
curNode

# 'B'에서 갈 수 있는 노드는 'A', 'finish' 다.
print(curNode)
visits.add(curNode)
nodes.remove(curNode)
neighbors = _neighbor(curNode)
print(neighbors)

# 모든 이웃에 대해 현재 노드를 통해 이웃노드에 접근하는 cost가 더 작을 경우, dist 값을 갱신하고 부모노드를 변경한다.
# 'A' 로 갈 수 있는 방법이 'start'에서 직접 가는 것 보다 'B'를 통과해 가는 것이 비용이 작아 'A'의 비용과 부모노드가 갱신되었다.

for node in neighbors:
    if cost[curNode][0] + _getWeight(curNode,node) < cost[node][0]:
        cost[node][0] = cost[curNode][0] + _getWeight(curNode, node)
        cost[node][1] = curNode
print(curNode, nodes)
print(cost)

# {'finish', 'A'} 중에 비용이 작은 노드는 'A'다.
curNode = dicFilter(cost, nodes)
print(curNode)

neighbors = _neighbor(curNode)
print(neighbors)

visits.add(curNode)
nodes.remove(curNode)

for node in neighbors:
    if cost[curNode][0] + _getWeight(curNode,node) < cost[node][0]:
        cost[node][0] = cost[curNode][0] + _getWeight(curNode, node)
        cost[node][1] = curNode
print(curNode, nodes)
print(cost)

print('========================================')
# 그래프를 정의한다.(이 그래프는 양방향이다.)

graph = [(0, 1, 7), (0, 4, 3), (0, 5, 10), (1, 2, 4), (1, 4, 2),
         (1, 5, 6), (1, 3, 10), (2, 3, 2),(3, 5, 9), (3, 6, 4), (4, 6, 5)]

nodes = set()
for node in graph:
    nodes.add(node[0])
    nodes.add(node[1])
nodes

# 방문한 노드를 기록하기 위한 집합을 만든다.
visits = set()

# 출발점에서 모든 노드와 거리는 무한대로 설정하고 각 노드의 부모노드는 "모름"으로 초기설정한다.

cost = {}

for node in nodes:
    cost[node] = [float("inf"),None]

# 시작과 끝 노드를 정의한다.
start = 0
end = 3

# 시작노드의 거리는 0으로 설정한다.
curNode = start
cost[curNode][0] = 0

print(cost)

def _neighbor(curNode):
    # curNode에 연결된 이웃노드를 리스트로 리턴한다.
    neighbor = {}
    for node in graph:
        if node[0] == curNode:
            neighbor[node[1]]= node[2]
        elif node[1] == curNode:
            neighbor[node[0]] = node[2]
    return neighbor

def _getWeight(n1, n2):
    # 그래프에서 노드 n1, n2의 가중값을 리턴한다.
    for node in graph:
        if node[0] == n1 and node[1] == n2:
            return node[2]
        elif node[0] == n2 and node[1] == n1:
            return node[2]
    return None

def _dicFilter(cost, nodes):
    # 이동할 수 있는 노드 중에 cost기 최소인 노드를 리턴한다. --> 탐욕 알고리즘
    # cost 중에 현재 노드에서 이동 가능한 노드만 cost가 갱신 되어 있으므로 최소노드는 이동 가능한 노드 중에만 선택된다.
    import sys
    mini = sys.maxsize
    for key, value in cost.items():
        if key in nodes: # 아직 방문하지 않은 노드만
            if value[0] < mini:
                mini = value[0]
                curNode = key
    return curNode

while True:
    visits.add(curNode)       # 현재 노드를 방문 처리한다.
    nodes.remove(curNode)     # 남은 노드집합에서 현재 노드를 삭제한다.
    neighbors = _neighbor(curNode) # 현재 노드에서 갈 수 있는 이웃노드 집합을 구한다.

    # 모든 이웃에 대해 현재 노드를 통해 이웃노드에 접근하는 cost가 더 작을 경우, cost 값을 갱신하고 부모노드를 변경한다.
    for node in neighbors:
        if cost[curNode][0] + _getWeight(curNode,node) < cost[node][0]:
            cost[node][0] = cost[curNode][0] + _getWeight(curNode, node)
            cost[node][1] = curNode

    if len(nodes) > 0:
        print(curNode)
        curNode = _dicFilter(cost, nodes) # 이웃노드 중 가장 빠르게 갈 수 있는 노드를 구해 현재 노드를 갱신한다.(Greedy Algorithm)
        print(curNode)
    else:
        break

path = [end]

while end != start:
    path.append(cost[end][1])
    end = cost[end][1]

print(path[::-1])

class Graph :
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.s = []
        self.visit = []

    def dfs(self) :
        self.s.append(self.start) # start를 스택에 푸시
        while self.s :            # 스택 비어있지 않으면
            curNode = self.s.pop()# 스택에서 팝
            if curNode not in self.visit : # 가본 곳X?
                self.visit.append(curNode) # 가본 곳에 추가
                for node in sorted(list( # 이웃중 방문X 노드 집합?
                    set(self.graph[curNode])
                    - set(self.visit))) :
                    self.s.append(node) # 스택에 푸시
                print(curNode,end=' ')
                print(self.s)
        return self.visit