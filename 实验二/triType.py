num = input("请输入三个正整数，逗号隔开：")
a, b, c = map(int, num.split('，'))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print(f"边长{a},{b},{c}可以组成等边三角形")
    elif a==b or a==c or b==c:
        print(f"边长{a},{b},{c}可以组成等腰三角形")

    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print(f"边长{a},{b},{c}可以组成直角三角形")
    else:
        print(f"边长{a},{b},{c}可以组成三角形")
else:
    print(f"边长{a},{b},{c}不能组成三角形")