# -*- coding:utf-8 -*-
import wx
import sys
import os


class MainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent)
        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label="Your Quote", pos=(20,30))
        self.Show()


def main():
    app = wx.App(False)
    panel = MainWindow(None)
    app.MainLoop()


if __name__ == '__main__':
    main()
