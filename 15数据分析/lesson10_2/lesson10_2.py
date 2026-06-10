import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wcwidth import width

# 1.全局设置
#指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 2.导入数据并预览
df_tips = pd.read_csv('data/tips.csv')
print(df_tips.head())
print(df_tips.info())

# 3.数据预处理：按日期分组，计算每日的平均小费和计数
# re.sub  re.replace  df.loc[df[""]] = 'sat'
# groupby(as_index=False) 不将分组变量设置为index
df_tips_stats = df_tips.groupby('day',as_index=False)['tip'].agg(['mean','count'])
df_tips_stats.columns = ['用餐日期','平均小费','小费次数']
print(df_tips_stats.head())

# 4.matplotlib画图 柱状图：x 分组变量 height 数值
# 柱状图：按时序可以观察数据的变化情况 也可以对分类变量进行比较
plt.bar(x = df_tips_stats['用餐日期'],
        height = df_tips_stats['平均小费'],
        label = '平均小费',width=0.6)
plt.show()
# 额外工作：设置图像的标题plt.title/设置图像每个柱子【数值标签】
# sns.画图(数据集,x 变量名,y)
sns.barplot(data = df_tips_stats,x='用餐日期',y='小费次数')
plt.show()

# 条形图:一般不做看趋势，用作比较数据（排序后再作图，从大到小）
# plt：plt.barh  sns: sns,barplot(设置桉树orient = 'h')
plt.barh(y = df_tips_stats['用餐日期'],
         width = df_tips_stats['小费次数'].sort_values(),height = 0.6)
plt.show()

sns.barplot(data = df_tips_stats,
            x='小费次数',y = '用餐日期',orient = 'h')
plt.show()
# 作业：参考上面的代码：对gdp文件按照GDP排序
# 取前3化条形图，要求添加数据标签
gdp = pd.read_excel('data/Province GDP 2017.xlsx')
print(gdp.info())
gdp_sort = gdp.sort_values(by='GDP',ascending=False).reset_index(drop=True)
gdp_sort_top3 = gdp_sort.iloc[:3,]
print(gdp_sort_top3)
sns.barplot(gdp_sort_top3,
            x='GDP',
            y='Province',orient = 'h')
plt.title('数科2571_郭沅森_29')
plt.show()