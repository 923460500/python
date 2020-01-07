# -*-coding:utf-8-*-
import requests
import wx
import wx.grid

column_name = ['环境', '地址', '启动状态']


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
            req1 = requests.get(url=url, timeout=3)

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
        result.append(something)
    return result


result = status()


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="环境状态启动检测", size=(-1,-1))
        self.Center()
        self.grid = self.CreateGrid(self)


    def CreateGrid(self, parent):
        grid = wx.grid.Grid(parent)
        grid.CreateGrid(len(column_name), len(result))
        for i in range(len(column_name)):
            grid.SetColLabelValue(i, column_name[i])

        for r in range(len(result)):
            for j in range(len(result[r])):
                if result[r][j] is True:
                    grid.SetCellValue(r, j, "On")
                elif result[r][j] is False:
                    grid.SetCellValue(r, j, "Off")
                else:
                    grid.SetCellValue(r, j, str(result[r][j]))
        grid.SetBackgroundColour('red')
        grid.AutoSize()
        return grid


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
    #    frame.SetToolBar(wx.StaticText('this is frame'))
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0


def main():
    app = App(wx.App)
    app.MainLoop()


if __name__ == '__main__':
    main()
