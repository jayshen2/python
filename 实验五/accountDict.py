print("-"*30+"(1)"+"-"*30)
accountDict = dict((["user1","pw1"],["user2","pw2"],["user3","pw3"],
                    ["user4","pw4"],["user5","pw5"],["user6","pw6"],["user7","pw7"],["user8","pw8"],["user9","pw9"]))
print(accountDict)

print("-"*30+"(2)"+"-"*30)
accountDict.pop("user9")
print(list(accountDict.keys()))

print("-"*30+"(3)"+"-"*30)
accountDict.popitem()
accountDict.popitem()
accountDict.popitem()
accountDict.popitem()
for v in accountDict.values():
    print(v,end=' ')
print()

print("-"*30+"(4)"+"-"*30)
del accountDict["user4"]
for item in accountDict.items():
    print(item,end=' ')
print()

print("-"*30+"(5)"+"-"*30)
accountDict.get("user4","未知")
print(accountDict)

print("-"*30+"(6)"+"-"*30)
accountDict.setdefault('user4',"pw4")
print(accountDict)

print("-"*30+"(7)"+"-"*30)
d1={"user4":"bacd","admin":"dataScience"}
accountDict.update(d1)
print(accountDict)