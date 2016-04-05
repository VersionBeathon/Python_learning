# _*_　coding:utf-8 _*_
from random import randrange
num = input("how many dices? ")
sides = input("how many sides per dices? ")
sum = 0
for i in range(num):
    sum += randrange(sides) + 1
print "The result is ", sum
