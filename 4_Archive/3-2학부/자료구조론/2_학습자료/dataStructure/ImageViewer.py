import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog 
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap, QImage
import cv2 # pip install opencv-python
import matplotlib.pyplot as plt
import glob
import os

form_class=loadUiType("imageViewer.ui")[0]
class ViewerClass(QMainWindow, form_class):

    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.fileSelect)
        self.actionFolder_Open.triggered.connect(self.folderSelect)
        #self.nextButton.clicked.connect(self.moveNextClick)
        self.hh = 600
        self.ww = 600

    def fileSelect(self):
        self.fName = QFileDialog.getOpenFileName(self, 'Open file', 'D:/NaverCloud/Lecture/자료구조',"Image files (*.jpg)")[0]
        self.qPixmapVar = QPixmap(self.file2QImage(self.fName))
        self.qPixmapVar = self.qPixmapVar.scaled(self.hh, self.ww, aspectRatioMode=True)
        self.label.setPixmap(self.qPixmapVar)

    def folderSelect(self):
        dirName = QFileDialog.getExistingDirectory(self, 'Open Folder', 'D:/NaverCloud/Lecture/자료구조')
        self.files = []
        for file in glob.glob(os.path.join(dirName, '*.jpg')):
            self.files.append(file)
        self.idx = 0
        self.qPixmapVar = QPixmap(self.file2QImage(self.files[0]))
        self.qPixmapVar = self.qPixmapVar.scaled(self.hh, self.ww, aspectRatioMode=True)
        self.label.setPixmap(self.qPixmapVar)

    def file2QImage(self, fName):
        self.img = plt.imread(fName)
        return QImage(self.img, self.img.shape[1], self.img.shape[0], self.img.shape[1] * 3, QImage.Format_RGB888)

app = QApplication(sys.argv)
myWindow = ViewerClass(None)
myWindow.show()
app.exec_()
