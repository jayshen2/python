import requests
from lxml import etree

URL = "https://s.weibo.com/top/summary"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
           "cookie":"SUB=_2AkMen0JQf8NxqwFRm_oUxG7jbIVzzA7EieKow7OLJRMxHRl-yT8XqkgrtRB6NR9sv7u-cW230wC5jilmHnw4gTE5fBUc; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWWzvNvRCGYp2qSrCn52EHI; _s_tentry=passport.weibo.com; Apache=3852192788071.1616.1774439782915; SINAGLOBAL=3852192788071.1616.1774439782915; ULV=1774439782915:1:1:1:3852192788071.1616.1774439782915:",
           "referer":"https://passport.weibo.com/"
           }
response = requests.get(url=URL,headers=headers)
content = response.content.decode("utf-8")

html = etree.HTML(content)

# 获取排名
ids = html.xpath("//tr[@class]/td[1]/text()")
# 获取词条
title = html.xpath("//td[@class='td-02']/a/text()")
# 获取链接(不完整，后续要补齐)
urls = html.xpath("//td[@class='td-02']/a/@href")
# 获取热搜值
hots = html.xpath("//td[@class='td-02']/span/text()")
print(ids,title,urls,hots)
print(len(ids),len(title),len(urls),len(hots))