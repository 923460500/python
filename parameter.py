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
    elif jug == 3:
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
            return "inject url"

        else:
            print("error input,check you parameter")
    elif jug == 4 and  param[1] == "-u" and param[3] == "-D":
        return "inject db"
    elif jug == 6 and  param[1] == "-u" and param[3] == "-D" and param[5] == "-T":
        return  "inject table"
    elif jug == 8 and param[1] == "-u" and param[3] == "-D" and param[5] == "-T" and param[7] == "-C":
        return  "inject Cloumn"
    elif jug == 10 and param[1] == "-u" and param[3] == "-D"  and param[5] == "-T" and param[7] == "-C" and param[9] =="--dump":
        return dump
#sqlmap.p -u url -D db -T a -C