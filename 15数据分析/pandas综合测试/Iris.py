import pandas as pd
import numpy as np

#读取数据并存为一个名叫iris的数据框
iris = pd.read_csv("pandas/2-Iris/iris.data")

#创建数据框的列名称['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class']
iris.columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class']

#数据框中有缺失值吗？
print(iris.isnull().any())

#将列petal_length的第10到19行设置为缺失值
iris[11:21] = np.nan

#将petal_length缺失值全部替换为1.0
iris['petal_length'].fillna(1.0)

#删除列class
del iris["class"]

#将数据框前三行设置为缺失值
iris[0:3] = np.nan

#删除有缺失值的行
iris = iris.dropna()

#重新设置索引
iris = iris.reset_index()
