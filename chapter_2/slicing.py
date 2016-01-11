# _*_ coding:utf-8 _*_
# 分片操作来访问一定范围内的元素。分片通过冒号（“:”）隔开的两个索引来实现
tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30]
print tag[32:-4]
# 第一个索引是要提取的第一个元素的编号，而最后的索引则是分片之后剩余部分的第一个元素的编号
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[3:6]
print numbers[0:1]
# 分片操作的实现需要提供两个索引作为边界。第一个索引的元素是包含分片内的，第二个则不包含在分片内

# 访问最后3个元素，索引10指向的是第11个元素——这个元素并不存在，却是在最后一个元素之后。
# 为了让分片部分能够包含列表的最后一个元素，必须提供最后一个元素的下一个元素对应的索引作为边界
print numbers[7:10]
print numbers[-3:-1]
# 只要分片中最左边的索引比它最右边的晚出现在序列中，结果就是一个空序列
print numbers[-3:0]
# 捷径：如果分片所得部分包括序列结尾的元素，只需置空最后一个索引即可
print numbers[-3:]
print numbers[0:-3]
print numbers[:3]
# 如果需要复制整个序列，可以将两个索引都置空
print numbers[:]

# 步长（step length）
# 通常都是隐式设置的。在普通的分片中，步长是1——分片操作就是按照这个步长逐个遍历序列的元素，然后返回开始和结束点之间的所有元素
print numbers[0:10:1]
# 步长为2的分片包括大的是从开始到结束每隔1个的元素
print numbers[0:10:2]
print numbers[3:6:3]
# 捷径
print numbers[::4]
# 步长不能为0（不会执行），但可以使复数，此时分片从右到左提取元素
print numbers[8:3:-1]
print numbers[10:0:-2]
print numbers[0:10:-2]
print numbers[::-2]
print numbers[5::-2]
print numbers[:5:-2]
# 使用一个负数作为步长时，必须让开始点（开始索引）大于结束点
# 对于一个正数步长，Python会从序列的头部开始向右提取元素
# 对于一个负数步长，则是从序列的尾部开始向左提取元素，直到第一个元素