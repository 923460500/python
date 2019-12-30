# -*- coding:utf-8 -*-
import wx
import sys
import os

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        self.dirname = ''
        wx.Frame.__init__(self, parent , title=title ,size =(200,-1) )
        self.control = wx.TextCtrl(self,style = wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()

        menuOpen = filemenu.Append(wx.ID_OPEN,'&OEPN','OPEN A FILE')
        menuAbout = filemenu.Append(wx.ID_ABORT,'&ABOUT','ABOUT THE EDITOR')
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, 'E&XIT',"EXIT THE PROGRAM")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,'&file')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.OnOpen,menuOpen)
        self.Bind(wx.EVT_MENU,self.OnAbout,menuAbout)
        self.Bind(wx.EVT_MENU,self.OnExit,menuExit)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0,6):
            self.buttons.append(wx.Button(self,-1,"Button &" + str(i)))
            self.sizer2.Add(self.buttons[i],1,wx.SHAPED)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control,1,wx.EXPAND)
        self.sizer.Add(self.sizer2,0,wx.GROW)

        self.SetSize(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)
        self.Show(True)

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self,"a samll editor","small",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self,e):
        self.Close(True)

    def OnOpen(self,e):
        dlg = wx.FileDialog(self,"Choose a file","","*.*",wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname,self.filename),'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()



def main():
    app = wx.App(False)
    frame = MainWindow(None,'Samell editor')
    app.MainLoop()

if __name__ == '__main__':
    main()


