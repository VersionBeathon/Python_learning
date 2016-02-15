# _*_ coding:utf-8 _*_
# 使用逗号输入
print 'Age', 42

print 1, 2, 3
print(1, 2, 3)

name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello'
print greeting, salutation, name
print greeting + ',', salutation, name

print 'hello,'
print 'world!'
# 把某件事作为另一件事导入
# 三种不同导入方法
# import somemodule 
# from somemodule import somefunction 
# from somemodule import somefunction, anotherfunction, yetanotherfunction

# 为整个模块提供别名
import math as foobar
print foobar.sqrt(4)
# 为函数提供别名
from math import sqrt as foobar
print foobar(4)
