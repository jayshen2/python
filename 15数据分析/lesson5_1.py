import numpy as np
import pandas as pd

# apply 应用到整个数据框
# map 应用到某个序列
# 排序和排名
# sort_index() #对行标列标进行排序，不对values,不对原始数据修改
# asis=  0或1 
# 倒序排列 ascending = False
df1 = pd.Series(np.arange(4),index=["c","b","a","d"])
print(df1.sort_index()) #直接返回排序后
print(df1.sort_index(axis=0)) #直接返回排序后

df2 = pd.DataFrame(np.arange(18).reshape(3,6),index=["three","two","one"],columns=["d","c","a","b","f","e"])
print(df2.sort_index(axis=0)) #对行索引排序（从小到大）
print(df2.sort_index(axis=1)) #对列索引排序（从小到大）
# 对行和列同时进行排序
df3 = df2.sort_index(axis=0)
df4 = df3.sort_index(axis=1)
print(df4)
print(df2.sort_index(axis=1,ascending=False))

#index_values() 只能对Series排列,默认从小到大排序
# 对dataframe排序要设置by参数（按照某个变量对整个表格排序）
# 排序时缺失值会放在最后
# by可以设置多个参数进行排列by=["a","b","c"]相同的根据下一个参数排序
print(df2["d"].sort_values(ascending=False))
print(df2.sort_values(by="b",ascending=False))


# rank :从1开始排名默认降序排名 默认情况下分配的是平均排名
# 可以通过method = 按照不同原则排序
# max多个值按正常排序 把这些排名中的最大值作为所有的排名
# min常用的考试排名
obj = pd.Series([7,-5,7,4,2,0,4])
print(obj)
print(obj.rank(method = "min"))
obj["rank"]=obj.rank(method='min')
print(obj)
frame = pd.DataFrame({'b':[4,1,-5,2],"a":[3,2,3.4,1],'c':[-2,2,1,4]})
print(frame)
# 默认是axis = 0 遍历所有行位置，列不变
frame.rank(method="min")
# 常见操作，取出某列排名添加数据框中
frame["rank"] = frame["c"].rank()
print(frame)

print(frame.rank())
