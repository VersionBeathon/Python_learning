# _*_ coding:utf-8 _*_
# pass语句
'''伪代码
if name == 'Ralph Auldus Melish':
    print 'Welcome!'
elif name == 'Enid':
    # 还没完……
elif name == 'Bill Gates':
    print 'Access Denied'
代码不会执行，因为Python中空代码是非法的。解决的办法就是在语句块中加上一个pass语句
if name == 'Ralph Auldus Melish':
    print 'Welcome!'
elif name == 'Enid':
    # 还没完……
    pass
elif name == 'Bill Gates':
    print 'Access Denied'
'''

# 使用del删除
scoundrel = {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
robin = scoundrel
print scoundrel
print robin
scoundrel = None
print robin
x = ['hello', 'world']
y = x
y[1] = 'Python'
print x
del x
print y
# x,y都指向同一个列表，但是删除x并不会影响y。删除的只是名称，而不是列表本身。

# exec 和 eval 执行和求值字符串
# exec
exec "print'Hello,world!'"
from math import sqrt
scope = {}
exec "sqrt = 1" in scope
print sqrt(4)
print scope['sqrt']

# eval(用于“求值”)是类似于exec的内建函数。eval会计算Python表达式，并且返回结果值
# 创建Python计算器
eval(raw_input("Enter an arithmetic expression: "))
