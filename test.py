#!/usr/bin/env python
import wx
import random


class MouseEventFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button', size=(300, 100))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Not Over", pos=(100, 15))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)

    def OnButtonClick(self, event):
        '''''
        两个交替变换的颜色
        '''
        # if self.panel.BackgroundColour == 'Green':
        #    self.panel.SetBackgroundColour('Red')
        # else:
        #    self.panel.SetBackgroundColour('Green')
        ''''' 
        多个随机选择的颜色 
        '''
        # self.panel.SetBackgroundColour(random.choice(['Green','Yellow','Grey','Red','White','Black']))
        ''''' 
        随机选择所有颜色 
        '''
        self.panel.SetBackgroundColour((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.panel.Refresh()

    def OnEnterWindow(self, event):
        self.button.SetLabel("Over Me!")
        event.Skip()

    def OnLeaveWindow(self, event):
        self.button.SetLabel("Not Over")
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MouseEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()