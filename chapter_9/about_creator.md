# 通用生成器
生成器是一个包含yield关键字的函数。当它被调用时，在函数体重的代码不会被执行，而会返回一个迭代器。每次请求一个值，就会执行生成器中的代码，知道遇到一个yield或者return语句。yield语句一位置应该生成一个值。return语句一位置生成器要停止执行。
生成器是由两部分组成：生成器的函数和生成器的迭代器。生成器的函数使用def语句定义的，包含yie的部分，生成器的迭代器是这个函数返回的部分。按一种不是很准确的说法，两个实体经常被当做一个，和起来叫做生成器。
```Python
>>>def simple_generator():
        yield 1
>>>simple_generator
<function simple_generator at 153b44>
>>>simple_generator()
<generator object at 1510b0>
```

# 生成器方法
生成器的新特征是在开始运行后为生成器提供值的能力。表现为生成器和“外部世界”进行交流的渠道，要注意下面两点。
* 外部作用域访问生成器的send方法，就像访问next方法一样，只不过前者使用一个参数（要发送的“消息”——任意对象）。
* 在内存则挂起生成器，yield现在·作为表达式而不是语句使用，换句话说，当生成器重新运行的时候，yield方法返回一个值，也就是外部通过send方法发送的值。如果next方法被使用，那么yie方法返回None。
注意：使用send方法只有在生成器挂起之后才有意义（也就是说在yield函数第一次被执行后）
一个简单的例子：
```Python
def repeater(value):
    while true:
        new = (yield value)
        if new is not None = value = new
r = repeater(42)
r.next()
42
r.send("hello,world!")
"hello,world!"
```

# 生成器另外两个方法：
* throw方法（使用异常类型调用，还有可选的值以及回溯对象）用于在生成器内引发一个异常（在yield表达式中）
* close方法（调用时不用参数）用于停止生成器