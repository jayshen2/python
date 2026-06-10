from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from lxml import etree

# 1.打开浏览器
driver = webdriver.Edge()

# 2.获取本地页面，打开
#  标记文件所在的位置 "file://"表示本地的html页面
#   os.path.abspath
location_url = "file://" + os.path.abspath('login.html')
driver.get(location_url)

# 输入密码点击登录
driver.find_element(By.ID,"username").send_keys('username')
driver.find_element(By.ID,"password").send_keys('123')
driver.find_element(By.ID,"loginBtn").click()

time.sleep(100)

driver.quit()

# 考点
"""
给一个网页的标签和属性值，做模拟登录
根据网页的标签或属性值，填写查找位置

"""