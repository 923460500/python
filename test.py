# coding:utf-8
# 一些疑惑的内容，在这个文件里面测试

import numpy

try:
    with open('test.txt', 'r', encoding='utf-8') as fp:
        all = fp.readlines()
        print(all)
    for i in all:
        result = i.split()

        print(type(result))
except FileNotFoundError:
    print('no file')
except LookupError:
    print('error encode')

a = [1, 1, 1]
b = [2, 2, 2]
c = []
c.append(a)
c.append(b)
print(c)
