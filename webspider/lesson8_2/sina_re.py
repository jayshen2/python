import requests
#from lxml import etree
import re

url = "https://s.weibo.com/top/summary"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'cookie':'SUB=_2AkMetDdif8NxqwFRm_sdyG7maYx1zgDEieKo6Ma5JRMxHRl-yT9kqh0ZtRB6NTQZjT-qfMoL4OWhclRr1HhCgUkpImUi; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Wh6Uz7HqUcVDeyLVD2GxcTK; _s_tentry=passport.weibo.com; Apache=8516259520160.447.1776859221837; SINAGLOBAL=8516259520160.447.1776859221837; ULV=1776859221839:1:1:1:8516259520160.447.1776859221837:',
}
response = requests.get(url,headers = headers)
content = response.content.decode("utf-8")
# 为什么不需要通过其他的包或函数解析html
# content已经是含有html内容的字符串 re可以直接对字符串提取内容
# 如果用etree.HTML反而拿字符串变成了HTML网页
#etree = etree.HTML(content)

events = re.findall('<td class="td-02".*?<a.*?>(.*?)</a>',content,re.S)[1::]
hots = re.findall('<td class="td-02".*?<span>(.*?)</span>',content,re.S)

sina_hot = []
for event,hot in zip(events,hots):
    sina = {
        "事件":event,
        "热度值":hot
    }
    sina_hot.append(sina)

print(sina_hot)