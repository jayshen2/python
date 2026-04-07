import re

print("="*30 + "第1题" + "="*30)
s1 = "I love Python, python is easy!"
print(re.findall('python',s1,re.IGNORECASE))

print("="*30 + "第2题" + "="*30)
s2 = "apple banana cherry date egg"
print(re.findall(r"\b[ac]\w+\b",s2))

print("="*30 + "第3题" + "="*30)
s3 = "我的电话是13800138000，学号是2024001，房间号302"
print(re.findall("\d+",s3))

print("="*30 + "第4题" + "="*30)
s4 = "a1b2c3d4!@#"
print(re.sub("(\d)",'',s4))

print("="*30 + "第5题" + "="*30)
s5 = "AbC123xyzXYZ"
print(re.findall("[a-z]",s5))

print("="*30 + "第6题" + "="*30)
s6_text = []
s6 = ["user_123","user-name","123user"]
for text in s6:
    # 正则规则：^开头 [A-Za-z_] 字母/下划线开头 \w* 后续任意字母/数字/下划线 $结尾
    t = re.match("^[A-Za-z_]\w*$", text)
    if t is not None:  # 推荐用 is not None 替代 != None
        s6_text.append(t.group())
print(s6_text)


print("="*30 + "第7题" + "="*30)
s7 = "hello@world#123"
result7 = re.findall("[^@#]",s7) # ^在括号外表示字符串开头，在中括号内表示排除
print(''.join(result7))

print("="*30 + "第8题" + "="*30)
s8 = "123 4567 89 12345"
print(re.findall(r"\b\d{3}\b", s8))

print("="*30 + "第9题" + "="*30)
s9 = "a ab abc abcd abcde"
print(re.findall(r"\w{3,}",s9))

print("="*30 + "第10题" + "="*30)  # 【考】选择题
s10 = "<div>test1</div><div>test</div>"
print(re.findall("<div>?(.*)</div>",s10))  #就算中途遇到了你指定的结尾，它也假装没看见，继续往后吃，一直吃到最后一个结尾才停！
print(re.findall("<div>?(.*?)</div>",s10))

print("="*30 + "第11题" + "="*30)
s11 = "姓名：张三，年龄：20，性别：男"
s11_1 = re.search(r"姓名：(.*?)，年龄：(.*?)，性别：(.*)",s11)
print(s11_1.group(1))
print(s11_1.group(2))
print(s11_1.group(3))

print("="*30 + "第12题" + "="*30)
s12 = ["ababab","abcabc","ababx"]
print(re.findall(r"(\w+)\1",s12[0]))
print(re.findall(r"(\w+)\1",s12[1]))
print(re.findall(r"(\w+)\1",s12[2]))
# 重复一次（）\1 重复多次（）\1{n}

print("="*30 + "第13题" + "="*30)
s13 = ["http://www.baidu.com","https://www.taobao.com"]
print(re.findall("[httpshttp]://(.*)",s13[0]))
print(re.findall("[httpshttp]://(.*)",s13[1]))

print("="*30 + "第14题" + "="*30)
s14 = "the there these"
print(re.findall(r"\bthe\b",s14))

print("="*30 + "第15题" + "="*30)
s15 = "Python"
print(re.match(r"^Python!&",s15))

print("="*30 + "第16题" + "="*30)
s16 = "iphone15 iphone14 ipad pro"
print(re.findall(r"iphone(?=\d)",s16))

print("="*30 + "第17题" + "="*30)
s17 = "apple app apply"
print(re.findall("app(?!ly)\w*",s17))

print("="*30 + "第18题" + "="*30)
s18 = "15559039460"
print(re.findall(r"^1[345789]\d{9}",s18))

print("="*30 + "第19题" + "="*30)
s19 = "gys200429@gmail.com"
print(re.findall(r'\w+@\w+[.]\w+',s19))

print("="*30 + "第20题" + "="*30)
s20 = "<p>正则表达式<span></span>"
print(re.sub("<.*?>","",s20))

print("="*30 + "第21题" + "="*30)
s21 = "真逊666真逊"
print(re.sub("(真逊)",'',s21))

print("="*30 + "第22题" + "="*30)
s22 = "a,b;c.d e"
print(re.split("[,;. ]",s22))

print("="*30 + "第23题" + "="*30)
s23 = "192.168.1.1"
print(re.findall(r"1\d{2}|\d{1,2}|2[0-4]\d{1},25[0-5]",s23))

print("="*30 + "第24题" + "="*30)
s24 = "今天是2026/04/26,昨天是2026/04/25"
print(re.findall(r"\d{4}[/-]\d{2}[/-]\d{2}",s24))

print("="*30 + "第25题" + "="*30)
num = {}
s25 = "Pythonis good Pythonis easy"
cc = (re.split(r" ",s25))
for i in cc:
    num[i] = num.get(i,0)+1

print(num)