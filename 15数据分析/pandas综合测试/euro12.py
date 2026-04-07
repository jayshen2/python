import pandas as pd
import numpy as np


#将数据集命名为euro12
euro12 = pd.read_csv(r"D:\python\15数据分析\pandas综合测试\pandas\3-Euro2012\Euro2012.csv")

#只选取 Goals 这一列
Goals = euro12["Goals"]

#有多少球队参与了2012欧洲杯？
teamcount = euro12['Team'].nunique() # 统计数据集唯一值，计数

#该数据集中一共有多少列(columns)?
columns = euro12.shape[1]

#将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
discipline = euro12[['Team','Yellow Cards','Red Cards']]

#对数据框discipline按照先Red Cards再Yellow Cards进行排序
discipline = discipline.sort_values(by=['Red Cards','Yellow Cards'])
# ascending = False 从大到小排序

#计算拿到的黄牌数的平均值
yellow_car_dmean = euro12['Yellow Cards'].mean()

#找到进球数Goals超过6的球队数据
high_goal = euro12[euro12['Goals']>6]
print(high_goal)

#选取以字母G开头的球队数据
G_team = euro12[euro12['Team'].str.startswith('G')]

#选取前7列
print(euro12.iloc[:,:7])

#选取除了最后3列之外的全部列
print(euro12.iloc[:,:-3])

#找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
t_team = ['England','Italy','Russia']
eir_sa =  euro12.loc[euro12['Team'].isin(t_team),['Team','Shooting Accuracy']]
print(eir_sa)
# team变量是否在设置的目标列表中 作为条件放入iloc和


