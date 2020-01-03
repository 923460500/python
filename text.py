# -*- coding:utf-8 -*-
import wx
import sys
import os


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='窗口', size=(600, 500), pos=(100, 100))
        panel = wx.Panel(parent=self)
        statictext = wx.StaticText(parent=panel, label='url:', pos=(20, 20))
        TextCtrl = wx.TextCtrl(parent=panel, size=(110, 25), pos=(40, 20))  # 添加URL
        self.savebutton = wx.Button(panel, -1, "save", pos=(155, 20), size=(50, 25))  # 点击保存
        urlshow = wx.StaticText(parent=panel, label='all url in here:', pos=(20, 50))
        self.allurl = wx.TextCtrl(parent=panel, pos=(20, 70), size=(200, 350),
                                  style=wx.TE_MULTILINE | wx.TE_READONLY)  # 显示已经保存的url

        self.startbutton = wx.Button(panel, -1, "start", pos=(225, 220), size=(50, -1))

        statustext = wx.StaticText(parent=panel, label="start status:", pos=(280, 20))

        self.statusshow = wx.TextCtrl(parent=panel, size=(280, 370), pos=(280, 48), style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.Bind(wx.EVT_LEFT_DOWN, self.OnSave, self.savebutton)
        self.Bind(wx.EVT_BUTTON, self.Refresh, self.savebutton)
        self.Bind(wx.EVT_BUTTON,self.OnStart,self.startbutton)

    #   startbutton.Bind(self.OnStart)
    def OnSave(self, event):
        print("save")
        with open('url.txt', 'a') as fp:
            fp.write('%s' % event.GetString())
        fp.close()
        event.Skip()

    def Refresh(self, event):
        self.allurl.Clear()  # 清空输出
        with open('url.txt', 'r') as fp:
            for i in fp.readlines():
                self.allurl.AppendText("%s" % i)
        fp.close()
        event.Skip()

    def OnStart(self,event):
        self.statusshow.Clear()
        with open('url.txt','r') as fp:
            for i in fp.readlines():
                i = i.rstrip("\n")
                self.statusshow.AppendText("%s startup ok!\n" % i)
        fp.close()

    def 

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0


def main():
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()
