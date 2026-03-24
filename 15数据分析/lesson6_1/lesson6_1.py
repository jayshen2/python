import pandas as pd
import numpy as np

df = pd.read_excel(r'data/data_test02.xlsx')
print(df)

df1 = pd.read_excel(r'data/data_test02.xlsx',
                   header = None,
                   names = ['编号','产品','颜色','价格'])

df2 = pd.read_excel(r'data/data_test02.xlsx',
                   header = None,
                   names = ['编号','产品','颜色','价格'],
                   converters = {0:str,3:float})
# converters制定列更改数据类型
print(df2)

cars = pd.read_csv(r'data/sec_cars.csv')
print(cars.head())
print(cars.dtypes)
# print(df3.tail()) 显示后五行
print(cars['New_price'].str[:-1].astype('float')) #cars.New_price 仅支持英文

cars['New_price'] = cars['New_price'].str[:-1].astype('float')
print(cars.head())
cars['差价'] = cars['New_price']-cars["Sec_price"]
print(cars.head())
del cars['New_price']


# 描述性统计：统计变量最大，最小，均值，方差
print(cars.describe())

# 统计数据集中所有的品牌（Brand）分布：统计字符串出现的频次
fraq = cars['Brand'].value_counts()
fraq_rate = fraq/sum(fraq)  #cars.shape[0] #数据框大小返回几行几列’
print(fraq_rate)

# 把手机转化成百分比

# 默认保存时index（行索引）和header（列索引）
# columns 保存指定的列
cars.to_csv('data/out.csv',sep='&',index=False,header=False)


# 导入data_test03.xlsx
df = pd.read_excel(r'data/data_test03.xlsx')
print(df.head())
print(df.dtypes)
# pandas中关于时间类型的to——date_time
# birthday 转换为日期类型
df["birthday"] = pd.to_datetime(df["birthday"],format = '%Y/%m/%d')
print(df.dtypes)

# 增加工龄和年龄
df['年龄'] = pd.Timestamp.today().year - df["birthday"].dt.year
print(df)
df['工龄'] =pd.Timestamp.today().year - df['start_work'].dt.year
print(df)

# apply map 将电话中间四位转换为****
# lambda def

# 邮箱以@为界分离，提取邮箱名和域名
str1 = "zhangsan@qq.com"
print(df["email"].apply(lambda x:x.split("@")[1]))