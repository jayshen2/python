from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

# 自动化设置
# 下面几行代码是对浏览器访问页码进行初始化
# 浏览器(无头：没有请求头)
edge_options = Options()
edge_options.add_argument("--headless=new")
edge_options.add_argument("--no-sandbox")
edge_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Edge(options=edge_options)

# 由于动态网页，大量的网页内容由js控制，只要访问过程中触发了JS进程，自动化的扩展了访问的程序
# 直接访问会提示“正在受自动化软件控制”，只要关闭相应的自动化控制，关闭js的进程就可以避免被检测到是机器人
# 如果要避免机器人检测，绕过js控制

# 1 关闭浏览器的“正在受自动化软件控制”提示条
edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 2 禁用于一切自动化扩展程序(隐藏爬虫特征)
edge_options.add_experimental_option('useAutomationExtension', False)

driver.get("https://www.baidu.com")
driver.save_screenshot('baidu.png')
time.sleep(1)

driver.execute_script('document.getElementById("kw").value = "蔡徐坤";')
time.sleep(2)
driver.save_screenshot('baidu_input.png')

driver.execute_script('document.getElementById("su").click();')
time.sleep(1)

driver.save_screenshot('1.png')
print("截图完毕")

# 关闭浏览器
time.sleep(2)
driver.quit()

