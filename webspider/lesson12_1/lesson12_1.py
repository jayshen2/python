# selenium 定位到相应的位置(find_elements()) 发送账号密码send_key() 点击click
# 当浏览，下载，都之前跳出验证方式（滑块，旋转，短信验证码，选择正确的顺序）

# 通过selenium 在百度的主页完成某个词语的搜素（验证码），截图

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 自动化设置
# 下面几行代码是对浏览器访问页码进行初始化
# 浏览器(无头：没有请求头)
edge_options = Options()
edge_options.add_argument("--headless=new")
edge_options.add_argument("--window-size=2560,1600")
driver = webdriver.Chrome(options=edge_options)

# 创建的浏览器去访问百度的主页
driver.get('https://www.baidu.com/')
time.sleep(5)
# 找到百度的搜素框输入想要搜素的关键词
driver.find_element(By.ID,"kw").send_keys("蔡徐坤")
driver.find_element(By.ID,"su").click()
# 截图
driver.save_screenshot('1.png')
print("截图完毕")

# 关闭浏览器
time.sleep(2)
driver.quit()


# 考试
#  在某些网站爬虫中，服务器会认定当前访问为机器人访问，经常会需要通过相关验证才能继续访问
# 如果利用selenium进一步破解避免跳过验证环节