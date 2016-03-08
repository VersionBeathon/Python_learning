# _*_ coding:utf-8 _*_
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height

r = Rectangle()
r.width = 10
r.height = 5
print r.getSize()
r.setSize((150,100))
print r.width
print r.height

# property函数 创建属性的一种方法
__metaclass__ = type
class rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize) # 在新式类中应该使用property函数而不是访问器方法
r = rectangle()
r.size = 150, 200 # size作为 一种属性 不用考虑它怎么实现的 与15行代码做比较
print r.width

# 静态方法和类成员方法
__metaclass__ = type
class MyClass1:
    def smeth():
        print 'This is a static method'
    smeth = staticmethod(smeth)
    def cmeth(cls):
        print 'This is a class method of', cls
    cmeth = classmethod(cmeth)
MyClass1.smeth()
MyClass1.cmeth()
# 使用@操作符，在方法（或函数）的上方将装饰器列出，从而制定一个或者更多的装饰器
# 装饰器：它能对任何可调用的对象进行包装，即能够用于方法也能用于函数
__metaclass__ = type
class MyClass2:
    @staticmethod
    def smeth():
        print 'This is a static method'
    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls
    
MyClass2.smeth()
MyClass2.cmeth()
