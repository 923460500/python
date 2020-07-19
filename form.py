# coding:utf-8

import requests

url = "http://192.168.225.96:288"
token_api = "/seeyon/rest/token"
rest_user = {
    "password": "4455a602-340c-4519-9d3c-fb632213d947", \
    "userName": "zwj"
}
token_url = url + token_api
req = requests.post(url=token_url, json=rest_user)
binduser_token = req.json()["id"]
bind_user = {
    "loginName": "gjr2",
    "token": binduser_token
}
r = requests.put(url=token_url, json=bind_user)
for i in range(500):
    subject_num = "测试表单" + str(i)
    form_json = {"appName": "collaboration",
                 "data": {"data": {"formmain_0124": {"发起者部门": "2774786845270297953", "发起者姓名": "-5512594795463686679"},
                                   "formson_0125": [{"序号": "2"}]}, "attachments": [], "relateDoc": "",
                          "templateCode": "TEST_01", "draft": "0", "subject": subject_num}
                 }
    headers = {
        "token": binduser_token,
        "Content-Type": "application/json"
    }
    bpm_api = "/seeyon/rest/bpm/process/start"
    bpm_url = url + bpm_api
    re = requests.post(url=bpm_url, headers=headers, json=form_json)
    print(i)