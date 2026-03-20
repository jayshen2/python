import pandas as pd
import numpy as np
from matplotlib.pyplot import axis

stat1 = ["Android精彩编程200例",89.8,1300,"Android","程序设计"]
ts= pd.Series(stat1,index=['图书名称',"定价","销量","类别","大类"])
print(ts)
stat2 = {'图书名称':"Android精彩编程200例","定价":89.8,"销量":1300,"类别":"Android","大类":"程序设计"}
ts = pd.Series(stat2)
print(ts)

stat3 = {"语文":{"张三":80,"李四":55,"王五":78},
         "数学":{"张三":88,"李四":99,"王五":59},
         "英语":{"张三":59,"李四":36,"王五":20},
         "班级":{"张三":"数科1991","李四":"数科1991","王五":"数科1991"}}
cj = pd.DataFrame(stat3)
print(cj)
stat4 = [[80,88,59,"数科1991"],
         [55,99,36,"数科1991"],
         [78,59,20,"数科1991"]]
cj = pd.DataFrame(stat4,index=['张三','李四',"王五"],columns=["语文","数学","英语","班级"])
print(cj)
stat5 = [{"语文":80,"数学":88,"英语":59},
         {"语文":55,"数学":99,"王五":36},
         {"语文":79,"数学":59,"王五":20}]
cj = pd.DataFrame(stat3,index=['张三','李四',"王五"])
print(cj)
print("*"*50)

#调整成绩
df1 = pd.DataFrame(cj,columns=["数学","英语","语文",'班级'])
print(df1)
df1['英语'] = np.sqrt(df1["英语"])*10
print(df1)
print("*"*50)

#汇总成绩
df2 = df1.copy()
df2.loc["学科汇总"]=cj[["语文","数学","英语"]].mean(axis=0)
print(df2)
df2["成绩汇总"] = df2[["数学","英语","语文"]].sum(axis=1)
print(df2)
df2['极差'] = df2[["数学","英语","语文"]].max(axis=1)-df2[["数学","英语","语文"]].min(axis=1)
print(df2)
print("*"*50)

#等级制
df3 = df2.copy()
df3["数学"] = pd.cut(cj["数学"],bins=[0,60,75,85,100],labels=["不及格","及格","良好","优秀"])
df3["语文"] = pd.cut(cj["语文"],bins=[0,60,75,85,100],labels=["不及格","及格","良好","优秀"])
df3["英语"] = pd.cut(cj["英语"],bins=[0,60,75,85,100],labels=["不及格","及格","良好","优秀"])
df3.loc["学科汇总","极差"] = None
print(df3)
print("*"*50)

#排序
df4 = df2.copy()
df4 = df4.sort_values("成绩汇总",ascending=False)
print(df4)
print("*"*50)