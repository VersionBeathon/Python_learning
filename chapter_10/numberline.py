# _*_ coding:utf-8 _*_                   #  1
# 为Python脚本添加行号            #  2
import fileinput                         #  3
for line in fileinput.input(inplace=True): #  4
    line = line.rstrip()                 #  5
    num = fileinput.lineno()             #  6
    print "%-40s # %2i" % (line, num)    #  7
