import time
import paramiko

username = input("username=:")
password = input("password=:")
f = open("E:/ip_add.txt")
for line in f.readlines():
    ip_address = line.strip()
    ssh_client = paramiko.SSHClient()  # 开启命令行
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # 自动添加主机名及主机密钥到本地HostKeys
    # 对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
    ssh_client.connect(hostname=ip_address, username=username, password=password, allow_agent=False, look_for_keys=False)
    # 连接SSH服务端，以用户名和密码进行认证 ，调用connect方法连接服务器
    print("已经连接到", ip_address)
    command = ssh_client.invoke_shell()
    command.send("ftp 192.168.56.1\n")
    time.sleep(1)
    command.send("python\n")
    time.sleep(1)
    command.send("python\n")
    time.sleep(1)
    command.send("bin\n")
    command.send("put vrpcfg.zip " + ip_address + '_vrfcfg.zip' + '\n')
    time.sleep(1)
    command.send("quit\n")
    time.sleep(2)
    output = command.recv(65535)
    print(output.decode("GB2312"))

f.close()
ssh_client.close()
time.sleep(10000)
