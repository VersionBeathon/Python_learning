# _*_ coding:utf-8 _*_
# bool
# False None 0 "" () [] {} 在作为布尔表达式的时候，会被解释器看作假（False）
print True
print False
print True == 1
print False == 0
print True + False + 42
print bool('I think, there before I am')
print bool(42)
print bool('')
print bool(0)

# 条件执行, if语句, else字句， elif字句
name = raw_input('What is your name? ')
if name.endswith('Gumby'):
    print 'Hello, Mr. Gumby'
else:
    print 'Hello, stanger'
# elif 是elif的简写
num = input('Enter a number: ')
if num > 0:
    print 'The number is positive'
elif num < 0:
    print 'The number is negative'
else:
    print 'The number is zero'

name = raw_input('What is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print "Hello, Mr. Gumby"
    elif name.startswith('Mrs'):
        print "Hello,Mrs Gumby"
    else:
        print "Hello,Gumby"
else:
    print 'Hello,stranger'

# 比较运算符
