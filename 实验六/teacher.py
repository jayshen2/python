pq = {"小张", "小邱", "小肖", "小赵"}
ymq = {"小刘", "小赵", "小胡", "小曾", "小潘"}
print(f"既是排球又是羽毛球{pq & ymq}")
print(f"是排球不是羽毛球{pq - ymq}")
print(f"小潘是排球俱乐部的吗{"是" if "小潘" in pq else "不是"}")
print(f"只参加一个俱乐部的{(pq - ymq) | (ymq - pq)}")
print(f"共有{len(pq|ymq)}分别是{pq|ymq}")
