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
