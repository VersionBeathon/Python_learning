# _*_ coding:utf-8 _*_
# 按字节处理
# 用read方法对每个字符进行循环
import fileinput
def process(string):
    print 'Processing: ', string
f = open('somefile.txt')
char = f.read(1)
while char:
    process(char)
    char = f.read(1)
f.close()

# 用不同的方式写循环
f = open('somefile.txt')
while True:
    char = f.read(1)
    if not char:
        break
    process(char)
f.close()

# 按行操作
f = open('somefile.txt')
while True:
    line = f.readline()
    if not line:
        break
    process(line)
f.close

# 用read迭代每个字符
f = open('somefile.txt')
for char in f.read():
    process(char)
f.close

# 用readlines迭代行
f = open('somefile.txt')
for line in f.readlines():
    process(line)
f.close()

# 使用fileinput实现懒惰行迭代
for line in fileinput.input('somefile.txt'):
    process(line)

# 文件迭代器
f = open('test2.txt', 'w')
f.write('First line\n')
f.write('Second line\n')
f.write('Third line\n')
f.close()
lines = list(open('test2.txt'))
print lines
first, second, third = open('test2.txt')
print first
print second
print third