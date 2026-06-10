import requests
import re
import csv
import pandas as pd

url = 'https://s.weibo.com/top/summary?cate=realtimehot'

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    'cookie':'SUB=_2AkMetD7pf8NxqwFRm_sdyG_hb4tyzA3EieKo6M8yJRMxHRl-yT9yqm0ntRB6NTQQBqEwRdCXfwouAqxb6dapStVZgHiV; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5ma0G_C-AkJ0gK7DD7VnKp; _s_tentry=passport.weibo.com; Apache=2456177369834.2715.1776857562765; SINAGLOBAL=2456177369834.2715.1776857562765; ULV=1776857562766:1:1:1:2456177369834.2715.1776857562765:'
}

respones = requests.get(url, headers = headers)
content = respones.content.decode('utf8')

events = re.findall('<td class="td-02".*?<a.*?>(.*?)</a>',content, re.DOTALL)[1:]
hots = re.findall('<td class="td-02".*?<span>(.*?)</span>',content, re.DOTALL)

sina_hot = []
for event,hot in zip(events,hots):
    sina = {
        "事件":event,
        "热度值":hot
    }
    sina_hot.append(sina)
print(sina_hot)

head = ['事件','热度值']
with open('sina.csv','w',newline = '\n',encoding = 'utf-8') as f:
    writer = csv.DictWriter(f,head,delimiter=';')
    # 先写表头
    writer.writeheader()
    writer.writerows(sina_hot)
