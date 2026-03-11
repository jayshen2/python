import numpy as np
def myarr(start,end,row):
    if (end-start+1)%row != 0:
        print("输入有误")
        return None
    list1 = list(range(start,end+1))
    list1.sort(reverse=True)
    arr = np.array(list1)
    Arr = arr.reshape((row,int((end -start+1)//row)))
    print(Arr)

myarr(11,60,5)

arr5 = np.random.randint(100,201,size=(10,15))
arr6 = arr5[0::2,1::2]
print(arr5[[1,2,6],[3,11,14]])
print(arr5[np.ix_([1,2,6],[3,11,14])])
print(arr6)
def myarr2(arr,rowlist,collist):
    return arr[np.ix_(rowlist,collist)]
row = [0,2,8]
col = [3,7,11]
arr7 = myarr2(arr5,row,col)
print(arr7)