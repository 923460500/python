# coding:utf-8

import cx_Oracle

conn = cx_Oracle.connect('v80_a82/Seeyon123456@192.168.225.99/pdborcl18c')

sql = "select * from ctp_config"

curs = conn.cursor()

rr=curs.execute(sql)
row=curs.fetchone()
print(row[0])
curs.close()
conn.close()