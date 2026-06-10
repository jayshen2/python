import  pandas  as pd
import numpy as np
import matplotlib.pyplot as plt  # 考
import seaborn as sns

#指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 画了散点--连线 plot
data = np.arange(10)
plt.plot(data,linestyle = '--',linewidth = 5,markersize = 10,color = 'g')
plt.show()

labels = ['大专','本科','研究生','博士']
edu = [200,800,159,65]
# 画饼图  x 设置具体数据 ，label设置饼图的标签文本
plt.pie(x = edu,labels = labels, autopct = '%1.2f%%')
plt.title ("受教育人数饼图")
plt.show()

# 画多图并行显示：设置一张白纸、区域进行划分
# 设置新图
fig  = plt.figure()
# 设置子图区域 fig.add_Subfiggure(m,n,k) # 把纸分成m*n块，当前记为1
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.plot(data)
ax2.pie(x = edu,labels=labels)
plt.show()
# 数据可视化流程
# 数据导入--数据预处理---选择需要的数据带入到可视化图像代码---通过参数设置实现美工---得出数据的图像和规律

df = pd.read_excel(r"C:\Users\Administrator\Desktop\data\SuperMarket.xlsx")
# print(df.head())
# print(df.dtypes)

# 1.按照品类 对销售额求和 画柱状图
cate_sale_sum = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(cate_sale_sum)

# 柱状图 原则：从大到小（时序数据不要排序），用来反应数据的趋势
plt.bar(x = cate_sale_sum.index, height = cate_sale_sum)
plt.show()