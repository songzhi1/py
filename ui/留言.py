# -*-coding:UTF-8 -*-
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('http://www.shuomingkj.com/559')
driver.maximize_window()

for i in range(100000):
    driver.find_element_by_name('parameter5141').send_keys('宿迁硕铭广告科技有限公司是一家集设计、生产、研发为一体的城市公共设施生产型企业。公司专业设计和生产公交候车亭、垃圾箱、阅报栏、指路牌、交通标牌、宣传栏、ATM防护罩、报刊亭等市政设施系列产品和工程配套设施系列产品。')
    driver.find_element_by_class_name('btn_inner').click()
    
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, '确定')), message="对不起，找不到")
    # driver.switch_to.alert.accept()
    driver.find_element_by_link_text('确定').click()