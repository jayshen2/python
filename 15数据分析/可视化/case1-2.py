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
df = pd.read_csv(r"data\titanic_train.csv")
gdp = pd.read_excel(r"data\Province GDP 2017.xlsx")
iris = pd.read_csv(r"data\tips.csv")

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna('Q')
#编码进行转换
df['Survived'] = df['Survived'].map({0:'死亡',1:'存活'})
df['Pclass'] = df['Pclass'].map({1:'头等座',2:'二等座',3:'三等座'})
df['Sex'] = df['Sex'].map({'male':'男','female':'女'})
#cut函数对数据进行切割分组

#5、特征相关性热力图
#用不同的颜色表明程度的变化（）
#变量有很多x1-----x10，两两之间的相关程度（相关系数）
#例如：消费x1：d1,d2,----,dn
#     收入x2：e1,e2,----,en 计算相关系数[-1,1]  0.8强相关  0.2弱相关 -0.9负相关
data = df.copy()
data['Survived'] = data['Survived'].map({'死亡':0,'存活':1})
data['Pclass'] = data['Pclass'].map({'头等座':3,'二等座':2,"无座":1})
data['Sex'] = data['Sex'].map({'男':0,'女':1})
data_corr = data[['Survived','Pclass','Sex','Age','Fare']].corr()
sns.heatmap(data_corr,vmin=-1,vmax=1,cmap ='coolwarm',center=0,annot = True,fmt='.2f',square=True)
plt.show()