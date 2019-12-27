# coding:utf-8
import wx
import win32api
import sys, os

APP_TITLE = u'launch status'


class mainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, APP_TITLE, style=wx.DEFAULT_FRAME_STYLE)
        self.SetBackgroundColour(wx.Colour(255, 250, 250))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.SetSize((800, 600))
        self.Center()

        wx.StaticText(self, -1, u'第一行输入框', pos=(10, 10), size=(100, -1), style=wx.ALIGN_LEFT)
        wx.StaticText(self, -1, u'第二行输入框', pos=(10, 50), size=(100, 100), style=wx.ALIGN_LEFT)
        self.tip = wx.StaticText(self, -1, u'', pos=(100, 150), size=(150, -1), style=wx.ST_NO_AUTORESIZE)

        self.tc1 = wx.TextCtrl(self, -1, u'', pos=(100, 10), size=(150, -1), name='TC01', style=wx.TE_CENTER)
        self.tc2 = wx.TextCtrl(self, -1, u'', pos=(100, 50), size=(150, -1), name='TC02', style=wx.TE_PASSWORD | wx.ALIGN_RIGHT)

        btn_mea = wx.Button(self, -1, u'鼠标左键时间', pos=(300, 50), size=(100, 25))
        btn_meb = wx.Button(self, -1, u'鼠标右键事件', pos=(400, 50), size=(100, 25))
        btn_close = wx.Button(self, -1, u'关闭窗口', pos=(500, 50), size=(100, 25))

        self.tc1.Bind(wx.EVT_TEXT, self.EvtText)
        self.tc2.Bind(wx.EVT_TEXT, self.EvtText)
        self.Bind(wx.EVT_BUTTON, self.OnClose, btn_close)

        btn_mea.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        btn_mea.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        btn_mea.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        btn_meb.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

   #     self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_SIZE, self.On_Size)

    def EvtText(self, evt):
        obj = evt.GetEventObject()
        objName = obj.GetName()
        text = obj.GetString()

        if objName == 'TC01':
            self.tc2.SetValue(text)
        elif objName == 'TC02':
            self.tc1.SetValue(text)

    def OnClose(self, evt):
        dlg = wx.MessageDialog(None, u'确认关闭本窗口？', u'操作提示',wx.YES_NO | wx.ICON_QUESTION)
        if (dlg.ShowModal() == wx.ID_YES):
            self.Destroy()

    def On_Size(self, evt):
        self.Refresh()
        evt.Skip()

    def OnLeftDown(self, evt):
        self.tip.SetLabel(u'左键按下')

    def OnLeftUp(self, evt):
        self.tip.SetLabel(u'左键弹起')

    def OnMouse(self, evt):
        self.tip.SetLabel(str(evt.EventType))

    def OnMouseWheel(self,evt):
        vector = evt.GetWheelRotation()
        self.tip.SetLabel(str(vector))

    def OnKeyDown(self, evt):
        key = evt.GetKeyCode()
        self.tip.SetLabel(str(key))


class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame()
        self.Frame.Show()
        return True


if __name__ == '__main__':
    app = mainApp(redirect=True, filename="debug.txt")
    app.MainLoop()
