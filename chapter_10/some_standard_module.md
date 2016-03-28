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

* os.environ映射包含本章前面讲述过的环境变量。比如要访问系统变量PYTHONPATH，可以使用表达式os.environ['PYTHONPATH']。这个映射也可以用来更改系统环境变量，不过并非所有系统都支持。
* os.system函数用于运行外部程序。也有一些函数可以执行外部程序，包括execv，它会退出Python解释器，并且将控制权交给被执行程序。还有popen，它可以创建与程序连接的类文件。
* os.sep模块变量是用于路径名中的分隔符
* os.linesep用于文本文件的字符串分隔符。
* urandom函数使用一个依赖于系统的“真”（至少是足够强度加密的）随机数的源。如果正在使用的平台不支持它，你会得到NotImplementError异常。

## fileinput
fileinput模块让你能够轻松地遍历文本文件的所有行

UNIX命令下
```Python
$ python some_script.py file1.text file2.text file3.text
```
这样可以一次对file1.txt到file3.txt文件中的所有进行遍历

|函数|描述|
|:-----------------------|:-----------------------|
|input([files[, inplace[, backup]]])|便于遍历多个输入流中的行|
|filename()|返回当前文件的名称|
|lineno()|返回当前（累计）的行数|
|filelineno()|返回当前文件的行数|
|isfirstline()|检查当前行是否是文件第一行|
|isstdin()|检查最后一行是否来自sys.stdin|
|nextfile()|关闭当前文件，移动到下一个文件|
|clos()|关闭序列|

* fileinput.filename函数返回当前正在处理的文件名(也就是包含了当前正在处理的文本行的文件)
* fileinput.lineno返回当前行的行数。这个数值是累计的，所以在完成一个文件的处理并且开始处理下一个文件的时候，行数并不会重置，而是将上一个文件的最后行数加1作为计数的起始。
* fileinput.filelineno函数返回当前处理文件的当前行数。每次处理完一个文件并且开始处理下一个文件时，行数都会重置为1，然后重新开始计数。
* fileinput.isfirstline函数在当前行是当前文件的第一行时返回真值，反之返回假值。
* fileinput.nextfile函数会关闭当前文件，跳到下一个文件，跳过的行并不计。在你知道当前文件已经处理完的情况下，这个函数就比较有用了————比如每个文件都包含经过排序的单词，而你需要查找某个词。如果已经在排序中推找到了这个词的位置，那么你就能放心地跳到下一个文件了。
* fileinput.close函数关闭整个文件链，结束迭代

## 集合、堆和双端队列
[集合]()





