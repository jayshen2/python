import pandas as pd
import numpy as np

frame = pd.DataFrame({'b':[4,1,-5,2],"a":[3,2,3.4,1],'c':[-2,2,1,4]})
print(frame)
# 默认是axis = 0 遍历所有行位置，列不变
frame.rank(method="min")
print(frame.rank(method="min"))
print(pd.Timestamp.today().year)