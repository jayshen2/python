from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

gdp = pd.read_excel('data/Province GDP 2017.xlsx')
gdp = gdp.sort_values(by='GDP',ascending=False).reset_index(drop = True)

plt.barh(y=gdp['Province'],width=gdp['GDP'],height=0.5,)
plt.gca().invert_yaxis()
plt.xlabel('GDP (亿元)', fontsize=12)
plt.ylabel('省份', fontsize=12)
plt.show()