import urllib.request

url = 'https://www.baidu.com'
# url的组成 1.协议（http/https），2主机（域名），3端口号（http80/https443） 4.路径 5.参数 6.锚点

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'}

# 请求对象的定制，因为urlopen方法中不能存储字典，所以header传递不进去
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
