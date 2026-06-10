from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1初始化网页，打开浏览器
driver = webdriver.Edge()
time.sleep(3)
# 2访问动态网页
driver.get('https://practice.expandtesting.com/login')

# 3模拟输入用户名
driver.find_element(By.ID,"username").send_keys("practice")
# 当前浏览器，找到网页元素元素（By方法,找到Username的位置，该位置是出入账号的地方），发送关键词（账号名）
# 注意：找到网页输入账号的方框位置，不是输入账号文本的位置

# 4模拟输入密码
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")

# 5 点击登录
time.sleep(3)
driver.find_element(By.XPATH,'//button[@id="submit-login"]').click()


time.sleep(15)
alert_elem = driver.find_element(By.XPATH, '//*[@class="alert"]')
alert_text = alert_elem.text
print("提示信息：", alert_text)
# 6 退出网页
time.sleep(100)
driver.quit()