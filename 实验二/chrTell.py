a =input("请输入一个字符")
if "a"<=a<="z":
    print("您输入的是小写字母")
elif "A"<=a<="Z":
    print("您输入的是大写字母")
elif "0"<=a<="9":
    print("您输入的是数字")
else:
    print("您输入的是其他字符")

match a :
    case a if "a" <= a <= "z":
        print("您输入的是小写字母")
    case a if "A" <= a <= "Z":
        print("您输入的是大写字母")
    case a if "0" <= a <= "9":
        print("您输入的是数字")
    case _:
        print("您输入的是其他字符")
