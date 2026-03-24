import pandas as pd
import numpy as np

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
# 数据框序列 不一样size允许运算；用一个index完成运算，不存在的index返回a
# 所有的index都会被保留+
print(s1+s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),  index=['Ohio', 'Texas', 'Colorado'])
# list("str")把每个字符串拆分？》》》》
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# 数据框数据框 所有的index和columns允许运算；用一个index完成运算，不存在的index返回a
print(df1+df2)
# df1.add(df2)  #效果和+相同，
print(df1.add(df2,fill_value=0))
print(df2.add(df1,fill_value=0))
# 当填充的元素在df1和df2都没有 仍然返回NaN（本质上仍然是fill_value+nan=nan）

# 课件中国其他的函数(add  sub  mul div  floordiv pow)
# 以字母r开头会翻转阐述  df1.sub(df2) = df2.rsub(df1) = df1-df2

#广播(broadcasting)
#将小维度的shape自动扩展成大的
# 1---N 2----2N 自动扩展试下是成倍数扩大 不支持非1变成N
#【3，4】-【1，4】
#【3，4】-【2，4】
# DataFrame和Series之间的运算 也支持广播规则【考：判断df1(10,5),(2,5)】
# 若遇到不存在的index或columns，那么在index和columns中取并集
# 出现公有的index和columns 执行广播规则，若没有，则返回NaN （本质上还是value+NAN=NAN）
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
s1= frame.iloc[0]
print(s1+frame)

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
f = lambda x:x.max() -x
print(frame.apply(f))
# 将f apply到数据对象,frame是数据框 在执行max时，早了最大，并且按列执行了f
print(frame.apply(f,axis =1)) #axis 按行执行，按行找最大值 列固定按行执行
#【考】 给出两个数据框，根据数据框判断axis按照哪个维度执行
# 给出数据框，给出axis写出运行结果

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
x1 = frame.sum()   #默认axis=‘index’
x2 = frame.sum(axis=0)
x3 = frame.sum(axis=1)
x4 = np.sum(frame)
x5 = np.sum(frame, axis=1)
print(x5)
# 求总和x5 = np.sum(frame, axis=1).sum()