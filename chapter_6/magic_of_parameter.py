# _*_ coding:utf-8 _*_
# 字符串（以及数字和元组）是不可变的，即无法被修改（只能用新值覆盖）


def try_to_change(n):
    n = 'Mr. Gumby'
name = 'Mrs. Entity'
try_to_change(name)
print name

name = 'Mrs. Entity'
n = name
n = 'Mr. Gumby'
print name

# 列表可修改：当两个变量同时引用一个列表的时候，它们同时引用一个列表


def change(n):
    n[0] = 'Mr. Gumby'
names = ['Mrs. Entity', 'Mrs. Thing']
change(names)
print names

names = ['Mrs. Entity', 'Mrs. Thing']
n = names
n[0] = 'Mr. Gumby'
print names

# 一个修改参数的例子
storge = {}
storge['first'] = {}
storge['middle'] = {}
storge['last'] = {}
me = 'Magrus Lie Hetland'
storge['first']['Magrus'] = [me]
storge['middle']['Lie'] = [me]
storge['last']['Hetland'] = [me]
print storge
print storge['middle']['Lie']  # 获得所有注册的中间名为lie的人
# 添加一个sister
my_sister = 'Anne Lie Hetland'
storge['first'].setdefault('Anne', []).append(my_sister)
storge['middle'].setdefault('Lie', []).append(my_sister)
storge['last'].setdefault('Hetlan', []).append(my_sister)
# 通过字典方法setdefault添加姓名，通过列表append方法添加sister
print storge
print storge['middle']['Lie']  # 获得所有注册的中间名为lie的人

# 通过抽象的方法实现该功能
# 初始化


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
storge = {}
init(storge)
print storge
# 获取名字函数


def lookup(data, label, name):
    return data[label].get(name)
# 添加名字函数


def store(data, full_name):
    names = full_name.split()  # 将名字分片
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
# test
Myname = {}
init(Myname)
store(Myname, 'Magnus Lie Hetland')
print lookup(Myname, 'middle', 'Lie')

# 在Python中函数只能修改参数对象本身。但是如果参数不可变，并没有任何办法修改


def inc(x):
    return x + 1
foo = 10
foo = inc(foo)
print foo

# 如果想改变参数可将值放置到列表中


def inct(x):
    return x[0] == x[0] + 1
foo = [10]
inct(foo)

# 关键字参数和默认值


def hello_1(greeting, name):
    print '%s, %s!' % (greeting, name)


def hello_2(name, greeting):
    print '%s, %s!' % (name, greeting)
hello_1('Hello', 'world')
hello_2('Hello', 'world')
# 当参数过多的时候可提供参数的名字赋值,这类参数叫做关键字参数
hello_1(greeting='hello', name='world')
hello_1(name='world', greeting='hello')

# 关键字参数可以再函数中给参数提供默认值


def hello_3(greeting='hello', name='world'):
    print '%s, %s!' % (greeting, name)
hello_3()
hello_3(name='Gumby')
