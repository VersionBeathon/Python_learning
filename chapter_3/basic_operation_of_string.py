# _*_ coding:utf-8 _*_
# 所有标准的序列操作（索引、分片、乘法、判断成员资格、求长度、取最小值和最大值）对字符串同样适用
website = 'http://www.python.org'
# website[-3:] = 'com' 字符串都是不可变的，分片赋值是不合法的
print len(website)
print website * 2
print website[-8:-3]
print website[-8:-1:]
print 'w' in website
print max(website)
print min(website)