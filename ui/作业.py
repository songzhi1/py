# -*-coding:UTF-8 -*-
from time import sleep


from selenium import webdriver


driver=webdriver.Chrome()

# driver.get('https://mkt.51job.com/tg/sem/LP_2020_1.html?from=baidupz')
# driver.maximize_window()
# 
# 
# 
# 
# driver.find_element_by_link_text('登录').click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('15920413866')
# sleep(1)
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('xiu360360')

driver.get('https://login.51job.com/login.php')
driver.maximize_window()
 
 
 
 
# driver.find_element_by_link_text('登录').click()
# sleep(1)
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('15920413866')

driver.find_element_by_xpath('//*[@id="password"]').send_keys('xiu360360')

driver.find_element_by_id('login_btn').click()

driver.find_element_by_link_text('职位搜索').click()

driver.find_element_by_id('keywordInput').send_keys('测试工程师')

driver.find_element_by_id('search_btn').click()


