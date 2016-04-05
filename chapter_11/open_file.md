# 打开文件
open函数用来打开文件，语法如下：

open(name[, mode[, buffering]])

open函数使用一个文件名作为唯一的强制参数，然后返回一个文件对象。模式(mode)和缓冲(buffering)参数都是可选的。

因此，假设有一个名为somefile.txt的文本文件（可能使用文本编辑器创建的），其存储路径是c:\text(或者Unix下的~/text)，那么可以像线面这样打开文件：
```Python
>>> f = open(r'C:\text\somefile.txt')
```
如果文件不存在，则会看到一个类似下面这样的异常回溯:
```Python
Traceback (most recent call last):
    File "<pyshell#0>", line 1, in ?
IOError: [Errno 2] No such file or directory: "C:\\text\\somefile.txt"
```


## 文件模式
open函数中模式参数的常用值：

|值|描述|
|:------------|:-----------|
|'r'|读模式|
|'w'|写模式|
|'a'|追加模式|
|'b'|二进制模式(可添加到其他模式中使用)|
|'+'|读/写模式(可添加到其他模式中使用)|

## 缓冲

open函数的第3个参数(可选)控制着文件的缓冲。如果参数是0(或者是False),I/O(输入/输出)就是无缓冲的(所有的读写操作都直接针对硬盘)；如果是1(或者是True)，I/O就是有缓冲的(意味着Python使用内存来代替硬盘，让程序更快，只用使用flush或者close时才会更新硬盘上的数据)。大于1的数字代表缓冲区的大小(单位是字节)，-1(或者时任何负数)代表使用默认的缓冲区大小。