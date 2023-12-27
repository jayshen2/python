# 利用列表推导式找出所有可能的公鸡、母鸡、小鸡数量组合
a = [(x, y, z) for x in range(0, 21) for y in range(0, 34) for z in range(0, 101) if 5 * x + 3 * y + z / 3 == 100 and x + y + z == 100]
for i in a:
    print(f"公鸡{i[0]} 母鸡{i[1]} 小鸡{i[2]}")
