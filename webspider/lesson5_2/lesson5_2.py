import time
import requests
from lxml import etree

data_url  = []
URL = "https://movie.douban.com/review/best/?start={}"
for i in range(0,100,20):
    full_URL = URL.format(i)
    data_url.append(full_URL)

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
           "cookie":"SUB=_2AkMen0JQf8NxqwFRm_oUxG7jbIVzzA7EieKow7OLJRMxHRl-yT8XqkgrtRB6NR9sv7u-cW230wC5jilmHnw4gTE5fBUc; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWWzvNvRCGYp2qSrCn52EHI; _s_tentry=passport.weibo.com; Apache=3852192788071.1616.1774439782915; SINAGLOBAL=3852192788071.1616.1774439782915; ULV=1774439782915:1:1:1:3852192788071.1616.1774439782915:",
           "referer":"https://movie.douban.com/review/best/?start=80"
           }
movi_detail_url = []
for url in data_url:
    response = requests.get(url=url,headers=headers)
    content = response.content.decode("utf8")
    html = etree.HTML(content)
    urls = html.xpath('//div[@class="main-bd"]/h2/a/@href')
    movi_detail_url.extend(urls)

print(movi_detail_url)