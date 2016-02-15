# _*_ coding:utf-8 _*_
# while 循环
x = 1
while x <= 100:
    print x
    x += 1
name = ''
while not name:
    name = raw_input('Please enter your name: ')
print 'Hello, %s' % name

# for 循环
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print word
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print number
# range 方法类似于分片，如果希望下限为0，可以只提空上限,可以提供第三个参数作为步长
print range(0, 10)
print range(10)
for number in range(0, 101):
    print number
'''如果能使用for循环，就尽量不用while循环'''

# 循环遍历字典
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print key, 'corresponds to', d[key]
for key, value in d.items():
    print key, 'corresponds to', value

# 并行迭代
names = ['anne', 'beth', 'george', 'damon']
age = [12, 45, 32, 102]
for i in rang(len(names)):
    print name[i], 'is', age[i], 'years old'
# 内建zip函数可以用来进行并行迭代
print zip(names, age)
for name, age in zip(names, age):
    print name, 'is', age, 'years old'
# zip函数也可以用于任意多的序列。zip可以处理不等长的序列，当最短的序列“用完”的时候就会停止
print zip(rang(5), xrange(1000000000000000))

# 按索引迭代
''' 伪代码
for string in strings:
    if 'xxx' in string:
        # search for the string in the list of strings
        index = strings.index(string)
        strings[index] = '[censored]'
index = 0
for string in strings:
    if 'xxx' in string:
        strings[index] = '[censored]'
    index += 1
'''
# 内建 enumerate 函数
''' 伪代码
for index, string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[censored]'
'''
# 翻转和排序迭代
print sorted([4, 3, 6, 8, 3])
print sorted('hello, world!')
print list(reversed('hello, world!'))

# 跳出循环
# break
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
# continue
'''伪代码
for x in seq:
    if condition1: continue
    if condition2: continue
    if condition3: continue

    do_something()
    do_something_else()
    do_another_thing()
    etc()

for x in seq:
    if not (conditional1 or conditional2 or condition3):
        do_something()
        do_something_else()
        do_another_thing()
        etc()
'''
# while True/break习语
word = 'dummy'
while word:
    word = raw_input('Please enter a word: ')
    print 'The word was ' + word

word = raw_input('Please enter a word: ')
while word:
    print 'The word was ' + word
    word = raw_input('Please enter a word: ')
while True:
    word = raw_input('Please enter a word: ')
    if not word: break
    print 'The word was' + word

# 循环中else字句
from math import sqrt
for n range(99,81,-1):
    root =sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "Don't find it!"
