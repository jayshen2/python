from re import findall

import requests
import re
headers = {
    'cookie':'login=flase; Hm_lvt_9811648d1409c4608cf19093200cee83=1777374253; Hm_lpvt_9811648d1409c4608cf19093200cee83=1777374253; HMACCOUNT=90E1B90D297847BE',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
}

# 1. 批量构造URL
urls = []
for i in range(1,11):
    url = f'https://www.guwendao.net/default_{i}.aspx'
    urls.append(url)
print(urls)

# 2。 遍历所有的网页
gushi = []
for page_num,url in enumerate(urls,1):
     try:

        response = requests.get(url,headers=headers)
        content = response.content.decode('utf-8')

        # 3. 正则表达式提取标题
        titles = re.findall(r'<p>.*?<a.*?<b>(.*?)</b>',content,re.DOTALL)
        # 作者
        zuozhes = re.findall(r'<p class="source">.*?<a.*?>.*?<img src=.*? alt=.*?>(.*?)</a>',content,re.DOTALL)
        # 头像
        imgs = re.findall(r'<p class="source">.*?<a.*?<img src="(.*?)" alt=.*?>',content,re.DOTALL)
        # 朝代
        dynasties = re.findall(r'p class="source">.*?<a.*?<a.*?>(.*?)</a>',content,re.DOTALL)
        # 诗词内容
        poems = re.findall(r'<div class="contson" id=.*?>(.*?)</div>',content,re.DOTALL)

        # 4.清洗古诗词内多余内容
        new_poems = []
        for poem in poems:
            # 找到标签，用sub替换
            new_poem = re.sub(r"<.*?>","",poem)
            # 去掉多余的空格，将古诗词合并
            new_poem = new_poem.strip()
            new_poem = re.sub(r'\s+','',new_poem)
            new_poems.append(new_poem)

        for title,zhuozhe,igm,dynastie,new_poem in zip(titles,zuozhes,imgs,dynasties,new_poems):
            data = {
                "标题" : title.strip(),
                "头像" : igm.strip(),
                "作者" : zhuozhe.strip(),
                "朝代" : dynastie.strip(),
                "诗词" : new_poem.strip(),
            }
            gushi.append(data)
        print(f"第{page_num}页已经爬取完毕")
     except Exception as e:
        print(f"第{page_num}页爬取失败")

print(gushi)