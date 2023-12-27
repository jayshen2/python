# 获取https://https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
import urllib.request
import urllib.parse
url = "https://www.baidu.com/s?wd="
# 请求对象的定制为了解决反爬的一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}
# 请求对象定制
name = urllib.parse.quote('周杰伦')
url = url + name
# 将周杰伦变成Unicode编码格式，需要利用urllib.parse
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)