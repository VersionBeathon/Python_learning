# _*_ coding:utf-8 _*_
# 读和写
# 没有指定文件路径，路径名不存在，open会在当前文件夹下创建(有可能只限于windows)
from __future__ import with_statement

f = open('somefile.txt', 'w')
f.write('Hello, ')
f.write('world!')
f.close

f = open('somefile.txt', 'r')
print f.read(4)  # 指定读取的字符数"4"
print f.read()
f.close

# 读写行
f = open('somefile.txt', 'r')
print f.readline(5)
print f.readline()
f.close

f = open('somefile.txt', 'a')
f.writelines('\ntest')
f.close

# 唉使用其他符号作为换行符的平台上，用\r(mac中)和\r\n(windows中)代替\n(由os.linesep决定)

# 关闭文件
'''牢记使用close方法关闭文件'''
# 使用try/finally语句，并且在finally字句中调用close方法。

f = open('somefile.txt', 'a')
try:
    f.write('\ntest')
finally:
    file.close
# with语句：

with open('somefile.txt', 'a') as somefile:
    somefile.write('\ntest with')

''' 谨记在打开文件时要记得加入模式参数，如果不加，默认为只读操作'''