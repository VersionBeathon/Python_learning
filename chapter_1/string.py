#_*_coding:utf-8_*_
print '\'hello.world\''  # " \' "反斜线对字符串中的引号进行转义。使得编译器能够识别
print 'let\'s say "hello.world"'
print "let's say " '"hello.world"'
x = "hello."
y = "world"
print x + y  # 拼接字符串就像加法运算一样
print repr("hello.world")
print str("hello.world")
print repr(100000000000000)  # repr会创建一个字符串，以合法的Python表达式的形式来表示值
print str(10000000000000)  # str会把值转换为合理形式的字符串
temp = 42
print "the temperature is " + `temp` # repr(x)也可以用`x`来实现
#函数str让字符串更容易于阅读，而repr（和反引号）则把结果字符串转换为合法的Python表达式
print 