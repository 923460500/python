# coding:utf-8

import os

sql_path = "E:\\v5_git\\sql\\"
os.walk(sql_path)
dir = os.listdir(sql_path)
target_path = []
ctp_organization = "E:\\v5_git\\sql\\ctp-organization\\oracle\\"
apps_edoc = "E:\\v5_git\\sql\\apps-edoc\\oracle\\"
cap_core = "E:\\v5_git\\sql\\cap-core\\oracle\\"


def get_file(path):
    x = os.listdir(path)
    return x


def read_file(path):
    sql = get_file(path)
    all_sql = []
    for i in sql:
        with open(path + i, "r", encoding="UTF-8") as fp:
            for j in fp.readlines():
                all_sql.append(j)
    return all_sql


def main():
    sql = []
    ctp_organization_sql = read_file(ctp_organization)
    for i in ctp_organization_sql:
        sql.append(i)
    apps_edoc_sql = read_file(apps_edoc)
    for j in apps_edoc_sql:
        sql.append(j)
    cap_core_sql = read_file(cap_core)
    for x in cap_core_sql:
        sql.append(x)
    print(sql)
    with open(sql_path+"Oracle_V80SP1_TO_V80SP2_UPGRADE.SQL","w",encoding="UTF-8") as fp:
        for i in sql:
            fp.write(i)


if __name__ == '__main__':
    main()
