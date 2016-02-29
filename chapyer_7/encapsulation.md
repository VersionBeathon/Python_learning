# 封装：

封装是指向程序中的其他部分隐藏对象的具体实现细节的原则。听起来游戏像多态，也是使用对象而不用知道其内部细节，两者概念有些相似，因为它们都是抽象原则，他们都会帮助处理程序组件而不用过多关心多余细节，就像函数一样。
但封装并不等同于多态。多态可以让用户对于不知道是什么类(对象类型)的对象进行方法调用，而封装是可以不用关心对象是如何构建的而直接进行使用。

1. 假设有个叫做OpenObject的类
```Python
>>>o = OpenObject() # This is how we create object...
>>>o.setName('Sir lancelot')
>>>o.getName()
'Sir Lancelot'
#创建了一个对象后，将变量o绑定到该对象上就可以使用setName和getName方法
```

2. 假设变量o将它的名字存储在全局变量globalName中
```Python
>>>globalName = 'Sir Gumby'
>>>o.getName()
'Sir Gumby'
```

3. 创建了多个OpenObject实例就会出现问题，变量相同，可能会混淆
```Python
>>>o1 = OpenObject()
>>>o2 = OpenObject()
>>>o1.setName('Robin Hood')
>>>o2.getName() # 设定一个名字后，其他的名字也就自动设定了。
'Robin Hood'
```

基本上，需要将对象进行抽象，调用方法的时候不用关系其他的东西，比如它是否干扰了全局变量。可以将名字“封装”在对象内，将其作为特性存储。
正如方法一样，特性是作为变量构成对象的一部分，事实上方法更像是绑定到函数上的属性

4. 如果不用全局变量而用特性重写类，并且重命名为CloseObject
```Python
>>>c = ClosedObject()
>>>c.setName('Sir Lancelot')
>>>c.getName()
'Sir Lancelot'
# 值可能还是存储在全局变量中，在重创建另一个对象
>>>r = ClosedObject()
>>>r.setName('Sir Robin')
>>>r.getName()
'Sir Robin'
# 新的对象名称已经正确设置，第一个对象也没有改变
>>>c.getName()
'Sir Lancelot'
```

对象的状态由它的特性（比如名称）来描述。对象的方法可以改变它的特性。所以就像是将一大堆函数（方法）捆在一起，并且给予他们访问变量（特性）的权利，它们可以在函数调用之间保持保存的值。