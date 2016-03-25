# _*_ coding:utf-8 _*_
# 模块里有什么 
import copy
# 使用dir
print [n for n in dir(copy) if not n.startswith("_")]
print [n for n in dir(copy)]
# __all__变量
print copy.__all__
# __all__从哪里来，为什么会在那儿？
#__all__是在copy模块内部被设置的，如：__all__ = ["Error", "copy", "deepcopy"]
#它定义了模块的共有接口(public interface)。它告诉解释器：从模块导入所有名字代表什么含义。
#如果使用下面的代码就能使用__all__变量中的四个函数。
from copy import *
#如果要导入PyStringMap
from copy import PyStringMap

# 使用help获取帮助
help(copy)
print copy.__doc__

# 查看文档
print range.__doc__

# 使用源代码
# 一种方法是检查sys.path
# 另一种方法是检查模块的__file__属性
import copy
print copy.__file__
# 如果文件名以.pyc结尾，只要查看对应的以.py结尾的文件即可
# 对于真正理解Python语言的人来说，要了解模块，是不能脱离源代码的，阅读源代码，事实上是学习Python最好的方式。