# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ---------------------- 关键：隐藏自动化特征（绕过验证） ----------------------
chrome_options = Options()
# 1. 关掉“正在受自动化软件控制”提示
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 2. 禁用自动化扩展
chrome_options.add_experimental_option('useAutomationExtension', False)

# 3. （可选）无头模式仍可用，但上面两行必须保留
# chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)

# 4. 关键：JS 删掉 webdriver 标记（百度最认这个）
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """
    }
)
# -----------------------------------------------------------------------------

# 创建的浏览器去访问百度的主页
driver.get('https://www.baidu.com/')
time.sleep(5)
# 找到百度的搜素框输入想要搜素的关键词
driver.execute_script('document.getElementById("kw").value = "蔡徐坤";')
time.sleep(3)
driver.save_screenshot('baidu_input.png')
driver.execute_script('document.getElementById("su").click();')
time.sleep(5)
# 截图
driver.save_screenshot('1.png')
print("截图完毕")

# 关闭浏览器
time.sleep(2)
driver.quit()
