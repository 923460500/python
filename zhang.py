# coding:utf-8

import sys
import os


def main():
    print("目录为: %s" % os.listdir(os.getcwd()))
    print(os.sep)
    print(os.name)

 #   os.rename("test.py","zhang.py")
    print("目录为：%s" %os.listdir(os.getcwd()))

if __name__ == '__main__':
    main()
