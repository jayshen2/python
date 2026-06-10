import numpy as np
import pandas as pd 


df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'], 
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})

people = pd.DataFrame(np.random.randn(5, 5),columns=['a', 'b', 'c', 'd', 'e'], 
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
stock = pd.read_csv(r"stock_px.csv")
tips = pd.read_csv(r"tips.csv")

# 可以对数据框分组，也可以对某个变量，分组可以设置为变量
g1 = df['data1'].groupby(df['key1']).mean()

# 分组时，groupby设置某个变量
g2 = df.groupby(by = 'key1').mean(numeric_only=True)
# by =[k1,k2] 两个变量以上的分组，把各自取值进行全部组合
# a,one a.two b.one b.two ,如果组合没有值，则直接不显示 【考】
g3 = df.groupby(by = ['key1','key2']).mean()
g3 = df.groupby(by = ['key1','key2']).mean()


# 设置字典 对分组进行重构
# abcd原始数据，不会改变数据的原始结果，按照设定的匹配进行分组
p1 = people.groupby(people.index).count()
mapping = {"a":"python","b":"math","c":"english","d":"web","e":"data"}
maps = pd.Series(mapping)
p2 = people.groupby(mapping).sum()

# 设置函数进行分组
# len()求字符串长度
p3 = people.groupby(len).sum()
keylist = ["one","one","one","two","two"]
p4 = people.groupby([len,keylist]).sum()

# 函数的聚合:在分组后直接函数计算
# quantile :计算样本分位数，sum mean median std
p5 = df.groupby("key1").quantile(0.75,numeric_only=True)
# 复杂的函数聚合：def + agg(def) 再传递给分左右
def maxmin(arr):
    return arr.max() - arr.min()
# 自定义函数（没有结果groupby优化的函数）无法直接进行分组聚合
p6 = df.groupby("key1")[['data1','data2']].agg(maxmin)
p7 = df.groupby("key1")[['data1','data2']].agg("mean")

# 计算小费占总消费的比例
tips["pct"] = tips["tip"] / tips["total_bill"]
pctmean = tips.groupby(["smoker","day"])['pct'].mean()

# 要计算多个函数值
# 在agg中传递一个列表
t1 = tips.groupby(["smoker","day"])['pct'].agg(["mean","std",maxmin])
# 设置元组
t2 = tips.groupby(["smoker","day"])['pct'].agg(("mean","std",maxmin))
# 列表+二元元组(“名称，具体函数)
t3 = tips.groupby(["smoker","day"])['pct'].agg([("平均数","mean"),
                                                ("极差",maxmin)])

# 字典{“变量”：要对该变量执行的函数}
dict1 = {"size":"sum","tip":np.max,"total_bill":maxmin}
t4 = tips.groupby(["smoker","day"]).agg(dict1)

# 分组后，分组变量默认设置index
# groupby(as_index=False) 分组变量不转化为index常用
t4 = tips.groupby(['smoker',"day"],as_index = False).agg(dict1)

# agg 类似 apply：按照分组对拆分后的多个片段数据使用调用函数
# 前5 消费情况sort_values?

def topk(df,k=5,column = "pct"):
    df.sort_values(column,ascending = False)[:k]
    
# t51 = tips.groupby("smoker").agg(topk)
t51 = tips.groupby("smoker").apply(topk)
t52 = tips.groupby("smoker").apply(topk,k = 3,column='tip')


# 数据运行的标准格式
# 行是个案 列是变量
#  数据透视表 交叉表 ： 行是变量，列也是变量

## pivot_table
# index 可以使用多个列表添加分组的变量 == 哪些变量作为行变量
# values 指定哪些变量作为列变量
# aggfunc 设置聚合的犯法
b1 = pd.pivot_table(tips,index=["smoker","sex"],values=['total_bill','tip'],aggfunc=sum)

# margins 分类总计
b2 = pd.pivot_table(tips,index=['smoker',"sex"],
                    values=['total_bill','tip'],
                    margins=True,
                    aggfunc=sum)
print(b2)

# 交叉表 按照分组中的值统计分组的计数
b3 = pd.crosstab(index = [tips['day'],tips['time']],columns=[tips["smoker"],tips['sex']])
print(b3)



