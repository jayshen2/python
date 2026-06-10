import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 导入数据
tips = pd.read_csv(r"data\tips.csv")
train = pd.read_csv(r"data\titanic_train.csv")
gdp = pd.read_excel(r"data\Province GDP 2017.xlsx")
iris = pd.read_csv(r"data\iris.csv")

# 第二题
bars = sns.barplot(data = tips,x='day',y = 'tip',palette='Blues_d',ci=95)

for b in bars.patches:
    h = b.get_height()
    # b.get_x() 柱子的左下角坐标 b.get_width()柱子的宽度
    bars.text(b.get_x()+b.get_width()/2,h+0.06,f'{h:.2f}',ha='center')
plt.show()

# 第三题

gdp_sort = gdp.sort_values(by = 'GDP',ascending = False).reset_index(drop = True)

bars = plt.barh(gdp_sort['Province'], gdp_sort['GDP'])
for bar in bars:
    w = bar.get_width()
    plt.text(w+0.05,bar.get_y() + bar.get_height()/2,f'{w:.2f}')

plt.show()

# 第四题
# 直方图：对数据的取值范围做分组【a,b】:[a,x1][x1,x2]
#         数据落到对应小区间上的数量有多少，根据该数量画出区间的柱状图
#         主要用于观察数据的分布情况

tip_mean = tips['total_bill'].mean()
tip_median = tips['total_bill'].median()

plt.hist(tips['total_bill'], bins = 20,edgecolor='b',alpha=0.8,density=True)
plt.axvline(tip_mean,linestyle = '--',linewidth = 2,label = "均值f{tip_mean:.2f}")
plt.axvline(tip_median,linewidth = 2,label = "中位数f{tip_mean:.2f}")
# 图例
plt.legend(loc='best')
#网格
plt.grid(alpha=0.5)
plt.show()
# 大部分数据集中在10-20之间，大部分数据和均值，中位数差异不大，数据的分布情况整体偏左


# 第五题 ：箱线图（盒须图）
# 可以在图中显示min，四方位数，max，mean 通过几个数的位置关系————数据分布
# （70%---max区间较短：数据紧密在该区间）

# 箱线图各箱子的标签
labels = tips['day'].unique()

# 按照不同天数做数据提取
day_tip = [tips.loc[tips['day'] == d,]['tip'].values for d in tips['day'].unique()]

box = plt.boxplot(day_tip,labels = labels,patch_artist= True,showfliers=True)
plt.show()
# 可以看出四天的小费的四分位数：最大最小，均值
# 以周四为例：均值和四分位数较近，大量的数集中分布在四分位数到均值之间
# 以周六位例：分布较为均匀（相互之间距离较为接近）

#第六题
ax = sns.barplot(x="Pclass", y="Fare", hue="Sex", data=train, ci=None, palette="muted")
ax.set_xlabel("仓位等级")
ax.set_ylabel("平均票价")
ax.legend(title="性别")
plt.show()



# 第七题
data1 = train.copy()
group = data1.groupby("Pclass")["Survived"].value_counts().unstack(fill_value=0)
# 转成百分比
ratio = group.div(group.sum(axis=1), axis=0) * 100

# 3. 准备数据
x = ratio.index  # 客舱等级1/2/3
dead = ratio.iloc[:, 0].tolist()  # 未生存占比
alive = ratio.iloc[:, 1].tolist() # 生存占比

# 4. 画堆叠柱状图
plt.figure(figsize=(6,4))
plt.bar(x, dead, label="未生存", color="#d62728")
plt.bar(x, alive, bottom=dead, label="生存", color="#2ca02c")

# 5. 加百分比标签
for i in range(len(x)):
    # 未生存标签
    plt.text(x[i], dead[i]/2, f"{dead[i]:.1f}%", ha="center", va="center", color="white")
    # 生存标签
    plt.text(x[i], dead[i] + alive[i]/2, f"{alive[i]:.1f}%", ha="center", va="center", color="white")

# 6. 美化
plt.xticks(x, ["一等舱", "二等舱", "三等舱"])
plt.ylabel("占比 (%)")
plt.title("不同客舱等级乘客生存占比")
plt.legend()
plt.tight_layout()
plt.show()


# 第八题
corr = iris.corr(numeric_only=True)
plt.figure(figsize = (10,6))
sns.heatmap(corr,annot = True,cmap='coolwarm',fmt = '.2f',center = 0)
plt.show()

# 第九题
print(iris)
sns.pairplot(data= iris ,hue="Species",diag_kind="hist",corner=True)
plt.show()

# 第十题
#数据预处理
train = pd.read_csv(r"data\titanic_train.csv")
#补充缺失值
train['Age'] = train['Age'].fillna(train['Age'].median())
train['Embarked'] = train['Embarked'].fillna('Q')
#编码进行转换
train['Survived'] = train['Survived'].map({0:'死亡',1:'存活'})
train['Pclass'] = train['Pclass'].map({1:'头等座',2:'二等座',3:'三等座'})
train['Sex'] = train['Sex'].map({'male':'男','female':'女'})
train['年龄分组'] = pd.cut(train['Age'],bins=[0,10,20,50,200],labels=['儿童','青少年','中年','老年'])
plt.figure(figsize = (8,6))
ax = sns.countplot(data=train,x='Survived')
for p in ax.patches:
    h = p.get_height()
    ax.text(p.get_x() + p.get_width()/2,p.get_height()+10,f'{h:.2f}',ha='center')
plt.show()

#(2)客舱+性别生存概率分组柱状图
plt.figure(figsize = (10,6))
ax = sns.barplot(data=train,x="Pclass", y="Survived", hue="Sex")
plt.gca().invert_yaxis()
plt.ylabel("死亡人数")
plt.xlabel("座位人数")
plt.show()

#（3）年龄分组生存概率柱状图
plt.figure(figsize = (10,6))
ax = sns.barplot(data=train,x="年龄分组", y="Survived")
plt.gca().invert_yaxis()
plt.show()

# (4)
plt.figure(figsize = (10,6))
ax = sns.boxplot(data=train,x="Survived", y="Fare")
plt.show()

plt.figure(figsize = (10,6))
ax = sns.boxplot(data = train,x='Embarked',y='Age')
plt.show()
# (5) 特征相关热力图
# 用不同的颜色表明程度的变化
# 变量有很多x1，...,x10 两两之间的相关程（相关系数）
# 例如 ： 消费x1:d1,d2...dn
# 例如 : 收入x2:e1,e2...en  计算相关系数[-1,1] 0.8 强相关 0.2 弱相关 -0.9 负相关
data = train.copy()
data['Survived'] = data['Survived'].map({'死亡':0,'存活':1})
data['Pclass'] = data['Pclass'].map({'头等座':3,'二等座':2,"无座":1})
data['Sex'] = data['Sex'].map({'男':0,'女':1})
data_corr = data[['Survived','Pclass','Sex','Age','Fare']].corr()
sns.heatmap(data_corr,vmin=-1,vmax=1,cmap ='coolwarm',center=0,annot = True,fmt='.2f',square=True)
plt.show()
