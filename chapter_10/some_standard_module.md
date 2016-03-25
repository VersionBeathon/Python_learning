# 一些标准模块
## sys

sys这个模块让你能够访问与Python解释器联系紧密的变量和函数。

|函数/变量|描述|
|:--------------------------|:------------------------------|
|argv|命令行参数，包括脚本名称|
|exit([arg])|退出当前程序，可选参数为给定的返回值或者错误信息|
|modules|映射模块名字到载入模块的字典|
|path|查找模块所在的目录名列表|
|platform|类似sunos5或者win32的平台标识符|
|stdin|标准输入流——一个文件(file-like)对象|
|stdout|标准输出流——一个类文件对象|
|stderr|标准错误流——一个类文件对象|

* 变量sys.argv包含传递到Python解释器的参数，包括脚本名称。
* 函数sys.exit可以退出当前程序
* 映射sys.modules摸块变量将模块名映射到实际存在的模块上，它只应用于目前导入的模块
* sys.path是一个字符串列表，其中每个字符串都是一个目录名，在import语句执行时，解释器就会从这些目录中查找模块。
* sys.platform模块变量是解释器正在其他运行的平台名称。它可能是标识操作系统的名字（比如sunos5或者win32），也可能标识其他种类的平台，如果运行Jython的话就是Java虚拟机（比如java1.4.0）
* sys.stdin sys.stdout和sys.stderr模块是类文件流对象。它们标识标准UNIX概念中的标准输入、标准输出和标准错误。

反序打印命令行参数
```Python
# reverseargs.py
import sys
args = sys.argv[1:]
args.reverse()
print ' '.join(args)
# another_way
print ' '.join(reversed(sys.argv[1:]))
```

## os

os模块提供了访问多个操作系统服务的功能。os模块包括的内容很多。os和它的子模块os.path还包括一些用于检查、构造、删除目录和文件的函数，遗迹一些处理路径的函数（例如，os.path.split和os.path.join让你在大部分情况下都可以忽略os.pathsep）
|函数/变量|描述|
|:----------------------------|:-------------------------|
|environ|对环境变量8进行映射|
|system(command)|在子shell中执行操作系统命令|
|sep|路径中的分隔符|
|pathsep|分个路径的分隔符|
|linesep|行分隔符('\n', '\r', or '\r\n')|
|urandom(n)|返回n字节的加密强随机数据|






