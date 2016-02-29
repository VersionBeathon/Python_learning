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