# _*_ coding:utf-8 _*_
# finally字句，可以用来在可能异常后进行清理。它和try字句联合使用：

x = None
try:
    x = 1 / 0
finally:
    print 'Clearning up...'
    del x

# 上述代码中，finally字句肯定会被执行，不管try字句中是否发生异常

try:
    1 / 0
except NameError:
    print 'Unkown variable'
else:
    print "That went well"
finally:
    print 'Clearning up.'