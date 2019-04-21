import xlwt, xlrd
import random


def create_excel():
    # 使用xlwt创建新的Excel表格
    English_ExcelTable = xlwt.Workbook()
    sheet = English_ExcelTable.add_sheet("sheet 1")
    sheet.write(0, 1, 'Example Text')
    English_ExcelTable.save('LearningEnglish')


def read_excel():
    # 使用xlrd读取Excel表格
    English_ExcelTable = xlrd.open_workbook('LearningEnglish')
    sheet = English_ExcelTable.sheet_by_name('sheet 1')

    dicts = {}
    rows_len = sheet.nrows
    # print(type(rows_len))
    # print(rows_len)
    # print("...")

    for i  in range(rows_len):
        content = sheet.row_values(i)
        dicts[content[0]] = content[1]

    return dicts


'''
 记单词v1版本,实现去除单词部分字符进行默写,帮助记忆
        v2功能预实现:
            1.打乱单词出现顺序,不要从第一个开始进行
            2.把错误单词提取,写入新Excel表格进行加强练习;
            3.在中文解释参杂英文解释,尽可能少出现中文,帮助英文记忆
'''


def app_v1():
    dicts = read_excel()
    num = 0
    for k, v in dicts.items():
        old_k = k
        nwords = int(len(k) * 0.3)
        for i in range(nwords):
            new_k = k.replace(k[random.randint(0,len(k)-1)], '_')
            k = new_k
        print("{0}:{1}".format(k, v))
        return_world = input("填写完整单词过关:")
        if return_world == old_k:
            print("NEXT")
            continue
        else:
            print("WORRY")
            num += 1
            continue


if __name__ == '__main__':
    app_v1()
