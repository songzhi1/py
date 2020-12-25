# -*-coding:UTF-8 -*-
from selenium import webdriver


driver=webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('https://www.baidu.com/?tn=21002492_27_hao_pg')
driver.maximize_window()
