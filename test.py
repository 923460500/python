# coding:utf-8

a=["creat table asd", "{test varchar(4)","test1 varchar(4)","};"]

for i in a:
    if ";" in i:
        print(";")
    print(i)