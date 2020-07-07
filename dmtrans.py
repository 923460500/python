# coding:utf-8
import re
import sys
import os

all_dir = sys.argv[1]
upgrade_dir = sys.argv[2]
# all_dir = "C:\\Users\\Administrator\\Desktop\\sql\\"
# upgrade_dir = "C:\\Users\\Administrator\\Desktop\\sql\\"
# oracle特殊字符
oracle_special_string = ["ALTER SESSION SET NLS_DATE_FORMAT='YYYY-MM-DD HH24:MI:SS';",
                         "ALTER SESSION SET NLS_TIMESTAMP_FORMAT='YYYY-MM-DD HH24:MI:SS.FF';", "commit"]
# postgresql特殊字符
postgresql_special_string = ["DROP CAST IF EXISTS (SMALLINT AS BOOLEAN);",
                             "DROP CAST IF EXISTS (BOOLEAN AS SMALLINT);",
                             "CREATE CAST (SMALLINT AS BOOLEAN) WITH INOUT AS IMPLICIT;",
                             "CREATE CAST (BOOLEAN AS SMALLINT) WITH INOUT AS IMPLICIT;",
                             "DROP CAST IF EXISTS (VARCHAR AS SMALLINT);",
                             "DROP CAST IF EXISTS (SMALLINT AS VARCHAR);",
                             "CREATE CAST (VARCHAR AS SMALLINT) WITH INOUT AS IMPLICIT;",
                             "CREATE CAST (SMALLINT AS VARCHAR) WITH INOUT AS IMPLICIT;"]
# postgresql任意位置均可
postgresql_anywhere_string = ["create or replace internal function sys_catalog.bool_eq_numeric(bool, numeric) returns "
                              "bool as $$ select $1::numeric = $2; $$ language sql;",
                              "create operator sys_catalog.= (procedure = bool_eq_numeric,leftarg = bool,rightarg = "
                              "numeric,commutator = =);",
                              "create or replace internal function sys_catalog.numeric_eq_bool(numeric, bool) returns "
                              "bool as $$ select $1 = $2::numeric; $$ language sql;",
                              "create operator sys_catalog.= (procedure = numeric_eq_bool,leftarg = numeric,rightarg "
                              "= bool,commutator = =);",
                              "create or replace internal function sys_catalog.numeric_eq_bool(smallint, "
                              "bool) returns bool as $$ select $1 = $2::smallint; $$ language sql;",
                              "create operator sys_catalog.= (procedure = numeric_eq_bool,leftarg = smallint,rightarg "
                              "= bool,commutator = =);",
                              "create or replace internal function sys_catalog.varchar_eq_bool(varchar, bool) returns "
                              "bool as $$ select $1::bool = $2; $$ language sql;",
                              "create operator sys_catalog.= (procedure = varchar_eq_bool,leftarg = varchar,rightarg "
                              "= bool,commutator = =);",
                              "create or replace INTERNAL function DATE_FORMAT(timestamp, text) returns text as $$ "
                              "declare fm_string text;begin fm_string := $2;fm_string := replace (fm_string, '%Y', "
                              "'yyyy');fm_string := replace (fm_string, '%m', 'mm');fm_string := replace (fm_string, "
                              "'%d', 'dd');fm_string := replace (fm_string, '%H', 'hh24');fm_string := replace ("
                              "fm_string, '%i', 'mi');return to_char($1, fm_string);end;$$ language plsql;",
                              ]
# create table语句后添加
postgresql_after_create_string = [
    "ALTER TABLE JK_FIRED_TRIGGERS ALTER COLUMN IS_NONCONCURRENT  TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE JK_FIRED_TRIGGERS ALTER COLUMN REQUESTS_RECOVERY TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE JK_SIMPROP_TRIGGERS ALTER COLUMN BOOL_PROP_1  TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE JK_SIMPROP_TRIGGERS ALTER COLUMN BOOL_PROP_2 TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE JK_JOB_DETAILS ALTER COLUMN IS_DURABLE TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE JK_JOB_DETAILS ALTER COLUMN IS_NONCONCURRENT TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE JK_JOB_DETAILS ALTER COLUMN IS_UPDATE_DATA TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE JK_JOB_DETAILS ALTER COLUMN REQUESTS_RECOVERY TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE WORKTIME_CURRENCY ALTER COLUMN IS_WORK TYPE CHARACTER VARYING(8 byte);",
    "ALTER TABLE WORKTIME_SPECIALDAY ALTER COLUMN WEEK_NUM TYPE CHARACTER VARYING(8 byte);"]


# 数据库脚本语言替换。
def multiple_replace(text):
    strinfo = re.compile("INTEGER")
    rx = strinfo.sub("BIGINT", text)
    strinfo = re.compile("DATE;$")
    rx = strinfo.sub("TIMESTAMP;", rx)
    strinfo = re.compile("NUMBER\(4\)")
    rx = strinfo.sub("SMALLINT;", rx)
    strinfo = re.compile("NUMBER\(19\)")
    rx = strinfo.sub("BIGINT;", rx)
    strinfo = re.compile("NUMERIC\(19,0\)")
    rx = strinfo.sub("BIGINT;", rx)
    strinfo = re.compile("DATE,$")
    rx = strinfo.sub("TIMESTAMP,", rx)
    strinfo = re.compile("DATE {1,30}NOT NULL,$")
    rx = strinfo.sub("TIMESTAMP    NOT NULL,", rx)
    return rx


class all_in_one:
    def dm_read_file(self):
        # SQL文件路径
        # all_dir = sys.argv[1]
        # oracle文件名称
        oracle_file = ["A8-1_ALL_IN_ONE_ORACLE.SQL", "A8-2_ALL_IN_ONE_ORACLE.SQL"]
        exists_sql = []
        for i in oracle_file:
            #        print(all_dir+i)
            if os.path.exists(all_dir + i):  # 获取存在的SQL文件
                exists_sql.append(i)

        for j in exists_sql:
            version = j.split("_")[0]  # 获取对应的版本号
            target_file = version + "N_ALL_IN_ONE_" + "DM" + ".SQL"  # 写入目标文件
            print(target_file)
            dm_string = []
            with open(all_dir + j, "r", encoding="UTF-8") as fp:
                for k in fp.readlines():
                    strip_string = multiple_replace(k.strip("\n\t"))
                    if strip_string in oracle_special_string:
                        continue
                    else:
                        dm_string.append(strip_string)
            try:
                with open(all_dir + target_file, "w", encoding="UTF-8") as fp:
                    for x in dm_string:
                        fp.write(x + "\n")
            except FileNotFoundError:
                print("no")

    def kingbase_read_file(self):
        postgresql_file = ["A8-2_ALL_IN_ONE_POSTGRESQL.SQL", "A8-1_ALL_IN_ONE_POSTGRESQL.SQL"]
        exists_sql = []
        for i in postgresql_file:
            #        print(all_dir+i)
            if os.path.exists(all_dir + i):  # 获取存在的SQL文件
                exists_sql.append(i)
        flag = 0
        for j in exists_sql:
            version = j.split("_")[0]  # 获取对应的版本号
            target_file = version + "N_ALL_IN_ONE_" + "KINGBASE" + ".SQL"  # 写入目标文件
            print(target_file)
            kingbase_string = []
            with open(all_dir + j, "r", encoding="UTF-8") as fp:
                for k in fp.readlines():
                    strip_string = k.strip("\n\t")
                    if strip_string in postgresql_special_string:
                        continue
                    elif "CREATE INDEX" in strip_string and flag == 0:
                        flag = 1
                        kingbase_string = kingbase_string + postgresql_after_create_string
                    else:
                        kingbase_string.append(strip_string)
            kingbase_string = kingbase_string + postgresql_anywhere_string
            try:
                with open(all_dir + target_file, "w", encoding="UTF-8") as fp:
                    for x in kingbase_string:
                        fp.write(x + "\n")
            except FileNotFoundError:
                print("no")


class upgrade:
    # 人大金仓的升级脚本，不需要做任何操作，为了以后方便，先读一遍再写进去。
    def kingbase_upgrade(self):
        postgresql_file = ["PostgreSQL_9_Z_V80_TO_V80SP1_A8-1.SQL", "PostgreSQL_9_Z_V80_TO_V80SP1_A8-2.SQL"]
        exists_sql = []
        for i in postgresql_file:
            if os.path.exists(upgrade_dir + i):  # 获取存在的SQL文件
                exists_sql.append(i)
        for j in exists_sql:  # 挨个读取
            version = j.split("_")[-1]  # 获取对应的版本号
            target_file = "Kingbase_9_Z_V80_TO_V80SP1_" + version  # 写入目标文件
            print(target_file)
            with open(upgrade_dir + j, "r", encoding="UTF-8") as fp:  # 打开对应的postgresql SQL
                with open(upgrade_dir + target_file, "w", encoding="UTF-8") as kb_fp:  # 打开需要写入的kingbase文件
                    for k in fp.readlines():  # 逐行写入
                        kb_fp.write(k)

    def dm_upgrade(self):
        dm_file = ["Oracle_9_Z_V80_TO_V80SP1_A8-1.SQL", "Oracle_9_Z_V80_TO_V80SP1_A8-2.SQL"]
        exists_sql = []
        for i in dm_file:
            if os.path.exists(upgrade_dir + i):  # 获取存在的SQL文件
                exists_sql.append(i)
        for j in exists_sql:  # 挨个读取
            version = j.split("_")[-1]  # 获取对应的版本号
            target_file = "Dm_9_Z_V80_TO_V80SP1_" + version  # 写入目标文件
            print(target_file)
            with open(upgrade_dir + j, "r", encoding="UTF-8") as fp:  # 打开对应的postgresql SQL
                with open(upgrade_dir + target_file, "w", encoding="UTF-8") as kb_fp:  # 打开需要写入的kingbase文件
                    for k in fp.readlines():  # 逐行写入
                        kb_fp.write(multiple_replace(k))


def main():
    allinone = all_in_one()
    allinone.kingbase_read_file()
    allinone.dm_read_file()
    upgrade_sql = upgrade()
    upgrade_sql.kingbase_upgrade()
    upgrade_sql.dm_upgrade()


if __name__ == '__main__':
    main()
