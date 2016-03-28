# _*_ coding:utf-8 _*_
# 集合、堆和双端队列
# 集合
print set(range(10))
# 集合是由序列（或者其他可迭代的对象）构建的。它们主要用于检查成员资格，因此副本是被忽略的：
print set([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5])
# 和字典一样，集合元素的顺序是随意的，因此我们不应该以元素的顺序作为依据进行编程
print set(['fee', 'fie', 'foe'])
# 除了检查成员资格外，还可以使用标准的操作集合
# 找出两个集合的并集
a = set([1, 2, 3])
b = set([2, 3, 4])
print a.union(b)
print a | b
c = a & b
print c
print c.issubset(a)
print c <= a
print c.issuperset(a)
print a.intersection(b)
print a.difference(b)
print a - b
print a.symmetric_difference(b)
print a ^ b
print a.copy()
print a.copy() is a
# 集合是可变的，所以不能用做字典中的键。另外一个文件就是集合本身只能包含不可变（可散列的）值，所以也就不能包含其他集合。
# frozenset类型，用于代表不可变（可散列）的集合
a = set()
b = set()
a.add(frozenset(b))

