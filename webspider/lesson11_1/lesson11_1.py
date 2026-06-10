import selenium
import requests
from lxml import etree

"""
网页分为两种:静态网页，动态网页
静态网页:requests直接获取得到了HTML页面(直接给)
动态网页:requests访问页面，通过JavaScript去访问后台数据(类似访问-保安-数据)requests无法直接对动态网页提取数据
Selenium:自动化测试工具，可以用来模拟打开网页、等待加载点击按钮、滚动页面
Selenium:核心组件1、WebDriver(浏览器驱动)
2、Selenium核心库(具体访问网页的指令:打开网页，提取数据)
Selenium:可以帮助我们完成:
1、模拟打开浏览器自动打开一个Chrome
2、等待网页的加载
提取页面的元素，可以直接进行数据提取(xpath,正则)
"""

# 1、列表：存有批量的我也
url = 'https://careers.tencent.com/search.html?index=1'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    "cookie": "SUB=_2AkMen0JQf8NxqwFRm_oUxG7jbIVzzA7EieKow7OLJRMxHRl-yT8XqkgrtRB6NR9sv7u-cW230wC5jilmHnw4gTE5fBUc; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWWzvNvRCGYp2qSrCn52EHI; _s_tentry=passport.weibo.com; Apache=3852192788071.1616.1774439782915; SINAGLOBAL=3852192788071.1616.1774439782915; ULV=1774439782915:1:1:1:3852192788071.1616.1774439782915:",

    }

# 2、爬取手机：职位，地点，类别，工作经验，时间
# 2.1
detail_urls = []
for i in range(1,6):
    url = f'https://careers.tencent.com/search.html?index={i}'
    detail_urls.append(url)
print(detail_urls)

#2.2
for page in detail_urls:
    response = requests.get(page,headers=headers)
    content = response.content.decode('utf-8')
    html = etree.HTML(content)
    # 职位
    jobs = html.xpath('//span[@class="job-recruit-title"]/text()')
    # 地点
    locations = html.xpath('//span[@class="icon-location"]/text()')
    # 类别
    categorys = html.xpath('//p[@class="recruit-tips"]/span[3]/text()')
    # 工作经验
    tips = html.xpath('//p[@class="recruit-tips"]/span[5]/text()')
    # 时间
    times = html.xpath('//p[@class="recruit-tips"]/span[7]/text()')
    print(jobs,locations,categorys,tips,times)