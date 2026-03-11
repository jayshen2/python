from wsgiref import headers

import requests

url ="https://www.baidu.com/s"
parmas = {"wd":"番茄"}
#向服务器发送get请求，发送网址到电信DNS查询ip，ip返回后网网站服务器发送请求
#网页的服务器返回html内容的文本（text），不是html文件
proxies = {"http":"http:163.125.17.105:8888"} #设置代理
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}
r = requests.get(url,headers=headers,proxies=proxies)
#请求头参数：访问时避免被服务器判定为机器访问或恶意访问，禁止访问
# 避免禁止访问
#如果返回时因网速或其他原因访问较慢，服务器会停止服务，可以设置timeout时间
r = requests.get(url,headers=headers,proxies=proxies,timeout=10) #r已经
content = r.content.decode('utf-8')
#print(r.text) #r.text自动判断网页的编码格式，会导致部 分网页获取html时变成乱码
print(content)
print(r.status_code)

#豆瓣案例
