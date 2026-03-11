import numpy as np
arr1 = np.random.randn(3,5)
arr2 = arr1*10
arrFloat, arrInt = np.modf(arr2)
arr3 = np.where(arr2>1,arrInt,arrFloat)
arr4 = arr3.astype(str)
arr8 = np.random.randint(0,2,size=(10))
arr8 = np.where(arr8==1,True,False)
print(arr8)

import numpy as np
def myArr(start,end,row):
    arr1 = np.arange(end,start-1,-1).reshape(row,(end-start+1)//row)
    return arr1
print(myArr(11,60,5))


arr5 = np.random.randint(100,201,size=(10,15))
arr6 = arr5[0::2,0::2]
print(arr6)

def myArr2(arr,rowList,colList):
    arr1 = arr[[rowList],[colList]]
    return arr1
print(myArr2(arr6,2,3))