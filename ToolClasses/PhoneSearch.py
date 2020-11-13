# phone search to get the place which phone belongs to
from phone import Phone


class PhoneSearch(object):

    def search(self, number):
        ph = Phone()
        city = ph.find(number)

        print(city)  # 所有信息
        print('手机号：' + number)
        print('所属省份：' + city['province'])
        print('所属市区：' + city['city'])
        print('邮    编：' + city['zip_code'])
        print('电话区号：' + city['area_code'])
        print('运 营 商：' + city['phone_type'])

        return city
