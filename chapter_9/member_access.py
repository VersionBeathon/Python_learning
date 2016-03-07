# _*_ coding:utf-8 _*_
# 创建一个无穷序列

__metaclass__ = type


def checkIndex(key):
    if not isinstance(key, (int, long)):  # 检查是否为整数
        raise TypeError
    if key < 0:  # 检查是否为负数
        raise IndexError


class ArithmeticSequence:

    def __init__(self, start=0, step=1):
        self.start = start  # 保存开始值
        self.step = step  # 保存步长值
        self.change = {}  # 没有项被修改

    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.change[key]  # 修改了么？
        except KeyError:  # 否则
            return self.start + key * self.step  # ……计算值

    def __setitem__(self, key, value):
        '''修改算数序列中的一个项'''
        checkIndex(key)
        self.change[key] = value  # 保存更改后的值

s = ArithmeticSequence(1, 2)  # 初始化开始值和步长
print s[4]  # 输入 key
print s[10]
# s['four'] # 触发TypeError异常
# s[-42] # 触发 IndexError异常

# 子类化列表，字典和字符串


class CounterList(list):

    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
c1 = CounterList(range(10))
print c1
c1.reverse()
print c1

del c1[3:6]

print c1
print c1.counter
print c1[4] + c1[2]
print c1.counter
