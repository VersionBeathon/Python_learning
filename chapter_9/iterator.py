# _*_ coding:utf-8 _*_
# 迭代器规则
'''迭代的意思是重复做一些很多次，就像在循环中做的那样。到现在为止只在for循环中对序列和字典进行过迭代，但实际上也能对其他对象进行迭代：只要该对象实现了__iter__方法。
__iter__方法会返回一个迭代器（iterator），所谓的迭代器就是具有next方法（这个方法在调用时不需要任何参数）的对象。在调用next方法时，迭代器会返回它的下一个值。如果next方法被调用，但迭代器没有值可以返回，就会引发一个StopIteration异常。'''
# 斐波那契数列 使用迭代器


class Fibs:

    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print f
        break

# 内建函数iter可以从可迭代的对象中获得迭代器
it = iter([1, 2, 3])
print it.next()
print it.next()

# 从迭代器上得到序列
class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti = TestIterator()
print list(ti)
