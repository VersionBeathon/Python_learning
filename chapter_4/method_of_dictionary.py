# _*_ coding:utf-8 _*_
# clear 方法清除字典中所有的项。这个是原地操作，所以无返回值
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print d
return_value = d.clear()
print return_value

# 第一种清除方法
x = {}
y = x
x['key'] = 'value'
print y
x = {}
# y = x
print y

# 第二种清空
x = {}
y = x
x['key'] = 'value'
print y
x.clear()
print y
# 第一种方法对y一点影响都没有，要想清空原始字典中所有元素，必须用clear方法

# copy方法
x = {'username': 'admin', 'machine': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machine'].remove('bar')
print y
print x
# 在副本中替换值的时候，原始字典不受影响，但是如果修改了某个值（原地修改而不是替换）原始字典也会改变
# 可采用deepcopy函数来避免这个问题
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c, '\n', dc

# fromkeys方法使用给定的键建立新的字典，每个键都对应一个默认的值None
a = {}.fromkeys(['name', 'age'])
print a
# 也可以用dict方法
a = dict.fromkeys(['name', 'age'])
print a
# 可以使用自定义默认值
a = dict.fromkeys(['name', 'age'], '(unknown)')
print a

# get方法是个更宽松的访问字典项的方法。
d = {}
# print d['name'] 试图访问字典中不存在的项会出错
print d.get('name')
# 而get不会
# get访问一个不存在的值时，没有任何异常，得到了None值，还可以自定义“默认”值，替换None
print d.get('name', 'N/A')
d['name'] = 'Eric'
print d.get('name')

# has_key方法可以检查字典中是否含有特定的键。相当于k in d。Python3.0中不包括这个函数
d = {}
print d.has_key('name')
d['name'] = 'Eric'
print d.has_key('name')

# items方法将字典所有的项以列表方式返回，列表中每一项都表示为（键， 值）对的形式
d = {'title': 'python web site', 'url': 'http://www.python.org', 'spam': 0}
print d.items()
# iteritems方法的作用大致相同，但是会返回一个迭代器（一个容器）对象而不是列表
it = d.iteritems()
# print it # 并不会返回
print list(it)
# 很多情况下使用iteritems会更高效

# key方法将字典中的键以列表形式返回，而iterkeys则返回针对键的迭代器
d = {'title': 'python web site', 'url': 'http://www.python.org', 'spam': 0}
print d.keys()
print list(d.iterkeys())

# pop方法用来获得对应于给定的值，然后将这个键——值对从字典中移除
d = {'x': 1, 'y': 2}
print d.pop('x')
print d

# popitem方法类似于list.pop（移除列表中的一个元素）
''' popitem弹出随机的项，因为字典并没有 “最后的元素”或者其他有关顺序的概念
若想一个接一个地移除并处理项，这个方法就非常有效 '''
d = {'title': 'python web site', 'url': 'http://www.python.org', 'spam': 0}
print d.popitem()
print d
# 字典中没有与append等价的方法。因为字典是无序的，类似于append（在列表末尾追加新的对象）的方法是没有任何意义的

# setdefault方法在某种程度上类似于get方法，能够获得与给定键相关联的值
# setdefault能在字典中不含有给定值键的情况下设定相应的键值
d = {}
print d.setdefault('name', 'N/A')
print d
{'name': 'N/A'}
d['name'] = 'Gumby'
print d.setdefault('name', 'N/A')
print d
d = {}
print d.setdefault('name')
print d

# update方法可以利用一个字典更新另一个字典
d = {
    'title': 'python web site',
    'url': 'http: // www.python.org',
    'change': 'Mar 14 22:09:15 MET 2008'
}
x = {'title': 'Python Language Website'}
d.update(x)
print d

# values和itervalues 一个返回列表，一个返回值的迭代器
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print d.values()
print list(d.itervalues())
