import pandas as pd
import numpy as np

book = pd.read_csv('book_sale1.csv')
print(book)

book['时间'] = pd.to_datetime(book['时间'])
book['月份'] = book['时间'].dt.month


book_maxmin = book.groupby(by=['三级类目','月份'])['平均停留时长(秒)']
book_new = book.groupby(by=['三级类目','月份']).agg(
    总浏览量=('浏览量', 'sum'),
    访客量方差 = ('访客量','var'),
    停留时间极差 = ('平均停留时长(秒)',lambda x:x.max()-x.min()),
    平均成交量 = ('成交商品件数','mean')
)
print(book_new)

def get_period(date):
    if date <= 10:
        return '上旬'
    elif date <= 20:
        return '中旬'
    else:
        return '下旬'
book['旬'] = book['月份'].apply(get_period)
book_pivo = pd.pivot_table(
    book,
    index = ['月份','旬'],
    columns = '三级类目',
    values = '浏览量',
    aggfunc = sum,
    margins = True
)
print(book_pivo)

book_new = book.dropna(subset=['三级类目','首次入库时间'])
print(book_new)
book['首次入库时间'] = pd.to_datetime(book['首次入库时间'])
book['首次月份'] = book['首次入库时间'].dt.month
book_cross = pd.crosstab(
     index = book['三级类目'],
    columns = book['首次月份']
)
print(book_cross)