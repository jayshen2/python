import pandas as pd
import numpy as np

#将数据集命名为euro12
euro12 = pd.read_csv(r"pandas/3-Euro2012/Euro2012.csv")

#只选取 Goals 这一列
print(euro12["Goals"])

#有多少球队参与了2012欧洲杯？
print(euro12.shape[1])

#该数据集中一共有多少列(columns)?
print(euro12.shape[0])

#将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
discipline = pd.DataFrame([euro12["Team"],euro12["Yellow Cards"],euro12["Red Cards"]]).T
print(discipline.head())

#对数据框discipline按照先Red Cards再Yellow Cards进行排序
discipline = pd.DataFrame(discipline,columns=["Team","Red Cards","Yellow Cards"])
print(discipline.head())

#计算拿到的黄牌数的平均值
print(round(discipline["Yellow Cards"].mean(),2))

#找到进球数Goals超过6的球队数据
print("进球数超过6球的球队：")
print(euro12[euro12['Goals'] > 6][['Team', 'Goals']])

#选取以字母G开头的球队数据