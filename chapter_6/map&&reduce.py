# _*_ coding:utf-8 _*_
from functools import reduce


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print char2num('1')
print map(char2num, '13579')
print reduce(fn, map(char2num, '13579'))
