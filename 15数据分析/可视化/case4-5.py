from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

tips = pd.read_csv('data/tips.csv')

#指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

"""
第4题:基于tips.csv绘制总账单金额Matplotlib直方图
题目:使用tips.csv 数据集，用Matplotlib绘制顾客总账单金额分布直方图，设置20个分箱，添加均值与中位数垂直线、网格与图例。提示
可视化函数:plt.hist()
核心参数:x(数值变量)、bins(分箱数)、edgecolor(边框色)、alpha(透明度)
辅助函数:plt.axvline()添加均值/中位数线
"""
plt.hist(x =tips['total_bill'],bins= 20)
mean_bill = tips['total_bill'].mean()
median_bill = tips['total_bill'].median()
plt.axvline(mean_bill, color='red')

# 添加中位数垂直线
plt.axvline(median_bill, color='green')
plt.grid(True)
plt.show()


"""
第5题:基于tips.csv绘制不同日期小费分布Matplotlib箱线图
题目:使用tips.csv 数据集，用Matplotlib绘制不同日期小费金额分布箱线图，自定义填充色、显示异常值、设置中位数样式。提示
.可视化函数:plt.boxplot()
核心参数:labels (分类标签)、patch_artist(填充色)、
showfliers(显示异常值
"""
days = tips['day'].unique().tolist()
thur_tip = tips[tips['day'] == 'Thur']['tip']  # 只要周四的小费
fri_tip  = tips[tips['day'] == 'Fri']['tip']   # 只要周五的小费
sat_tip  = tips[tips['day'] == 'Sat']['tip']  # 只要周六的小费
sun_tip  = tips[tips['day'] == 'Sun']['tip']  # 只要周日的小费
data_to_plot = [thur_tip, fri_tip, sat_tip, sun_tip]


plt.boxplot(data_to_plot,label=days,medianprops={'color':'red'},showfliers=True)
plt.show()