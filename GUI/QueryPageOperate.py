import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from GUI.UIQuery import Ui_query_Form


class UI_program_query_person_op(QWidget):
    def __init__(self, database, parent=None):
        super(UI_program_query_person_op, self).__init__(parent)
        self.ui_query = Ui_query_Form()
        self.ui_query.setupUi(self)
        self.ui_query.tableWidget.setColumnCount(7)

        self.ui_query.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取
        self.ui_query.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置选取方式为单个选取
        self.ui_query.tableWidget.setHorizontalHeaderLabels(
            ["name", "title", "tel", "email", "comp", "addr", "id"])  # 设置行表头
        self.ui_query.tableWidget.horizontalHeader().setVisible((True))
        self.ui_query.tableWidget.verticalHeader().setVisible(True)  # 隐藏列表头
        self.ui_query.pushButton.clicked.connect(self.query_button)
        self.ui_query.pushButton_2.clicked.connect(self.delete_button)
        self.ui_query.pushButton_3.clicked.connect(self.save_change)
        self.ui_query.pushButton_4.clicked.connect(self.exit_program)
        self.ui_query.pushButton_5.clicked.connect(self.add_one)
        self.database = database

        self.new_sig = False

    def query_button(self):
        print("查询信息按键")
        # 获得要搜索的属性
        attribute = self.ui_query.comboBox.currentText()
        # 获得要搜索的属性对应的内容
        query_infomation = self.ui_query.lineEdit.text()
        # 首先进行查询
        print(attribute + query_infomation)
        dataframe_result = self.database.search(attribute, query_infomation)
        # 先将表格清空

        self.ui_query.tableWidget.setRowCount(0)
        self.ui_query.tableWidget.clearContents()

        line_count = 0
        # 循环遍历结果dataframe_result然后注入表格中的空行
        for row_line in dataframe_result.itertuples():
            line_count = line_count + 1
            # 获取当前的空行
            row = self.ui_query.tableWidget.rowCount()
            self.ui_query.tableWidget.insertRow(row)

            item_name = QTableWidgetItem(getattr(row_line, 'name'))
            item_title = QTableWidgetItem(getattr(row_line, 'title'))  # 我们要求它可以修改，所以使用默认的状态即可
            item_tel = QTableWidgetItem(getattr(row_line, 'tel'))
            item_email = QTableWidgetItem(getattr(row_line, 'email'))
            item_comp = QTableWidgetItem(getattr(row_line, 'comp'))
            item_addr = QTableWidgetItem(getattr(row_line, 'addr'))
            item_id = QTableWidgetItem(getattr(row_line, 'id'))
            item_id.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

            self.ui_query.tableWidget.setItem(row, 0, item_name)
            self.ui_query.tableWidget.setItem(row, 1, item_title)
            self.ui_query.tableWidget.setItem(row, 2, item_tel)
            self.ui_query.tableWidget.setItem(row, 3, item_email)
            self.ui_query.tableWidget.setItem(row, 4, item_comp)
            self.ui_query.tableWidget.setItem(row, 5, item_addr)
            self.ui_query.tableWidget.setItem(row, 6, item_id)

        ms = '查询到%d条信息' % line_count
        self.ui_query.label_4.setText(ms)

    def delete_button(self):
        print("删除数据按键")
        row_select = self.ui_query.tableWidget.selectedItems()
        if len(row_select) == 0:
            return
        id = row_select[6].text()
        row = row_select[0].row()
        print(row)
        print(id)

        ms1 = '*name:    %s' % row_select[0].text() + '\n'
        ms2 = '*title:   %s' % row_select[1].text() + '\n'
        ms3 = '*tel:     %s' % row_select[2].text() + '\n'
        ms4 = '*email:   %s' % row_select[3].text() + '\n'
        ms5 = '*comp:    %s' % row_select[4].text() + '\n'
        ms6 = '*addr:    %s' % row_select[5].text() + '\n'
        ms7 = '*id:      %s' % row_select[6].text() + '\n'

        result = ms1 + ms2 + ms3 + ms4 + ms5 + ms6 + ms7
        ms = '信息：\n' + result + '从数据库中删除！\n'

        self.ui_query.textBrowser.setText(ms)
        print(ms)
        self.ui_query.tableWidget.removeRow(row)
        self.database.delete(id)

    def add_one(self):
        print("创建新的行")
        self.new_sig = True
        row = self.ui_query.tableWidget.rowCount()
        self.ui_query.tableWidget.insertRow(row)
        item1 = QTableWidgetItem()
        item2 = QTableWidgetItem()
        item3 = QTableWidgetItem()
        item4 = QTableWidgetItem()
        item5 = QTableWidgetItem()
        item6 = QTableWidgetItem()
        item7 = QTableWidgetItem()

        self.ui_query.tableWidget.setItem(row, 0, item1)
        self.ui_query.tableWidget.setItem(row, 1, item2)
        self.ui_query.tableWidget.setItem(row, 2, item3)
        self.ui_query.tableWidget.setItem(row, 3, item4)
        self.ui_query.tableWidget.setItem(row, 4, item5)
        self.ui_query.tableWidget.setItem(row, 5, item6)
        self.ui_query.tableWidget.setItem(row, 6, item7)

        self.ui_query.textBrowser.setText('请在此新行中编辑信息,并保持选中此行,然后点击——保存信息变动——按键进行保存\n')

    def save_change(self):
        print("当信息被修改时调用")
        row_select = self.ui_query.tableWidget.selectedItems()
        if len(row_select) == 0:
            return
        print("name")
        row = row_select[0].row()
        name = '%s' % row_select[0].text()
        title = '%s' % row_select[1].text()
        tel = '%s' % row_select[2].text()
        email = '%s' % row_select[3].text()
        comp = '%s' % row_select[4].text()
        addr = '%s' % row_select[5].text()
        id = '%s' % row_select[6].text()

        new_data = dict(name=name,
                        title=title,
                        tel=tel,
                        email=email,
                        comp=comp,
                        addr=addr,
                        id=id)
        print(new_data)

        ms1 = '*name:    %s' % row_select[0].text() + '\n'
        ms2 = '*title:   %s' % row_select[1].text() + '\n'
        ms3 = '*tel:     %s' % row_select[2].text() + '\n'
        ms4 = '*email:   %s' % row_select[3].text() + '\n'
        ms5 = '*comp:    %s' % row_select[4].text() + '\n'
        ms6 = '*addr:    %s' % row_select[5].text() + '\n'
        result = ms1 + ms2 + ms3 + ms4 + ms5 + ms6
        ms = '信息：\n' + result + '将存入数据库！\n'

        self.ui_query.textBrowser.setText(ms)
        print(ms)
        if self.new_sig:
            print(self.new_sig)
            id = self.database.store_dict(new_data)
            print(id)
            item_id = QTableWidgetItem(id)
            self.ui_query.tableWidget.setItem(row, 6, item_id)
            self.new_sig = False
        else:
            new_data['id'] = row_select[6].text()
            print(new_data)
            self.database.update(new_data)

    def exit_program(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = UI_program_query_person_op()
    program.show()
    sys.exit(app.exec_())
