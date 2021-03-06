# 继承
继承是另一个懒惰（褒义）的行为。程序员不想把同一段代码输入好几次。之前使用的函数避免了这种情况，但现在又有几个更微妙的问题。如果已经有了一个雷，而又想创建一个非常类似的，新的类可能只是添加几个方法。在编写新类时，又不想把旧类的代码全部复制过去。

比如说有个Shape类，可以用来在屏幕上画出指定的形状。现在需要创建一个叫做Rectangle的类，它不但可以在屏幕上画出制定的形状，而且汉能计算该形状的面积。但又不想把Shape里面已经写好的draw方法再写一次。可以让Rectangle从Shape类继承方法。在Rectangle对象上调用draw方法时，程序会自动从Shape类调用该方法。
