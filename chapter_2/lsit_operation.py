# _*_ coding:utf-8 _*_
# appeng方法用于在列表末追加新的对象
lst = [1, 2, 3]
lst.append(4)
print lst
# 如果使用list作为变量名，就无法调用list函数
''' append方法和其他一下方法类似，知识在恰当位置修改原来的列表。
它不是简单地返回一个修改过的新列表——而是直接修改原来的列表'''

# count方法用来统计某个元素在列表中出现的次数
example = ['to', 'be', 'or', 'not', 'to', 'be']
print example.count('to')
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x.count(1)
x = [1, 1]
print x.count(1)

# extend方法可以在列表的末尾一次性追加另一个序列中的多个值
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b[1:3])
print a
''' extend看起来很像连接操作，两者最主要的区别在于：
extend方法修改了被扩展的序列。而原始连接操作则不然，它会返回一个全新的列表'''
a = [1, 2, 3]
b = [4, 5, 6]
print a + b
print a
a = a + b
print a
# 也可以使用分片赋值来实现相同的结果
a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print(a)

# index方法用于从列表中找出某个值第一个匹配项的索引位置
knights = ['we', 'are', 'the', 'knights', 'who', 'say', 'ni']
print knights.index('who')
# knights.index('herring') 如果未找到该单词那么就会引发一个异常
print knights[4]

# insert方法用于将对象插入到列表中
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print numbers
# 也可以用分片的方法来实现insert
numbers[3:3] = ['four']
print numbers

# pop方法会移除列表中的一个元素（默认是最后一个），并且返回该元素的值
x = [1, 2, 3]
print x.pop()
print x
print x.pop(0)
print x
# pop方法是唯一一个既能修改列表又返回元素值（除了None）的列表方法
# 利用pop实现——栈（先进后出）
x = [1, 2, 3]
x.append(x.pop())
print x
# 利用pop实现FIFO
x = [1, 2, 3]
x.insert(0, x.pop())
x.insert(1, x.pop())
print x
x = [1, 2, 3]
x.append(x.pop(0))
print x

# remove方法用于移除列表中某个值的第一个匹配项
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print x
# x.remove('bee') 不存在于列表中的值是不会被移除
# remove是一个没有返回值的原位置改变方法。它修改了列表却没有返回值，这与pop方法相反

# reverse方法将列表中的元素反向存放,该方法也改变了列表但不返回值
x = [1, 2, 3]
x.reverse()
print x

x = [1, 2, 3]
print list(reversed(x))

# sort方法用于在原位置对列表进行排序。
# 在原位置意味着改变原来的列表，从而让其中的元素能按照一定的顺序排列，而不是简单地返回一个已排序的列表副本
x = [1, 2, 3, 5, 4, 9, 8, 7]
x.sort()
print x
# 当用户需要一个排好序的列表副本，同时又保留原有列表不变，可采用赋值的方法
x = [4, 6, 2, 1, 7, 9, 8]
y = x[:]
y.sort()
print x, y
# 不采用分片方法只是简单地把x赋值给y是没用的，因为这样做就让x，y都指向同一个列表了
y = x
y.sort()
print x, y
# 另一种获取已排序的列表副本的方法是，使用sorted函数
x = [4, 6, 2, 1, 7, 9, 8]
y = sorted(x)
print y
# sorted可以用于任何序列，却总是返回一个表
test = sorted('python')  # 按照ASCII表顺序排序
print test
# 把一些元素按照相反的顺序排列,先使用sort，在使用reverse
x = [4, 6, 2, 1, 7, 9, 8]
x.sort()
x.reverse()
print x

# 高级排序
# compare(x,y)会在x < y时返回负数，x > y时返回整数，x = y 时返回0
print cmp(42, 32)
print cmp(32, 42)
print cmp(10, 10)
# 定义好cmp函数后，就可以提供给sort方法作为参数
numbers = [5, 2, 9, 7]
numbers.sort(cmp)
print numbers
# 参数key并不是直接用来确定对象的大小，而是为每个元素创建一个键，然后所有元素根据键来排序。
# 例如按照 长度排序
x = ['adfadf', 'adfggikiopujoihj', 'asfd', 'ageahg', 'qweiuuqbbhjkbjkhasgdjh']
x.sort(key=len)
print x
# reverse是简单的布尔值（True or False）,用来指明列表是否要进行反向排序
x = [4, 6, 2, 1, 7, 9, 8]
x.sort(reverse=True)
print x
