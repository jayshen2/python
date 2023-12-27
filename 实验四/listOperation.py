nameList=['韩信','吕布','孙尚香']
print(nameList)
nameList.insert(0,'兰陵王')
print(nameList)
nameList.extend(['鲁班','安琪拉','后裔'])
print(nameList)
nameList=sorted(nameList,key=len)
print(nameList)
name2=nameList[0:4]
print(name2)

n = len(nameList)
for i in range(n):
    print(f'{i}-{nameList[i]}')