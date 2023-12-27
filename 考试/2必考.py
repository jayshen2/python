print("输入内容 输出内容")
while True:
    a = eval(input(""))
    print(a, end='')
    name = a[0]
    days = a[1:]
    avg = sum(days) / len(days)
    match avg:
        case a if a >= 28:
            s = "全勤模范"
        case a if 25 <= a < 28:
            s = "优秀考勤"
        case a if 22 <= a < 25:
            s = "达标考勤"
        case _:
            s = "考勤待改进"

    # 输出结果
    print(f"{name}{s}")
