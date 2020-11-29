from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QFrame, QHBoxLayout
import os

class VisulizeData(object):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.mainLayout()

    def initUI(self):
        self.setWindowTitle("中国各省人口")

    def mainLayout(self):
        self.mainhboxLayout = QHBoxLayout(self)
        self.frame = QFrame(self)
        self.mainhboxLayout.addWidget(self.frame)
        self.hboxLayout = QHBoxLayout(self.frame)


        self.myHtml = QWebEngineView()
        file = os.path.abspath('system.html')
        self.myHtml.load(QUrl('file:///'+file))

        self.hboxLayout.addWidget(self.myHtml)
        self.setLayout(self.mainhboxLayout)

