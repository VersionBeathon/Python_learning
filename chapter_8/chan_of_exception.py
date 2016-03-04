# _*_ coding:utf-8 _*_
# 使用if/else语句


def describePerson(person):
    print 'Description of', person['name']
    print 'Age:', person['age']
    if 'occupation' in person:
        print 'Occupation:', person['occupation']
test = {'name': 'Bob', 'age': '42'}
describePerson(test)
test = {'name': 'Bob', 'age': '42', 'occupation': 'camper'}
describePerson(test)
# 此段代码效率不高。程序会两次打印'occupation'键，其中一次用来查看键是否存在

# 使用try/except


def describePerson1(person):
    print 'Description of', person['name']
    print 'Age:', person['age']
    try:
        print 'Occupation:' + person['occupation']
    except KeyError: pass
test = {'name': 'Bob', 'age': '42'}
describePerson1(test)
test = {'name': 'Bob', 'age': '42', 'occupation': 'camper'}
describePerson1(test)

# 检查对象是否存在特定特性时，也可用try/except
'''伪代码
try:
    obj.write
except AttributeError:
    print 'The object is not writeable'
else:
    print 'The object is writeable'
'''

# 很多情况下，使用try/except语句比使用if/else会更自然（更'Python化'）
# 养成尽可能使用try/except语句的习惯