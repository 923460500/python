# coding:utf-8
import re

import random
import string
import os


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)

    return round(fsize, 2)


s = "JLH6ynNVUfuCIQjxTzXBaeZpdh0srR9DkgWb3EliO2wvMo57Kq"
with open("test.txt", "w") as fp:
    size = get_FileSize("test.txt")
    while size <= 10:
        size=get_FileSize("test.txt")
        fp.write(s)
    print(size,"M")


class c:
    def multiple_replace(text):
        strinfo = re.compile("INTEGER,")
        rx = strinfo.sub("BIGINT,", text)
        strinfo = re.compile("INTEGER;")
        rx = strinfo.sub("BIGINT;", rx)
        strinfo = re.compile("INTEGER {1,30}NOT NULL,")
        rx = strinfo.sub("BIGINT NOT NULL,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT {1,30}NULL,")
        rx = strinfo.sub("BIGINT       DEFAULT NULL,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT {1,30}-1,")
        rx = strinfo.sub("BIGINT       DEFAULT -1,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT {1,30}1,")
        rx = strinfo.sub("BIGINT       DEFAULT 1,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT {1,30}0,")
        rx = strinfo.sub("BIGINT       DEFAULT 0,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT 1 NOT NULL,")
        rx = strinfo.sub("BIGINT       DEFAULT 1 NOT NULL,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT 0 NOT NULL,")
        rx = strinfo.sub("BIGINT       DEFAULT 0 NOT NULL,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT -1 NOT NULL,")
        rx = strinfo.sub("BIGINT       DEFAULT -1 NOT NULL,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT 100,")
        rx = strinfo.sub("BIGINT       DEFAULT 100,", rx)
        strinfo = re.compile("INTEGER {1,30}DEFAULT 4,")
        rx = strinfo.sub("BIGINT       DEFAULT 4,", rx)
        strinfo = re.compile("DATE;$")
        rx = strinfo.sub("TIMESTAMP;", rx)
        strinfo = re.compile("NUMBER\(4\)")
        rx = strinfo.sub("SMALLINT", rx)
        strinfo = re.compile("NUMBER\(19\)")
        rx = strinfo.sub("BIGINT", rx)
        strinfo = re.compile("NUMERIC\(19,0\)")
        rx = strinfo.sub("BIGINT", rx)
        strinfo = re.compile("DATE,$")
        rx = strinfo.sub("TIMESTAMP,", rx)
        strinfo = re.compile("DATE {1,30}NOT NULL,$")
        rx = strinfo.sub("TIMESTAMP    NOT NULL,", rx)
        strinfo = re.compile("DATE {1,30}DEFAULT NULL,$")
        rx = strinfo.sub("TIMESTAMP  DEFAULT NULL,", rx)
        return rx

    dir = "C:\\Users\\Administrator\\AppData\\Roaming\\ZhiXin\\file\\马向超\\"
    with open(dir + "Oracle_9_Z_V71SP1_TO_V80_A8-1.SQL", "r", encoding="UTF-8") as file:
        a = file.readlines()
        with open(dir + "Dm_9_Z_V71SP1_TO_V80_A8-1.SQL", "w", encoding="UTF-8") as fp:
            for i in a:
                x = multiple_replace(i)
                fp.write(x)
