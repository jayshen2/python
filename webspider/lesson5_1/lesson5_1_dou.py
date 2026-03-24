import requests
from lxml import etree

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "cookie":'ll="118201";bid=Z6xyp_iGeo4;_pk_id.100001.4cf6=390897bb62e738b4.1773144567.;_vwo_uuid_v2=DBC2C0D494E3054C0764A92E342BDAE06|069f0bc62662c9ba06ebda84c8616c98; __utma=30149280.1667535315.1773230337.1773823461.1774958198.3; __utmc=30149280; __utmz=30149280.1774958198.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.442987104.1773230338.1773823461.1774958202.3; __utmb=223695111.0.10.1774958202; __utmc=223695111; __utmz=223695111.1774958202.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1774958202%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utmb=30149280.3.10.1774958198',
    "referer":"https://movie.douban.com/review/7389993/"
}

URL = "https://movie.douban.com/review/7389993/"
response = requests.get(url=URL,headers=headers)
content = response.content.decode("utf-8")

html = etree.HTML(content)

titles = html.xpath('//div[@class="article"]/h1/span/text()')[0]
commenters = html.xpath('//header[@class="main-hd"]/a/span/text()')[0]
movies = html.xpath('//header[@class="main-hd"]/a[2]/text()')[0]
ranks = html.xpath('//header[@class="main-hd"]/span/@title')[0]
comments = html.xpath('//div[@class="review-content clearfix"]//p/text()')

def func(ranks):
    if ranks == '力荐':
        return "五星"
    elif ranks == '推荐':
        return "四星"
    elif ranks == '推荐':
        return "三星"
    elif ranks == '较差':
        return '两星'
    else:
        return '很差'

cc = ''
for i in comments:
    new = i.strip()
    cc += ",".join(new.split("\n"))
data ={
    "标题":titles,
    "评论人":commenters,
    "电影":movies,
    "评分":func(ranks),
    "文章":cc
    }
print(data)