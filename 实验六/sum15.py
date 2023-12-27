import random
numList = [random.randint(1,20) for i in range(10)]
a = {(i,j) for i in numList for j in numList if i+j==15 if i>j }
print(a)
