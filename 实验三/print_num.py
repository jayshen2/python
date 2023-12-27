a = eval(input("请输入一个正整数"))
for i in range(1,a+1):
    print("{:<5}".format(i),end=" ")
    if i%10 == 0:
        print()