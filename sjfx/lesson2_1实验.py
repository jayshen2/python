import numpy as np
arr1 = np.random.randn(15).reshape(3,5)*10
arrfloat,arrint = np.modf(arr1)
arr3 = np.where(arr1>0,arrint,arrfloat)
arr4 = arr3.astype(str)
arrB = np.random.choice()
print(arrB)