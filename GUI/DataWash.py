class Data_Wash():
    def wash_op(self, data):
        print("[*] Data_Wash : data has lodaded into Data_Wash!")
        # 删除不需要的列属性
        del data['rotatedAngle']
        del data['result']
        del data['code']
        del data['im']
        del data['numOther']
        del data['extTel']
        # 将各个列信息规范化
        for key, value in data.items():
            part = len(data[key]) / 5
            a = ""
            if part > 1:
                for i in range(1, int(part) + 1):
                    a = a + "+" + data[key][(i - 1) * 5]
                data[key] = a
            if part == 0:
                data[key] = ''
            if part == 1:
                data[key] = data[key][0]
        print(data)
        return data
