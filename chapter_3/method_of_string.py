# _*_ coding:utf-8 _*_
# 字符串从“string”模板中“继承”了很多方法

# find方法可以在一个较长的字符串中查找子串。它返回子串坐在位置的最左端索引。如果没找到返回-1
print 'With a moo-moo here, and a moo-moo there'.find('moo')
title = "Monty Python's Flying Circus"
print title.find('Monty')
print title.find('Python')
print title.find("Flying")
print title.find('Zircus')
# 也可以用find判断成员资格
subject = '$$$ Get rich now!!! $$$'
print subject.find('$$$')
# find还可以接受可选的起始点和结束点参数
print subject.find('$$$', 1)
print subject.find('!!!')
print subject.find('!!!', 0, 16)
# 由起始和终止制定的范围包含第一个索引不包括第二个索引

# join 方法是split方法的逆方法，用来连接序列中的元素
seq = [1, 2, 3, 4, 5] # 数字列表
print seq
# sep = '+'
# sep.join(seq)
# 被连接的序列元素都必须是字符串
seq = ['1', '2', '3', '4', '5'] # 字符串列表
sep = '+'
print sep.join(seq)
print seq

# lower 方法返回字符串的小写字母版
print 'Trondheim Hammer Dance'.lower()
# 如果想编写“不区分大小写”的代码，此方法可用
if 'Gumby' in ['gumby', 'bob', 'rose']:
    print 'Fount out!'
name = 'Gumby'
names = ['gumby', 'bob', 'rose']
if name.lower() in names:
    print "Found out"
# 与lower方法相关的是title方法，它会将字符串转换为标题——也就是所有单词的首字母大写，而其他字母小写
print "that's all folks".title()
print 'thst is all folks'.title()
# 另外一个string模块的capwords函数
import string
print string.capwords("that's all folks")

# replace方法返回某字符串的所有匹配项均被替换之后得到的字符串
print 'This is a test'.replace('is', 'ezz')  # 类似于查找并替换功能

# split方法是join的的逆方法，用来将字符串分割成序列
print '1+2+3+4+5'.split('+')
print "1+2+3+4+5".split("+")
print '/usr/bin/env'.split('/')
print 'using the default'.split()
# 如果不提供任何分隔符，程序会把所有空格作为分隔符

# strip方法返回去除两侧（不包括内部）空格的字符串
print '     internal whitespace is kept       '.strip()
# 与lower方法一直使用的就可以很方便的比对输入和存储的值
names = ['gumby', 'smith', 'jones']
name = 'Gumby '
if name.lower() and name.strip() in name:
    print 'Fount it!'
# 可以去除指定的字符，把他们作为参数即可
print '*** SPAM * for * everyone!!! ***'.strip(' *!')
# 这个方法只能去除两侧的字符，所以字符串中的星号没有被去掉

# translate方法可以替换字符串中的某些部分，但与replace不同的是，它只处理单个字符。
# 它的优势在于可以同时进行多个替换

# 创建转换表
from string import maketrans 
# maketrans函数接受两个参数：两个等长的字符串，表示第一个字符串中的每个字符都用第二个字符串中相同位置的字符替换
table = maketrans('cs', 'kz')
print len(table)
print table[97:123]
print maketrans('','')[97:123]
# 将表用作translate方法的参数
print 'this is an incredible test'.translate(table)
# translate第二个参数是可选的，这个参数是用来指定需要删除的字符。
print 'this is an incredible test'.translate(table,' ')
