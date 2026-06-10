import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.sandbox.tsa.example_arma import myacf

from webspider.lesson3_1.实验1 import result

# （1）读取 employee.xlsx 数据，并命名为 empd
emp = pd.read_excel(r"employee.xlsx")
# （2）将 birthday 和 start_work 转换为日期类型
emp['birthday'] = pd.to_datetime(emp['birthday'])
emp['start_work'] = pd.to_datetime(emp['start_work'])
# （3）新增 age 列，按当前年份减出生年份计算年龄
emp['age'] = pd.Timestamp.today().year - emp['birthday'].dt.year
# （4）新增 work_age 列，按当前年份减入职年份计算工龄
emp['work_age'] = pd.Timestamp.today().year-emp['start_work'].dt.year
# （5）将 tel 转换为字符串，并把中间四位替换为 ****
emp['tel'] = emp['tel'].astype(str)
emp['tel'] = emp['tel'].apply(lambda x : x.replace(x[3:7],"****"))
# （6）从 email 中拆分出 邮箱名 和 域名 两列
emp['邮箱名'] = emp['email'].apply(lambda x :x.split('@')[0])
emp['域名'] = emp['email'].apply(lambda x :x.split('@')[1])
# （7）输出处理后的前 5 行数据
print(emp.head(7))

# （1）根据示例数据创建 DataFrame，变量名为 score_df
score_df = pd.DateFrame({
	"name":["TOM","LUCY"],
	"python":[90,60],
	"math":['80,75']
})
# （2）将 name 列设置为行索引
sorce_df = score_df.set_index('name')
# （3）使用 loc 查询 Tom 的 python 成绩
score_df.loc['TOM','python']
# （4）使用 iloc 查询第 2 行全部数据
score_df.ilic[1,:]
# （5）使用 iloc 查询前 3 行、前 2 列数据
score_df.iloc[:3,:2]
# （6）筛选 python 成绩大于等于 85 分的学生
score_df[score_df['python']>=85]


# （1）读取 sales.xlsx 数据，并命名为 sales
sales = pd.read_excel(r"sales.xlsx")
# （2）使用 duplicated 检测重复记录
sales.duplicated()
# （3）删除重复记录，默认保留第一次出现的数据
sales = sales.drop_duplicates(keep='first')
# （4）统计每一列缺失值个数
sales.isnull().any()  # 判断
sales.isnull().sum()  # 计数
# （5）使用 0 填充 sales 列缺失值
sales['sales'] = sales['sales'].fillna(0)
# （6）将 date 列转换为日期类型
sales['date'] = pd.to_datetime(sales['date'])
# （7）输出清洗后的数据基本信息
print(sales.info())


# （1）读取 tips.csv 数据，并命名为 tips
tips = pd.read_csv("tips.csv")
# （2）新增 pct 列，计算小费率 tip / total_bill
tips['pct'] = tips['tip']/tips['total_bill']
# （3）定义自定义函数 maxmin，计算极差
def maxmin(x):
    return x.max()-x.min()
# （4）按照 smoker 和 day 两个字段分组
# （5）统计 pct 的平均值和标准差
tips_pct = tips.groupby(by = ['smoker','day'])['pct'].agg(['mean','std'])
# （6）统计 tip 的平均值和极差
tips_tip = tips.groupby(by = ['smoker','day'])['tip'].agg(['mean',maxmin()])



# （1）读取 iris.csv，列名按数据预览中的变量名设置
iris = pd.read_csv("iris.csv",names = ['s_length','s_width','p_length','p_width','class'])
# （2）检查每一列是否存在缺失值
iris.isnull().any()
# （3）计算 p_length 列均值
iris['p_length'].mean()

# （4）使用 p_length 均值填充该列缺失值
iris['p_length'] = iris['p_length'].fillna(iris['p_length'].mean())
# （5）删除仍存在缺失值的行
iris = iris.dropna()
# （6）重置索引，并丢弃旧索引列
iris = iris.reset_index(drop = True)
# （7）输出清洗后的前 10 行
print(iris.head(10))

# （1）读取 Province GDP 2017.xlsx，并命名为 gdp
gdp = pd.read_excel(r"Province GDP 2017.xlsx")
# （2）检测是否存在重复记录
# （3）删除重复记录
# （4）按照 GDP 从高到低排序
gdp_sort = gdp.sort_values(by = 'GDP',ascending= False)
# （5）提取 GDP 前 5 名省份
gdp_top5 = gdp_sort.iloc[:5,:]
# （6）新增人均 GDP 列 per_gdp，计算 GDP / Population
gdp['per_gdp'] = gdp['GDP']/gdp['Population']
# （7）使用 seaborn 绘制前 5 名 GDP 水平柱状图
import seaborn as sns
import matplotlib.pyplot as plt
sns.barplot(data=gdp_top5,x='GDP',y='Population')
# （8）给图形添加标题并显示图形
plt.title('GDP per capita')
plt.show()


# （1）使用 np.random.randint 生成 10×15 成绩数组 score，取值范围为 60 到 100
import numpy as np
score = np.random.randint(60,101,size=(10,15))

# （2）使用切片提取奇数行、奇数列位置的数据，保存为 odd_score
odd_socre = score[0::2,0::2]
# （3）编写函数 myArr2(arr, rowList, colList)，返回指定行列交叉形成的新二维数组
def myArr2(arr,rowList,collist):
    return arr[np.ix_(rowList,collist)]
# （4）调用函数提取 rowList=[0,2,8] 与 colList=[1,4,9] 的数据
rowList = [0,2,8]
rowList = [1,4,9]
result = myArr2(score,rowList,rowList)
# （5）输出原数组、odd_score 和函数返回结果
print(result)
