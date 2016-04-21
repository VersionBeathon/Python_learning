# Python和Web

三个主题：屏幕抓取（爬虫）、CGI和mod_python

## 屏幕抓取

* XHTML：XHTML是HTML的最新放眼，是XML的一种形式。

XHTML和旧版本HTML之间最主要的区别是XHTML对于显式关闭所有元素要求更加严格。所以在HTML中可能只用一个开始标签结束一段然后开始下一段，而在XHTML中首先要显式地关闭当前段落（成对的标签）。这种行为让XHTML更容易理解，因为可以直接告诉程序什么时候进入或者离开各种元素。XHTML的另一个好处是它是XML的一种，所以可以对它使用XML工具

* Tidy：Tidy是用来修复不规范且有些随意的HTML文档的工具。Tidy不能修复HTML文件的所有问题，但是它会确保文件的格式是正确的。（Tidy库，Python包装程序μTidyLib、mxTidy）
注：mxTidy网站打不开

* 使用HTMLParser

使用HTMLParser意味着要生成它的一个子类，并且对handdle_starttage和handle_data之类事件处理方法进行覆盖

HTMLParser的回调方法

|回调方法|何时使用|
|:----------------------|:---------------------------|
|handle_starttag(tag, attrs)|找到开始标签时调用。attrs是（名称，值）对的序列|
|handle_startendag(tag, attrs)|使用空标签时调用。默认分开处理开始和结束标签|
|handle_endtag(tag)|找到结束标签时调用|
|handle_data(data)|使用文本数据时调用|
|handle_charref(ref)|当使用&#ref;形式的实体引用时调用|
|handle_entityref(name)|当使用&name；形式的实体引用时调用|
|handle_comment(data)|注释时调用。只对注释内容调用|
|handle_decl(decl)|声明<!..>形式时调用|
|handle_pi(data)|处理指令时调用|

* 使用Beautiful Soup
Beautiful Soup是个小模块，用来检查经常在网上看到的那些乱七八糟而且不规范的HTML。
