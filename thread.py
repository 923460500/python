# coding:utf-8
import random
from threading import Thread
from time import sleep

def action(max):
    for i in range(max):
        print("当前线程:%s" %i)
        sleep(1)

def main():
    Thread(target=action, args=(10,))
    for i in range(20):
        threads=Thread(target=action,args=(10,))
        threads.start()
        threads.join()
if __name__ == '__main__':
    main()
