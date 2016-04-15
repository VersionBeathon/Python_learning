# 网络编程

Python是一个很强大的网络编程工具：
* Python内有很多针对常见网络协议的库，对网络协议的各个层次进行了抽象封装。
* Python非常善于处理字节流的各个模式，使用Python可以很容易地写出处理各种协议格式的代码。

## 少数几个网络设计模块

### socket模块

在网络编程中的一个基本组件就是套接字(socket)。套接字基本上是两个端点的程序之间的“信息通道”。程序可能分布在不同的计算机上（通过网络连接），通过套接字相互发送信息。在Python中的大多数的网络编程都隐藏了socket模块的基本细节，不直接和套接字交互。

套接字包括两个：服务器套截止和客户机套接字。在创建一个服务器套接字后，让它等待连接。这样它就在某个网络地址处（IP地址和一个端口号的组合）监听，直到有客户端套接字连接。连接完成后，两者就可以进行交互了。

处理客户端套接字通常比处理服务器端套接字容易，因为服务器必须准备随时处理客户端的链接，同时还要处理多个链接，而客户机只是简单地链接，完成事务，断开链接。

一个套接字就是socket模块中的socket类的一个实例。它的实例化需要三个参数:第一个参数是地址族（默认是socket.AF_INET）；第二个参数是流（socket.SOCK_STREAM，默认值）或数据包（socket.SOCK_DGRAM）套接字；第三个参数是使用的协议（默认是0，使用默认值即可）。对于一个普通的套接字，不需要提供任何参数。

服务器端套接字使用bind方法后，在调用listen方法去监听某个特定的地址。客户端套接字使用connect方法连接到服务器，在connect方法中使用的地址与服务器在bind方法中的地址相同（在服务器端，能实现很多功能，比如使用函数socket.gethostname得到当前主机名）。在这种情况下，一个地址就是一个格式为(host,post)的元组，其中host是主机名（比如www.example.com），port是端口号（一个整数）。listen方法只有一个参数，即服务器未处理的连接的长度（即允许排队等待的连接数目，这些连接在禁用之前等待）。

服务器端套接字开始监听后，它就可以接受客户端的链接。这个步骤使用accept方法来完成。这个方法会阻塞（等待）直到客户端连接，然后该方法就返回一个格式为（client，address）的远足，client是一个客户端套接字，address是一个前面解释过的地址。服务器在处理完与该客户端的链接后，再次调用accept方法开始等待下一个链接。这个过程通常都是在一个无线循环中实现的。

注意：这种形式的服务器端编程为阻塞或者是同步网络编程。

套接字有两个方法，send和recv（用于接收），用于传输数据。可以使用字符串参数调用send以发送数据，用一个所需的（最大）字节数做参数调用recv来接收数据。如果不能确定使用哪个数字比较好，那么1024是个很好的选择。

[simple_server]()和[simple_client]()展示了一个最简单的客户机/服务器程序。如果在同一台机器上运行它们（先启动服务），服务器会打印出发现的一个连接的信息。然后客户端打印从服务端收到的信息。可以在服务器运行同时运行多个客户机。通过用服务器端所在机器的实际主机名来代替客户端调用gethostname所得到的主机名，就可以让两个运行在不同机器上的程序通过网络连接起来。

### urllib 和 urllib2模块

在能使用的各种网络函数库中，功能最强大的可能是urllib和urllib2.通过它们在网络上访问文件，就好像访问本地电脑上的文件一样。通过一个简单的函数调用，几乎可以把任何URl所指向的东西用做程序的输入。使用这两个模块与re，模块结合使用：可以下载web页面，提取信息，以及自动生成报告等。

这两个模块的功能都差不多，但urllib2更好一些。
* 如果只使用简单的下载，urllib就足够了。
* 如果需要使用HTTP验证（HTTP authentication）或cookie，或者要为自己的协议编写扩展程序，urllib2是更好的选择。

1. [打开远程文件]()

可以像打开本地文件一样打开远程文件，不同之处是只能使用只读模式。使用来自urlib模块的urlopen，而不是open（或file）；

2. 获取远程文件

函数urlopen返回一个能从中读取数据的类文件对象。如果希望urllib为你下载文件并在本地文件中存储一个文件的副本，那么可以使用urlretreive。urlretreive返回一个元组（filename, headers）而不是类文件对象，filename是本地文件的名字（由urllib自动创建），headers包含一些远程文件的信息，如果想要为下载的副本指定文件名，可以在urlretrieve函数的第二个参数中给出。
```Python
urlretrieve('http://www.python.org', 'C:\\python_webpage.html')
```
z这个语句获取Python的主页并把它储存在文件'C:\\\python_webpage.html'中。如果没有指定文件名，文件就会放在临时的位置，用open函数可以打开它，但如果完成了对它的操作，就可以删除它以节省硬盘空间。要清理临时文件，可以调用urlcleanup函数，但不要提供参数，该函数会负责清理工作。

#### 一些功能

除了通过URL读取和下载文件，urllib还提供了一些函数操作URL本身，这些函数如下

* quote(string[, safe])。它返回一个字符串，其中所有的特殊字符（这些字符串在URL中有特殊含义）都已被对URL友好的字符所代替。如果想在URL中使用一个包含特殊字符的字符串，这个函数就很有用。
* quote_plus(string[, safe])。功能和quote差不多，但用+代替空格
* unquote(string)。和quote相反。
* unquote_plus(string)和quote_plus相反。
* urlencode(query[, doseq])。把映射（比如字典）或者包含两个元素的元组的序列——（key，value）形式——转换成URL格式编码的字符串，这样的字符串可以在CGI查询中使用。

### 其他模块

* 标准库中一些与网络相关的模块

|模块|描述|
|:-----------------------|:---------------------------|
|asynchat|asyncore的增强版本|
|asyncore|异步套接字处理程序|
|cgi|基本的CGI支持|
|Cookie|Cookie对象操作，主要用于服务器|
|cookielib|客户端cookie支持|
|email|E-mail信息支持（包括MIME）|
|ftplib|FTP客户端模块|
|gopherlib|gopher客户端模块|
|httplib|HTTP客户端模块|
|imaplib|IMAP4客户端模块|
|mailbox|读取几种邮箱的格式|
|mailcap|通过mailcap文件访问MIME配置|
|mhlib|访问MH邮箱|
|nntplib|NNTP客户端模块|
|poplib|POP客户端模块|
|robotparser|支持解析Web服务器的robot文件|
|SimpleXMLRPCserver|一个简单的XML-RPC服务器|
|smtpd|SMTP服务器模块|
|smplib|SMTP客户端模块|
|telnetlib|Telnet客户端模块|
|urparse|支持即时URL|
|xmlrpclib|XML-RPC的客户端支持|

* gopher是Internet提供的一种采用菜单式驱动的信息查询工具，采用客户机/服务器模式。

## SocketServer

SocketServer模块是标准库中很多服务器框架的基础，这些服务器框架包括BaseHTTPServer、SimpleHTTPServer、CGIHTTPServer、SimpleXMLRPCServer和DocXMLRPCServer，所有的这些服务器框架都为基础服务器增加了特定的功能。

SocketServer包含了四个基本的类：针对TCP流式套接字的TCPServer；针对UDP数据报套接字的UDPServer；以及针对性不强的UnixSteamServer和UnixDatagramServer。通常可能很少用到后3个。

如果要编写一个使用SocketServer框架的服务器，可能会将大部分代码放在一个请求处理程序(request handler)中。每当服务器收到一个请求（来自客户端的链接）时，就会实例化一个请求处理程序，并且它的各种处理方法（handler method）会在处理请求时被调用。具体调用哪个方法取决于特定的服务器和使用的处理程序类（handler class）。还可以把它们子类化，使得服务器调用自定义的处理程序集。BaseRequestHandler类把所有的操作都放到了处理器一个叫做handle的方法中。这个方法会被服务器调用。然后这个方法就会访问属性self.request中的客户端套接字。如果使用的是流（如果使用的是TCPServer，这就是可能的），那么可以使用SteamRequestHandler类，创建了其他两个新属性，self。rfile（用于读取）和self.wfile（用于写入）。然后就能使用这些类文件对象和客户机进行通信。