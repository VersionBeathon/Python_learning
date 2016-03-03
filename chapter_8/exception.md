# 异常
## 什么是异常：

Python用异常对象（exception object）来表示异常情况。遇到错误后，会引发异常。如果异常对象并未被处理货捕捉，程序就会用所谓的回溯（traceback，一种错误信息）终止执行：

```Python
>>>1/0
Traceback (most recent call last):
 File "<stdin>", line 1, in ?
 ZeroDivisionError: integer division or modulo by zero
```

如果这些错误信息就是异常的全部功能，那么它也就不必存在了。事实上，每个异常都是一些；类（本例中是ZeroDivision）的实例，这些实例可以被引发，并且可以用很多种方法进行捕捉，使得程序可以捉住错误并且对其进行处理，而不是让整个程序失效。

## 按自己的方式出错

异常可以在某些东西出错时自动引发。在学习如何处理异常之前，先看一下自己如何引发异常，以及创建自己的异常类型。

## raise语句

为了引发异常，可以使用一个类（应该是Exception的子）或者实例参数调用raise语句。使用类时。程序会自动创建类的一个实例。下面是一些简单的例子，使用内建的Exception异常类：

```Python
>>> raise Exception
Traceback (most recent call last):
 File "<stdin>", line 1, in ?
Exception
>>> raise Exception('hyperdrive overland')
Traceback (most recent call last):
 File "<stdin>", line 1, in ?
Exception: hyperdrive overland
```

第一个例子raise Exception引发了一个没有任何有关错误信息的普通异常。后一个李子红，则添加；了错误信息hyperdrive overland。
内建的异常类有很多。Python库参考手册的Built-in Expression一节中有关于他们的描述。用交互式解释器也可以分析它们，这些内建异常都可以在exception模块（和内建的命名空间）中找到。可以使用dir函数列出模块的内容。

```Python
import exceptions
dir(exceptions)
['ArithmeticError', 'AssertionError', 'AttributeError', ...]
# 所有异常都可以用在raise语句中
>>>raise ArithmeticError
Traceback (most recent call last):
 File "<stdin>", line 1, in ?
ArithmeticError 
```

一些最重要的内建异常类：
|类名|描述|
|:-----------------------------------|:-------------------------------------|
|Exception|所有异常的基类|
|AttributeError|特性引用或复制失败时引发|
|IOError|试图打开不存在文件（包括其他情况）时引发|
|IndexError|在使用徐累中不存在的索引时引发|
|KeyError|在使用映射中不存的键时引发|
|NameError|在找不到名字（变量）时引发|
|SyntaxError|在代码为错误形式时引发|
|TypeError|在内建操作或者函数应用于错误类型的对象时引发|
|ValueError|在内建操作或者函数应用于正确类型的对象，但是该对象使用不合适的值时引发|
|ZeroDivisionError|在除法或者模除操作的第二个参数为0时引发|

## 自定义异常类

尽管内建的异常类已经包括了大部分的情况，而且对于很多要求都已经足够了，但有些时候还是需要创建自己的异常类。比如超光速推进装置过载（hyperdrive overland）的例子中，如果有个具体的HyperDriveError类来表示超光速推进装置的错误状态是不是更自然一些。

如何创建自己的异常类：要确保从Exception类继承，编写一个自定义异常类入下
```Python
class SomeCustomException(Exception): pass
```

