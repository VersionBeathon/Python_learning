# _*_ coding:utf-8 _*_
import socket

s = socket.socket()

host = socket.gethostname()     # 获取主机名
port = 1234                     # 定义接口

s.connect((host, port))         # 使用connect方法连接到服务器
print s.recv(1024)              # 调用recv来接收数据