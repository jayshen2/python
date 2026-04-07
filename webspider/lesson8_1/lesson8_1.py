import re
string8 = ("{ymd:'2018-01-01',tianqi:'晴',aqiInfo:'轻度污染'},"
           "{ymd:'2018-01-02',tianqi:'阴~小雨',aqiInfo:'优'},"
           "{ymd:'2018-01-03',tianqi:'小雨~中雨',aqiInfo:'优'},"
           "{ymd:'2018-01-04',tianqi:'中雨~小雨',aqiInfo:'优'}")

text = \
"""
<tr class="hots">
	<td class="1">hot1</td>
	<td class="2">hot2</td>
	<td class="3">hot3</td>
	<td class="4">hot4</td>
	<td class="5">hot5</td>
	<td class="6">爬虫</td>
</tr>
"""

# 贪婪模式：正则表达式会尽可能地多匹配字符串

# 非贪婪模式：正则表达式会尽可能少的匹配字符串，正则表达式后加一个？（？表示最多匹配一次）
result = re.match('\n<tr [\d\D]+?>',text)
print(result.group())

# 想要获取tr标签中所有的属性值
result0  = re.findall("<td .*?>(.*?)</td>",text)
print(result0)
# 万能公式（.*?） 提取的内容用万能公式
# ()正则表达式内的字符串全部提取出来
# . 任意字符 * 匹配0次或多次 ？非贪婪模式
result1 = re.search("tianqi:(.*?)",string8)
result2 = re.findall("tianqi:'(.*?)'",string8)
result3 = re.findall("aqiInfo:'(.*?)'",string8)
print(result1.group())
print(result2)
print(result3)
# 提取日期年份
result4 = re.findall("ymd:'(.*?)-",string8)
print(result4)
# 提取日期月份
result5 = re.findall("ymd:'\d+-(.*?)-",string8)
print(result5)
# 提取日期中的日期
result6 = re.findall("ymd:'\d+-\d+-(.*?)'",string8)
print(result6)