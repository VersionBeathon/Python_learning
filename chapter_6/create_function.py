# _*_ coding:utf-8 _*_
# 计算斐波那契额数列
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print fibs
fibs = [0, 1]
num = int(raw_input('how many fibonacci numbers do you want: '))
# 此处int()的作用是将读取到的数据转换成整型
for i in range(num):
    fibs.append(fibs[-2] + fibs[-1])
print fibs

# 创建函数
# 定义hello函数


def hello(name):
    return 'Hello, ' + name + '!'
# 定义fib函数


def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

print hello('world')
print hello('Gumby')
print fibs(10)

# 文档化函数
# 如果想给函数写文档，除了常用的注释方法外，可以直接写上字符串，这类字符串通常在def语句后面
def square(x):
    '计算x的平方'
    return x * x
# 文档字符串可以按如下方式访问
square.__doc__
print square.__doc__

# 无返回值函数
def test():
    print 'this is printed'
    return
    print 'this is not'
x = test()