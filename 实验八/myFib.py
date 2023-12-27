def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = eval(input("请输入正确n："))
print(f"第{n}个斐波那契数为：{fib(n)}")