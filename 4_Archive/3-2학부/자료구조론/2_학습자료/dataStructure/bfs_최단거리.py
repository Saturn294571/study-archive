class BFS:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end

    def minPath(self):
        queue = []
        parentsQueue = []
        queue += self.graph[self.start]
        # BFS를 수행하면서 큐에 추가되는 item의 parent를 parentsQueue에 추가함
        parentsQueue += [self.start] * len(self.graph[self.start])  
        # temps: 시작노드의 이웃노드를 큐에 추가하고 큐에 추가된 노드의 부모는 시작노드이므로 시작노드를 부모로 추가함
        visit = [self.start]
        parents = ['None']  # parent는 경로에서 현재 노드를 방문하기 위해 거쳐야하는 노드를 의미함

        #d = 0
        while queue:
            item = queue.pop(0)
            temp = parentsQueue.pop(0)
            if not item in visit:  # 현재 아이템이 가본 곳이 아니면 ...
                queue += self.graph[item]
                parentsQueue += [item] * len(self.graph[item])
                visit.append(item)
                parents.append(temp)
                if item == self.end:  # 순회 도중 목적지를 만나면 ...
                    visits = dict(zip(visit, parents))  # visit item과 그의 부모 item을 딕셔너리로 만들어 리턴함
                    print(visits)    
        path = [self.end]

        curNode = self.end
        while True:
            parent = visits[curNode]
            path.append(parent)
            curNode = parent
            if parent == 'None': break
        return path[::-1][1:]

korea = {'세종': set(['서울', '대구', '광주']),
         '서울': set(['평양', '인천', '세종', '강릉','대구']),
         '강릉': set(['서울']),
         '광주': set(['세종', '여수']),
         '대구': set(['세종', '울산', '서울']),
         '평양': set(['서울']),
         '인천': set(['서울']),
         '여수': set(['광주', '부산']),
         '울산': set(['대구', '부산']),
         '부산': set(['울산' ,'여수' ]),
         }
path = BFS(korea, '부산', '평양')  # 부산에서 평양을 가는 BFS를 생성한다.
print(path.minPath())

