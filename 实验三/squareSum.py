a = 1
s = 0
while True:
    for i in range(1,a+1):
        s+=i**2
    print(f"当a={a}时，s={s}")
    if s > 1000:
        print(f"故和小于1000的最大项n是{a-1},此时的平方和是{s-i**2}")
        break
    a+=1
    s=0