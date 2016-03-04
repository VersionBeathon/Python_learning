# _*_ coding:utf-8 _*_
# 处理异常可以使用try/except语句来实现
try:
    x = input('Enter the first number: ')
    y = input("Enter the second number: ")
    print x / y
except ZeroDivisionError:
    print "The second number can`t be zero!"

# 不止一个except字句
try:
    x = input('Enter the first number: ')
    y = input("Enter the second number: ")
    print x / y
except ZeroDivisionError:
    print "The second number can`t be zero!"
except TypeError:
    print "That wasn`t a number , was it ?"

# 用一个模块捕捉多个异常，可将他们作为元组列出
try:
    x = input('Enter the first number: ')
    y = input("Enter the second number: ")
    print x / y
except (ZeroDivisionError， TypeError, NameError):
    print "The second number can`t be zero!"

# 捕捉对象
try:
    x = input('Enter the first number: ')
    y = input("Enter the second number: ")
    print x / y
except (ZeroDivisionError, TypeError), e
    print e

# 真正的全捕捉(用空的except语句)
try:
    x = input('Enter the first number: ')
    y = input("Enter the second number: ")
    print x / y
except:
    print "Something wrong happened..."


# 屏蔽 ZeroDivisionError，打印错误信息而不是让异常传播


class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise
calculator = MuffledCalculator()
print calculator.calc('10/2')
calculator.calc('10/0')
calculator.muffled = True
calculator.calc('10/0')
