# _*_ coding:utf-8 _*_
# 字符串格式化适用字符串格式化操作符，即百分号%来实现。
fromat = "Hello, %s. %s enough for ya?"
x = ('world', 'Hot')  # 一般情况下用元组
print fromat % x
# 如果使用列表或者其他的序列代替元组，那么序列会被解释为一个值。只有元组和字典可以格式化一个以上的值。
''' 格式化字符串的%s部分称为转换说明符（conversion specifier）, 他们标记了需要插入转换值的位置
s表示值会被格式化为字符串——如果不是字符串，则会用str将其转换为字符串。这个方法对大多数数值都有效'''
fromat = "Hello, %s. %s %%enough for ya?"  # 如果要在格式化字符串里包括百分号，那么必须使用%%
x = ('world', 'Hot')
print fromat % x
''' 如果要格式化实数（浮点数），可以使用f说明转换说明的字符，同时提供所需要的精度：
一个句点加上希望保留的小数位数。因为格式化转换说明符总是以表示类型的字符结束，所以精度应该放在类型字符前面 '''
format = "Pi with three decimals: %.3f"
from math import pi
print format % pi

# 模板字符串
''' string模板提供另为一种格式化值的方法：模板字符串。
它的工作方式类类似于很多UNXI Shell里的变量替换。
如下所示，substitute（代替、替换）这个模板方法会用传递进来的关键字参数foo替换字符串中的$foo'''
from string import Template  # 模板
s = Template('$x, glorious $x!')
print s.substitute(x='slurm')
# 如果替换字段是单词的一部分，那么参数名就必须用括号括起来，从而准确指明结尾
s = Template("It's ${x}tastic!")
print s.substitute(x='slurm')
# 可以使用$$插入美元符号
s = Template("Make $$ selling $x!")
print s.substitute(x='slurm')
# 除了关键字参数之外，还可以使用字典变量提供值/名称对
s = Template('A $thing must never $action')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print s.substitute(d)  # 方法safe_substitute不会因缺少或者不正确使用$而出错

# 如果右操作符是元组的话，则其中的每一个元素都会被单独格式化，每个值都需要一个对应的转换说明符
# 如果需要转换的元组作为表达式的一部分存在，那么必须将它用圆括号括起来
test = '%s plus %s equals %s'
x = 1, 1, 2
print test % x
print '%s plus %s equals %s' % (1, 1, 2)

# 基本字符串说明
# %字符：标记转换说明符的开始
# 转换标志： -表示左对齐；+ 表示在转换值之前要加上正负号；
# ""（空白字符）表示正数之前保留空格；0表示转换值若位数不够用则用0填充
# 点（.）后跟精度值：如果转换的实数，精度值就表示出现在小数点后的位数。
# 如果转换的是字符串，那么该数字就表示最大字段宽度。如果是*，那么精度会从元组中读出
# 转换类型：参见表3-1
#               表3-1
# 转换类型                              含意
# d,i                           带符号的十进制整数
# o                             不带符号的八进制
# u                             不带符号的十进制
# x                             不带符号的十六进制（小写）
# X                             不带符号的十六进制（大写）
# e                             科学计数法表示的浮点数（小写）
# E                             科学计数法表示的浮点数（大写）
# f,F                           十进制浮点数
# g                             如果指数大于-4或者小于精度值则和e相同，其他情况与f相同
# G                             如果指数大于-4或者小于精度值则和E相同，其他情况则与F相同
# C                             单字符（接受整数或者单字符字符串）
# r                             字符串（使用repr转换任意Python对象）
# s                             字符串（使用str转换任意Python对象）

# 简单转换
# 简单的转换只需要写出转换类型
print 'price of eggs: $%d' % 42
print 'Hexadecimal price of eggs : %x' % 42
from math import pi
print 'pi: %f...' % pi
print 'Very inexact estimate of pi : %i' % pi
print 'Using str : %s' %42l
print 'Using repe: %r' %42l

# 字段宽度和精度
# 格式(字段宽度.精度)，如果只给出精度，必须包括点号
print '%10f' % pi # 字段宽10
print '%10.2f' % pi #字段宽10，精度2
print '%.2f' % pi #精度2
print '%.5s' % ('Guido van Rossum')
# 可以使用*（星号)作为字段宽度或者精度（或者两者都能使用*），此时数值会从元组参数中读出
print '%*.*s' % (10, 5, 'Guido van rossum')

# 符号、对其和用0填充
# 在字符和精度值之前还可以放置一个“标志”，该标志可以是零、加号、减号或空格
print '%010.2f' % pi
print 010
# 减号 - 用来左对齐
print '%-10.2f' % pi
# 空白 "" 意味着在整数前加上空格。
print ('% 5d') % 10 + '\n' +('% 5d') % -10
print '%5d' % (5+2)
