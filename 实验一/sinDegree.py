import math #导入计算库
a = eval(input("请输入度数")) #获取度数
print(f"sin{a}°={math.sin(math.radians(a))}")
#先将度数转换成弧度，然后再计算弧度正弦值
#202542084029郭沅森