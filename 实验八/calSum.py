def calSum(*args,**kwargs):
    if args:
        sum_1 = sum(i for i in args)
        print(f"Sum of Position parameters equal：{sum_1}")
    if kwargs:
        eq = sum(i**2 for i in kwargs.values())
        print(f"Quadratic：{eq}")

calSum(1,2,3,x=5,y=6)
calSum(2,3,a=1,b=2,c=3,d=4)
calSum(1,2)
calSum(z=1,k=2,l=3)
