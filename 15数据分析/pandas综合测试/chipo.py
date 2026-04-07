import numpy as np
import pandas as pd

#将数据集存入一个名为chipo的数据框内
chipo = pd.read_csv(r'pandas/5-Chipotle/chipotle.csv')

#查看前10行内容
print(chipo.head(10))

#数据集中有多少个列(columns)？
print(chipo.shape[1])

#打印出全部的列名称
print(chipo.columns)

#被下单数最多商品(item)是什么?
choice_count = chipo['item_name'].value_counts()
print(choice_count)

#在choice_description中，下单次数最多的商品是什么？
choice_max = chipo['choice_description'].value_counts()
print(choice_count)

#一共有多少商品被下单？
chipo_sum = chipo['quantity'].sum
print(chipo_sum)

#在该数据集对应的时期内，收入(revenue)是多少？
item_price = chipo['item_price'].astype(str).str.replace("$",'').astype(float)
revenue = (item_price * chipo['quantity']).sum()
print(revenue)