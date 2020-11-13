# Pie Chart class , get a pie chart html or picture


from pyecharts.charts import Pie
import pyecharts.options as opts
from pyecharts.globals import CurrentConfig
from ToolClasses import PhoneSearch as ps
from DatabaseManager import DatabaseManager as dm

CurrentConfig.ONLINE_HOST = "https://cdn.bootcdn.net/ajax/libs/echarts/5.0.0-beta.1/"


class PieChart(object):

    # start the web server , and get the html files or pictures

    def GetPie(self):
        provinces = {}
        # Instantiate a phone search
        getCity = ps.PhoneSearch()
        frames = dm.DatabaseManager('lab.db').get_all()
        print(frames)
        for row in frames.itertuples():
            telephone = getattr(row, 'telephone')
            print(telephone)
            city = getCity.search(telephone)
            print(city)
            province = city['province']
            if province in provinces:
                provinces[province] = provinces[province] + 1
            else:
                provinces[province] = 1

        # attr = ["河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东",
        #         "海南", "四川", "贵州", "云南", "陕西", "甘肃", "青海", "台湾", "内蒙古", "广西", "西藏", "宁夏",
        #         "新疆", "北京", "天津", "上海", "重庆", "香港", "澳门"]
        attr = list(provinces.keys())
        v1 = list(provinces.values())
        print(attr)
        print(v1)
        print(provinces)
        pie = (Pie().add(
            "", [list(z) for z in zip(attr, v1)], center=["35%", "50%"]
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="人数省份分布饼图"),
            legend_opts=opts.LegendOpts(pos_left="78%")
        ).set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
        pie.render("lab.html")
        # c = (
        #     Pie()
        #         .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        #         .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        #         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        #         .render("pie_base.html")
        # )
