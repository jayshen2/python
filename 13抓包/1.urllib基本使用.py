import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
# 模拟浏览器向服务器发送请求
content = response.read().decode("utf-8")
# read方法返回字节格式的二进制数  二进制--》字符串 解码
# 编码格式设置为utf-8
print(content)
