from lxml import etree
#d语言写的，用来解析xml/html文件的解析器
#用etree对含有html内容的字符串解析，解析为html文档（字符串变成真正一个网页）
text = \
"""
<tr class="hots"
    <td class="1">hot1 </td>
    <td class="2">hot2 </td>
    <td class="3">hot3 </td>
    <td class="4">hot4 </td>
    <td class="5">hot5 </td>
    <td class="6">爬虫 </td>
</tr>
"""
html = etree.HTML(text)
result = etree.tostring(html)
print(result)
#在蔚蓝解析中，传输到本地是为bytes流数据
#在解析的过程中需要请对应的”翻译“编码的设置
result1 = etree.tostring(html,encoding="utf-8").decode('utf-8')
print(result1)


####################################################################################

#解析当前网页d
#对html文件解析
html = etree.parse(r"C:\Users\29433\Desktop\实例文件\test.html")
result = etree.tostring(html,encoding="utf-8").decode("utf-8")
# print(result)

#问题：能不能通过保持网页到本地，放到python====不行
#理由PPT P6
# xpath 提取数据之前，必须将含有html内容的字符串变成HTML页面

#xpath语法的提取
#1.获取所有的div标签
#html（页面） html.xpatn(接受xpath语法) xpath是字符串
divs = html.xpath("//div")
#html页面没有办法直接在python直接print 需要解析才能够看到结果，否则只回返回一个含有标签元素存在本地的信息
#所有xpath语法获取的标签全部被保持到【列表】中【标签1.标签2，标签3.。。】，质押对标签处理都要用for循环，要么从列表取出
print(divs)
for div in divs:
    d = etree.tostring(div,encoding="utf-8").decode("utf-8")
    print(d)

#2。获取指定的某个div标签
div1 = html.xpath("//div[1]")[0]
print(etree.tostring(div1,encoding="utf-8").decode("utf-8"))

#3. 获取所有id=‘even’的div标签
diveven = html.xpath("//div[@id='even']")
for div in diveven:
    d = etree.tostring(div,encoding="utf-8").decode("utf-8")
    print(d)
    print("#" * 50)




text = \
"""
<ul class="ullist" padding="1" spacing="1">
    <li>
        <div id="top">
            <span class="position" width="350">职位名称</span>
            <span>职位类别</span>
            <span>人数</span>
            <span>地点</span>
            <span>发布时间</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218">python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=29938&amp;keywords=python&amp;tid=87&amp;lid=2218">python后端</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31236&amp;keywords=python&amp;tid=87&amp;lid=2218">高级Python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31235&amp;keywords=python&amp;tid=87&amp;lid=2218">python架构师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34531&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34532&amp;keywords=python&amp;tid=87&amp;lid=2218">高级图像算法研发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31648&amp;keywords=python&amp;tid=87&amp;lid=2218">高级AI开发工程师</a>
            </span>
            <span>技术类</span>
            <span>4</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32218&amp;keywords=python&amp;tid=87&amp;lid=2218">后台开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32217&amp;keywords=python&amp;tid=87&amp;lid=2218">Python开发（自动化运维方向）</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34511&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据挖掘讲师 </a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
    </li>
</ul>
"""
html = etree.HTML(text)
#5. 获取div里面的所有的职位信息
# divs = html.xpath("//div")
# 获取所有的职位
zhiwei =html.xpath("//div/span/a/text()")
print(zhiwei)
# leibie = html.xpath("//div/span[2]/text()")
# print(leibie)
works =[]
divs = html.xpath("//div")[1::]
for div in divs:
    #为什么可以共用一组xpath语法。html页面在标记时是按规律
    work={}
    zhiwei = div.xpath(".//a/text()")[0]
    lianjie = div.xpath(".//a/@href")[0]
    place = div.xpath(".//span[4]/text()")[0]
    time = div.xpath(".//span[5]/text()")[0]
    number = div.xpath(".//span[3]/text()")[0]
    leibie = div.xpath(".//span[2]/text()")[0]
    work={
        "职位":zhiwei,
        "链接":lianjie,
        "地址":place,
        "时间":time,
        "数量":number,
        "类别":leibie
    }
    works.append(work)
print(works)
#强调：xpath获得的内容不管是标签的永远是（不加text（），看你打印不能直接编辑）
