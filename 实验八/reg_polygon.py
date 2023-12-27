import math
def reg_polygon(n,a):
    """
reg_polygon(n: int, a: float) -> tuple
    本函数用于返回边长为a的正n边形的内角度数与面积
    """
    c = (n-2)*180/n
    cot = 1/math.tan(math.pi/n)
    s = (n*a**2/4)*cot
    return c,s
print(help(reg_polygon))
print(reg_polygon(3,6))
print(reg_polygon(4,6))
print(reg_polygon(5,6))
print(reg_polygon(6,1.5))