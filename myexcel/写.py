# -*-coding:UTF-8 -*-



from xlwt.Formatting import Borders, Font, Alignment, Pattern
from xlwt.Style import XFStyle
from xlwt.Workbook import Workbook


wb=Workbook('utf-8')
sheet=wb.add_sheet('自動化報告')

title=['編號','姓名','職業','上级','入職時間']

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

content=[[1,'smith','测试','菜场','2020-10-10'],[2,'凤姐','开发','菜场','2020-10-11']]
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


wb.save(r'd:\zidonghuade.xls')
