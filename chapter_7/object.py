# _*_ coding:utf-8 _*_
# 创建自己的类
_metaclass_ = type  # 确定使用新式类


class Person:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, world! I`m %s. " % self.name
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()
# 特性是可以在外部访问的
print foo.name
bar.name = 'Yoda'
bar.greet()

# 特性、函数和方法


class Class:

    def method(self):
        print 'I have a self!'


def function():
    print "I don`t..."
instance = Class()
instance.method()
instance.method = function
instance.method()


class Bird:
    song = 'Squaawk!'

    def sing(self):
        print self.song


bird = Bird()
bird.sing()
birdsong = bird.sing
print birdsong()

# Python并不直接支持私有方式，而是要靠程序员自己把握在外部进行特性修改的时机
# 为了让方法或者特性变为私有（从外部无法访问），只需要在它的名字前面加上双下划线即可


class Secretive:

    def __inaccessible(self):
        print "Bet you can`t see me..."

    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()
# 现在__inaccessible是无法从外部访问的，但在类内部还能用
s = Secretive()
# s.__inaccessible()
s.accessible()

# 类的命名空间


# 这两行语句（几乎）等价：
def foo(x): return x * x
foo = lambda x: x * x
'''两者都返回参数平方的函数，而且都将变量foo绑定到函数上。变量foo可以在全局（模块）范围进行定义，也可处于局部的函数或方法内。定义类时，同样的事情也会发生，多有位于class语句中的代码都可在特殊的命名空间中执行————类命名空间（class namespace）。这个命名空间可由类内多有成员访问。'''
# 并不是所有Python程序员都知道类的定义起始就是执行代码块，这一点非常有用，比如，在类的定义去并不只限定使用def语句


class C:
    print 'class c being defined...'


class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1
m1 = MemberCounter()
m1.init()
print MemberCounter.members
m2 = MemberCounter()
m2.init()
print MemberCounter.members
# 类作用域内的变量也可以被所有实例访问：
print m1.members
print m2.members
# 重新绑定members 特性
m1.members = 'Two'
print m1.members
print m2.members

# 指定超类
# 子类可以扩展超类的定义。将其他类名卸载class语句后的圆括号内可以制定超类


class Filter:

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):  # SPAMFilter是Filter的子类

    def init(self):  # 重写Filter超类中的init方法
        self.blocked = ['SPAM']
# Filter是个用于过滤序列的通用类，实际上他不能过滤任何东西
f = Filter()
f.init()
print f.filter([1, 2, 3])
# Filter类的用处在于它可以用作其其他类的基类（超类），比如SPAMFilter类，可以将序列中的"SPAM"过滤出去
s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'egg', 'apple', 'fuck', 'SPAM'])
# 注意SPAMFilter定义的两个要点
# 这里用提供新定义的方法重写了Filter的init定义。
# filter方法的定义是从Filter类中拿过来（继承）的，所以不用重写它的定义

# 检查继承
# 如果想要查看一个类是否是另一个子类，可以使用内建的issubclass函数：
print issubclass(SPAMFilter, Filter)
print issubclass(Filter, SPAMFilter)
# 如果想要知道已知类，可以直接使用它的特殊属性__bases__:
print SPAMFilter.__bases__
print Filter.__bases__
# 还能使用isinstance方法检查一个对象是否是一个类的实例：
s = SPAMFilter()
print isinstance(s, SPAMFilter)
print isinstance(s, Filter)
# 使用isinstance并不是一个好习惯，使用多态会更好一些

# 如果只想知道一个对象术语哪个类，可以使用__class__特性：
print s.__class__

# 多个超类


class Calculator:

    def calculator(self, expression):
        self.value = eval(expression)


class Talker:

    def talker(self):
        print 'Hi, my value is', self.value


class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculator('1+2*3')
tc.talker()

# 接口和内省
# 接口 的概念与多态有关。在处理多态对象时，只要关心它的接口（或称“协议”）即可，也就是空开的方法和特性
# 检查所需方法是否存在
print hasattr(tc, 'talker')
print hasattr(tc, 'fnord')
# 检查talker特性是否可调用
print callable(getattr(tc, 'talker', None))