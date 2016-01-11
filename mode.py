#_*_coding:utf-8_*_
import math
print math.floor(32.9) # 返回下舍整数
print int(math.floor(32.9))  # 某些特殊函数需要从模块中调用，用import导入模块，然后按照“模块.函数”的格式使用这个函数。
from math import sqrt  # 在确定自己不会导入多个同名函数（从不同模块导入）的情况下，可以使用from 模块 import 函数 换行 函数()
print sqrt(9)
print int(sqrt(9))
# print sqrt(-1) math 函数不能求负数平方根
import cmath  # cmath (complex math，复数)
print cmath.sqrt(-1)  # 显示1j为虚数，虚数以j（或J）做结尾，长整数用L
print(1 + 3j) * (9 + 4j)#Python语言本身提供了对复数的支持。Python中没有单独的虚数类型。它们被看作实数部分为0的复数
