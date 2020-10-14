# coding:utf-8
import re
import os
import sys


def get_file(file_dir):
    sql_file = []
    for files in os.listdir(file_dir):
        if re.match(".*.SQL$", files):
            sql_file.append(files)
    return sql_file


def change(sql_path, sql_file):
    print(sql_file)
    sql = []
    time_sql = []
    file_path = sql_path + sql_file
    print(file_path)
    with open(file_path, "r", encoding="UTF-8") as fp:
        for i in fp.readlines():
            sql.append(i.strip())               # 记录SQL字符
            if re.match('-- {0,4}\d{1,9}', i.strip()):  # 挑选出日期
                time_sql.append(i.strip())  # 打开文件，去掉多余的空格。
    time_sql.sort()  # 按照时间排序
    sql_len = len(time_sql)
    print(time_sql)
    temp = 0
    date_sql = []
    for x in range(sql_len):            # 去重
        if x == 0:              # 初始化字符
            temp = time_sql[x]  # 初始化temp字符
            date_sql.append(time_sql[x])  # 记录第一个字符
        else:
            if temp != time_sql[x]:
                temp = time_sql[x]
                date_sql.append(time_sql[x])    # 记录时间字符串
            else:
                temp = time_sql[x]

    if len(date_sql) == 0:                      # 时间字符串为空
        return 0
    new_sql = []
    newsql_len = len(sql)
    for j in date_sql:  # 取出日期
        for k in range(newsql_len):
            if re.match(j, sql[k]):             # 判断日期是否相同
                for a in range(k, newsql_len):          # 判断当前数组所在位置
                    if re.match('^-- {0,5}\d{1,9}', sql[a]):     # 日期后面带人名
                        if re.match(j, sql[a]):
                            new_sql.append(sql[a])  # 记录日期
                            continue
                        else:
                            break
                    new_sql.append(sql[a])
    with open(file_path, "w") as f:
        for i in new_sql:
            f.write(i + '\n')


def main():
    all_dir = sys.argv[1]  # 完整路径
    micro_dir = ["1CTP/", "2WORKFLOW/", "3APPS/", "4MESSAGE/"]  # 微服务目录名称
    all_file = get_file(all_dir)
    for i in range(len(all_file)):
        print(all_file[i])
        change(all_dir, all_file[i])
    for j in range(len(micro_dir)):
        micro_path = all_dir + micro_dir[j]
        micro_file = get_file(micro_path)
        for l in range(len(micro_file)):
            print(all_file[l])
            change(micro_path, micro_file[l])


#  print(all_file)


if __name__ == '__main__':
    main()
