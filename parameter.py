# coding:utf-8
'''
这个文件是为了处理输入的参数，sys.argv有点不太好用。
多种注入会有太多重复代码
'''

import sys


def parameter():
    param = sys.argv
    jug = len(param)
    if jug < 2:
        return False
    elif jug < 4 and jug > 2:
        if param[1] == "-h":
            print("[*]**********************************************")
            print("[*]this is a short help for you")
            print("[*]use -u to add the url that you want to test ")
            print("[*]if you want to get more help,use -hh")
            print("[*]**********************************************")

        elif param[1] == "-hh":
            print("[*]**********************************************")
            print("[*]使用-u后加想要注入的url，如果存在注入，程序会有返回")
            print("[*]使用-D获取需要注入网站的数据库")
            print("[*]使用-T获取需要注入的网站的表")
            print("[*]使用-C获取需要注入的网站的字段名")
            print("[*]使用-dump获取字段内的内aa容")
            print("[*]**********************************************")

        elif param[1] == "-u":
            return True

        else:
            print("error input,check you parameter")
    elif jug < 6 and jug >= 4:
        if
