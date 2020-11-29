import pandas as pd


class Data_Base_op():
    def __init__(self, data_file):
        self.__data_file = data_file
        self.__data_base = pd.read_excel(self.__data_file)
        self.__data_base = pd.DataFrame(self.__data_base)
        print(self.__data_base)

    def insert_person(self, data):
        self.__data_base = self.__data_base.append(data, ignore_index=True)
        print("[*] Data_Base_op : insert 1 into database!")
        print(self.__data_base)

    def store_into_file(self):
        self.__data_base.to_excel(self.__data_file, index=False, encoding='utf-8')
        print("[*] Data_Base_op : Successfully store into file: test.xlsx !")
