import numpy as np
import pandas as pd

#pandas 数据结构 数据框和序列
#序列Series 向量 数据框DataFrame 矩阵，表格
#pd 有非常多的函数数据库
s1 = pd.Series([1,2,3,4]) #使用Series生成一维数组
#索引默认从零开始，左闭右开，支持-1索引

s2 = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s2)
print(s2["b"])
#多种索引值共村，既可以使用数字索引，也可以用索引名称完成索引,现在版本已经不行了
print(s2[["a","b","c"]])
#多值索引（与numpy相同）
print(s2[s2>3]) #s2>3返回一个True，False序列，然后根据这个对应查找
print(s2**2) #运算比较涵州数与nipy相同)，并且能与数组的计算方法同时使用

dict1 = {"a":123,"b":234,"c":456} #通过字典构建序列
s3 = pd.Series(dict1)
print(s3)

#创建时 按照index构成索引，字典有键值对的值放入对应index，如果设有键值返回NaN
#NaN并表示缺失
list1 = ["a","b","c","d"]
dict2 = {"a":123,"b":234,"c":456}
s4 = pd.Series(dict2,index=list1)
print(s4)
print(pd.isnull(s4)) #查找序列中有无缺失值，返回序列
print(pd.notnull(s4))

#索引标签自动对齐
s5 = pd.Series([1,2,3,4],index=[0,1,"a",3])
list2 = ["a","b","c","d"]
dict3 = {"a":123,"b":234,"c":456,"s":1264}
s6 = pd.Series(dict3,index=list2) #只合并索引有的，索引有数值没有的用NaN填充
print(s6)
print(s5+s6) #两个序列相同的索引相加，否则序列值为NaN

s5.name = "test"
s5.index.name = "test" #Series对象本身及其索引都有一个name属性
print(s5)

data = {"a":[1,2,3,4,5,123],
        "b":[6,7,8,9,10,234],
        "c":[11,12,13,14,15,456]}
df = pd.DataFrame(data) #创建一个数据框
print(df)
print(df.head()) #只读取前五行数据

#数据框按照指定的索引进行排序
df2 = pd.DataFrame(df,columns = ["a","c","b"])
print(df2)
print(df2.index)  #行索引
print(df2.columns) #列索引