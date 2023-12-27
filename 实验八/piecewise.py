import math
def f(x):
    if x<0:
        x = math.sqrt(x*-1)
        print(x)
    elif 0<=x<2:
        e = math.e
        x = e**x+1
        print(x)
    else:
        x = 3*x
        print(x)

f(0)
f(2)
f(-9)
f(-1.21)
f(1)
f(4)
f(10/3)