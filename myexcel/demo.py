# -*-coding:UTF-8 -*-
from xlrd import open_workbook
bk=open_workbook(r'd:\emp.xls')
sheet=bk.sheet_by_name('empinfo')
print(sheet.nrows)

print(sheet.ncols)

#读有多少列
print(sheet.ncols) #column

#读某单元格（ANALYST）

cell_value = sheet.cell_value(12,6) #下标从0开始
print(cell_value)


#读整个第X（7）行数据

row_values = sheet.row_values(6,4)
print(row_values)


#读某列（姓名）数据
col_values = sheet.col_values(5,5)
print(col_values)


#读整个列表数据


for i in range(14):
    row_values = sheet.row_values(i,4)
    print(row_values)
print('=======')
for i in range(5,14):
    row_values = sheet.row_values(i,4)
    print(row_values)

