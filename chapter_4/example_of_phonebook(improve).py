# _*_ coding:utf-8 _*_
# 使用get()的简单数据库
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9120',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = raw_input('Name: ')

# 查找电话号码还是地址？
request = raw_input('Phone number (p) or address (a)? ')
# 使用正确的键
key = request  # 如果请求既不是'p'也不是'a'
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
# 使用get()提供默认值
person = people.get(name, {})
labels = labels.get(key, key)
result = person.get(key, 'not available')

print "%s's %s is %s." % (name, labels, result)
