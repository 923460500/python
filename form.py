# coding:utf-8

import requests
import random
import time

rest115 = "b8d359d1-a582-4861-8fca-ae63b3821fe6"
rest37 = "154e2bd0-3061-4d5f-b84d-03594a8744b0"


user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
headers = {
    'User-Agent': random.choice(user_agent_list)
}

url37 = "http://10.3.4.37:8080"
url115 = "http://192.168.10.115:8083"
rest = rest37
url = url37
token_api = "/seeyon/rest/token"
rest_user = {
    "password": rest,\
    "userName": "zwj"
}
token_url = url + token_api
req = requests.post(url=token_url, json=rest_user)
print(req.json())
binduser_token = req.json()["id"]
print(binduser_token)
bind_user = {
    "loginName": "gjr2",\
    "token": binduser_token
}
r = requests.put(url=token_url, json=bind_user, headers=headers)
for i in range(1000):
    subject_num = "测试表单" + str(i)
    form_json = {"appName": "collaboration",
                 "data": {"data": {"formmain_0124": {"发起者部门": "2774786845270297953", "发起者姓名": "-5512594795463686679"},
                                   "formson_0125": [{"序号": "2"}]}, "attachments": [], "relateDoc": "",
                          "templateCode": "TEST_02", "draft": "0", "subject": subject_num}
                 }
    headers = {
        "token": binduser_token,
        "Content-Type": "application/json"
    }
    bpm_api = "/seeyon/rest/bpm/process/start"
    bpm_url = url + bpm_api
    re = requests.post(url=bpm_url, headers=headers, json=form_json)
    print(i)
    time.sleep(0.01)
print(re.text)