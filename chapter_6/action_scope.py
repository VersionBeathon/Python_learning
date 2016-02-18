# _*_ coding:utf-8 _*_
x = 1  # 变量和所对应的值用的是个“不可见”的字典
scope = vars()  # 内建vars函数可以返回x的值
print scope['x']
scope['x'] += 1
print x

# 这类不可见字典叫做命名空间或者作用域，每个函数调用都会创建一个新的作用域：


def foo():
    x = 42
x = 1
foo()
print x
# 函数内个变量被称为局部变量（local variable）参数的工作原理类似于局部变量


def output(x):
    print x
x = 1
y = 2
output(y)
output(x)
# 在函数内部访问全局变量,引用全局变量是很多错误引发原因，慎重使用全局变量


def combine(parameter):
    print parameter + external
external = 'berry'
combine('Shrub')
# 如果局部变量或者参数的名字和想要访问的全局变量名相同的话，就不能直接访问。全局变量会被局部变量屏蔽
# 可使用globals函数获取全局变量值


def combine_1(parameter):
    print parameter + globals()['parameter']
parameter = 'berry'
combine_1('Shrub')
# 重绑定全局变量。将局部变量变为全局变量
x = 1


def change_global():
    global x
    x += 1
change_global()
print x