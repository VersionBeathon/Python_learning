# _*_ coding:utf-8 _*_
''' 为了检查一个值是否在序列中，使用in运算符，这个运算符检查某个条件是否为真，然后返回相应的值
条件为真返回True，条件为假返回False。这样的运算叫做布尔运算符，返回的值叫做布尔值 '''
permissions = 'rw'
print 'w' in permissions
print 'x' in permissions
users = ['milh', 'foo', 'bar']
print raw_input('Enter your user name: ') in users
subject = '$$$ Get rich now!!! $$$'
print '$$$' in subject
