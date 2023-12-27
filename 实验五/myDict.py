database={"zhangsan":123,"lisi":345}
keys=eval(input("Please enter your name list:"))
values=eval(input("Please enter your phone list:"))
new = dict(zip(keys,values))
print(f"original database:{database}")
print(f"new database:{new}")
me={**database,**new}
print(f"merged database:{me}")