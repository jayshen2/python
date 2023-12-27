n = 7
num = 0
while True:
    num+=1
    a = eval(input("快来猜一猜我写的是什么数（0~9）"))
    if a >n:
        print("大了")
    elif a<n:
        print("小了")
    else:
        print(f"恭喜你猜中了！共猜了{num}次")
        break