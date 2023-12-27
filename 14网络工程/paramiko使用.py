import time
import paramiko

username = input("username=:")
password = input("password=:")
host = "10.0.12.1"

ssh_client = paramiko.SSHClient()  # 开启命令行
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # 自动添加主机名及主机密钥到本地HostKeys
# 对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
ssh_client.connect(hostname=host, username=username, password=password, allow_agent=False, look_for_keys=False)
# 连接SSH服务端，以用户名和密码进行认证 ，调用connect方法连接服务器
print("已经连接到", host)
remote_connection = ssh_client.invoke_shell()
remote_connection.send("screen-length 0 temporary\n")  #输出不分屏
time.sleep(1)
remote_connection.send("system\n")
remote_connection.send("dis cu\n")
time.sleep(1)
output = remote_connection.recv(65535)
print(output.decode('ascii'))
ssh_client.close()