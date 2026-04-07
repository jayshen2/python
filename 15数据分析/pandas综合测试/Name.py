import pandas as pd
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

#创建DataFrame
#将上述的DataFrame分别命名为data1, data2, data3
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

#将data1和data2两个数据框按照行的维度进行合并，命名为all_data
all_data = pd.concat([data1,data2],axis=0,keys=['data1','data2'])
all_data1 = pd.merge(data1,data2,how='outer')
print(all_data)

#将data1和data2两个数据框按照列的维度进行合并，命名为all_data_col
all_data_col = pd.concat([data1,data2],axis=1)
print(all_data_col)

#按照subject_id的值对all_data和data3作合并
data4 = pd.merge(all_data,data3,on='subject_id',how='outer')
print(data4)

#对data1和data2按照subject_id作内连接
data5 = pd.merge(data1,data2,on='subject_id',how='outer')
# pandas同时参赛的人有几个，且到处对应名单
# 找到data1 和 data合并后所有匹配的结构
all_data = pd.merge(data1,data2,how="inner")
all_data1 = pd.concat([data1,data2],join='inner')
print(all_data)
print(all_data1)