# coding:utf-8

import pymysql

conn = pymysql.connect(
    host="192.168.225.99",
    user="root",
    password="Seeyon@cd123456",
    database="zhangwj_test",
    charset="utf8"
)

cursor = conn.cursor()
sql = '''
    select * from ctp_config;
'''

res = cursor.execute(sql)

print(res.)

cursor.close()

conn.close()
