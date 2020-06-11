#coding=utf-8
import xlrd
import xlwt
from xlwt import Workbook
from xlutils.copy import copy
import os 
import sys 
reload(sys)
sys.setdefaultencoding('utf8')

excel_sheet=[]

lists = []
dicts = {}
def creat_excel():
    excel_name = excel_sheet[0]
    sheet = excel_sheet[1]
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet(sheet)
    sheet1.write(0,0,"姓名")
    sheet1.write(0,1,"年龄")
    sheet1.write(0,2,"学号")

    book.save(excel_name+".xls")

#TODO: 创建一个Excel表类
class Excel(object):
    def __init__(self, path):
        self.path = path #?绝对路径（带文件名）
 
 
#TODO: 读取Excel内全部数据 参数sname是sheet页名字 
    def read_all_data(self, sname): 
        workbook = xlrd.open_workbook(self.path)
        content = workbook.sheet_by_name(sname)
        ord_list=[]
        for rownum in range(content.nrows):
            ord_list.append(content.row_values(rownum))
        #返回的类型是一个list
        return ord_list
 
 
#TODO:  写入单行Excel表
    # 参数obj指的是新添加的按表头顺序排列的list类型数据，
    # sname指的是sheet页名字
    def write_row_data(self, obj, sname):
        wb = xlrd.open_workbook(self.path)
        sheet = wb.sheet_by_name(sname)
        nrows=sheet.nrows
        new_wb = copy(wb)  # 将原有的Excel，拷贝一个新的副本
        new_sheet = new_wb.get_sheet(0) # 重新在新的Excel中获取
        for i in range(len(obj)):
            new_sheet.write(nrows,i,obj[i])
        new_wb.save(self.path)
        return '存入成功！'
 
 
#TODO: 修改单行数据
#obj传的是字典对象，{'ID':'***','要修改的某一表头':'修改的内容'}，sname指的是sheet名
    def write_cell_data(self, obj, sname):
        #3.1 获取当前指定 sheet
        #3.2 Copy
        #3.3 get_sheet(0)
        #3.4 循环查找当前 sheet 内容
        #3.4.1 对 obj的指定内容 要进行匹配 
        #3.4.1.1如果找到了 就修改 msg = ok
        #3.4.1.2没有找到 就得  msg = error
        #3.5 save
        #3.6 return msg
        wb = xlrd.open_workbook(self.path)
        sheet = wb.sheet_by_name(sname)
        col_val=sheet.col_values(0)#第一列的值
        row_val=sheet.row_values(0)
        keys=list(obj.keys())
        set_col=0
        set_nrows=0
        # set_nrows=col_val.index(int(obj[keys[0]]))
        for j in range(len(col_val)):            
            if col_val[j]==obj[keys[0]]:
                set_nrows=j
        for i in range(len(row_val)):
            if row_val[i]==keys[1]:
                set_col=i
        if set_col==0 or set_nrows==0:
            msg=False
            return msg
        else:
            new_wb = copy(wb)
            new_sheet = new_wb.get_sheet(0)
            new_sheet.write(set_nrows,set_col,obj[keys[1]])
            new_wb.save(self.path)
            msg=True
            return msg
 
 
#TODO: 清空Excel表的内容，参数sname是sheet页名
    def delete_all_data(self,sname):
        red_all=self.read_all_data(sname)
        new_ord=[]
        new_ord.append(red_all[0])
        wbt = xlwt.Workbook()
            # 生成一个sheet页
        sheet = wbt.add_sheet(sname)
        for m in range(len(new_ord)):
            for n in range(len(new_ord[m])):
                sheet.write(m, n, new_ord[m][n])
        wbt.save(self.path)
 
 
#TODO: 删除某一行的数据，参数obj指的是某行，sname是sheet页名       
    def delete_row_data(self,obj,sname):
        wb = xlrd.open_workbook(self.path)
        sheet = wb.sheet_by_name(sname)
        col_val=sheet.col_values(0)#第一列的值
        del_nrows=0
        for j in range(len(col_val)):
            if col_val[j]==int(obj):
                del_nrows=j
        if del_nrows==0:
            msg=False
            return msg
        else:
            red_all=self.read_all_data(sname)
            a=red_all.pop(del_nrows)
            wbt = xlwt.Workbook()
            # 生成一个sheet页
            sheet = wbt.add_sheet(sname)
            for m in range(len(red_all)):
                for n in range(len(red_all[m])):
                    sheet.write(m, n, red_all[m][n])
            wbt.save(self.path)
            msg=True
            return msg
def creat_data():
    excel_name = raw_input("请输入要操作的文件名：")
    sheet = raw_input("请输入操作的sheet名：")
    excel_sheet.append(excel_name)
    excel_sheet.append(sheet)

def input_excel():
    name = raw_input("请输入姓名：")
    age = raw_input("请输入年龄：")
    number = raw_input("请输入学号：")
        
    lists.append(name)
    lists.append(age)
    lists.append(number)

#    print lists

def revise_data():
    olddata = raw_input("请输入要修改的数据：")
    newdata =  raw_input("请输入修改后的内容：")
    dicts[olddata] = newdata
    dicts[1]= 1
    print dicts


def main():
    creat_data()
    filename = excel_sheet[0]
    sheet = excel_sheet[1]
    while 1==1:
        print("""
                功能菜单：
                1.创建表
                2.查看表内容
                3.增加一行数据
                4.修改单行数据
                5.删除某一行数据
                6.查找数据
                7.删除数据
                0.exit
                """
            )
        youinput = int(raw_input("请输入你的选择："))
        if youinput == 1:
            creat_excel()
        elif youinput ==2:
            excel = Excel("/home/ubuntu/ryan/python/10-excel/"+filename+".xls")
            data = excel.read_all_data(sheet)
            print data
        elif youinput == 3:
            input_excel()
            excel.write_row_data(lists,sheet)
            lists = []
        elif youinput ==4:
            revise_data()
            excel.write_cell_data(dicts,sheet)
        elif youinput == 0:
            sys.exit(0)    
    #path __file__
    #动态获取路径 获取当前py文件 所在的目录
    # d = os.path.dirname(__file__)
    #获取当前py文件执行时候的父级目录
if __name__ == "__main__":
    main()
