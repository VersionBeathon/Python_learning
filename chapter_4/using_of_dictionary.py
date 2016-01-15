# _*_ coding:utf-8 _*_
# 创建一个电话表,采用序列的方法
names = ['Alice', 'Beth', 'Bob', 'Cecil', 'Dee-Dee', 'Earl']
numbers = ['2341', '2455', '4567', '9999', '2345', '9876']
print numbers[names.index('Cecil')]

# 创建和使用字典
phonebook = {'Alice': '2341', 'Beth': '2455', 'Bob': '4567',
             'Cecil': '9999', 'Dee-Dee': '2345', 'Earl': '9876'}
# 字典由多个键及与其对应的值构成的键——值对组成。每个键和它的值之间用冒号 “ : ”隔开，项之间用逗号 “ , ”隔开
# 整个字典是由一堆大括号扣起来，空字典{}

# dict函数：通过其他映射（比如其它字典）或者（键、值）对的序列建立字典
items = [('names', 'Gumby'), ('age', 42)]
d = dict(items)
print d
print d['names']
# dict函数也可以通关键字参数来创建字典
d = dict(name='Gumby', age=42)
print d

# 基本字典操作
# len(d)返回d中项（键——值对）的数量；
# d[k]返回关联到键k上的值；
# d[k]=v将值v关联到键k上；
# del d[k]删除键为k的项；
# k in d检查d中是有含有键为k的项。
# 键类型：字典的键不一定为整型数据，键可以使任意的不可变烈性，比如浮点型、字符串或者元组
# 自动添加：即使键起初在字典中并不存在，也可为它赋值
# 成员资格： 表达式k in d查找的是键，而不是值

# x = []
# x[42] = 'Foobar'
# print x  # 列表无法赋值整型数据
x = {}
x[42] = 'Foobar' # 字典可以任意赋值
print x

# 字典的格式化字符串
print phonebook
print "Cecil'substitute phone number is %(Cecil)s." % phonebook

template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s<p>
</body>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print template % data