# _*_ coding:utf-8 _*_
'''为了组织好模块，可以将它们分组为包（package）。包基本上就是另外一类模块。当模块存储在文件中时（扩展名.py），包就是模块所在的目录。为了让Python将其作为包对待，它必须包含一个命名为__init_py的文件（模块）。如果将它作为普通模块到入得话，文件的内容就是包的内容。例如有个名为constans的包(constans其实为一文件夹)，文件constants/__init__.py包括语句PI=3.14'''
import constants
print constants.PI