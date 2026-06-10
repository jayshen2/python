import re
from http.client import responses

import requests

# url = f"https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E8%94%A1%E5%BE%90%E5%9D%A4&pn={i}

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'cookie':"BAIDUID=8979335DAFE66258AD3A3F2109ECBA39:FG=1; BDUSS=09hWX5VRnJsTC1McVhGVDhKRXoyM21JNWxCMDd-VTJCZy1PUDNtV0p3cWVoQWhwSVFBQUFBJCQAAAAAAAAAAAEAAAAsVZ32y~vWu86qy~3X7QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ734Gie9-Boa; BDUSS_BFESS=09hWX5VRnJsTC1McVhGVDhKRXoyM21JNWxCMDd-VTJCZy1PUDNtV0p3cWVoQWhwSVFBQUFBJCQAAAAAAAAAAAEAAAAsVZ32y~vWu86qy~3X7QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ734Gie9-Boa; BIDUPSID=8979335DAFE66258AD3A3F2109ECBA39; PSTM=1759681602; BAIDU_WISE_UID=wapp_1762580589248_65; BAIDUID_BFESS=8979335DAFE66258AD3A3F2109ECBA39:FG=1; ZFY=jeOrr4OMTc5IkZHuN:A2244yVHY6OOI2:ACDplAnvKqjg:C; MCITY=-%3A; __bid_n=19d432bd0d784323c8970f; H_PS_PSSID=63147_67861_68166_68265_68297_68380_68421_68447_68438_68543_68516_68624_68611_68666_68739_68896_68925_69001_69011_69019_69013_69024_69056_68553_69070_69037_69095_69089_69112_69127_69163_69183_69211_69242_69228_69239_69232_69234_69249; H_WISE_SIDS=68166_68421_68447_69001_69013_69070_69037_69163_69183_69242_69228_69239_69232_69234_69294_68779_69318_69251_69253_69255_69256_69258_68970_69085_69369_69417_69413_69422_69444_69435_69452_69488_69508_69559_69553_69591_69584_69642_69668_69665_69658; ab_sr=1.0.1_OTZhNmVkMTRlYzI1MGY4ZjgzZWY3YmIyYjgzNmQ5MDZkMDM5ZDVlYzE5NzhhMmViNTYyNDY2M2I0YjY0M2MzMDJmYjdhODY5MDM1NTU2YzIwMGMzZWQyNzY0NDdjMGMyMWEzNjRlZWZlNDE4YTdjN2UzYzU4NzkwNTc4Nzk3NmU4OGU1YzA3ODAzOTgzODNhMzA0ZTY4YTUyMzMxMjE4Yw==",
}
# 设置爬取的关键字
wd = "蔡徐坤"
# 用代码来设置网页关键词，设置批量爬取的页面数
# 【考】 要求批量爬取8页，爬取的图片设置为电脑，接下去for循环如何写，使得detail_urls内存储得到8页的url
detail_urls = []
for i in range(0,5):
    # 设置一个字典，等会代码中将字典设置的键值对传送给url，python自动补全正确的网页链接
    kw = {
        "word" : wd,
        "pn" : i*20,
    }
    # 只需要word前的部分链接
    url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8"
    # 通过设置params参数让url自动补全正确的链接
    response = requests.get(url, headers=headers, params=kw)
    content = response.content.decode("utf8")
    # 百度图片的链接并不在网页的检查html页面中，而是通过get，decode获得的是网页的源代码
    # 下源代码中（ctrl+f），搜索objurl（大量图片存在objurl中）
    detail_url = re.findall(r'"objURL":"(.*?)"', content,re.S)
    # detail_url 满足正则表达式的字符集合到一个列表中
    # detail_urls 列表中嵌套列表，意味着要写双循环，如果不想写则直接写extend
    detail_urls.append(detail_url)
print(detail_urls)
i = 0
for page in detail_urls:
    for url in page:
        try:
            print(f"正在爬取第{i}张图片")
            response = requests.get(url,headers)
            content = response.content  # 图片这种传输过程中是bytes流数据，不需要按照某个编码进行解析
            if url[-3:] == 'jpg':
                with open(f"{i}.jpg", "wb") as f:
                    f.write(content)
            elif url[-3:] == 'png':
                with open(f"{i}.png", "wb") as f:
                    f.write(content)
            elif url[-3:] == 'jpeg':
                with open(f"{i}.jpeg", "wb") as f:
                    f.write(content)
            else :
                print(f"第{i}张图片爬取错误")
                i += 1
                continue
            print(f"第{i}张图片爬取成功")
            i += 1
        except:
            print(f"第{i}张图片爬取失败")
            i += 1
            continue