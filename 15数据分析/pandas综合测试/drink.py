import pandas as pd
import numpy as np

#将数据框命名为drinks
drinks = pd.read_csv(r"pandas/4-Drinks/drinks.csv")
print(drinks)

#哪个大陆(continent)平均消耗的啤酒(beer)更多？
# data.groupby('x') data按照x变量进行分组后运算
beer_drink = drinks.groupby('continent')['beer_servings'].mean().sort_values(ascending=False)
print(beer_drink.index[0])

#打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值
wine_drink  = drinks.groupby('continent')['wine_serv ings'].describe()
print(wine_drink)

#打印出每个大陆每种酒类别的消耗平均值
all_drink = drinks.groupby('continent')[['spirit_servings','wine_servings','beer_servings','total_litres_of_pure_alcohol']].mean()
print(all_drink)

#打印出每个大陆每种酒类别的消耗中位数
all_drink = drinks.groupby('continent')[['spirit_servings','wine_servings','beer_servings','total_litres_of_pure_alcohol']].median()
print(all_drink)

#打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
#all_drink = drinks.groupby('continent')['spirit_servings'].mean()
#max_drink = drinks.groupby('continent')['spirit_servings'].max()
#min_drink = drinks.groupby('continent')['spirit_servings'].min()
sprint_drink =drinks.groupby('continent')['spirit_servings'].agg(['mean','max','min'])
print(sprint_drink) 