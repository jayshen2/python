import numpy as np

arr = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6]])
#创建array（手动创建和自动创建

print(arr.ndim)   #维度
print(arr.shape)  #形状
#array的维度和形状

print(arr.dtype)
# array的数据类型 dtype astype()
# array运算（加减乘除比较）点对点的运算

print(arr[2])  #索引
print(arr[2:])
#n:m==n,...,m-1
# n:  == n到最后一个
# :n ==0,...,n-1
# n:m:k == 从n到m-1，步长设置为k
# :表示全部索引
# 数组的索引和切片（一维）

print(arr2[1]) #array[n] 取第n行
print(arr2[1][2]) #取array[i][j] 取第i行第j列
print(arr2[1,2])

ones = np.ones((5,9))
print(ones.shape[1])  #取出第1列
print(ones)
for i in range(len(ones)):
    ones[i] = ones[i]*i
print(ones)
print(ones[:2,3:]) #行数0到1，列数3到最后
#二维数组的切片和索引 超过索引范围会报错，不能使用（）

arr_copy = arr.copy()
arr[4]=9
print(arr)
print(arr_copy)
#修改和赋值,数组的索引修改后会直接传递到原始数据
#如果要保留原始数据 arr_copy = arr.copy()

names = np.array(["bob","lucy","hong"])
python = np.array([98,50,78])
math = np.array([60,70,80])
print(python[names == "bob"]) #只返回对应ture上的值，查询满足这个条件的值
print(names[python>60]) #这门课的及格名字
print(names[(python>60) & (math >70)])
print(names[(python>60) & (math >100)])  #没找到没有超过范围返回一个空值
# 布尔型索引，在[]内放入判断语句（生成出一个对应的布尔值的数组）
# 把true对应位置的值返回
# arr[condion] 返回满足condion的arr中的值
# condion产生了一个TRUE和False的数组（列表），返回ture对应的位置

arr = np.arange(64).reshape(8,8)
print(arr)
#arr = np.array(k).reshape(m,n)  m*n=k
#重构

print(ones[[1,2,3]])
print(ones[[1,4,2,3]]) #先选取第1行，再选取第4行
#选取指定的（无规则）位置，这些位置参数需要用另外一个[]括起来
#【考】给出数组的索引和切片 问结果

arr = np.arange(15).reshape(3,5)
arr1 = np.arange(15).reshape(5,3)
# print(arr)
print(arr.T.shape) #转置
print(np.dot(arr,arr1)) #数组的内积
# print(arr)