from pandas.core.algorithms import duplicated

import pandas as pd
import numpy as np
# pandas 基础
# 数据的清洗和准备
# 进一步分析（describe（），画图）
iris = pd.read_csv(r'D:\python\15数据分析\lesson6_2\pandas\2-Iris\iris.data',
                   header=None,
                   names = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())
print(iris.shape) # 输出数据的行列

# 数据框中有缺失值吗？
print(iris.isnull().any().any())  # 整个数据框是否存在缺失值
# isnull() 检查是否存在缺失值，存在则未True
# any() 任意一个，变量中每一个只只要存在一个True就返回True,第一个为列，第二个全部。对数据一直汇总

# 将列petal_length 的第10到19行设置为缺失值
iris.loc[10:20,'petal_length'] = np.nan  #loc[行，列] 可以使用文本索引
print(iris.isnull().any().any())

# 前三行设置缺失值
iris.iloc[0:3,:] = np.nan  # 前三行设置为缺失值
print(iris.head(20))

# 删除缺失值
# iris = iris.dropna("class")
# axis=1 列不变，遍历所有的行
print(iris)

# 删除缺失值所有行
iris = iris.dropna() # dropna() 只要存在空值所在的行全删掉
print(iris)

# 将petal_lengt缺失值全部替换为1.0
iris["petal_length"] = iris["petal_length"].fillna(1.0)
mean = iris["petal_length"].mean  # 计算这一列的平均值
iris["petal_length"].fillna(mean, inplace=True)  # fillna不会覆盖原始数据

# 按列填充fillna + 字典
# fillna可以在参数中输入一个字典，{columns:value}==批量替换
iris = iris.fillna({"petal_length": 2.0, "sepal_length": 8.5})
# 数据标准格式：行==每一个行数据个案（整数做定位）  列==变量

# 重新设置索引 删除以后建议做
iris = iris.reset_index()
print(iris.head())

iris.loc[[0, 1, 2], :] = np.nan
iris = iris.dropna(how='all')  # 整行全空才删
print(iris.head(20))

# 数据转换
# 重复值：某两行一样 === 重复值不一定要删除
# 数据重复值检测:返回结果由bool值组成的数列，前面出现过的数据该行会显示True
# data.duplicates()

# 删除重复值
# 删除以后保留最后一个重复值 默认保留第一个值
# data.drop_duplicates(keep='lest')

# 替换值  数据要做复制：哑变量（用中文，用特定的设置表示具体的数据含义）
# data.replace("需要替换的值"，"替换的值")


# 异常值：个别数值和大部分数值偏离较大
# 异常值检测IQR
# 计算Q1和Q3 计算IQR = Q3-Q1  确定异常值便捷：[Q1-1.5*IQR.]
# 遇到异常值常见办法：删除，大数据前提下，异常值需要单独取出来进行研究
