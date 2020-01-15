# coding:utf-8

import datetime
import time


def sum(p):
    def wrapper():
        starttime = datetime.datetime.now()
        p()
        endtime = datetime.datetime.now()
        print("total time:  ",(endtime-starttime))
    return  wrapper

@sum
def decorator():
    print("hello")
    time.sleep(1)
    print("goodbye")


def main():
    f=decorator()



if __name__ == '__main__':
    main()
