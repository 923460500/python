# coding:utf-8

import time


def sum(p):
    def wrapper():
        print("sum")
        p()

    return wrapper


def sum1(p):
    def wrapper():
        print("sum1")
        p()

    return wrapper


@sum
@sum1
def decorator():
    print("start...")
    time.sleep(1)
    print("end...")


def main():
    decorator()


if __name__ == '__main__':
    main()
