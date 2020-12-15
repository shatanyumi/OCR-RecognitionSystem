import sys

import pyqtgraph as pg
import qdarkstyle
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from DatabaseManager import DatabaseManager
from GUI.LoadPictureOp import Load_Picture_Op
from GUI.QueryPageOperate import UI_program_query_person_op
from GUI.VisualizeData import VisualizeData
from GUI.mainUI import Ui_Main
from ToolClasses import PyechartsGenerator


class UIProgramMainOperation(QMainWindow):
    def __init__(self, database_manager, parent=None):
        super(UIProgramMainOperation, self).__init__(parent)
        pg.setConfigOption('background', '#19232D')
        pg.setConfigOption('foreground', 'd')
        pg.setConfigOptions(antialias=True)

        self.ui_main = Ui_Main()
        self.ui_main.setupUi(self)
        self.database_manager = database_manager
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # 创建查询页面
        self.ui_main.query_form = UI_program_query_person_op(self.database_manager)
        self.ui_main.visual_form = VisualizeData()
        self.ui_main.load_picture_form = Load_Picture_Op(self.database_manager)

        # 设置堆叠格式
        self.ui_main.widget2.stacked_layout = QStackedLayout()
        self.ui_main.widget2.setLayout(self.ui_main.widget2.stacked_layout)

        self.ui_main.widget2.stacked_layout.addWidget(self.ui_main.query_form)
        self.ui_main.widget2.stacked_layout.addWidget(self.ui_main.visual_form)
        self.ui_main.widget2.stacked_layout.addWidget(self.ui_main.load_picture_form)

    def load_picture(self):
        print("上传照片方法")
        self.ui_main.widget2.stacked_layout.setCurrentIndex(2)

    def query_person(self):
        print("查询联系人方法")
        self.ui_main.widget2.stacked_layout.setCurrentIndex(0)

    def visualize_data(self):
        print("数据可视化发方法")
        PyechartsGenerator.PieChart().GetPie()
        self.ui_main.visual_form.mainLayout()
        self.ui_main.widget2.stacked_layout.setCurrentIndex(1)

    def exit_program(self):
        sender = self.sender()
        App = QApplication.instance()
        App.quit()


if __name__ == '__main__':
    databaseManager = DatabaseManager.DatabaseManager('system.db')
    databaseManager.set_tablename('peoples')
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    program = UIProgramMainOperation(databaseManager)
    program.show()
    sys.exit(app.exec_())
