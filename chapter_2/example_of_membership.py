# _*_ coding:utf-8 _*_
#检查用户名和PIN密码
database = [
        ['albert',  '1234']
        ['dilbert', '4242']
        ['smith',   '7524']
        ['jones',   '9843']
]
username = raw_input('User name: ')
pin = raw_input('PIN code: ')

if[username,pin] in database: print 'Access granted'
# 测试