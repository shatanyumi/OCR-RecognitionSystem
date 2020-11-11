# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from DatabaseManager import DatabaseManager as dm


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("hello world")
    y = open('test.json', 'r').read()
    # y = json.loads(y)
    # df = pd.DataFrame(y)
    dbs = dm.DatabaseManager('lab.db')
    print(dbs.search('赵'))
    x = {'name': '赵云', 'title': '帆总经理', 'telephone': '0109959179', 'email': 'zhaoyunfan@hanwang.com',
         'company': '汉王科技股份有限公司', 'address': '中关村软件园汉王科技'}
    dbs.store_dict(x)
    # y = ps.PhoneSearch('18383059638')
    # print(y.search())
    # print(y)
    # t = jd.JsonDataDealer('lab.db', y)
    # print(t.get_all())

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
