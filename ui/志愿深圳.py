# -*-coding:UTF-8 -*-

from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('http://www.sva.org.cn/Default.aspx')
driver.maximize_window()


for i in range(100):
    
    driver.find_element_by_name('Account').send_keys('0099135418')
    driver.find_element_by_id('Kpwd').send_keys('szyg12355')
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="FORM_SignIn"]/div[3]/div/button')).click(), message="对不起，找不到")
    driver.find_element_by_xpath('//*[@id="FORM_SignIn"]/div[3]/div/button').click()
    sleep(1)
    
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[20]/a').click()


#     driver.find_element_by_class_name('btn btn-primary btn-flat').click()
#     driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[20]/a/span').click()