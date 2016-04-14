# 理解Cookie和Session机制

会话（Session）跟踪是Web程序中常用的技术，用来跟踪用户的整个会话。常用的会话跟踪技术是Cookie与Session。
* Cookie通过在客户端记录信息确定用户身份
* Senssion通过在服务器端记录信息确定用户身份

## Cookie机制

Cookie技术是客户端的解决方案，Cookie就是由服务器发给客户端的特殊信息，而这些信息以文本文件的方式存放在客户端，然后客户端每次向服务器发送请求的时候都会带上这些特殊的信息。
Cookie这样的技术实现，服务器在接收到来自客户端浏览器的请求后，就能通过分析存放于请求头的Cookie得到客户端特有的信息，从而动态生成与该客户端相对应的内容。

Web应用程序是使用HTTP协议传输数据的。HTTP协议是无状态的协议。一旦数据交换完毕，客户端与服务器的连接就会关闭，再次交换数据需要建立新的链接。这就意味着服务器无法从连接上跟踪会话。要跟踪会话，必须引入一种机制。

Cookie就是这样一种机制。它可以弥补HTTP协议无状态的不足。在Session出现之前，基本所有的网站都采用Cookie来跟踪会话。

本质上cookies就是http的一个扩展。有两个http头部是专门负责设置以及发送cookie的，它们分别是Set-Cookie以及Cookie。当服务器返回给客户端一个http相应信息时，并且在后续的http请求中自动发送这个cookie到服务器，直到这个cookie过期。如果cookie的生存时间是整个会话期间的话，那么浏览器会将cookie保存在内存中，浏览器关闭时就会自动清除这个cookie。另一种情况就是保存在客户端的硬盘中，浏览器关闭，该cookie也不会被清除，下次打开浏览器访问对应网站时，这个cookie就会自动再次发送到服务端。

### 一个cookie的设置以及发送分为以下四步：
* 客户端发送一个http请求到服务器端
* 服务器端发送一个http响应到客户端（其中包含Set-Cookie头部）
* 客户端发送一个http请求到服务器端（其中包含Cookie头部）
* 服务器端发送一个http响应到客户端

如图所示：

![cookie_transport](http://static.oschina.net/uploads/space/2015/0406/201833_rQQV_120166.png)

在客户端的第二次请求中包含的Cookie头部中，提供给了服务器端可以用来唯一标识客户端身份的信息。这时，服务器端也就可以判断客户端是否启用了cookies。

### 什么是Cookie

Cookie意味“甜饼”，是由W3C组织提出，最早由Netscape社区开发的一种机制。目前Cookie已经成为标准，所有主流浏览器如IE、Netscape、Firefox、Opera等都支持Cookie。

由于HTTP是一种无状态的协议，服务器单从网络连接上无从知道客户身份。怎么办？就给客户端们颁发一个通行证，每人一个，无论是谁访问都必须携带自己通行证。这样服务器就能从通行证上确认客户身份了。这就是Cookie的工作原理。

Cookie实际上就是一小段的文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用response向客户端浏览器颁发一个Cookie。客户端浏览器会把Cookie保存起来。当浏览器再请求该网站时，浏览器把请求的网址联通该Cookie一桶提交给服务器。服务器检查该Cookie，从此来辨认用户状态。服务器还可以根据需要修改Cookie的内容。

![cookie_status](http://static.oschina.net/uploads/space/2015/0403/140007_OZCH_120166.gif)

### Cookie的不可跨域名性

Cookie具有不可跨域名性。根据Cookie规范，浏览器访问Google只会携带Google的Cookie，而不会携带Baidu的Cookie。Google也只能操作Google的Cookie，而不能操作Baidu的Cookie。

Cookie在客户端是由浏览器来管理的。

## Session机制

除了使用Cookie，Web应用程序中还经常使用Session来记录客户端状态。Session是服务器端使用的一种记录客户端状态的机制，使用上比Cookie简单一些，相应的也增加了服务器的存储压力。

Session技术则是服务器端的解决方案，它是通过服务器来保持状态的。我们把Session翻译成会话，因此我们可以把客户端浏览器与服务器之间的一系列交互的动作成为一个Session；其次，Session指的是服务器端为客户端所开辟的存储空间，在其中保存的信息就是用于保持状态。

Session在何时创建：在服务器端程序运行的过程中创建

### 什么是Session

Session是另一种记录客户状态的机制，不同的是Cookie保存在客户端浏览器中，而Session保存在服务器上。客户端浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上。这就是Session。客户端浏览器再次访问时只需要从该Session中查找该客户的状态就可以了。

如果说Cookie机制是通过检查客户身上的"通行证"来确定客户身份的话，那么Session机制就是通过检查服务器上的"客户明细表"来确认客户身份。Session相当于程序在服务器上搭建的一份客户档案，客户来访的时候只需要查询客户档案表就可以了。

### Session的生命周期

Session保存在服务器端。为了获得更高的存取速度，服务器一般把Session放在内存里。每个用户都会有一个独立的Session。如果Session内容过于复杂，当大量客户访问服务器时可能会导致内存溢出。因此，Session里的信息应该尽量精简。

Session在用户第一次访问服务器的时候自动创建。需要注意只有访问JSP、Servlet等程序时才会创建Session，只访问HTML、IMAGE等静态资源并不会创建Session。如果尚未生成Session，也可以使用request.getSession(true)强制生成Session。

Session生成后，只要用户继续访问，服务器就会更新Session的最后访问时间，并维护该Session。用户每访问服务器一次，无论是否读写Session，服务器都认为该用户的Session"活跃（active）"了一次。

### Session的有效期

由于会有越来越多的用户访问服务器，因此Session也会越来越多。为了防止内存溢出，服务器会把长时间内没有活跃的Session从内存删除。这个时间就是Session的超时时间。如果超过了超时时间没访问过服务器，Session就自动失效了。

### Session对浏览器的要求

虽然Session保存在浏览器，对客户端是透明的，它的正常运行仍然需要客户端浏览器的支持。这是因为Session需要使用Cookie作为识别标志。HTTP协议是无状态的，Session不能依据HTTP连接来判断是否为同一客户，因此服务器向客户端浏览器发送一个名为JSESSIONID的Cookie，它的值为该Session的id。Session依据该Cookie来识别是否为同一用户。

该Cookie为服务器自动生成，它的maxAge属性一般为-1，表示仅当前浏览器内有效，并且各浏览器窗口间不共享，关闭浏览器就会失效。

如果客户端浏览器将Cookie功能禁用，或者不支持Cookie怎么办？例如，绝大多数的手机浏览器都不支持Cookie。Java Web提供了另一种解决方案：URL地址重写。

### URL重写

URL重写是对客户端不支持Cookie的解决方案。URL地址重写的原理是将该用户Session的id信息重写到URL地址中。服务器能够解析重写后的URL获取Session的id。这样即使客户端不支持Cookie，也可以使用Session来记录用户状态。


## Cookie与Session的区别

1. cookie数据存放在客户的浏览器上，Session数据放在服务器上；
2. cookie不是很安全，别人可以分析存放在本地的Cookie并进行Cookie欺骗，考虑到安全应当使用session；
3. session会在一定时间内保存在服务器上。当访问增多，会比较占用服务器的性能。考虑到减轻服务器性能方面，应当使用Cookie；
4. 单个cookie在客户端的限制是3K，就是说一个站点在客户端存放的cookie不能超过3K；

Cookie和Session的方案虽然分别属于客户端和服务端，但是服务端的session的实现对客户端的cookie有依赖关系的，服务端执行session机制时候会生成session的id值，这个id值会发送给客户端，客户端每次请求都会把这个id值放在http请求的头部发送给服务端，而这个id值在客户端会保存下来，保存的容器就是cookie，因此当我们完全禁掉浏览器的cookie的时候，服务器的session也会不能正常使用。


