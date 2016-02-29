# _*_ coding:utf-8 _*_
# 多态和方法
# 绑定到对象特性上面的函数称为方法(method)。例如：字符串、列表和字典方法
print 'abc'.count('a')
print[1, 2, 'a'].count('a')
# 标准库random中包含choice函数，随机选出元素
from random import choice
x = choice(['Hello, world !', [1, 2, 3, 4, 'e', 'e', '4']])
print x.count('e')
# 关键点不在于检测类型：只需要知道x有个叫做count的方法。带有一个字符作为参数，并且返回参数值就够了。

# 多态的多种形式


def add(x, y):
    return x + y
print add(1, 2)
print add('Fish', 'license')

#打印对象长度函数
def length_message(x):
    print "The length of", repr(x), "is", len(x)
#repr函数时多态特性的代表之一
length_message('fnord')
length_message([1, 2, 3])
# 注:很多函数和运算符都是多态的，唯一能够毁掉多态的就是使用函数显式地检查类型
