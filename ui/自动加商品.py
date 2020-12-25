# -*-coding:UTF-8 -*-


from pymysql import connect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
 
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('添加新商品').click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, '商品列表')))

driver.switch_to.default_content()
driver.switch_to.frame('main-frame')

driver.find_element_by_name('goods_name').send_keys('大哥大')



Select(driver.find_element_by_name('cat_id')).select_by_visible_text('    小型手机')


driver.find_element_by_xpath('//*[@id="tabbody-div"]/form/div/input[2]').click()

conn = connect('192.168.1.4', 'root', 'root', 'ecshop', 3306)
cursor = conn.cursor()
cursor.execute("select goods_name from ecs_goods where goods_name ='大哥大'")

rs = cursor.fetchall()
print(rs)

if '大哥大' == rs[0][0]  :
    print('测试通过')
else:
    print("测试不通过")
cursor.close()
conn.close()