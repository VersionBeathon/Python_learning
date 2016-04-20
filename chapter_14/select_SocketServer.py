# _*_ coding:utf-8 _*_

import socket
import select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, por))

s.listen(5)

inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print 'Got connection from ', addr
            inputs.append(c)
        else:
            try:
                data = r.rev(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print r.getpeername(), 'disconnected'
                iputs.remove(r)
            else:
                print data