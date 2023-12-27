import math
m = int(input("m="))
Sum = 0
i = 2
while i <= m:
    Sum = Sum + math.sqrt(i)
    i +=2
print(Sum)