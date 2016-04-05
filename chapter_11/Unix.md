# 管式输出

在UNIX的shell中，使用管早可以在一个命令后面续写其他的多个命令，就像下面这个例子：

```Unix
$ cat somefile.txt | python somescript.py | sort 
```

这个管道(pipeline)由一下三个命令组成。
* cat somefile.txt: 只是把somefile.txt的内容写到标准输出(sys.stdout)
* python somescript.py:这个命令运行了Python脚本somescript。脚本应该是从标注你输入读，把结果写入到标准输出。
* sort:这条命令从标准输入(sys.stdin)读取所有的文本，按字母排序，然后把结果写入标准输出。
* [somescript]()
* [somefile]()

管道符号(|)将一个命令的表准输出和下一个命令的标准输入连在一起。

