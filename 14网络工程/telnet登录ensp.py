import telnetlib3
import time

# 交换机的IP地址、用户名和密码
HOST = "10.0.12.1"
USER = "huawei"
PASSWORD = "huawei123"

try:
    # 建立Telnet连接
    tn = telnetlib3.Telnet(HOST)

    # 输入用户名
    tn.read_until(b"Username: ")
    tn.write(USER.encode('ascii') + b"\n")

    # 输入密码
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode('ascii') + b"\n")

    # 登录成功，执行命令
    tn.write(b"dis cu\n")
    time.sleep(1)
    output = tn.read_very_eager().decode('ascii')

    print(output)

    # 关闭连接
    tn.write(b"exit\n")
    tn.close()

except Exception as e:
    print(f"Login failed: {e}")