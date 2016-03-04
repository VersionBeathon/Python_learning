# _*_ coding:utf-8 _*_
# 可以像对条件和循环语句那样，给try/except语句加else语句
try:
    print 'A simple task'
except:
    print 'What? Something went wrong'
else:
    print 'Ah... It went as planned.'

while True:
    try:
        x = input('Enter the first number: ')
        y = input("Enter the second number: ")
        print x / y
    except:
        print "Invalid input. Please try again."
    else:
        break

# 捕捉对象
while True:
    try:
        x = input('Enter the first number: ')
        y = input("Enter the second number: ")
        print x / y
    except Exception,e:
        print "Invalid input:",e
        print 'Please try again'
    else:
        break
