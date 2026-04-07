import numpy as np
import pandas as pd


df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],'data2': range(3)})

print(df1)
print(df2)

# 表的合并merge(left,right)，只接受两个数据库的合并
df3 = pd.merge(df1, df2)
print(df3)
# 默认：找到两个数据框的公共字段，按照key相同的字段进行合并组合，形成新的表
# 不同值的数据无法合并
# 也可以通过设置on参数进行公共字段指定 直接设置公共字段字符串
df3 = pd.merge(df1, df2,on = 'key')

df4 = pd.DataFrame({'key123': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df5 = pd.DataFrame({'key234': ['a', 'b', 'd'],'data2': range(3)})

# 使用left_on,right_on 的设置进行合并
df6 = pd.merge(df4,df5,left_on="key123",right_on="key234")
# 在实际问题，该方法将left_on,right都保留，去掉其中一列data["key234"].drop

# 两个表格连接的方式 通过how来设置，inner（默认，公共字段值的交集）
# outer(外联，公共字段中值取并集，没有的值nan填充)
print(pd.merge(df1,df2,how='outer'))
print(pd.merge(df1,df2,how='left'))
print(pd.merge(df1,df2,how='right'))
# left(左联)按照左表的公共字段进行连接  right（右联）

# on可以设置为列表：指定多个变量进行组合连接，公共字段是指定的变量组合
left = pd.DataFrame({'key1':['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})

print(pd.merge(left,right,on=["key1","key2"]))
# key1和key2合并后作为公共字段进行连接

# 遇到相同列？？ 不会报错，数据框不接受相同列名，在结果相同的变量名key2后补_x，_y(右表)
print(pd.merge(left,right,on="key1"))
# 也可以指定参数来标记来自不同表的相同变量名 suffixes('_left','_right')
print(pd.merge(left,right,on="key1",suffixes=('_left','_right')))
# 标记相同变量名的变量数据来源


# 如果一个表的公共字段不是变量（列），而是行索引，直接使用on报错
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],   'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(pd.merge(left1,right1,left_on='key',right_index=True))
# 表示使用右表的index作为连接的公共字段

#如果公共字段是层次化的index
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002], 
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'], 
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
print(lefth)
print(righth)
print(pd.merge(lefth,righth, left_on = ['key1','key2'],right_index=True))
# 层次化index问题：其中一个表通过_on=[]设置，其中一个通过left_index(right_index)设置

#join可以使用多表合并 meger只能接受两个表(可以多次使用merge,但是merge要先保存一下),参数设置和merge一样
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]], 
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])

another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York','Oregon'])
print(left2)
print(right2)
print(left2.join(right2,how='outer'))
print(left2.join([right2,another],how='outer'))

# 轴向连接concat 拼接 + axis =1
# concat： numpy/pandas都可以做
# concat 对所有变量都相同的表格进行合并

# numpy： np.concatenate()针对数据进行合并