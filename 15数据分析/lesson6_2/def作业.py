# 异常值：个别数值和大部分数值偏离较大
# 异常值检测IQR
# 计算Q1和Q3 计算IQR = Q3-Q1  确定异常值便捷：[Q1-1.5*IQR.]
# 遇到异常值常见办法：删除，大数据前提下，异常值需要单独取出来进行研究
import pandas as pd
import numpy as np
data = np.array([2,4,6,18,21,3,45,1,8,32,45])
def IQR(data):
    data = np.sort(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    for i in data:
        if i > q3+1.5*iqr:
            print("超过上界异常值:",i)
        if i < q1-1.5*iqr:
            print("超过下界异常值:", i)

