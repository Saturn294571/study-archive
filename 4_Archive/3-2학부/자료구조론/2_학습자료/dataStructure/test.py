class Dijkstra:
    def __init__(self,nodes):
        self.nodes = nodes
        self.g = {}
        self.dist = {}
        for node in nodes:
            self.g[node] = {}
            self.dist[node] = [float("inf"), "none"]

    def setEdge(self,a,b,w,bidirection=True):
        self.g[a][b] = w
        if bidirection == True: self.g[b][a] = w

    def _dicFilter(self, cost, nodes):
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
            self.nodes.remove(curNode)
            neighbors = self.g[curNode]

            for node in neighbors:
                if min(self.dist[node][0], self.dist[curNode][0] + self.g[curNode][node]) < self.dist[node][0]:
                    self.dist[node][0] = min(self.dist[node][0], self.dist[curNode][0] + self.g[curNode][node])
                    self.dist[node][1] = curNode

            if len(self.nodes) > 0:
                curNode = self._dicFilter(self.dist, self.nodes)
            else:
                break

        path = [end]
        dist = []

        while end != start:
            path.append(self.dist[end][1])
            dist.append(self.dist[end][0])
            end = self.dist[end][1]

        return path[::-1], dist[::-1]

import sys
import csv
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtGui
from PyQt5.uic import loadUiType
import folium # pip install folium
import webbrowser

form_class=loadUiType("subway.ui")[0]

class SubwayClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.stationLists.clicked.connect(self.selectStationClick)
        self.runButton.clicked.connect(self.runClick)

        self.subwayLoc = {} # 지하철역 이름과 [위도, 경도] 딕셔너리 구성

        f = open('D:/NaverCloud/Lecture/PyWork/datastructure/subwayLocation.csv', 'r', encoding='utf-8-sig')
        rdr = csv.reader(f)
        for line in rdr:
            if line[0] not in self.subwayLoc:
                self.subwayLoc[line[0]] = [float(line[1]), float(line[2])]
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

        # names = subwayLoc.keys()
        # location = list(subwayLoc.values())

        f = open('D:/NaverCloud/Lecture/PyWork/datastructure/subway.csv', 'r', encoding='utf-8-sig')
        rdr = csv.reader(f)

        self.d = Dijkstra(nodes)

        for line in rdr:
            self.d.setEdge(line[0],line[1], int(line[2]))
        f.close()
        #print(nodes)

        self.model = QtGui.QStandardItemModel()
        self.stationLists.setModel(self.model)

        for node in nodes:
            self.model.appendRow(QtGui.QStandardItem(node))

    def selectStationClick(self, index):
        if len(self.station_start.text()) > 0 and len(self.station_destination.text()) > 0:
            self.station_start.setText(self.model.itemFromIndex(index).text())
            self.station_destination.setText("")
        elif len(self.station_start.text()) == 0:
            self.station_start.setText(self.model.itemFromIndex(index).text())
        else:
            self.station_destination.setText(self.model.itemFromIndex(index).text())

    def runClick(self):
        pathList, pathTime = self.d.getPath(self.station_start.text(),self.station_destination.text())
        pathNames = []
        pathLine = []
        xbar = 0
        ybar = 0
        for item in pathList:
            pathNames.append(item[:-3])
            xbar += self.subwayLoc[item[:-3]][0]
            ybar += self.subwayLoc[item[:-3]][1]
            pathLine.append(item[-2])

        xbar = xbar / len(pathList)
        ybar = ybar / len(pathList)

        # folium 패키지를 이용하여 평균 위치의 지도를 가져온다.
        map_osm = folium.Map(location=[xbar, ybar],  zoom_start=12)
        paths = []
        # 지도상에 경로상의 지하철역을 CircleMarker로 표시하고 역 사이를 PolyLine으로 연결한다.
        for name in pathNames:
            loc = self.subwayLoc[name]
            idx = pathNames.index(name)
            if pathLine[idx] == '1': color = 'blue'
            elif pathLine[idx] == '2': color = 'green'
            elif pathLine[idx] == '3': color = 'orange'
            elif pathLine[idx] == '4': color = 'cyan'
            folium.CircleMarker(loc, radius=5, popup=name, color=color,fill=True,fill_color=color).add_to(map_osm)
            paths.append(loc)

        folium.PolyLine(paths, color="red", weight=3, opacity=1).add_to(map_osm)

        # 지도를 html 파일로 저장하고 저장된 파일을 웹브라우저로 출력한다.

        map_osm.save('minPath.html')
        webbrowser.open_new_tab('minPath.html')


app = QApplication(sys.argv)
myWindow = SubwayClass(None)
myWindow.show()
app.exec_()    