import time
import requests
from lxml import etree

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
           "cookie":'ll="118201"; bid=Z6xyp_iGeo4; _pk_id.100001.4cf6=390897bb62e738b4.1773144567.; _vwo_uuid_v2=DBC2C0D494E3054C0764A92E342BDAE06|069f0bc62662c9ba06ebda84c8616c98; __utmz=30149280.1774958198.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1774958202.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; __utma=30149280.1667535315.1773230337.1775563743.1775567584.7; __utmb=30149280.0.10.1775567584; __utma=223695111.442987104.1773230338.1775563743.1775567584.7; __utmb=223695111.0.10.1775567584; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1775567585%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1',
            "referer":"https://movie.douban.com/review/best/",
           }

# 步骤一构造5页分页URL
data_url  = []
URL = "https://movie.douban.com/review/best/?start={}"
for i in range(0,100,20):
    full_URL = URL.format(i)
    data_url.append(full_URL)

#步骤二遍历分页URL提取分页的链接
movie_detail_url = []
for url in data_url:
        response = requests.get(url,headers=headers)
        content = response.content.decode("utf8")
        html = etree.HTML(content)
        urls = html.xpath('//div[@class="main-bd"]/h2/a/@href') #获取对应的页面中每一步
        movie_detail_url.extend(urls)
        time.sleep(1)

#
# enumerate():遍历索引和元素

all_movie_comments = []
for i,url in enumerate(movie_detail_url):
    try:
        comment = ''
        print(url)
        response = requests.get(url,headers=headers)
        content = response.content.decode("utf8")
        html = etree.HTML(content)
        # 获取评论的标题
        title = html.xpath('//div[@class="article"]/h1/span/text()')[0].strip() if html.xpath('//div[@class="article"]/h1/span/text()') else "未知电影"
        # 获取影评的评论者
        commenter = html.xpath('//header[@class="main-hd"]/a/span/text()')[0].strip() if html.xpath('////header[@class="main-hd"]/a/span/text()') else "匿名评论"
        # 获取影评的电影
        movie = html.xpath('//header[@class="main-hd"]/a[2]/text()')[0].strip() if html.xpath('//header[@class="main-hd"]/a[2]/text()') else "未知电影"
        # 获取评分
        rank = html.xpath('//header[@class="main-hd"]/span[2]/text()')[0].strip() if html.xpath('//header[@class="main-hd"]/span[2]/text()') else "未评级"
        # 获取具体的影评数据
        comment_list = html.xpath('//div[@class="review-content clearfix"]//p/text()')
        comment += ''.join(i.replace('\n', '') for i in comment_list )
        all_movie_comments.append({
            "评论标题":title,
            "评论者":commenter,
            "电影":movie,
            "评分":rank,
            "影评":comment,
        })
        # 设置反爬时间间隔
        time.sleep(2)
        print(f"第{i}部电影爬取成功")
    except Exception as e:
        print(f"第{i}部电影爬取失败")
        continue

print(all_movie_comments)