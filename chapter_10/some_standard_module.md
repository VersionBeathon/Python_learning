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

### [集合](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/gather.py)

### 堆

它是优先队列的一种。使用优先队列能够以任意顺序增加对象，并且能在任何时间（可能在增加对象的同时）找到（也可能是移除）最小的元素，也就是说它比用于列表的min方法要有效的多。

事实上，Python中并没有独立的堆类型，只有一个包含一些堆操作函数的模块，这个模块叫做heapq（q是queue的缩写，即队列），包括6个函数，其中前4个直接和堆操作相关。

|函数|描述|
|:-------------------------|:----------------------|
|heappush(head, x)|将x入堆|
|heappop(heap)|将堆中最小的元素弹出|
|heapify(heap)|将heap属性强制应用到任意一个列表|
|heapreplace(heap, x)|将堆中最小的元素弹出，同时将x入堆|
|nlargest(n ,iter)|返回iter中第n大的元素|
|nsmallest(n ,iter)|返回iter中第n小的元素|

* [heappush](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/examlple_heapq.py)函数用于增加堆的项。注意：不能将它用于任何之前讲述的列表中，它只能用于通过各种堆函数建立的列表中。原因是元素的顺序很重要。元素的顺序并不像看起来那么随意。它们虽然不是严格排序的，单是也是有规则的：位于i位置上的元素总比i/2位置处的元素大。这是底层堆算法的基础，而这个特性称为堆属性
* [heappop](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/examlple_heapq.py)函数弹出最小的元素，一般来说都是在索引0处的函数，并且会确保剩余元素中最小的那个占据这个位置（保持刚才提到的堆属性）
* [heapify](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/examlple_heapq.py)函数使用任意列表作为参数，并且通过尽可能少的位移操作，将其转换为合法的堆。如果没有用heappush建立推，那么在使用heappush和heappop前应该使用这个函数
* [heapreplace](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/examlple_heapq.py)函数不像其他函数那么常用。它弹出堆得最小元素，并将新元素推入。这样做比调用heappo之后再调用heappush更高效。
* heapq模块中剩下的两个函数nlargest(n,iter)和nsmallest(n,iter)分别用来寻找任何可迭代对象iter中第n大或第n小的元素。

### 双端队列
[双端队列](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/examlple_deque.py)(double-ended queue,或称deque)在需要按照元素增加的顺序来移除元素时非常有用
。Python2.4增加了collection模块，它包括deque类型。

双端队列好用的原因是它能够有效地在开头（左侧）增加和弹出元素，这是在列表中无法实现的。除此之外，使用双端队列的好处还有:能够优先第旋转(rotate)元素(也就是将它们左移或右移，使头尾相连)。双端队列对象还有extend和extendleft方法，extend和列表的extend方法差不多，extendleft则类似于appandleft。注意，extendleft使用的可迭代对象中的元素会反序出现在双端队列中。

## time

time模块所包含的函数能够实现以下功能：获得当前时间、操作时间和日期、从字符串读取时间以及格式化时间为字符串。日期可以用实数（从“新纪元”的1月1日0点开始计算到现在的描述，新纪元是一个与平台相关的年份，堆Unix来说是1970年），或者包含有9个整数的远足。这些整数的意义如下所示，比如，元组：
(2008, 1, 21, 12, 2, 56, 0, 21, 0)
标识2008年1月21日12时2分56秒，星期一，并且是当年的第21天（无夏令时）。

### Python日期元组的字段含义：

|索引|字段|值|
|:---------|:--------|:-------|
|0|年|比如2000， 2001， 等等|
|1|月|范围1~12|
|2|日|范围1~31|
|3|时|范围0~23|
|4|分|范围0~59|
|5|秒|范围0~61|
|6|周|当周一为0时，范围0~6|
|7|儒略日|范围1~366|
|8|夏令时|0、1、或-1 -1是决定是否为夏令时的旗帜|

秒的范围是0~61是为了应付闰秒和双闰秒。夏令时的数字是布尔值（真或假），但是如果使用了-1，mktime(该函数将这样的远足转换为时间戳，它包含从新纪元开始以来的秒数)就会工作正常。

### time模块中最重要的函数：

|函数|秒数|
|:---------------|:----------------|
|asctime([tuple])|将时间远足转换为字符串|
|localtime([secs])|将秒数转换为日期元组，以本地时间为准|
|mktime(tuple)|将时间元组转换为本地时间|
|sleep(secs)|休眠（不做任何事情）secs秒|
|strptime(string[, format])|将字符串解析为时间元组|
|time()|当前时间(新纪元开始后的秒数，以UTC为准)|

* 函数time.asctime()将当前时间格式化为字符串：
```Python
>>>time.asctime()
'Fri Dec 21 05:41:27 2008'
```
* 函数time.localtime将实数（从新纪元开始计算的秒数）转换为本地时间的日期元组。如果想获得全球统一时间，则可以使用gmtime。
* 函数time.sleep让解释器等待给定的描述。
* time.strptime将asctime格式化过的字符串转换为日期元组（可选的格式化参数所遵循的规则与strftime的一样，详情请参见标准文档）
* 函数time.time使用自新纪元开始计算的秒数返回当前（全球统一）时间，尽管每个平台的新纪元可能不同，但是你仍然可以通过记录某件事情（比如函数调用）发生前后time的结果来对该事件计时，然后计算差值。 

## random
random模块包括返回随机数的函数，可以用于模拟或者用于任何产生随机输出的程序。（任何计算机产生的随机数都是伪随机数）。 

|函数|描述|
|:-----------------------|:-------------------|
|random()|返回 0<n<=1 之间的随机实数n|
|getrandbits(n)|以长整数形式返回n个随机位|
|uniform(a, b)|返回随机实数n，其中a<=n<=b |
|randrange([start], stop, [step])|返回range(start,stop,step)中的随机数|
|choice(seq)|c从序列seq中返回任意随机元素|
|shuffle(seq[, random])|原地1指定序列seq|
|sample(seq, n)|从序列seq中选择n个随机且独立的元素|

* 函数random.random时最基本的随机函数之一，它只是返回0~1的伪随机数n。
* random.getrandbits以长整型形式返回给定的位数(二进制数)。如果处理的是真正的随机事物（比如加密），这个函数尤为有用。
* 函数random.uniform提供两个数值参数a和b，它会返回在a~b的随机(平均分布的)实数n。则能够产生该范围内的随机整数
* 函数random.choice从给定序列中(均一第地)选择随机元素
* 函数random.shuffle将给定（可变）序列的元素进行随机位移，每种排列的可能性都是近似相等的。
* 函数random.sample从给定序列中(均一地)选择给定数目的元素，同时确保元素互不相同。
* [example_of_random&&time]()
* [dice]()
* [deck]()

## shelve

shelve.open函数返回的对象并不是普通的映射，这一点尤其要注意，如下所示：

```Python
>>>import shelve
>>>s = shelve.open('test.dat')
>>>s['x'] = ['a', 'b', 'c']
>>>s['x'].append('d')
>>>s['x']
['a', 'b', 'c']
```
显然d并没有添加进去：当你在shelf对象中查找元素的时候，这个对象都会根据已经存储的版本进行重新构建，当你将元素赋给某个键的时候，它就被存储了。上述例子中执行的操作如下:
* 列表['a', 'b', 'c']存储在键x下；
* 获得存储的标识，并且根据它来创建新的列表，而'd'被添加到这个副本中。修改的版本还没有被保存！
* 最终，在此获得原始版本————没有'd'
* 
为了正确地始终shel模块修改存储的对象，必须将临时变量绑定到获得的副本上，并且在它被修改后重新存储这个副本：

```Python
>>>temp = s['x']
>>>temp.append('d')
>>>s['x'] = temp
>>>s['x']
['a', 'b', 'c', 'd']
```

### [简单的数据库示例](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/database.py)

## re(正则表达式)
* 过段时间整理，这部分比较难（又乱又难懂，先研究一段时间）


