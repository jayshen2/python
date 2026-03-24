# Xpath爬虫实战内容总结 + 可运行代码整合
# 本次实战基于requests请求库和lxml的etree解析库，通过Xpath语法完成百度导航标签爬取、新浪热搜爬取、豆瓣电影影评爬取（基础 + 进阶） 三个核心爬虫任务，核心流程均为：导入库→定义请求头和URL→获取并解码页面→etree解析→Xpath
# 提取数据→数据存储，同时进阶任务涉及多页构造、嵌套遍历、异常处理等爬虫进阶技巧。
# 一、核心任务梳理
# 1.百度页面：抓取百度首页id = "u1"下的导航标签文本（如新闻、地图）及对应跳转链接，并用zip整合存储；
# 2.新浪热搜：爬取新浪实时热搜榜的热搜关键词和对应热度值，提供单节点遍历和批量提取 + zip整合两种实现方法；
# 3.豆瓣电影 - 基础：爬取单篇电影影评页面的电影名、评论者、评分、完整影评，解决数据清洗（异常字符、列表拼接）问题；
# 4.豆瓣电影 - 进阶：爬取豆瓣最受欢迎影评的5页共100条影评数据，实现分页URL构造、详情页链接提取、嵌套遍历爬取，并通过try - except处理页面格式不一致导致的报错。
# 二、环境准备
# 先安装所需依赖库，命令行执行：
# 运行pip install requests lxml
# 三、可运行代码整合（分任务实现，已修复失效问题、补全请求头、优化Xpath）任务
# 1：爬取百度首页导航标签及链接

import requests
from lxml import etree
import pandas

# 1. 定义请求头和URL（补全完整User-Agent，避免反爬）
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "cookie":"BAIDUID_BFESS=FD73FC94633E2B55E306E13E97C40089:FG=1; channel=baidusearch; COOKIE_SESSION=5892_0_2_2_4_2_1_0_1_1_0_0_5903_0_137_0_1750661635_0_1750661772%7C3%230_0_1750661772%7C1; PSTM=1774435106; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=0105ag20210g00850520008l8k20ak1ks7ep227; BIDUPSID=FD73FC94633E2B55615DC65DCE697CCC; ZFY=uqCb04bD8GabRPghZ:A8Bt:APW7QOpJJejrAq35AmWw5g:C; H_PS_PSSID=63141_65592_67721_67862_67885_67887_67942_67964_68047_67986_68004_68131_68143_68149_68146_68153_68139_68188_68218_68265_68285_68288_68296_68310_68350_68334_68369_68436_68450_68446_68464_68511_68527_68543; H_PS_645EC=1006k1E42e5BtcbKEjm4wm0mXITTgkMe8ip2%2BmOUxE3IHvE8Yp5%2BJr5c0O0; baikeVisitId=03dd88a5-95e2-45d5-9d05-fe01f1a02bcc; BD_HOME=1"

}
url = "https://www.baidu.com"

# 2. 获取页面并解码（处理编码问题，使用apparent_encoding自动识别）
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding  # 修复原代码硬编码utf8的问题
content = response.text

# 3. etree解析
html = etree.HTML(content)

# 4. Xpath提取数据（文本+链接）
contents_list = html.xpath('//div[@id="s-top-left"]/a/text()')  # 导航标签文本
contents = [i.strip() for i in contents_list]

urls = html.xpath('//div[@id="s-top-left"]/a/@href')

#5. 存储数据*（数据的配对）
baidu = []
for cont,Url in zip(contents,urls):
    baidu.append({"文本":cont,
                  "链接":Url,
                  })

pd_baidu = pandas.DataFrame(baidu)
print(pd_baidu)