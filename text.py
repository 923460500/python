# -*- coding:utf-8 -*-
import wx
import sys
import os

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(500,200))
        self.control = wx.TextCtrl(self,style = wx.TE_MULTILINE)
        self.CreateStatusBar()
        tb = wx.ToolBar(self,wx.ID_ANY)
        self.ToolBar = tb

        filemenu = wx.Menu()


        menu_about = filemenu.Append(wx.ID_ABORT,u'关于',u'关于程序的信息')
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,u'退出',u'退出程序')

        btn_mea = wx.Button(self,-1,u'打开文件',pos=(300,100),size=(100,-1))

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,u"文件")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.OnAbout,menu_about)
   #     self.Bind(wx.EVT_MENU,self.OnOpen,menu_open)
        self.Show(True)

    def OnAbout(self,evt):
        dlg = wx.MessageDialog(self,"A small text editor;","a editor for test")
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self,evt):
        self.dirname=  ''
        dlg = wx.FileDialog(self,"choose a file",self.dirname,"","*",wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename == dlg.getname()
            self.dirname == dlg.GetDirectory()
            f=open(os.path.join(self.dirname,self.filename),'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

def main():
    app = wx.App(False)
    frame = MainWindow(None,'Samell editor')
    app.MainLoop()

if __name__ == '__main__':
    main()


