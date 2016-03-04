# 要点
* 将属于一类的对象放在一起。如果一个函数操纵一个全局变量，那么两者最好都在类内作为特性和方法出现。
* 不要让对象过去亲密。方法应该只关心自己实例的特性。让其他实例管理自己的状态
* 要小心继承，尤其是多重继承。继承机制有时很有用，但也会在某些情况下让事情变得过去复杂。多继承难以正确使用，更难以调试。
* 简单就好。让你的方法小巧。一般来说，多数方法能在30秒内被读完（以及理解），尽量将代码行数控制在一页或者一屏之内。

# 当考虑需要什么类以及类要有什么方法时，应该尝试下面的方法：
* 写下问题的描述（程序要做什么），把所有名词、动词和形容词加下划线。
* 对于所有的名词，用作可能的类
* 对于所有的动词，用作可能的方法。
* 对于所有形容词，用作可能的特性。
* 把所有方法和特性分配到类。

# 考虑类和对象之间的关系（比如继承或协作）以及它们的作用，可以用一下步骤精炼模型。
* 写下（或者想象）一系列的使用实例，也就是程序应用时的场景，试着包括所有的功能。
* 一步步考虑每个使用实例，保证模型包括所有需要的东西。如果有遗漏的话就添加进来。如果某处不太正确则改正。继续指导满意为止

当认为已经有了可以应用的模型时，那么就可以开工了。可能需要修正自己的模型，或者是程序的一部分