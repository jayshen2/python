def is_prime(n):
    for i in range(2,n):
        if n==2:
            return True
        elif n%i==0:
            return False
    else:
        return True

def is_primes_within(n):
        a = []
        for i in range(2,n):
            if is_prime(i):
                a.append(i)
        return a

while True:
    try:
        n = input("请输入一个正整数")
        if n == "stop":
            break
        elif int(n) > 0:
            print(f"所有小于等于{n}的素数列表为{is_primes_within(eval(n))}")
        else:
            print("输入无效")
    except:
        print("输入无效")