# import requests
# #请求头参数
# #use-agent:浏览器
# #referer:记录从哪个网站跳转过来
# #cookie:访问的标识
# r = requests.get("https://news.baidu.com/")
# # requests.get 实现了==网页请求的基本原理
# # 前面的工作都完成了，但html页面解析（浏览器）没有完成
# print(r.text)
# print(r.status_code)

# #get 请求
# import requests
# data = {
#     "name":"cc",
#     "age":18
# }
# r = requests.get("https://httpbin.org/get",params=data)
# print(r.text)
# print(r.status_code)

#get请求--图标的下载
#今后获取数据，写代码从html文件获取数据页面必须是html页面，所以gat获取页面之后解析之前====r.content
import requests
r = requests.get("https://scrape.center/favicon.ico")
with open("favicon.ico",'wb') as f:
    f.write(r.content)