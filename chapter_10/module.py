# _*_ coding:utf-8 _*_
import sys
sys.path.append('H:\workspace\python\pythonlearning\chapter_1')
import begin
begin = reload(begin)

# 包含函数的简单模块
sys.path.append('H:\workspace\python\pythonlearning\chapter_10')
import hello2
hello2.hello()
import hello3
hello3.hello()
print __name__
print hello3.__name__

# 使用条件测试代码的模块
import hello4
hello4.hello()
hello4.test()

# 让你的模块可用
# 让sys.path包含正确的目录
# 方法1：将模块放置在合适的位置
import sys, pprint
pprint.pprint(sys.path)
import another_hello
another_hello.hello()
# 方法2：告诉编辑器去哪找
# 适用情况：不希望将自己的模块填满Python解释器的目录、没有在python解释器目录中存储文件的权限、想将模块放在其它地方。
'''编辑autoexec.bat文件，可在c盘的根目录下找到,如果想要添加目录c:\\python
可以这么做：set PYTHONPATH=%PYTHONPATH%;c:\\python'''
