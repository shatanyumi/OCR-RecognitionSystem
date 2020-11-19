import sys

from PIL.Image import Image
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from DatabaseManager import DatabaseManager
from GUI.DataWash import Data_Wash
from GUI.FirstEdition import Ui_main_Form
from GUI.QueryPageOperate import UI_program_query_person_op
from ToolClasses import OCR
from ToolClasses import PyechartsGenerator
from GUI import VisualizeData

class UI_program_main_op(QWidget):
    def __init__(self, database_manager, parent=None):
        super(UI_program_main_op, self).__init__(parent)
        self.ui_main = Ui_main_Form()
        self.ui_main.setupUi(self)
        self.database_manager = database_manager

    def load_picture(self):
        print("load--file")
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        if fname == "":
            return
        pixmax = QPixmap(fname)
        scarepixmap = pixmax.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)
        self.ui_main.label.setPixmap(scarepixmap)
        img = Image.open(fname)
        # 通过OCR类获取到字典
        json_result = OCR('5aba1bb3-ffef-4c5b-ad93-974d406edd49', img).remote_call()
        if json_result['code'] == '434':
            self.ui_main.textBrowser.setText("名片识别今天20次已经用完！\n")
            return
        # result = json.loads(json_result)
        dict_result = Data_Wash().wash_op(json_result)
        #
        self.database_manager.store_dict(dict_result)

        ms0 = '成功生成信息！\n'
        ms1 = '*姓名:   %s' % dict_result['name'] + '\n'
        ms2 = '*头衔:   %s' % dict_result['title'] + '\n'
        ms3 = '*公司:   %s' % dict_result['comp'] + '\n'
        ms4 = '*地址:   %s' % dict_result['addr'] + '\n'
        ms5 = '*电话:   %s' % dict_result['mobile'] + '\n'
        ms6 = '*手机:   %s' % dict_result['tel'] + '\n'
        ms7 = '*email:  %s' % dict_result['email'] + '\n'
        ms8 = '*传真:   %s' % dict_result['fax'] + '\n'
        result = ms0 + ms1 + ms2 + ms3 + ms4 + ms5 + ms6 + ms7 + ms8
        print(result)
        self.ui_main.textBrowser.setText(result)

    def query_person(self):
        print("查询联系人方法")
        # self.query_app = QApplication(sys.argv)
        # 启动查询UI程序，并向其传入数据库对象
        self.query_program = UI_program_query_person_op(self.database_manager)
        self.query_program.show()
        # sys.exit(self.query_app.exec_())

    def visualize_data(self):
        print("数据可视化发方法")
        PyechartsGenerator.PieChart().GetPie()
        app = QApplication(sys.argv)
        ex = VisualizeData()
        ex.show()
        sys.exit(app.exec_())

    def exit_program(self):
        sender = self.sender()
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    database_manager = DatabaseManager.DatabaseManager('system.db')
    database_manager.set_tablename('peoples')
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    program = UI_program_main_op(database_manager)
    program.show()
    sys.exit(app.exec_())
