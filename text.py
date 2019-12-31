# -*- coding:utf-8 -*-
import wx
import sys
import os


class MainWindow(wx.Panel):
    def __init__(self, parent):
        self.quote = wx.StaticText(self, label = 'your quote;', pos=(20,30))
        self.logger = wx.TextCtrl(self, pos=(300,20),size=(200,300),style=wx.TE_MULTILINE| wx.TE_REA)
        self.button = wx.Button(self,label='Save',pos=(200,325))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        self.lblname =wx.StaticText(self, laber='Your name:', pos=(20,60))
        self.editname = wx.TextCtrl(self, value = 'Enter here your name:', pos=(150,60), size=(140,-1))

        self.Bind(wx.EVT_TEXT,self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        self.sampleList = ['friends', 'advertising', 'web search', 'Yellow Pages']
        self.lblhear = wx.StaticText(self, label='Hwo did you here from me?',pos=(20, 90))

        self.edithear = wx.ComboBox(self, pos=(150, 90), size=(95,-1), choices =self.sampleList, style=wx.CB_DROPDOWN)

        self.insure = wx.CheckBox(self,label="Do you want Insured Shipment?",pos=(20,180))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        radioList = ['blue','red','yellow','orange','greeb','purple','navy blue','black','gray']
        self.rb = wx.RadioBox(label="What color would you like?",pos=(20,210),choices=radioList,majorDimension=3,style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX,self.EvtRadioBox,self.rb)

        def OnClick(self,event):
            self.logger.AppendText('Click on object with id %d\n' % event.GetId())

        def EvtText(self,event):
            self.logger.AppendText('EvtChar:%d\n' %event.GetKeyCode())
            event.Skip()

        def EvtComboBox(self,event):
            self.logger.AppendText('EvtComboBox:%s\n' % event.GetString())

        def EvtCheckBox(self,event):
            self.logger.AppendText('EvtCheckbox:%d\n' % event.Checked())

        def EvtRadioBox(self,event):
            self.logger.AppendText('EvtRadioBox:%d\n' % event.GetInt())
def main():
    app = wx.App(False)
    frame = wx.Frame(None)
    panel = MainWindow(frame)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
