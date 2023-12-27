def aa(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s

def bb(n):
    if n == 1:
        return 1
    return n+bb(n-1)

n = int(input(""))
print(aa(n))
print(bb(n))


#-----妈的还要用斐波那契数列，666666
def dd(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return dd(n-1)+dd(n-2)
n = int(input(""))
print(dd(n))

def ee(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
print(ee(n))

#一个21行一个15行，我看看是什么试卷可以写这么多行，你是人啊自己写得出来吗