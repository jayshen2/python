m = input("").split(";")

c = {a:m.count(a) for a in m}
print(c)

max_num = max(c.values())
m_max = [mm for mm,num in c.items() if num==max_num]
print(m_max)