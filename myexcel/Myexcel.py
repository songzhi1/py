# -*-coding:UTF-8 -*-
from xlrd import open_workbook

class MyExcel():
    def __init__(self,workbook_name,sheet_name):
        self.workbook_name=workbook_name
        self.sheet_name=sheet_name
        
    def __sheet(self):
        bk=open_workbook(self.workbook_name)
        sheet=bk.sheet_by_name(self.sheet_name)
        return sheet
    
    def total_rows(self):
        return self.__sheet().nrows
    
    
    def total_columns(self):
        return self.__sheet().ncols
    
    def cell_value(self):
        cell_value=self.__sheet().cell_value()