# -*-coding:UTF-8 -*-
from time import sleep

from pymysql import connect
from selenium import webdriver


driver=webdriver.Chrome('..\drivers\chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
 
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')
driver.find_element_by_name('keyword').send_keys('车')
sleep(1)
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()
# driver.find_elements_by_xpath("//input[@value=' 搜索 ']").click()

sleep(1)
text_che=driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text

text_total=driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[10]/span').text


conn=connect(host='192.168.1.4',user='root',password="root",database='ecshop',port=3306)
cursor=conn.cursor()
result=cursor.execute("select goods_name from ecs_goods where goods_name like'%车%'")
rs = cursor.fetchall()
print(rs)

if text_che==rs[0][0] :
    print('测试通过')
else:
    print("测试不通过")
cursor.close()
conn.close()


# driver=webdriver.Chrome('..\drivers\chromedriver.exe')
# driver.get('https://kehu51.com/')
# driver.maximize_window()
#  
# driver.find_element_by_name('username').send_keys('13392898871')
# driver.find_element_by_name('password').send_keys('song789')
# driver.find_element_by_class_name('btn').click()