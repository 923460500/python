# -*-coding:utf-8-*-
import requests
import wx
import wx.grid
import time
import threading
import datetime

column_name = ['环境', '地址', '启动状态']


class MyThread(threading.Thread):
    def __init__(self, target_ip, something, ip):
        threading.Thread.__init__(self)
        self.target_ip = target_ip
        self.something = something
        self.ip = ip


    def get_result(self):
        try:
            test = check(self.target_ip,self.something,self.ip)
            return test
        except Exception:
            return None


def OpenTxt():
    try:
        with open('url.txt', 'r', encoding='utf-8') as fp:
            ips = fp.readlines()
    except FileNotFoundError:
        print('url.txt文件不存在')
    except LookupError:
        print('错误的编码，推荐使用utf-8')
    return ips


ips = OpenTxt()


def CreatValue():
    word = []
    for i in ips:
        something = i.split()
        something.append("ready for checking")
        word.append(something)
    return word


def check(target_ip, something, ip):
    try:
        #      url=str(ip)+'/seeyon'
        url = 'http://%s/seeyon/main.do' % target_ip
        req1 = requests.get(url=url, timeout=2)

        if req1.status_code == 200:
            if 'localhost.log' in req1.text:
                something.append(False)
            else:
                something.append(True)
        elif req1.status_code == 403:
            something.append(False)
        elif req1.status_code == 404:
            something.append(False)
    except requests.exceptions.ConnectTimeout:
        something.append(False)
    except requests.exceptions.ConnectionError:
        something.append(False)
    except requests.exceptions.ReadTimeout:
        something.append(False)
    except requests.exceptions:
        something.append(False)
    return something


def status():
    result = []
    threadlist = []
    count = 0
    for ip in ips:
        something = ip.split()
        target_ip = something[1]
        t = MyThread(target_ip, something, ip,)
        threadlist.append(t)
    for i in threadlist:
        i.start()
        i.join()
        result.append(i.get_result())
    return result


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="环境状态启动检测", size=(500, 500))
        self.Center()
        panel = wx.Panel(parent=self, size=(500, 500))
        self.CreateStatusBar()
        self.button = wx.Button(panel, -1, label="start", pos=(0, 0))

        self.grid = self.SimpleGrid(self)
        self.Bind(wx.EVT_BUTTON, self.OnStart, self.button)

    def OnStart(self, evt):
        self.grid.ClearGrid()
        self.grid = self.CreateGrid(self)

    def SimpleGrid(self, parent):
        word = CreatValue()
        grid = wx.grid.Grid(parent, pos=(0, 30))
        grid.CreateGrid(len(word), len(column_name))
        for i in range(len(column_name)):
            grid.SetColLabelValue(i, column_name[i])
        for j in range(len(word)):
            for l in range(len(word[0])):
                grid.SetCellValue(j, l, str(word[j][l]))
        grid.AutoSize()
        return grid

    def CreateGrid(self, parent):
        result = status()
        grid = wx.grid.Grid(parent, pos=(0, 30))
        grid.ClearGrid()
        grid.CreateGrid(len(result), len(column_name))
        for i in range(len(column_name)):
            grid.SetColLabelValue(i, column_name[i])
        for j in range(len(result)):
            for l in range(len(result[0])):
                if result[j][l] is True:
                    grid.SetCellValue(j, l, "On")
                elif result[j][l] is False:
                    grid.SetCellValue(j, l, "Off")
                else:
                    grid.SetCellValue(j, l, str(result[j][l]))
        grid.AutoSize()
        return grid


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        #      frame.SetToolBar(wx.StaticText('this is frame'))
        frame.Show()
        return True


def main():
    app = App(wx.App)
    app.MainLoop()



if __name__ == '__main__':
    main()