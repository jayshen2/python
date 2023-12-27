s=''
a = input("请尽情敲键盘输入吧：")
for i in range(0,len(a)):
    if "a" <=a[i] <"z" and a[i]!="s":
        s+=a[i]+"  "
print(f"您输入的非s小写字母依次为{s}")