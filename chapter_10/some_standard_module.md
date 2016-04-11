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

* [heappush](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/example_heapq.py)函数用于增加堆的项。注意：不能将它用于任何之前讲述的列表中，它只能用于通过各种堆函数建立的列表中。原因是元素的顺序很重要。元素的顺序并不像看起来那么随意。它们虽然不是严格排序的，单是也是有规则的：位于i位置上的元素总比i/2位置处的元素大。这是底层堆算法的基础，而这个特性称为堆属性
* [heappop](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/example_heapq.py)函数弹出最小的元素，一般来说都是在索引0处的函数，并且会确保剩余元素中最小的那个占据这个位置（保持刚才提到的堆属性）
* [heapify](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/example_heapq.py)函数使用任意列表作为参数，并且通过尽可能少的位移操作，将其转换为合法的堆。如果没有用heappush建立推，那么在使用heappush和heappop前应该使用这个函数
* [heapreplace](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/example_heapq.py)函数不像其他函数那么常用。它弹出堆得最小元素，并将新元素推入。这样做比调用heappo之后再调用heappush更高效。
* heapq模块中剩下的两个函数nlargest(n,iter)和nsmallest(n,iter)分别用来寻找任何可迭代对象iter中第n大或第n小的元素。

### 双端队列
[双端队列](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/example_deque.py)(double-ended queue,或称deque)在需要按照元素增加的顺序来移除元素时非常有用
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
* [example_of_random&&time](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/example_of_random.py)
* [dice](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/dice.py)
* [deck](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/deck.py)

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

re模块中一些重要的函数

|函数|描述|
|:-------------|:------------------|
|compile(pattern[, flags])|根据包含正则表达的字符串创建模式对象|
|search(pattern, string[, plags])|在字符串中需要模式|
|match(pattern, string[, flags])|在字符串的开始处匹配模式|
|split(pattern, string[, maxsplit=0])|根据模式的匹配项来分割字符串|
|findall(pattern,string)|列出字符串中模式的所有匹配项|
|sub(pat, repl, stringh[, count=0])|将字符串中所有pat的匹配项用repl替换|
|escape(string)|将字符串中所有特殊正则表达式字符转义|

* re.compile将正则表达式（以字符串书写的）转换为模式对象，可以实现更有效率的匹配。如果在调用search或者match函数的时候使用字符串表示的正则表达式，它们也会在内部将字符串转换为正则表达式对象。使用compile完成一次转换之后，在每次使用模式的时候就不用进行转换。模式对象本身也有查找/匹配的函数，就像方法一样，所以re.search(pat, string)(pat使用字符串表示的正则表达式)等价于pat.search(string)(pat使用compile创建的模式对象)。经过compile转换的正则表达式对象也能用于普通的re函数。
* re.search会在给定字符串中寻找第一个匹配给定正则表达式的子字符串。一旦找到子字符串，函数就会返回MatchObject(值为True)，否则返回None(值为False)。因为返回值的性质，所以该函数可以用在条件语句中，如下所示
```Python
if re.search(pat, string):
    print 'Found it'
```
* 函数re.match会在给定字符串的开头匹配正则表达式。因此，match('p', 'python')返回真（即匹配对象MatchObject），而re.match('p','www.python.org')则返回假(None)。
* re.split会根据模式的匹配项来分割字符串。它类似于字符串方法splite，不过是用完整行的正则表达式代替了固定的分隔符字符串。比如字符串方法split允许用字符串','的匹配项来分割字符串，耳机re.split则润徐用任意长度的逗号和空格序列来分割字符串:
```Python
>>> some_text = 'alpha, beta,,,,gama delta'
>>> re.split('[, ]+', some_text)
['alpha', 'beta', 'gamma', 'delta']
# maxsplite参数表示字符串最多可以分割的次数
>>> re.split('[, ]+', some_text， maxsplit=2)
['alpha', 'beta', 'gamma   delta']
>>> re.split('[, ]+', some_text， maxsplit=1)
['alpha', 'beta,,,,gamma   delta']
```
* re.findall以列表形式返回给定模式的所有匹配项。比如，要在字符串中查找所有的单词，可以如下
```Python
>>> pat = '[a-zA-Z]+'
>>> text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
>>> re.findall(pat, text)
['Hmm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']
# 查找标点符号
>>> pat = r'[.?\-",]+' # 转义-
>>> re.findall(pat, text)
['"', '...', '--', '?', ',', '.']
```
* re.sub的作用在于：使用给定的替换内容将匹配模式的子字符串（最左端并且非重叠的子字符串）替换掉。
```Python
>>> pat = '{name}'
>>> text = 'Dear {name}...'
>>> re.sub(pat, 'Mr. Gumby', text)
'Dear Mr. Gumby'
```
* re.escape可以对字符串中所有可能被注释为正则运算符的字符进行转义的应用函数。如果字符串很长且包含很多特殊字符，而你又不想输入一大堆反斜线，或者字符串来自于客户。且要用作正则表达式的一部分的时候，可以使用这个函数。
```Python
>>> re.escape('www.python.org')
'www\\.python\\.org'
>>> re.escape('But where is the ambiguity?')
'But\\ where\\ is\\ the\\ ambiguity?'
```

### 匹配对象和组

对于re模块中那些能够对字符串进行模式匹配的函数而言，当能找到匹配项的时候，它们都会返回MatchObject对象。这些对象包括匹配模式的子字符串写的信息。它们还包含了哪个模式匹配了字符串哪部分的信息——这些“部分”叫做组(group)。

简而言之，组就是放置在括号内的子模式。组的序号取决于它左侧的括号书。组0就是整个模式，所以在下面模式中：
```Python
'There (was a (wee) (cooper)) who (lived in Fyfe)'
```
包含下面这些组：
```Python
0 There was a wee cooper who lived in Fyfe
1 was a wee cooper
2 wee
3 cooper
4 lived in Fyfe
```
一般来说，如果组中包括诸如通配符或者重复运算符之类的特殊字符，那么你可能会对是什么与给定组实现了匹配感兴趣，例如
```Python
r'www\.(.)\.com$'
```
组0包含了整个字符串，而组1则包含了位于'www.'和'.com'之间的所有内容。

re匹配对象的一些重要方法：

|方法|描述|
|:--------|:--------|
|group([group1, ...])|获取给定子模式（组）的匹配项|
|start([group])|返回给定组的匹配项的开始位置|
|end([group])|返回给定组的匹配项的结束位置（和分片一样，不包括组的结束位置）|
|span([group])|返回一个组的开始和结束位置|

* group方法返回模式中与给定组的匹配的(子)字符串。如果没有给出组好，默认组为组0.如果给定一个组好（或者只用默认的0），会返回单个字符串。否则会将对应给定组数的字符串作为元组返回。
* start方法返回给定组匹配项的开始索引（默认为0，即整个模式）。
* 方法end类似于start，但是返回结果是结束索引加1。
* 方法span以元组（start, end）的形式返回给定组的开始和结束位置的索引（默认为0， 即整个模式）。
```Python
>>> m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
>>> m.group(1)
'python'
>>> m.start(1)
4
>>> m.end(1)
10
>>> m.span(1)
(4, 10)
```

### 作为替换的组号和函数
在使用re.sub迭代第一个例子中，只是把一个字符串用其他的内容替换调了。正则表达式很有用，因为它们允许以更灵活的方式搜索，同时它们也允许进行功能强大的替换。

见证re.sub强大功能的最简单方式就是在替换字符串中使用组号。在替换内容中以'\\\n'形式出现的任何转义序列都会被模式中与组n匹配的字符串替换掉。假如，假设要把'*something*'用'<em>something</em>'替换掉，前者是在普通文档中进行强调的常见方法，而后者则是相应的HTML代码（用于网页）。首先创建正则表达式：
```Python
>>> emphasis_pattern = r'\*(^\*)+\*'
>>> re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')
'Hello, <em>world</em>!'
```
将函数作为替换内容可以让替换功能变得更加强大。MathObect将作为函数的唯一参数、返回的字符串将会用做替换内容。换句话说，可以对匹配的字符串做任何事，并且可以细化处理过程，以生成替换内容。

### 寻找Email发信人的程序
```Python
import fileinput, re
pat = re.compile('From:(.*)<.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:
        print m.group(1)
```
运行：
```Unix
$ python find_sender.py message.eml
```
* 用compile函数处理了正则表达式，让处理过程更有效率；
* 将需要取出的子模式放在圆括号中作为元组；
* 使用非贪婪模式对邮件地址进行匹配，只有最后一对尖括号复合要求
* 使用 `$` 符号表明我要匹配整行
* 使用if语句确保在试图从特定组中取出匹配内容之前，的确进行了匹配。

#### 列出头部信息中所有的Email地址
```Python
import fileinput, re
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
address = set()
for line in fileinput.input():
    for address in pat.finall(line):
        addresses.add(address)
    for address in sorted(addresses):
    print address
```
运行结果：
```Uinx
Mr.Gumby@bar.baz
foo@bar.baz
foo@baz.com
magnus@bozz.floop
```

### 模版系统实例
[template.py](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_10/template.py)
简单来说，程序作了下面的事情：
* 定义了用于匹配字段的模式。
* 创建充当模版作用域的字典。
* 定义具有以下功能的替换函数。
    1. 强组1从匹配中取出，放入code中；
    2. 通过将作用域字典作为命名空间来对code进行求值，将结果转换为字符串返回。如果成功，字段就是个表达式，一切正常。否则（引发SyntaxError异常），跳到下一步；
    3. 执行在相同命名空间（作用域字典）内的字段来对表达式求值，返回空字符串（因为赋值语句没有对任何内容进行求值）。
* 只用fileinput读取所有可用的行，将其放入列表，组成一个大字符串。
* 将所有field_pat的匹配项用re.sub的替换函数进行替换，并且打印结果。

## 其他有趣的标准模块
* functiontools:可以从这个库找一些功能，让你能够通过部分参数来使用某个函数（部分求值），稍后再为剩下的参数提供数值。在Python3.0中，filter和reduce包含在该模块中。
* difflib:这个库让你可以计算两个序列“最像”的那个。difflib可以用于创建简单的搜索程序。
* hashlib:通过这个模块，可以通过字符串计算小“签名”（数字）。如果为两个不同的字符串计算出了签名，几乎可以确保这两个签名完全不同。该模块可以用于大文本文件，通知在加密和安全性方面有很多用途。
* csv:CSV是逗号分隔值（Comma-Separated Values）的缩写，这是一种很多程序（比如很多电子表格和数据库程序）都可以用来存储表格式数据的简写格式。它主要用于在不同程序间交换数据。使用csv模块可以轻松读写CSV文件，同时以显而易见的方式来处理这种格式的某些很难处理的地方。
* timeit、profile和trace：timeit模块（以及它的命令行脚本）是衡量代码片段运行时间的工具。它有很多神秘的共很难过，应该用它来代替time模块进行性能测试。profile模块（和伴随模块pstats）可用于代码片段效率的全面分析。trace模块（和程序）可以提供总的分析（也就是代码哪部分执行了，哪部分没执行）。在写测试代码的时候很有用。
* datetime:如果time模块不能满足时间追踪方面的需求，那么datetime可能就有用武之地。它支持特殊日期和时间对象，让你能够以多种方式对它们进行构建和联合。它的结构在很多方面比time的接口要更加直观。
* itertools:它有很多工具用来创建和联合迭代器（或者其他可迭代对象），还包括实现以下功能的函数：将可迭代的对象链接起来、创建返回无限连续整数的迭代器（和range类似，但没有上限），从而通过重复访问可迭代对象进行循环等等。
* logging:通过简单的print语句打印出程序的哪些方面很有用。如果希望对程序进行跟踪但又不想打印出太多调试内容，那么久需要将这些信息写入日志文件中。这个模块提供了一组标准的工具，以便让开发人员管理一个或多个核心的日志文件，同时还对日志信息提供了多层系的优先级。
* getopt和optparse:在UNIX中，命令行程序经常使用不同的选项(option)或者开关(switches)运行（Python解释器就是个典型的例子）。这些信息都可以在sys.argv中找到，但是自己要正确处理它们就没有那么简单。针对这个问题，getop库是个切实可行的解决方案，而optparse则更新，更强大并且更易用。
* cmd:使用这个模块可以编写命令解释器，就像Python的交互式解释器一样。你可以自定义命令，以便让用户能够通过提示符来执行。