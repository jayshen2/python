import re
# xpath 利用HTML网页结构使用语法提取数据（网页由标签构成，标签有层级关系）
# 正则表达式 用特定符号表示相应的数据 用符号的组合表示特定的网页数据

# 1 大额字符
# 1.1 匹配某个字符串
# match() search() 正则表达式中常见的搜索字符函数
# 显示的结果 要想显示完整的匹配结果 group（）
text  = "python"
result = re.match("py", text)  # match语法从起始位置匹配
print(result) # 返回匹配对象，没有匹配到会返回None
print(result.group())  # 返回匹配的结果，没有匹配到会报错

# 1.2 点（.）的匹配
# match 从头开始匹配。 . 表示单个字符（任何字符），不包含换行符（\n）
t1 = "\\t1ongcx"
r1 = re.match(".",t1)
print(r1)
print(r1.group())

# 1.3 匹配数字 \d 表示数字
t2 = "1ongcx"
r2 = re.match("\d",t2)
print(r2.group())

# 1.4 \D 匹配刺激了数字以外的所有内容
t3 = ".ongcx"
r3 = re.match("\D",t3)
print(r3.group())
# 【考】等价效果 \d\D ===== .  除了换行

# 1.5 \s 匹配空白字符  \n,\t,\r,空格都是空白字符
t4 = " ongcx"
r4 = re.match("\s",t4)
print(r4.group())

# 1.6 \w 匹配a-z，A-Z，数字0-9和下划线_
t5 = "_ongcx"
r5 = re.match("\w",t5)
print(r5.group())

# 1.7 \W 除了\w都可以匹配
t6 = "--ngcx"
r6 = re.match("\W",t6)
print(r6.group())
# \d\D ==== \w\W  完全等价

# 1.8 [] 中括号内的内容均可匹配
t7 = "oongcx"
r7 = re.match("[hon]",t7)
print(r7.group())
# [] 内的内容都可以匹配，[]内存在多个元素，多个元素是以或的方式并存。[]内的字符都可以匹配

# 2 多字符匹配
# 星号（*）匹配零个或多个字符
text = '0592-7797110'
re1 = re.match('[-\d]*',text)
print(re1.group())
# [\d] 找一个数字
# [\d]* [\d]匹配零次或多次 ：支持匹配不到，多次的意思表示后续满足正则表达式就继续匹配，直到不匹配为止


# 3 加号(+)匹配一个或多个
text = '0592-7797110'
r7 = re.match('[\d]+',text)
print(r7.group())

# 4 问号(?)匹配零个或一个
text8 = 'q0592-7797110'
r8 = re.match('[\d]?',text)
print(r8.group())
# 位置我也中存在多少个某标签， + * ？ 去做匹配 规避xpath网页没有该语法对应的数据匹配报错

# 已知字符串的匹配次数{} {m}表示匹配m次
text = '15559039460'
r9 = re.match('[\d]{5}',text) # 匹配5次
print(r9.group())
r10 = re.match('[\d]{2,5}',text) # 2到5个
r11 = re.match('[\d]{2,}',text) # 至少2个
r12 = re.match('[\d]{,5}',text) # 最多5个
print("r10:",r10.group())
print("r11:",r11.group())
print("r12:",r12.group())

# 身份证的正则表达式 身份证18位 \d{17}[xX\d]{1}
# 等价方法【考】 对应的正则表达式替换方案
# \w === 小写字母 大写字母 数字 下划线  ==  [A-Za-z0-9_]

# 在[^]中括号内取反 [^0-9] == [\D]
text = '11155-5903-9460'
r13 = re.search('[^\d]+',text)
print(r13.group())
# 在[]外^表示已^后面的内容开始匹配一次到多次
text = '350521200404299031'
r13 = re.match('^3505212[\d]+[xX\d]',text)
print(r13.group())

# 特殊匹配
#[.] 表示真的.  .表示除了\n以外的任意字符
#[+] [?] [*] [|] [$]  带有特殊含义的必须加[]


text = '155-5903-9460'
r14 = re.search('[\d]+',text)  # 从左往有搜索数字一次或多次，不满足则停止
print(r14.group())

# 以$结尾
text = 'gys200429@gmail.com'
r16 = re.search('\w+@gmail[.]com$',text)
print(r16.group())

# 中括号认为内部 都是单个字符
text = 'https://chengyi.jmu.com'
r17 = re.search('[http|https|ftp]',text) #===[httphttpsftp]
print(r17.group())

# 小括号内部认为是不同字符串
text = 'https://chengyi.jmu.com'
r17 = re.search('(https|http|ftp)',text)
print(r17.group())

"""
\d 数字
\D 除了数字
\w a-zA-Z0-9_
\W [^a-zA-Z0-9_]
\s 空白符号
[] 中括号内的内容取或
* 零次或多次
？ 零次或一次
+ 一次或多次
{m} 匹配m次
{m.n} 匹配m到n次，注意缺失一个情况
[.*+？^$|] 七个特殊符号
[^] 中括号取反
^ 中括号外(包含没有中括号的)表示以xxx开始
$ 以。。。结尾
| 多个字符串和多个表达式同时匹配
  结合[]表示每个字符
  结合()表示不同字符串
match 从头开始匹配 不满足条件停止
search 
"""

# text = "python123.com.cn"
# print(re.search("com$",text))

text = "a_9python"
print(re.match("[a-z_][\w]{2,4}", text).group())

