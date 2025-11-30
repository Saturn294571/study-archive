class Dijkstra:
    def __init__(self,nodes):
        self.g = {}
        self.dist = {}
        for node in nodes:
            self.g[node] = {}
            self.dist[node] = [float("inf"), "none"]

    def setEdge(self,a,b,w,bidirection=True):
        self.g[a][b] = w
        if bidirection == True: self.g[b][a] = w

    def _dicFilter(self, cost, nodes):
        import sys
        mini = sys.maxsize
        for key, value in cost.items():
            if key in nodes:
                if value[0] < mini:
                    mini = value[0]
                    curNode = key
        return curNode

    def getPath(self,start,end):
        visits = set()
        curNode = start
        self.dist[curNode][0] = 0
        while True:
            visits.add(curNode)
            nodes.remove(curNode)
            neighbors = self.g[curNode]

            for node in neighbors:
                if min(self.dist[node][0], self.dist[curNode][0] + self.g[curNode][node]) < self.dist[node][0]:
                    self.dist[node][0] = min(self.dist[node][0], self.dist[curNode][0] + self.g[curNode][node])
                    self.dist[node][1] = curNode

            if len(nodes) > 0:
                curNode = self._dicFilter(self.dist, nodes)
            else:
                break

        path = [end]
        dist = []

        while end != start:
            path.append(self.dist[end][1])
            dist.append(self.dist[end][0])
            end = self.dist[end][1]

        return path[::-1], dist[::-1]

import csv
subwayLoc = {} # 지하철역 이름과 [위도, 경도] 딕셔너리 구성
f = open('D:/NaverCloud/Lecture/PyWork/datastructure/subwayLocation.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    if line[0] not in subwayLoc:
        subwayLoc[line[0]] = [float(line[1]), float(line[2])]
f.close()

f = open('D:/NaverCloud/Lecture/PyWork/datastructure/subway.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
# 지하철역간의 거리 데이터로 부터 역 집합을 만든다.
nodes = set()
for line in rdr:
    temp1 = line[0]
    temp2 = line[1]
    nodes.add(temp1)
    nodes.add(temp2)
f.close()

lineNo = []
for node in nodes:
    lineNo.append(node[-2])

names = subwayLoc.keys()
location = list(subwayLoc.values())

f = open('D:/NaverCloud/Lecture/PyWork/datastructure/subway.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)

d = Dijkstra(nodes)

for line in rdr:
    d.setEdge(line[0],line[1], int(line[2]))
f.close()

print(d.getPath('남태령(4)','종각(1)'))
