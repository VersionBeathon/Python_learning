# _*_ coding:utf-8 _*_
print 'Hello.\nworld'
path = 'c:\nowhere'
print path
path = 'c:\\nowhere'
print path
print 'c:\\nowhere'
print r'c:\nowhere'
path = 'c:\\Program Files\\fnord\\foo\\bar\\baz\\frozz\\bozz'
print path
print r'c:Program Files\fnord\foo\bar\baz\frozz\bozz'
'''原始字符串以r开头。原始字符串不会把反斜线当做特殊字符。原始字符串中输入的每个字符都会与书写方式保持一致
如果不使用原始字符串则需使用“\”进行转义，例如例如第3行与第5行的比较、第9与第11行的比较'''
# print r"this is illega\"
# 不能再原始字符串结尾输入反斜线。原始字符串最后一个字符不能是反斜线，除非对反斜线进行转义
print r"this is illega\\"
print r'c:\Program Files\foo\bar' '\\'
# 如果希望原始字符串只以一个反斜线作为结尾，如第17行
print u'hello.world!'
'''Python中的普通字符串在内部是以8位的ASCII码形成存储的，而Unicode字符串则存储为16位Unicode字符，这样就能表示更多的字符集'''