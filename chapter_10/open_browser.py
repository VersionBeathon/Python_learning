# _*_ coding:utf-8 _*_
import os
# 打开浏览器
os.system(r'c:\"Program Files (x86)"\"Google"\"Chrome"\"Application"\chrome.exe')
# startfile接受一般路径，就算包含空格也没有问题
os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# 使用webbrowser模块 打开指定网址
import webbrowser
webbrowser.open("http://www.baidu.com")
