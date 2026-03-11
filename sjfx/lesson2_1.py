import numpy as np
arr = np.arange(10)
#print(arr>10)  #比较+-*/本质上就是通用函数
#np.sqrt 开根号

arr1 = np.random.randn(8).reshape((4,2))

arr2 = np.random.randn(8)*5
arr3 = np.random.randn(8)
#print(np.maximum(arr2,arr2))

float1,int1 = np.modf(arr2)
#print(int1) #取整数
#print(float1)#取小数

import matplotlib.pyplot as plt
points = np.arange(-10,10,0.01) #start end step
x, y = np.meshgrid(points,points)
z = np.sqrt(x**2 + y**2)
plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.show()
#思考题：中心白到外围黑色


xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
"""
result = [(x if c else y) 
          for x, y, c in zip(xarr, yarr, cond)]
"""
#comd标记为TURE返回xarr中对应位置的值，是FLASE范围yarr中对应的值
result = np.where(cond,xarr,yarr)
print(result)

arr2 = np.random.randn(18).reshape((3,6))*10
print(arr2)
#print(np.where(arr2>0, 2,-2)) #正值返回2，负值返回-2
# np.where(cond,x,y)满足cond返回x，不满足返回y
# cond x y 需要数组不需要满足相同大小,可以接受标量值和数组（condespape相同）   通用函数特点：广播
#print(np.where(arr2>0, 2,arr2))
print(np.where(arr2>0,np.modf(arr2)[1],np.modf(arr2)[0]))