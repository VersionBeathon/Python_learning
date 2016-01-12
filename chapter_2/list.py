# _*_ coding:utf-8 _*_
# list函数，把序列转换为列表
print list('Hello')
# 列表可以使用所有适用于序列的标准操作，例如索引、分片、连接和乘法。
# 改变列表：元素赋值
x = [1, 1, 1]
x[1] = 2  # 不能为一个不存在的元素赋值
print x
# 删除元素
names = ['Alice', 'Bob', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print names
# 分片赋值
name = list('Perl')
print name
name [2:] = list('ar')
print name
# 使用分片赋值时，可以使用与原序列不等长的序列将分片替换
name = list('Perl')
name[1:] = list('ython')
print name
# 分片赋值语句可以在不需要替换任何原有元素的情况下插入新的元素
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print numbers
numbers[1:4] = []
print numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
del numbers[1:4]
print numbers
del numbers[1:5:2]
print numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
del numbers[-5:-1:2]
print numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
del numbers[-1:-4:-2]
print numbers