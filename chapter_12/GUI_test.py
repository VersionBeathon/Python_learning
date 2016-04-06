# _*_ coding:utf-8 _*_
# 创建并显示一个框架
import wx
app = wx.App()
win = wx.Frame(None)
# 在框架上增加按钮
btn = wx.Button(win)
win.Show()
app.MainLoop()