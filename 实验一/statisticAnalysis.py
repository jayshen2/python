# count = 0 #计算总和
# num = 0  #计算个数
# a = input("请输入3位同学的成绩，以逗号分隔：")
# a = a.split(",") #根据逗号分隔成列表
# for i in range(len(a)): #循环列表个数
#     count = count+eval(a[i]) #计算去掉引号并计算总和
#     num+=1
# print("平均成绩为:",count/num)
# print("最高分是:",float(max(a))) #使用max函数计算最大
# print("最低分是:",float(min(a))) #使用min函数计算最小
# #202524084029郭沅森


a=eval(input("请输入成绩"))
b=eval(input("请输入成绩"))
c=eval(input("请输入成绩"))
print("平均分为",(a+b+c)/3)
print("最高分",max(a,b,c))
print("最低分",min(a,b,c))