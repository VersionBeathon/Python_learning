# _*_ coding:utf-8 _*_
# 在Python中构造方法很容易。只要把init方法的名字从简单的init改为魔法版本__init__即可
__metaclass__ = type


class FooBar:

    def __init__(self):
        self.somevar = 42
f = FooBar()
print f.somevar

# 给构造方法传递参数


class FooBar1:

    def __init__(self, value=42):
        self.somevar = value
f = FooBar1()
print f.somevar
f = FooBar1("I`m so stupid")
print f.somevar

# 在Python所有的魔法方法中，__init__是使用最多的一个


# 重写一般方法和特殊的构造方法
class A:

    def hello(self):
        print "Hello, I`m A."


class B(A):
    pass
a = A()
b = B()
a.hello()
b.hello()  # B类中名没有hello方法，从A类中继承

# 将hello方法重写


class C(A):

    def hello(self):
        print "Hello, I`m C"
c = C()
c.hello()

# 重写是继承机制中的一个重要内容，对于构造方法尤其重要
# 如果一个类的构造方法被重写，那么就需要调用超类（你所继承的类）的构造方法，否则对象可能不会被正确地初始化


class bird:

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print 'I need food Aaaah....'
            self.hungry = False
        else:
            print 'No,thanks.I`m full!'


class songBird(bird):

    def __init__(self):
        self.sound = 'Squawk!'

    def sing(self):
        print self.sound
sb = songBird()
sb.sing()
# sb.eat 无法调用
''' songBird没有hungry的特性。因为在songBird中，构造方法被重写，但新的构造方法没有任何关于出事化hungry特性的代码。为了达到预期的效果songBird的构造方法必须调用其超类bird的构造方法来确保进行基本的初始化'''

# 调用未绑定的超类构造方法


class SongBird(bird):

    def __init__(self):
        bird.__init__(self)  # 此处为调用超类构造方法
        self.sound = "Squawk"

    def sing(self):
        print self.sound
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()

# 使用supper函数
'''如果读者不想坚守旧版Python阵营，那么就应该使用super函数。它只能在新式类中使用，尽可能用新式类'''
# 更新 bird 例子
_metaclass_ = type  # super函数只能在新式类中起作用


class Bird:

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No,thanks!'


class SongBird1(Bird):

    def __init__(self):
        super(SongBird1, self).__init__()  # super函数调用超类构造方法
        self.sound = "Squawk"

    def sing(self):
        print self.sound
sb = SongBird1()
sb.sing()
sb.eat()