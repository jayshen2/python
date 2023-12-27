a = 112233
for i in range(0,5):
    x = input()
    if len(x) == 6:
        if a == int(x):
            print("登陆成功")
        else:
            print("登陆失败")
    else:
        print("请输入6位纯数字密码")
else:
    print("账号临时锁定")







#---------------------第二种
# a = 1234
# for i in range(0,4):
#     x = input()
#     if '1'<= x <= '9':
#         if a == int(x):
#             print("验证通过")
#             break
#         else:
#             print("密码错误")
#     else:
#         print("验证码需为纯数字")
#         continue
# else:
#     print("验证失败，请重新获取验证码")