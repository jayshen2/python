import random
sortedList=[]
A,B,C,D = 0,0,0,0
for i in range(10):
    sortedList.append(random.randint(40,100))
print(sortedList)
sortedList1=sorted(sortedList,reverse=True)
print(sortedList1)
while True:
    a = eval(input("请输入成绩"))
    if a in sortedList1:
        print(sortedList1.index(a)+1)
    else:
        print("该成绩不在列表中")
        break
for i in sortedList1:
    if i >= 88:
        A+=1
    elif i >= 75:
        B+=1
    elif i >= 60:
        C+=1
    elif i >= 0:
        D+=1
print(f"等级A共{A}人，成绩由低至搞排序为{sortedList1[:A]}")
print(f"等级B共{B}人，成绩由低至搞排序为{sortedList1[A:A+B]}")
print(f"等级C共{C}人，成绩由低至搞排序为{sortedList1[A+B:A+B+C]}")
print(f"等级D共{D}人，成绩由低至搞排序为{sortedList1[A+B+C::]}")

print(f"{sortedList.index(min(sortedList))+1}号取得最低分{min(sortedList)}分")
print(f"{sortedList.index(max(sortedList))+1}号取得最高分{max(sortedList)}分")