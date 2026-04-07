import numpy as np
import pandas as pd

# 数据读入data_test03.xlsx
df = pd.read_excel('data/data_test03.xlsx')
print(df.head())

# 各变量数据类型
print(df.dtypes)

# 将birthday变量转换为日期型
df["birthday"]= pd.to_datetime(df["birthday"],format='%Y/%m/%d')

print(df.head())

# 将start_work转换为日期型
#df["start_work"] = pd.to_datetime(df["start_work"],format='%Y%m%d')
print(df.head())

# 新增年龄和工龄两列
df["年龄"] = pd.Timestamp.today().year - df["birthday"].dt.year
df["工龄"] = pd.Timestamp.today().year - df["start_work"].dt.year

# 手机号转化为字符串
df["tel"] =  df["tel"].astype(str)

# 手机号中间四位隐藏起来
df["tel"] = df["tel"].map(lambda x : x.replace(x[4:8],"****"))

# 取出邮箱的域名
df["域名"] = df["email"].map(lambda x : x.split("@")[0])

# 取出birthday、start_work、other变量
df = df.drop(columns=['birthday','start_work','other'])