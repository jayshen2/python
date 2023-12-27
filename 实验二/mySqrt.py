import math
import cmath
a = eval(input("请输入任一个实数："))
if a>=0:  #判断是否大于零
    print(f"{a}的平方根为：{math.sqrt(a)}")
else:
    print(f"{a}的平方根为：{cmath.sqrt(a)}")