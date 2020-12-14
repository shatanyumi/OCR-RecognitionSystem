import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QApplication, QWidget
import pyqtgraph as pg
import qdarkstyle

class VisualizeData(QWidget):
    def __init__(self):
        super().__init__()
        pg.setConfigOption('background', '#19232D')
        pg.setConfigOption('foreground', 'd')
        pg.setConfigOptions(antialias=True)
        self.initUI()
        self.mainLayout()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


    def initUI(self):
        self.setWindowTitle("中国各省人口")

    def mainLayout(self):
        self.mainhboxLayout = QHBoxLayout(self)
        self.frame = QFrame(self)
        self.mainhboxLayout.addWidget(self.frame)
        self.hboxLayout = QHBoxLayout(self.frame)

        self.myHtml = QWebEngineView()
        file = os.path.abspath('system.html')
        file = file.replace("\\", '/')
        print('file:///' + file)
        self.myHtml.load(QUrl('file:///' + file))
        self.hboxLayout.addWidget(self.myHtml)
        self.setLayout(self.mainhboxLayout)
        self.setWindowOpacity(0.9)  # 设置窗口透明度


if __name__ == '__main__':
    App = QApplication(sys.argv)
    ex = VisualizeData()
    ex.show()
    sys.exit(App.exec_())
