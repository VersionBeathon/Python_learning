# _*_ coding:utf-8 _*_
print '''This is a very long string.
It continues here.
And it's not over yet.
"Hello.world!"
still here.'''
# 如果需要一个非常非常长的字符串，它需要跨多行，那么，可以使用三个引号代替普通符号，也可使用三个引号
print "hello.\
world"
print 1 + 2 +\
    4 + 5
print \
    'hello.world'
# 普通字符也可以跨行。如果一行之中最后一个字符是反斜线，那么，换行符本身就“转义”了，也就是被忽略