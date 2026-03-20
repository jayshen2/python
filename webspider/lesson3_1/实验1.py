from lxml import etree
text = \
"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>2024级Python班学生成绩表</title>
    <style>
        .title { color: #2c3e50; font-size: 20px; font-weight: bold; }
        .student-item { margin: 10px 0; padding: 5px; }
        .pass { color: #27ae60; }
        .fail { color: #e74c3c; }
        .score-table { border-collapse: collapse; width: 80%; }
        .score-table th, .score-table td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        .score-table th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">2024级Python班学生成绩汇总</h1>
        <p id="class-info">班级：Python爬虫班 | 人数：28人 | 考试时间：2024-12-20</p>
        
        <!-- 学生基本信息列表 -->
        <div class="student-list">
            <div class="student-item" data-student-id="001">
                <h3>张三</h3>
                <p>性别：男 | 年龄：19</p>
                <a href="https://example.com/student/001" class="detail-link">查看详细成绩</a>
            </div>
            <div class="student-item" data-student-id="002">
                <h3>李四</h3>
                <p>性别：女 | 年龄：18</p>
                <a href="https://example.com/student/002" class="detail-link">查看详细成绩</a>
            </div>
            <div class="student-item" data-student-id="003">
                <h3>王五</h3>
                <p>性别：男 | 年龄：20</p>
                <a href="https://example.com/student/003" class="detail-link">查看详细成绩</a>
            </div>
        </div>

        <!-- 成绩表格 -->
        <h2 class="title">科目成绩明细</h2>
        <table class="score-table">
            <thead>
                <tr>
                    <th>学号</th>
                    <th>姓名</th>
                    <th>Python基础</th>
                    <th>爬虫实战</th>
                    <th>总成绩</th>
                    <th>是否及格</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>001</td>
                    <td>张三</td>
                    <td>85</td>
                    <td>92</td>
                    <td>88.5</td>
                    <td class="pass">及格</td>
                </tr>
                <tr>
                    <td>002</td>
                    <td>李四</td>
                    <td>78</td>
                    <td>89</td>
                    <td>83.5</td>
                    <td class="pass">及格</td>
                </tr>
                <tr>
                    <td>003</td>
                    <td>王五</td>
                    <td>59</td>
                    <td>65</td>
                    <td>62</td>
                    <td class="fail">不及格</td>
                </tr>
                <tr>
                    <td>004</td>
                    <td>赵六</td>
                    <td>90</td>
                    <td>95</td>
                    <td>92.5</td>
                    <td class="pass">及格</td>
                </tr>
            </tbody>
        </table>

        <!-- 额外练习节点 -->
        <div class="extra-info">
            <p>本次考试平均分：81.6</p>
            <p>最高分：92.5（赵六）</p>
            <p>最低分：62（王五）</p>
            <ul>
                <li>优秀（≥90）：1人</li>
                <li>良好（80-89）：2人</li>
                <li>及格（60-79）：1人</li>
                <li>不及格（<60）：0人</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""
html = etree.HTML(text)
# result = etree.tostring(html,encoding='utf-8').decode('utf-8')
# print(result)
#题目1
print("*"*100)
title = html.xpath("//head/title/text()")[0]
print(title)

#题目2
print("*"*100)
class_title = html.xpath("//*[@class='title']/text()")
for item in class_title:
    print(item)
#题目3
print("*"*100)
p_class_info = html.xpath("//p[@id='class-info']/text()")[0]
print(p_class_info)

#题目4
print("*"*100)
a_href = html.xpath("//a/@href")
for item in a_href:
    print(item)

#题目5
print("*"*100)
th = html.xpath("//thead/tr/th/text()")
for item in th:
    print(item)

#题目6
print("*"*100)
data_st_id = html.xpath("//div[@data-student-id='002']/h3/text()")[0]
print(data_st_id)

#题目7
print("*"*100)
ww = html.xpath("//tr")[3]
ww_pa = ww.xpath("./td[4]/text()")
print(ww_pa)

#题目8
print("*"*100)
tr = html.xpath("//tr")[1::]
for item in tr:
    td = item.xpath(".//td/@class")[0]
    if td == "fail":
        print(item.xpath(".//td[2]/text()")[0])




#题目9
name_cj =[]
print("*"*100)
trs = html.xpath("//tr")[1::]
for item in trs:
    cj = {}
    if float(item.xpath(".//td[5]/text()")[0])>80:
        cj = {
            "姓名":item.xpath(".//td[2]/text()")[0],
            "成绩":item.xpath(".//td[5]/text()")[0]
        }
        name_cj.append(cj)

print(name_cj)



# td = html.xpath("//tr/td[5]/text()")[0]
# print(td)


#题目10
print("*"*100)
ul_ex = html.xpath("//div[@class='extra-info']/ul/li/text()")
for item in ul_ex:
    print(item)

#题目11
print("*"*100)
# 定位张三所在行的下一行
zhang_san_tr = html.xpath('//td[text()="张三"]/parent::tr')[0]  #获取张三所在行
next_tr = zhang_san_tr.xpath('following-sibling::tr[1]')[0]
print(etree.tostring(next_tr,encoding="utf-8").decode("utf-8"))

#题目12
print("*"*100)
c_pass = html.xpath('//td[@class="pass"]/parent::tr')  #定位所有td拥有class_pass的tr标签
pass_student = []
for i in c_pass:
    student_id = i.xpath(".//td[1]/text()")[0]  #循环获取每个td后在此基础上选择td
    name = i.xpath(".//td[2]/text()")[0]
    pass_student.append([student_id, name])
print(pass_student)

#题目13
xx =[]
print("*"*100)
stu_id = html.xpath('//tr[number(./td[4])>90]/td[1]/text()')
for i in stu_id:
    info = html.xpath(f'//*[@data-student-id="{i}"]')
    print(f"学号{i}：{info[0].xpath('.//h3/text()')[0] if info else '无信息'}")

#题目14
print("*"*100)
result = html.xpath('//div[@class="extra-info"]/p[not(contains(text(),"本次考试平均分"))]/text()')
print(result)
#p[not(contains(text(),"本次考试平均分"))]：筛选容器内 ** 不包含 “本次考试平均分”** 的<p>标签；

#题目15
print("*"*100)
last_row_cells = html.xpath('//table[@class="score-table"]/tbody/tr[last()]/td/text()')
print(last_row_cells)
#/tbody/tr[last()]：定位<tbody>内最后一行<tr>（last()是 XPath 内置函数，直接取最后一个元素）；
#/td/text()：提取该行所有<td>标签的纯文本。