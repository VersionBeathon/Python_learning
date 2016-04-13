# Python数据库编程接口（API）

## 全局变量
* Python DB API的模块特性

|变量名|用途|
|:---------------|:---------------|
|apilevel|所使用的Python DB API版本|
|threadsafety|模块的线程安全等级|
|paramstyle|在SQL查询中使用的参数风格|

* API(apilevel)级别是个字符串常量，提供正在使用的API版本号。对于DBAPI 2.0版本来说，其值可能是'1.0'或'2.0'。如果这个变量不存在，那么该模块就不兼容2.0版本的API，只能假定当前使用的是1.0版本的API。
* 线程安全性等级(threadsafety)是个取值范围为0~3的整数。0表示线程完全不共享模块，而3表示模块是完全线程安全的。1表示线程本身可以共享模块，但不对链接共享。如果不使用多个线程（多数情况下可能不会这么做），那么完全不用担心这个变量。
* 参数风格(paremstyle)表示在执行多次类似查询的时候，参数是如何被拼接到SQL查询中的。值'format'表示标准的字符串格式化（使用基本的格式代码），可以在参数中进行拼接的地方插入%s。而值'pyformat'表示扩展的格式代码，用于字典拼接中，比如%(foo)。除了Python风格之外，还有第三种结合方式：'qmark'的意思是使用问号，而'numeric'表示使用:1或者:2格式的字段（数字表示参数的序号），而'named'表示:foobar这样的字段，其中foobar为参数名。如果foobar为参数名。如果参数风格看起来有些让人迷惑，别担心。对于基础的程序来说，不会用到这些参数，如果需要了解特定的数据库接口如何处理参数，在相关的文档中会进行解释。

## 异常
API中定义了一些异常类，以便尽可能进行错误处理。

* 在DB API中使用的异常

|异常|超类|描述|
|:------------|:-----------|:--------------|
|StandardError||所有异常的泛型基类|
|Warning|StandardError|在非致命错误发生时引发|
|Error|StandardError|所有错误条件的泛型超类|
|InterfaceError|Error|关于接口而非数据库的错误|
|DatabaseError|Error|与数据库相关的错误的基类|
|DataError|DatabaseError|与数据相关的问题，比如值超出范围|
|OperationalError|DatabaseError|数据库内部操作错误|
|IntegrityError|DatabaseError|关系完整性收到影响，比如键检查失败|
|InternalError|DatebaseError|数据库内部错误，比如非法游标|
|ProgrammingError|DatabaseError|用户编程错误，比如未找到表|
|NotSupportedError|DatabaseError|请求不支持的特性（比如回滚）|

## 链接和游标
为了使用底层的数据库系统，首先必须要链接到它

### connect函数的常用参数

|参数名|描述|是否可选|
|:------------|:---------------|:-----------------|
|dsn|数据源名称，给出该参数标书数据库依赖|否|
|user|用户名|是|
|password|用户密码|是|
|host|主机名|是|
|database|数据库名|是|

### connect函数返回链接对象。这个对象表示目前和数据库的会话。链接对象支持的方法如下：

|方法名|描述|
|:-------------------|:---------------|
|close()|关闭链接之后，链接对象和它的游标均不可用|
|commit()|如果支持的话就提交挂起的事物，否则不做任何事|
|rollback()|回滚挂起的事物（可能不可用）|
|cursor()|返回链接的游标对象|

* rollback方法可能不用，因为不是所有的数据库都支持事务（事务是一系列动作）。若果可用，那么它就可以“撤销”所有未提交的事务。
* commit方法
* cursor方法将我们引入另外一个主题：游标对象。通过游标执行SQL查询并检查结果。游标比链接支持更多的方法，而且可能在程序中更好用。

### 游标对象：通过游标执行SQL查询并检查结果

* 游标对象方法

|名称|描述|
|:---------------|:--------------------|
|callproc(name[, params])|使用给定的名称和参数（可选）调用已命名的数据库过程|
|close()|关闭游标之后，游标不可用|
|execute(oper[, params])|执行一个SQL操作，可能带有参数|
|executemany(oper, pseq)|对序列中的每个参数集执行SQL操作|
|fetchone()|吧查询的结果集中的下一行保存为序列，或者None|
|fetchmany([size])|获取查询结果集中的多行，默认尺寸为arrysize|
|fetchall()|将所有（剩余）的行作为序列可选的序列|
|nextshell()|跳至下一个可用的结果集（）|
|setinputsizes(sizes)|为参数预先定义内存区域|
|setoutputsize(seze[, col])|为获取的大数据值设定缓冲区尺寸|

* 游标对象特性

|名称|描述|
|:------------------------|:------------------------------|
|description|结果列描述的序列，只读|
|rowcount|结果中的行数，只读|
|arraysize|fetchmany中返回的行数，默认为1|

## 类型

* DB API构造函数和特殊值

|名称|描述|
|:--------------|:---------------|
|Date(year, month, day)|创建保存日期值的对象|
|Time(hour, minute, second)|创建保存时间值的对象|
|Timestamp(y, mon, d, h, min, s)|创建保存时间戳的对象|
|DateFromTicks(ticks)|创建保存自新纪元以来秒数的对象|
|TimeFromTicks(ticks)|创建保存来自秒数的时间值的对象|
|TimestampFromTicks(ticks)|创建保存来自秒数的时间戳值的对象|
|Binary(string)|创建保存二进制字符串值的对象|
|STRING|描述基于字符串的列类型(比如CHAR)|
|BINARY|描述二进制列（比如LONG或RAW）|
|NUMBER|描述数字列|
|DATETIME|描述日期/时间列|
|ROWID|描述ID列|


