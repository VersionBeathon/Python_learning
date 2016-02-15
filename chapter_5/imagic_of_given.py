# _*_ coding:utf-8 _*_
# 序列解包（递归解包）
# 将多个值的序列解开，然后放到变量的序列中
# 多个赋值操作同时进行
x, y, z = 1, 2, 3
print x, y, z
x, y = y, z
print x, y, z

values = 1, 2, 3
print values
x, y, z = values
print x

# popitem方法，这个方法将键-值作为元组返回，这个元组就可以直接赋值到两个变量中
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print key
print value

# 链式赋值——将同一个值付给多个变量的捷径
# x = y = somefunction
# y = somefunction
# x = y
# 22行 与 24 25 等价 与下列两行不一定等价
# x = somefunction
# y = somefunction

# 增量赋值
x = 2
x += 1
x *= 2
print x
# 对于其他数据类型也是适用
fnord = 'foo'
fnord += 'bar'
fnord *= 2
print fnord