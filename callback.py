# -*-coding:utf-8-*-
import requests
import wx
from wx import grid

column_name = ['name', 'url', 'status']


def status():
    result = []
    try:
        with open('test.txt', 'r', encoding='utf-8') as fp:
            ips = fp.readlines()
    except FileNotFoundError:
        print('文件不存在')
    except LookupError:
        print('错误的编码，推荐使用utf-8')
    count = 0
    for ip in ips:
        something = ip.split()
        target_ip = something[1]
        try:
            #      url=str(ip)+'/seeyon'
            url = 'http://%s/seeyon/main.do' % target_ip
            req1 = requests.get(url=url, timeout=10)

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
        result.append(something)
    return result


class MyGridTable(wx.grid.GridTableBase):
    def __init__(self):
        super.__init__()
        self.colLabels = column_name

    def GetNumberRows(self):
        return len(result)

    def GetNumberCols(self):
        return len(result[0])

    def GetValue(self, row, col):
        return result[row][col]

    def GetColLabelValue(self, col):
        return self.colLabels[col]


class MyFrame(grid.PyGridTableBase):
    print(result)

    def __init__(self):
        super().__init__(parent=None, title='statu check', size=(500, 500))
        self.gridtable = MyGridTable()
        self.Centre()
        self.grid = self.CreateGrid(self)
        self.Bind(wx.grid.EVT_GRID_CMD_SELECT_CELL, self.OnClick, self.grid)

    def OnClick(self, event):
        print("row number:{0}".format(event.GetRow()))
        print("column number:{0}".format(event.GetCol()))
        print(result[event.GetRow()])
        print(self.gridtable.GetValue(event.GetRow(), event.GetCol()))
        event.Skip()

    def CreateGrid(self, parent):
        grid = wx.grid.Grid(parent)
        grid.SetTable(self.gridtable, True)
        grid.AutoSize()

        return grid
    #  for r in range(len(data)):


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


def main():
    global result
    result = status()
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()
