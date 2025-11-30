# PyQT Version
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, qApp, QFileDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap

form_class = loadUiType("imageViewer.ui")[0]

class ViewerClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.actionSelect.triggered.connect(self.fileSelect)
        self.actionExit.triggered.connect(qApp.quit)
        self.shuffleButton.clicked.connect(self.shuffle)

    def shuffle(self):
        pass
        
    def fileSelect(self):
        fname = QFileDialog.getOpenFileName(self)
        qPixmapVar = QPixmap()
        qPixmapVar.load(fname[0])
        qPixmapVar = qPixmapVar.scaled(700, 400, aspectRatioMode=True)
        self.label.setPixmap(qPixmapVar)

app = QApplication(sys.argv)
myWindow = ViewerClass(None)
myWindow.show()
app.exec_()