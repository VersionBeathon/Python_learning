# _*_ coding:utf-8 _*_
# 相等运算符
print "foo" == "foo"
print "foo" == "bar"

# is:同一性运算符
x = y = [1, 2, 3]
z = [1, 2, 3]
print x == y
print x == z
print x is y
print x is z  # is运算符是判定同一性而不是相等性
x = [1, 2, 3]
y = [2, 4]
print x is not y
del x[2]
y[1] = 1
y.reverse()
print x == y
print x is y
# 使用==运算符来判定两个对象是否相等，使用is判定两者是否等同（同一个对象）

# 字符串和序列的比较
print "alpha" < "bate"
print 'FnORd'.lower() == "fNorD".lower()
print[1, 2] < [2, 1]
print[2, [1, 4]] < [2, [1, 5]]

# bool运算符
number = input("Enter a number between 1 and 10: ")
if number <= 10:
    if number >= 1:
        print "Great!"
    else:
        print "Wrong!"
else:
    print "Wrong!"
number = input("Enter a number between 1 and 10: ")
if number >= 1 and number <= 10:
    print "Great!"
else:
    print "Wrong!"
number = input("Enter a number: ")
if number > 0 or number < 0:
    print "It is not a zero"
else:
    print "It is a zero"

# in:成员资格运算符
name = raw_input('what is your name? ')
if 's' in name:
    print 'Your name contains the letter "s".'
else:
    print 'Your name does not contain the letter "s".'

# 断言
# 断言工作模式：if not condition： crash program
# 如果确保程序中某个条件一定为真才能让程序正常工作的话，assert语言就用有了
# 条件后可以添加字符串,用来解释断言
age = -1
assert 0 < age < 100, 'The age must be realistic'
