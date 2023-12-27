scoreDict = {"张三":{'gs':78,'xd':62,"p":50,'yy':65},
             "李四":{'gs':60,'xd':50,"p":63,'yy':59},
             "王五":{'gs':89,'xd':80,"p":99,'yy':90}}
kc={"gs":"高数","xd":"线代","p":"python","yy":"英语"}
x = input("请输入要查询的学生姓名")
y = input("请输入要查询的课程代码，gs（高数）或xd（线代）或p（Python）或yy（英语）")
try:
    print(f'{x}的{kc[y]}成绩为:{scoreDict[x][y]}')
except:
    print("没有你的数据")