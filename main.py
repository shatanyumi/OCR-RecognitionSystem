# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import os
from pyecharts.globals import CurrentConfig
import subprocess
import threading

CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"

from pyecharts.charts import Bar

def server():
    subprocess.run("python -m http.server", shell=True)

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.mainLayout()

    def initUI(self):
        self.setWindowTitle("lab")

    def mainLayout(self):
        self.mainhboxLayout = QHBoxLayout(self)
        self.frame = QFrame(self)
        self.mainhboxLayout.addWidget(self.frame)
        self.hboxLayout = QHBoxLayout(self.frame)

        # 网页嵌入PyQt5
        self.myHtml = QWebEngineView()  ##浏览器引擎控件
        # url = "http://www.baidu.com"
        # 打开本地html文件#使用绝对地址定位，在地址前面加上 file:/// ，将地址的 \ 改为/
        location = os.path.abspath('render.html')
        print(location)
        self.myHtml.load(QUrl('file:///' + location))

        self.hboxLayout.addWidget(self.myHtml)
        self.setLayout(self.mainhboxLayout)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("hello world")
    # y = open('test.json', 'r').read()
    # # y = json.loads(y)
    # # df = pd.DataFrame(y)
    # dbs = dm.DatabaseManager('lab.db')
    # print(dbs.search('赵'))
    # x = {'name': '赵云', 'title': '帆总经理', 'telephone': '0109959179', 'email': 'zhaoyunfan@hanwang.com',
    #      'company': '汉王科技股份有限公司', 'address': '中关村软件园汉王科技'}
    # dbs.store_dict(x)
    # y = ps.PhoneSearch('18383059638')
    # print(y.search())
    # print(y)
    # t = jd.JsonDataDealer('lab.db', y)
    # print(t.get_all())

    # V1 版本开始支持链式调用
    # 你所看到的格式其实是 `black` 格式化以后的效果
    # 可以执行 `pip install black` 下载使用
    # bar = (
    #     Bar()
    #         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    #         .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    #         .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    #     # 或者直接使用字典参数
    #     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
    # )
    # bar.render_notebook()
    #
    # app = pg.mkQApp()
    # x = np.linspace(0, 6 * np.pi, 100)
    # y = np.sin(x)
    # p = pg.plot(x, y, title=u'最简单绘图例子', left='Amplitude / V', bottom='t / s')
    # p.setLabels(title='y = sin(x)')
    # app.exec_()
    # bar = Bar()
    # bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    # bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    # # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    # # 也可以传入路径参数，如 bar.render("mycharts.html")
    # bar.render()
    threading.Thread(target=server).start()
    app = QApplication(sys.argv)
    ex = UI()
    ex.show()
    sys.exit(app.exec_())
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
