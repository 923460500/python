# -*- coding:utf-8 -*-
import wx


def main():
    app = wx.App()
    frame = wx.Frame(parent=None,title="hello world")
    panel = wx.Panel(parent=frame)
    frame.Show()
    wx.StaticText(panel,label="hello",pos=(100,100))
    app.MainLoop()


if __name__ == '__main__':
    main()
