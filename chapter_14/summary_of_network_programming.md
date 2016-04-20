# 小节

* 套接字和socket模块。套接字程序（进程）之间进行通信的信息通道，可能会通过网络来通信。socket模块给提供了对客户端和服务器端套接字的低级访问功能。服务器端套接字会在制定的地址监听客户端的连接，而客户机是直接连接的。
* urllib和urllib2.这些模块可以在给出数据源的URL时让从不同的服务器读取和下载数据。urllib模块是一个简单一些的实现，而urllib2是可扩展的，而且很强大。两者都通过urlopen等简单的函数来工作
* SocketServer矿建。这是一个同步的网络服务器基类。位于标准库中，使用它可以很容易地编写服务器。它甚至用CGI支持简单的Web服务（HTTP）。如果想同时处理多个连接，可以使用分叉和线程来处理混入类。
* select和poll。这两个函数让你可以考虑一组连接并能找出已经准备好读取或者写入的连接。这就意味着能为通过时间片轮转来为几个连接提供服务。看起来就像是同时处理几个连接。尽管代码可能复杂一点，但在伸缩性和效率上要比线程或分叉好得多。
* Twisted。这是来自Twisted Matrix实验室的框架，支持大多数的网络协议，它内容丰富并且很复杂，尽管很庞大，有的习惯用语却不太容易记，但它的基本用法简单、直观。Twisted框架是异步的，因此它在伸缩性和效率方面表现得很好。如果能够使用Twisted，它可能很多自定义网络应用程序的最佳选择。

# 本章新函数

|函数|描述|
|:------------------|:--------------------|
|urllib.urlopen(url[, data[, proxies]])|通过URL打开一个类文件对象|
|urllib.urlretrieve(ur[, fanme[, hook[, data]]])|通过URL下载一个文件|
|urllib.quote(string[, safe])|引用特定的URL字符|
|urllib.quote_plus(string[, safe])|和quote相同，但是将空格引用为+|
|urllib.unquote(string)|和quote相反|
|urllib.unquote_plus(string)|和quote_plus相反|
|urllib.urlencode(query[, doseq])|在CGI请求中使用的编码映射|
|select.select(iseq, oseq, eseq[, timeout])|找出准备好读取/写入的套接字|
|select.poll()|为polling套接字创建一个poll对象|
|reactor.listenTCP(port, factory)|Twisted函数，监听连接|
|reactor.run()|Twisted函数，主服务器循环|
