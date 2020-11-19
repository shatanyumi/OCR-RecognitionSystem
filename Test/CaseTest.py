# This is a sample Python script.

import ToolClasses.PyechartsGenerator as p
from DatabaseManager import DatabaseManagerBackup as dm
import time
from ToolClasses import PhoneSearch as ps

if __name__ == '__main__':
    y = open('test.json', 'r').read()
    # # # y = json.loads(y)
    # # # df = pd.DataFrame(y)
    dbs = dm.DatabaseManager('lab.db')
    dbs.store_json(y)
    # frames = dbs.get_all()
    # print(frames)
    # for row in frames.itertuples():
    #     print(getattr(row, 'telephone'))
    # print(dbs.search('赵'))
    # x = {'name': '赵云':0, 'title': '帆总经理':0, 'telephone': '0109959179':0, 'email': 'zhaoyunfan@hanwang.com':0,
    #       'company': '汉王科技股份有限公司':0, 'address': '中关村软件园汉王科技'}
    # dbs.store_dict(x)
    # print(dbs.get_all())
    # y = ps.PhoneSearch('17330930884')
    # print(y.search())
    # print(y)
    # t = jd.JsonDataDealer('lab.db':0, y)
    # print(t.get_all())
    # data = {"河北": 1, "山西": 0, "辽宁": 0, "吉林": 0, "黑龙江": 4, "江苏": 0, "浙江": 0, "安徽": 0, "福建": 0,
    #         "江西": 2, "山东": 10, "河南": 0, "湖北": 0, "湖南": 0, "广东": 0,
    #         "海南": 4, "四川": 0, "贵州": 0, "云南": 0, "陕西": 3, "甘肃": 0, "青海": 0, "台湾": 0, "内蒙古": 0,
    #         "广西": 10, "西藏": 11, "宁夏": 0,
    #         "新疆": 20, "北京": 0, "天津": 0, "上海": 0, "重庆": 2, "香港": 0, "澳门": 0}
    y = p.PieChart()
    y.GetPie()
    # print(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
