# _*_ coding:-utf-8 _*_
# 一个基于SocketServer的小型服务器
from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):
    def handle(self):
        add = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

server = TCPServer(('', 1234), Handler)
server.serve_forever()