# _*_ coding:utf-8 _*_
# 字符串格式化：求模操作符 “ % ” 可以用来将其他值转换为包含转换标志的字符串，还能对值进行不同方法的格式化
# 字符串方法

# 本章的新函数
# 函数                                    描述
# string.capwords(s[, sep])     使用split函数分割字符串s（以sep为分隔符），使用capitalize函数将分隔符得到的各
#                               单词首字母大写，并且使用jion函数以sep为分隔符将个单词连接起来
# string.maketrans(from,to)     创建用于转换的转换表（与translate方法联合使用）