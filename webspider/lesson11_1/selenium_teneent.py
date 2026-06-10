from selenium import webdriver
from lxml import etree
import time

# 初始化浏览器，打开Chrome（）启动一个机器人打开网页
driver = webdriver.Edge()  # 错误1：调用浏览器大小写和括号。 错误2：相应浏览器未安装在本地，或selenium的浏览器驱动和本地浏览器驱动不一致
for i in range(1,6):
    url = f'https://careers.tencent.com/search.html?index={i}'
    # requests.get()访问静态网页  webdriver.get()访问动态网页
    driver.get(url)
    time.sleep(2)

    # 获取完整网页源代码
    html = etree.HTML() #原网页
    # 职位
    jobs = html.xpath('//span[@class="job-recruit-title"]/text()')
    # 地点
    locations = html.xpath('//span[@class="job-recruit-location"]/text()')
    # 类别
    categorys = html.xpath('//p[@class="recruit-tips"]/span[3]/text()')
    # 工作经验
    tips = html.xpath('//p[@class="recruit-tips"]/span[5]/text()')
    # 时间
    times = html.xpath('//p[@class="recruit-tips"]/span[7]/text()')

    print("职位:",jobs)
    print("地点:",locations)
    print("类别:",categorys)
    print("工作经验:",tips)
    print("时间:",times)

driver.quit()