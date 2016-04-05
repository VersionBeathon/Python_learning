# _*_ coding:utf-8 _*_
f = open(r'test1.txt')
print f.read(7)
print f.read(4)
f.close

f = open(r'test1.txt')
print f.read()
f.close

f = open(r'test1.txt')
for i in range(3):
    print str(i) + ': ' + f.readline()
f.close

import pprint
pprint.pprint(open(r'test1.txt').readlines())

f = open(r'test1.txt', 'w')
f.write('this\nis no\nhaiku')
f.close

f = open(r'test1.txt')
lines = f.readlines()
f.close
lines[1] = 'isn`t a\n'
lines.append('\ntest')
f = open(r'test1.txt', 'w')
f.writelines(lines)
f.close

