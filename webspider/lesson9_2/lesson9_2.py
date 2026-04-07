import requests
import re

from pip._internal.utils import urls

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',

}
url = "https://x0.ifengimg.com/ucms/2024_49/E2547E8D67605C0CA2C06809ABB26B41DB135104_size405_w1440_h1800.jpg"

response = requests.get(url, headers=headers)
content = response.content
# content = response.content.decode('utf-8')
# 正常的数据网页爬取，要将获取的网页进行编码的解析，utf8的格式
# 图片在网络的传输不是utf8，是一个bytes数据 字节数据
# 正确的做法，图片的解析还是保存都要使用btye数据

# 保存数据
# wb w:write b:二级制的字节数据
with open("../test.jpg", 'wb') as f: # 把读取的数据按照二级制bytes流数据写到本地0
    f.write(content)

    