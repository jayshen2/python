N=int(input("输入奇数"))
if N%2 == 1:
    for i in range(1,int((N+1)/2)+1):
        print(" "*(N-2-i)+"*"*(i*2-1))
    print()
else:
    print("输入错误")