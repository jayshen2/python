import numpy as np
import pandas as pd

#重建索引 reindex
df1 = pd.Series([2,3,4,1,4],index=['a','c','d','b','e'])
print(df1)

# 根据reindex设置的实例进行重排
# 缺失的index会自动补NaN
# REINDEX([])默认修改index 也可以通过指定columns=[]
df2 = df1.reindex(['a','b','c','d'])
print(df2)

df3 = pd.DataFrame(np.arange(10).reshape(2,5),
                   index = ["a","b"],
                   columns = ["xia","s",'a','d','c'])


df5 = df3.reindex(columns=['s','a','d','c',"chengyi"])
print(df5)

# 删除drop(del语法) 整行整列的删除
# 对指定的轴（行列）进行删除
# 只能drop存在的index
df6 = df5.drop("b") #不会在原始数据删除
# drop 默认对axis = 0 （按行处理）进行删除axis = 1 （按列处理）
#           axis = 'index'            axis = 'columns'
df7 = df5.drop(["a","s"],axis = 1)
print(df7)

#inplace = True 表示在源数据修改
df5.drop('a',inplace=True)
print(df5)


# 索引的切片（数据的选取过滤）
# Series索引：obj['a'] obj['a','b','c'] obj[2:4] obj[obj<2]
data = pd.DataFrame(np.arange(16).reshape(4,4),
                   index = ["a","b",'c','d'],
                   columns = ["s",'a','d','c'],dtype = float)

print(data[['s','a','c']])
data[data>10]=2.5
print(data)

# iloc 和 loc使用函数（函数语法ilco[] loc[] ）
# iloc[index,columns]整数索引   loc[index,columns]标签索引
# 复习在numpy取array 二维数组的第2，3，5行，第4，7，8列
# array[[2,3,5],[4,7,8]]只会提取array(2,4),(3,7),(5,8)===使用ix_
# iloc[k] 取k行，第二个参数没有指定表示取全部   
# iloc[:k] 取k列   ：表示全部
# iloc[[i1,i2],[c1,c2]] 取i1，i2行，c1，c2列，和numpy中二维数组不同，注意复习ix_
data = pd.DataFrame(np.arange(16).reshape(4,4),
                   index = ["a","b",'c','d'],
                   columns = ["s",'a','d','c'])

print(data)
print(data.iloc[[2,3],[0,1,3]])
print(data.iloc[:,2]) #取列

#data.iloc[1:3,2:8,2] # 取1，2行，2，4，6列
print(data.loc[['a','c'],['d','s']])
#loc的索引过程中含有重新排列，匹配过程中是逐一配对的

print(data.iloc[:,3][data.c>8])
# step1 data.iloc[:,3] 取所有行，前三列
# step2 data[data.c>8]c列中大于8的位置标记为True
#选取前三列数据c>8的
#【考】给代码写注释，给结果写代码