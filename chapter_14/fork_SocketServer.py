# _*_ coding:utf-8 _*_
from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeerame()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

server = Server(('', 1234), Handler)
server.serve_forever()