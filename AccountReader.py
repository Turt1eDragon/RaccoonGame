import csv


class CSVDealer:

    @staticmethod
    def read():
        filename = '.\\accounts.csv'
        data = []
        with open(filename) as csvfile:
            csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
            # header = next(csv_reader)        # 读取第一行每一列的标题
            for row in csv_reader:  # 将csv 文件中的数据保存到data中
                data.append(row)  # 选择某一列加入到data数组中
        return data

    @staticmethod
    def write(accounts: list):
        # print('write')
        filename = '.\\accounts.csv'
        with open(filename, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for i in accounts:
                csv_writer.writerow(i)
