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

服务器端套接字开始监听后，它就可以接受客户端的链接。这个步骤使用accept方法来完成。这个方法会阻塞（等待）直到客户端连接，然后该方法就返回一个格式为（client，address）的远足，client是一个客户端套接字，address是一个前面解释过的地址。服务器在处理完与该客户端的链接后，再次调用accept方法开始等待下一个链接。这个过程通常都是在一个无限循环中实现的。

注意：这种形式的服务器端编程为阻塞或者是同步网络编程。

套接字有两个方法，send和recv（用于接收），用于传输数据。可以使用字符串参数调用send以发送数据，用一个所需的（最大）字节数做参数调用recv来接收数据。如果不能确定使用哪个数字比较好，那么1024是个很好的选择。

[simple_server](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/simple_server.py)和[simple_client](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/simple_client.py)展示了一个最简单的客户机/服务器程序。如果在同一台机器上运行它们（先启动服务），服务器会打印出发现的一个连接的信息。然后客户端打印从服务端收到的信息。可以在服务器运行同时运行多个客户机。通过用服务器端所在机器的实际主机名来代替客户端调用gethostname所得到的主机名，就可以让两个运行在不同机器上的程序通过网络连接起来。

### urllib 和 urllib2模块

在能使用的各种网络函数库中，功能最强大的可能是urllib和urllib2.通过它们在网络上访问文件，就好像访问本地电脑上的文件一样。通过一个简单的函数调用，几乎可以把任何URl所指向的东西用做程序的输入。使用这两个模块与re，模块结合使用：可以下载web页面，提取信息，以及自动生成报告等。

这两个模块的功能都差不多，但urllib2更好一些。
* 如果只使用简单的下载，urllib就足够了。
* 如果需要使用HTTP验证（HTTP authentication）或cookie，或者要为自己的协议编写扩展程序，urllib2是更好的选择。

1. [打开远程文件](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/example_of_urllib.py)

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

## 多个链接

同步：即一次只能连接一个客户机并处理它的请求。

如果每个请求只是花费很少的时间，比如，比如一个完整的聊天会话，那么同时能处理多个连接就很重要。

有3种方法能实现这个目的：分叉（forking）、线程（threading）以及异步I/O(asynchronous I/O)。通过对SocketServer服务器使用混入类（mix-inclass），派生进程和线程很容易处理。

缺点：分叉占资源，并且如果有太多的客户端时分叉不能很好分叉；线程处理能导致同步问题。

注意：Windows不支持分叉

* [使用分叉技术的服务器](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/fork_SocketServer.py)
* [使用线程处理的服务器](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/treading_SocketSever.py)

### 带有select和poll的异步I/O

当一个服务器与一个客户端通信时，来自客户端的数据可能是不连续的。如果使用分叉或线程处理，那就不是问题。当一个程序在等待数据，另一个并行的程序可以继续处理它们自己的客户端。另外的处理方法是只处理在给定时间内真正要进行通信的客户端。不需要一直监听，只要监听（或读取）一会儿，然后把它放到其他客户端的后面。

这是asyncore/asynchat框架和Twisted框架采用的方法，这两种功能的基础是select函数，如果poll函数可用，那可以是它，这两个函数都来自select模块。这两个函数中，poll的伸缩性更好，但它只能在UNIX系统中使用（Windows中不可用，果然Windows是最烂的开发平台）。

select函数需要3个序列作为它的必选参数，此外还有一个可选的以秒为单位的超时时间作为第4个参数。这些序列是文件描述符证书。这写就是我们等待的连接。3个序列用于输入、输出以及异常情况（错误以及类似的东西）。如果没有给定超时时间，select会阻塞（也就是处于等待状态），直到其中的一个文件描述符已经为行动做好的准备；如果给定了超时时间，select最多阻塞给定的超时时间，如果给定的超时时间是0，那么就给出一个连续的poll（即不阻塞）。select的返回值是3个序列（也就是一个长度为3的元组），每个代表相应参数的一个活动子集。比如，返回的第1个序列是一个输入文件描述符的序列，其中有一些可以读取的东西。

序列能包含文件对象（在Windows中不行）或者套接字。

* [使用select的为很多连接服务的服务器](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/select_SocketServer.py)

注：fileno方法返回文件描述符整数

poll方法使用起来比select简单。在调用poll时，会得到一个poll对象。然后就可以使用poll对象的register方法注册一个文件描述符（或者是带有fileno方法的对象）、注册后可以使用unregister方法移除注册的对象。描述了一些对象（比如套接字）以后，就可以调用poll方法（带有一个可选的超时时间参数）并得到了一个（fd, event）格式列表（可能是空的），期中fd是文件描述符， event则告诉你发生了什么。这是一个位掩码（bitmask），意思是它是一个证书，这个证书的每个位对应不同的事件。那些不同的事件是select模块的常量，在下表中会进行解释，为了验证是否设置了一个给定位（也就是说，一个给定的事件是否发生了），可以使用按位与操作符（&）：
```Python
if event & select.POLLIN:...
```

* select模块中的polling事件常量

|事件名|描述|
|:----------------------|:------------------|
|POLLIN|读取来自文件描述符的数据|
|POLLPRI|读取来自文件描述符的紧急数据|
|POLLOUT|文件描述符已经准备好数据，写入时不会发生阻塞|
|POLLERR|与文件描述符有关的错误情况|
|POLLHUP|挂起，连接丢失|
|POLLNVAL|无效请求，连接没有打开|

* [使用poll的简单服务器](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/poll_SocketServer.py)使用poll来代替select。注意：添加了一个文件描述符（ints）到套接字对象的映射（fdmap）。

## Twisted

来自于Twisted Matrix实验室的Twisted 是一个事件驱动的Python网络框架，原来是为网络游戏开发的，现在被所有类型的网络软件使用。

Twisted使用一个事件甚至多个基于事件的方法。要编写基本的服务器就要实现处理比如新客户端连接、新数据到达以及一个客户端断开连接等事件的事件处理程序。具体的类能基本类建立更精炼的事件，比如包装“数据到达”事件、收集数据直到新的一行，然后触发“一行数据到达”的事件。

事件处理程序在一个协议（protocol）中定义；在一个新的连接到达时，同样需要一个创建这种协议对象的工厂（factory），但如果只是想要创建一个通用的协议类的实例，那么就可以使用Twisted自带的工厂。factory类在twisted.internet.protocol模块中。当编写自己的协议时，要使用和超类一样的模块中的protocol。得到了一个连接后，事件处理程序connectionMade就会被调用；丢失了一个连接后，connectionLost就会被调用。来自客户端的数据是通过处理程序dataReceived接收的。当然不能使用事件处理策略来把数据发回到客户端，如果要实现此功能，可以使用对象self.transport，这个对象有一个write方法，也有一个包含客户机地址（主机名和端口号）的client属性。

* [使用Twisted的简单服务器](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/twisted_Server.py)

Twisted版本更简单、容易读。这里只涉及一点设置，必须实例化factory，还要设置它的protocol属性，这样他在和客户机通信时就知道使用什么协议。然后就开始在给定的端口处使用工厂进行监听，这个工厂要通过实例化协议对象来准备处理连接。程序使用的是reactor中的listenTCP函数来监听，最后通过调用同一个模块中的run函数启动服务器。

* [使用了LineReceiver协议改进的记录服务器](https://github.com/VersionBeathon/Python_learning/blob/master/chapter_14/lineReceiver_Server.py)

