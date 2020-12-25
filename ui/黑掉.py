# -*-coding:UTF-8 -*-
from selenium import webdriver
from time import sleep


driver=webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('https://www.to8to.com/about/feedback.php')
driver.maximize_window()

for i in range(100):
    sleep(1)
    driver.find_element_by_id('fb').send_keys('图满意官方公众号渲染进度 投稿通知设计灵感 谈单获客功能教程 客服咨询扫一扫马上获取')
    driver.find_element_by_id('text').send_keys('cc')
    driver.find_element_by_class_name('new_btn').click()