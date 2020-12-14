import sys
from PIL import Image

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget

from GUI.OnloadPictureUI import Ui_Load_Picture_Form
from GUI.DataWash import Data_Wash
from ToolClasses.OCR import OCR


import pyqtgraph as pg
import qdarkstyle

class Load_Picture_Op(QWidget):
    def __init__(self, database, parent=None):
        super(Load_Picture_Op, self).__init__(parent)

        self.ui_query = Ui_Load_Picture_Form()
        self.ui_query.setupUi(self)
        self.database_manager = database
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


    def load_picture(self):
        print("load--file")
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png *jpeg)')
        if fname == "":
            print("can not open the picture!")
            return
        pixMax = QPixmap(fname)
        scarePixMap = pixMax.scaled(400, 400, aspectRatioMode=Qt.KeepAspectRatio)

        self.item = QGraphicsPixmapItem(scarePixMap)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.ui_query.graphicsView.setScene(self.scene)
        self.ui_query.graphicsView.show()

        print(fname)
        img = Image.open(fname)
        # 通过OCR类获取到字典
        json_result = OCR('5aba1bb3-ffef-4c5b-ad93-974d406edd49', img).remote_call()
        if json_result['code'] == '434':
            self.ui_query.textBrowser.setText("名片识别今天20次已经用完！\n")
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
        self.ui_query.textBrowser.setText(result)



