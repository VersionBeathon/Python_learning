# _*_ coding:utf-8 _*_
# 生成器是Python新引入的概念，也可叫简单生成器。
# 生成器是一种用普通的函数方法定义的迭代器。
# 创建生成器
nested = [[1, 2], [3, 4], [5]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
# 任何包含yield语句的函数称为生成器。
# 它不是像return那样返回值，而是每次产生多个值。每次产生一个值（使用yield语句），函数就会被冻结：即函数停在那点等待被重新唤醒，函数被重新唤醒后就从停止的那点开始执行。
for num in flatten(nested):
    print num
print list(flatten(nested))

# 循环生成器
g = ((i + 2) ** 2 for i in range(2, 27))
print g.next()
print g.next()
print g.next()
# 在函数调用中，不用增加另外一对括号，可以写成： sum(i ** 2 for i in range(10))

def flatten1(nested):
    try:
        for sublist in nested:
            for element in flatten1(sublist):
                yield element
    except TypeError:
        yield nested
test = [[1, 2], 3, 4, [5, [6,7]], 8]
print list(flatten1(test))
# 字符串情况下递归生成器
def flatten2(nested):
    try:
        try: nested + ''
        except TypeError:pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested
print list(flatten2(['foo', ['bar', ['barz']]]))

# 模拟生成器
def flatten3(nested):
    result = []
    try:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten3(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return rprint、esult