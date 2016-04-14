#-*- coding: utf-8 -*-
import socket

s = socket.socket()

host = socket.gethostname() # 获取当前主机名
port = 1234                 # 定义接口
s.bind((host, port))        # 绑定主机名和接口

s.listen(5)                 # 监听，参数是服务器未处理的连接的长度（即允许排队等待的连接数目，这些连接在禁用之前等待）
while True:
    c, addr = s.accept()    # 接收客户端连接
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    c.close()