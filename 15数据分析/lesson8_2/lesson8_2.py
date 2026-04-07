from operator import concat

import pandas as pd
import numpy as np


# 轴向连接concat 拼接 + axis =1
# concat： numpy/pandas都可以做
# concat 对所有变量都相同的表格进行合并

# numpy： np.concatenate()针对数据进行合并
arr = np.arange(12).reshape(4,3)
print(np.concatenate([arr,arr]))  # 默认横着拼 ：A表后接下来下一行放b表
print(np.concatenate([arr,arr],axis=0)) # 默认 列不变，行做遍历
print(np.concatenate([arr,arr],axis=1)) # 默认 行不变，列做遍历：在A表的最后一列后再发B表的列
arr1 = np.concatenate([arr,arr],axis=1)
# 【考】 print(arr1.shape)

# pandas : pd.concat()
s1 = pd.Series([0,1],index=['a','b'])
s2 = pd.Series([2,3,4],index=['c','d','e'])
s3 = pd.Series([5,6],index=['f','g'])
print(pd.concat([s1,s2,s3])) # 默认axis = 0 A放完下一行接着放b
print(pd.concat([s1,s2,s3],axis=1))
# 不继承原表中的列名（0）,concat过程中即使是同名的变量，也要换到另外一列拼接
# 严谨的做法：merge
# 等价于分块矩阵的对角矩阵
s4 = pd.concat([s1,s3])
print(pd.concat([s1,s4],axis=1))
# 完全不同的index 避免列名相同导致错误的合并（A表0列不一定是B表0列） 分块对角矩阵
# 存在相同的index表格上自动拼接到一起

# concat可以通过设置join设置合并方式，和merge中的how相同（默认outer）
print(pd.concat([s1,s4],axis=1,join='inner'))  # 内连接：连接相同的

# concat 设置key指定concat过程中表格的来源
result = pd.concat([s1,s2,s3],keys=['one','two','three'])
# s1的表是1班的表，合成后会多形成一个index

print(result)
