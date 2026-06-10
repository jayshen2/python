from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

"""
第6题:基于titanictrain.csv绘制分组柱状图题目:使用titanic_train.csv 数据集，用Seaborn绘制不同舱等级、性别的平均票价分组柱状图，要求添加数据标签、设置图例、解决中文乱码。提示
·可视化函数:sns.barplot()
核心参数:(二次分组)、ci(置信区间)、(配色)huepalette
"""
train = pd.read_csv('data/titanic_train.csv')
print(train.head())

#指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

ax = sns.barplot(x="Pclass", y="Fare", hue="Sex", data=train, ci=None, palette="muted")
ax.set_xlabel("仓位等级")
ax.set_ylabel("平均票价")
ax.legend(title="性别")
plt.show()

"""
题目:使用titanic_train.csv 数据集，统计不同客舱等级乘客生存/未生存占比，用Matplotlib绘制堆叠柱状图，要求添加百分比数据标签
提示
·可视化函数:plt.bar()(叠加bottom参数)
核心操作:分组统计占比、bottom指定下层高度
"""
counts = train.groupby(['Pclass', 'Survived']).size().unstack()
print(counts)