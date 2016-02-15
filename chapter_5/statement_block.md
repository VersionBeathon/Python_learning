#语句块：缩排的乐趣
***
语句块是在条件为真（条件语句）时执行或者执行多次（循环语句）的一组语句。在代码前防止空格来缩进语句即可创建语句块

伪代码：
```Python
this is a line
this is another line:
     this is another block
     continuting the same block
     the last line of this block
phew, there we escaped the inner block
```

在Python中，冒号（:）用来表示语句块的开始，块中每一个语句都是缩进的（缩进量相同)。当回退到和已经闭合的块一样的缩进量时，就表示当前块已经结束了 