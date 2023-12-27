# 调用python内置函数isinstance判断是否为迭代器，需用到collections库
from collections.abc import Iterable
print(isinstance([],Iterable))

#可以通过iter()函数从迭代对象生成迭代器
a = [65,87,21,38]
v = iter(a)
print(v)
v.__next__()#返回下一个值
next(v)#通过内置函数访问下一个值

"""
1.enumerate(iterable,start=0),构建迭代对象，每个元素为一个元组
每个元组两个元素，前一个为索引下表值，默认从零开始
后一个元素为可迭代对象iterable中的相应元素
"""
a = ["a","b","c","d"]
e = enumerate(a)
print(e.__next__())
a1 = list(e)
print(a1)
