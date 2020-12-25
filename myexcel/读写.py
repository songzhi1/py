# -*-coding:UTF-8 -*-


from pymysql import connect
from xlwt.Formatting import Borders, Font, Alignment, Pattern
from xlwt.Style import XFStyle
from xlwt.Workbook import Workbook


wb=Workbook('utf-8')
sheet=wb.add_sheet('自動化報告')

title=['編號','姓名','生日','性别']

title_style=XFStyle()
border=Borders()
border.left=border.THIN
border.right=border.THIN
border.top=border.THIN
border.bottom=border.THIN


font=Font()
font.bold=True
aligenment=Alignment()
aligenment.horz=Alignment.HORZ_CENTER

pattern=Pattern()
pattern.pattern=pattern.SOLID_PATTERN
pattern.pattern_fore_colour=0x35

title_style.borders=border
title_style.font=font
title_style.alignment=aligenment
title_style.pattern=pattern

for i in range(len(title)):
    sheet.write(4,4+i,title[i],title_style)


conn=connect(host='192.168.1.4',user='root',password="root",database='cms',port=3306)
cursor=conn.cursor()
cursor.execute('select * from _cai_student_cai')
result = cursor.fetchall()
print(result)



content=result
content_style=XFStyle()
border=Borders()
border.left=border.THIN
border.right=border.THIN
border.top=border.THIN
border.bottom=border.THIN

content_style.borders=border

for i in range(len(content)):
    for j in range(len(content[i])):
        sheet.write(5+i,4+j,content[i][j],content_style)

cursor.close()
conn.close()
wb.save(r'd:\读写.xls')
