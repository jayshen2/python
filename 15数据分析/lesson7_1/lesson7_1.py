import pandas as pd
import numpy as np

# 多个数据表，合并（聚合，连接）重塑

# 8.1层次化索引
# 含有多个index 的数据框
data = pd.Series(np.random.randn(9),index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],[1, 2, 3, 1, 3, 1, 2, 2, 3]])

data = pd.Series(np.random.randn(10),index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd','a'],[1, 2, 3, 1, 3, 1, 2, 2, 3,'4']])
# 不同层次的index是按照列表中的顺序出现（同一层级中的index不会进行整合）
# 相同index会有类似聚合的效果

# data[]表示索引 多层index 使用多个[]
print(data)
print(data['a'])
print(data['a'][3])

# unstack() 把标准数据表变成数据透视表  stack()把数据透视表转换为多层index的数据表
data1 = data.unstack()
print(data1)
data2 = data1.stack()
print(data2)
# 数据透视表正常在分析额保存过程中数据量会大于多层index的表

# 层次花可以体现在index columns : 数据shape【0】 == index对应长度  shape【1】 == columns 对应长度
frame1 = pd.DataFrame(np.arange(12).reshape((4, 3)),index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],columns=[['Ohio', 'Ohio', 'Colorado'],['Green', 'Red', 'Green']])
frame2 = pd.DataFrame({'a': range(7),
                       'b': range(7, 0, -1),
                       'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                       'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame1)
print(frame2)

# 设置多层次数据的表头
print(frame1.index.names)
frame1.index.names = ['class','number']
frame1.columns.names = ['start','color']
print(frame1.index.names)
print(frame1.columns.names)
print(frame1)

# 选取分组
# 对多层index columns 数据 data["x"] data中列names等于x的数值
print(frame1['Ohio'])
# 对行所有要借助于iloc loc
print(frame1.loc["a",:])
print(frame1.loc["a",:].loc[2,:])
print(frame1.loc["a",:].loc[2,:].loc["Ohio",:]["Red"])
# 数据透视表的索引需要一级一级往下完成索引

print(frame1)
# swaplevel(i,j) 交换i，j索引的位置
# 不会对原始数据进行覆盖
print(frame1.swaplevel("class","number"))
print(frame1)

# swaplevel对index的顺序进行调整

# 对调整顺序后的数据进行不同等级的数值排序
# sort_index()设置level 通过level = i 表示对第i层的index 进行排序
# 调整过程中上一层
print(frame1.sort_index(level=1))
print(frame1.swaplevel("number","class").sort_index(level=1,ascending=False))  # asceding = False 从大到小排

print(frame1)

print(frame1.sum(level=1))
