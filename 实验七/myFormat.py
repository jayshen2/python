import math

x = math.pi
y = 100000*math.tau
z = math.e
print("format顺序匹配：x={:-^11.3f},y={:0<12,.2f},z={:*>+13,.5f}".format(x, y, z))
print("format索引匹配：x={0:-^11.3f},y={1:0<12,.2f},z={2:*>+13,.5f}".format(x, y, z))
print("format关键字匹配：x={a:-^11.3f},y={b:0<12,.2f},z={c:*>+13,.5f}".format(a=x, b=y, c=z))
print(f"f-string字面量方法x={x:-^11.3f},y={y:0<12,.2f},z={z:*>+13.5f}")
print("%%格式化方法x=%.3f,y=%.2f,z=%.5f"%(x,y,z))
