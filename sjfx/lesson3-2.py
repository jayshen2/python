import  pandas as pd
import numpy as np
s1 = pd.Series([1,2,3],index = ['one','two','three'])
#序列索引和切片
#dataframe数据框
data = {'strat':['a','b','c','d'],
        'year':[132,123,412,21],
        "pop":[1.2,32,123,2.1]} #key一定是列名
fram = pd.DataFrame(data)
print(fram)
# 通过字典套字典的方式 {key1:{k1:v1,k2:v2},ley2:{k1:v11,k2,v22}}
dict1 = {"语文":{'张三':80,'李四':77},
         '数学':{"张三":45,'李四':72}}
print(pd.DataFrame(dict1))

#columns 设置列索引调整列的数据
#也可以设置新的列索引（NaN）组成的新列
df2 = pd.DataFrame(data,columns=['year','start','pop','da'],index=['one','two',"three",'four'])
print(df2)

#获取dataframe数据
#0 如何获取列名,获取行名
print(df2.columns)
print(df2.index)

#1 获取某一列['列名']
print(df2['pop'])
print(df2.year)
#[k]数据框不允许
#print(df2[0]) 【考】

#2 获取对应的行和列 用iloc loc两个函数执行【考】
print(df2.iloc[1]) #表示取出数据框第k行
print(df2.iloc[-1]) #表示取出数据框第k行

# print(df2.iloc['tow']) #iloc只能接受整数，使用行索引（行的变量名）是无法索引的
# loc[k] loc['xxx']支持变量名索引
print(df2.loc['two'])

# 修改数据框的值(接受标量，但是不能超过行)
df2['dabt'] = 8   #修改列
# df2['dabt'] = np.arange(6)
# pandas下的序列是可以不等擦干的赋值给数据框的
# 会按照对于的idex匹配赋值，如果不包含索引会无法匹配
s1 = pd.Series([1,2,3],index = ['six','two','three'])
df2['dabt']=s1
print(df2)

# 删除数据列
del df2['da']
print(df2)

#转置
df2 = df2.T
print(df2)

# 3 两个等价于对数据框先取某列===序列Seires[] ==对序列进行索引切片
print(df2['one'][:-1])
print(df2.values)