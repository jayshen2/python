import pandas as pd
import numpy as np
# 读取数据时绝对路径和相对路径问题

# 1.在同一个目录下
df = pd.read_csv("diamonds.csv")
print(df.head())

# 2.指明数据所在位置
df = pd.read_csv(r"data/diamonds.csv")
# 备注:斜杠为反斜杠/

df_excel = pd.read_excel(r"data/data_test02.xlsx",header=None,names=['a','b','c','d'])
print(df_excel.head())