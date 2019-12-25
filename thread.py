# coding:utf-8
import wx
import win32api
import sys,os

APP_TITLE = u'launch status'

class mainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,APP_TITLE,style=wx.DEFAULT_FRAME_STYLE)
        self.SetBackgroundColour(wx.Colour(224,224,224))
        self.SetSize((800,600))
        self.Center()

        wx.StaticText(self,-1,u'第一行输入框',pos=(50,100),size=(100,-1),style=wx.ALIGN_RIGHT)


class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame()
        self.Frame.Show()
        return  True

if __name__ == '__main__':
    app = mainApp(redirect=True,filename="debug.txt")
    app.MainLoop()