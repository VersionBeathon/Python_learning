# _*_ coding:utf-8 _*_
import socket, select

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

fdmap = {s.fileno(): s} # 获取文件操作符 创建字典映射

s.listen(5)
p = select.poll()
p.register(s)

while True:
    events = p.poll()
    for fd, event in event:
        if fd = s.fileno():
            c, addr = s.accept()
            print 'Got connection from ', addr
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data: # 没有数据——关闭链接
                print fdmap[fd].getpeername(), 'disconnected'
                p.unregister(fd)
                del fdmap[fd]
            else:
                print data