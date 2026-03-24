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
titles = html.xpath("//td[@class='td-02']/a/text()")
# 获取链接(不完整，后续要补齐)
hrefs = html.xpath("//td[@class='td-02']/a/@href")
# 获取热搜值
hots = html.xpath("//td[@class='td-02']/span/text()")
hots = ['无热度']+hots
new_hrefs = []
for href in hrefs:
    new = "https://s.weibo.com"+href
    new_hrefs.append(new)

sina_hots = []
for title,hot,href in zip(titles,hots,new_hrefs):
    dict = {"标题":title,
            "热度值":hot,
            "链接":href,}
    sina_hots.append(dict)
print(len(ids),len(titles),len(hrefs),len(hots))
print(sina_hots)
