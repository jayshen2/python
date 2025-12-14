a = input("").split(";")
dw = {i:a.count(i) for i in a}
print(dw)
max_dw = [i for i,j in dw.items() if j==max(dw.values())]
print(max_dw)