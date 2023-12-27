import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

print(type(response))
#

# content = response.read().decode("utf-8")
# 按照一个总结一个字节读
# print(content)

content = response.read(5)
# 返回5个字节
# print(content)

content = response.readline()
# 读取一行
# print(content)

content = response.readlines()
# 一行一行读取
# print(content)

print(response.getcode())
# 获取状态码200表示正确

print(response.geturl())
# 获取url地址
print(response.getheaders())
# 获取一些状态信息