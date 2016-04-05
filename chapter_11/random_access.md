# 随机访问
本章中的例子把文件都当成流来操作，也就是说只能按照从头到尾的顺序读取数据。实际上，在文件中随机移动读取位置也是可以的，可以使用类文件对象的方法seek和tell来直接访问感兴趣的部分(这种做法称为随机访问)。

seek(offset[, whence]):这个方法把当前位置（进行读和写的位置）移动到offset和whence定义的位置。offset类是一个字节（字符）数，标识偏移量。whence默认是0，标识偏移量是从文件开头开始计算的（偏移量必须是非负的）。whence可能被设置为1（相当于当前位置的移动，此时偏移量offset可以是负的）或者2（相对于文件结尾的移动）。

例如：
```Python
>>> f = open(r'c:\text\somefile.txt', 'w')
>>> f.write('01234567890123456789')
>>> f.seek(5)
>>> f.write('Hello, World!')
>>> f.close()
>>> f = open(r'c:\text\somefile.txt')
>>> f.read()
'01234Hello, world!89'
```
tell方法返回当前文件的位置如下所示：
```Python
>>> f = open(r'c:\text\somefile.txt')
>>> f.read(3)
'012'
>>> f.read(2)
'34'
>>>ｆ.tell()
5L
```
f.tell方法返回的数字在这种情况下是一个长整数。但不是所有的情况都是这样。
