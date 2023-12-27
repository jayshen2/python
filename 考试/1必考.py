for i in range (1,10):
    for k in range (1,i):
      print(" "*8,end='')
    for j in range (i,10):
        print(f"{j}*{i}={i*j}\t",end='')
    print()

#下for i in range(1,i+1)
#上for i in range(i,10)
#左不动
#右加下 for k in range(i,10)
#          print(' '*8,end='')
#右加上 for k in range(1,i)z
#          print(' '*8,end='')