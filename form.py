# coding:utf-8

import requests
import random
import time

rest115 = "b8d359d1-a582-4861-8fca-ae63b3821fe6"
rest37 = "154e2bd0-3061-4d5f-b84d-03594a8744b0"
rest117 = "6dc17e5d-9e33-4a96-9a77-fff7134e801f"
rest103 = "d4f59a22-5954-4569-af25-d994f3666b1b"

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
url117 = "http://192.168.225.117:8089"
url103 = "http://192.168.225.103"
rest = rest37
url = url37
token_api = "/seeyon/rest/token"
xt_token_api = "/coll/send"
rest_user = {
    "password": rest,\
    "userName": "zwj"
}
token_url = url + token_api
req = requests.post(url=token_url, json=rest_user)
print(req.text)
binduser_token = req.json()["id"]
print(binduser_token)
bind_user = {
    "loginName": "gjr2",\
    "token": binduser_token
}
r = requests.put(url=token_url, json=bind_user, headers=headers)
for i in range(20):
    subject_num = "测试表单" + str(i)
    form_json = {"appName": "collaboration",
                 "data": {"data": {"formmain_0124": {"发起者部门": "2774786845270297953", "发起者姓名": "-5512594795463686679"},
                                   "formson_0125": [{"序号": "2"}]}, "attachments": [], "relateDoc": "",
                          "templateCode": "TEST_02", "draft": "0", "subject": subject_num}
                 }
    xietong_json = {"_json_params":"{\"attFileDomain\":[],\"colMainData\":{\"importantLevel\":\"1\","
                                    "\"canTrack\":\"1\",\"trackType\":\"1\",\"zdgzry\":\"\",\"resend\":\"false\","
                                    "\"newBusiness\":\"1\",\"id\":\"-8945251727220585412\",\"prevArchiveId\":\"\","
                                    "\"colPigeonhole\":\"\",\"bodyType\":\"10\",\"tId\":\"\",\"formRecordid\":\"\","
                                    "\"formParentid\":\"\",\"formOperationId\":\"\",\"formAppid\":\"\",\"DR\":\"\","
                                    "\"contentTemplateId\":\"\",\"contentRightId\":\"\",\"contentDataId\":\"\","
                                    "\"contentSaveId\":\"8962142674522826838\","
                                    "\"contentZWID\":\"8962142674522826838\",\"canForward\":\"1\","
                                    "\"canModify\":\"1\",\"canEdit\":\"1\",\"canEditAttachment\":\"1\","
                                    "\"canArchive\":\"1\",\"canScanCode\":\"0\",\"canSetSupervise\":\"1\","
                                    "\"projectId\":\"\",\"archiveId\":\"\",\"deadline\":\"\","
                                    "\"deadlineDatetime\":\"\",\"awakeDate\":\"\",\"advanceRemind\":\"\","
                                    "\"advancePigeonhole\":\"\",\"archiveName\":\"\",\"archiveAllName\":\"\","
                                    "\"canMergeDeal\":\"0\",\"canAnyMerge\":\"0\",\"attachmentArchiveId\":\"\","
                                    "\"caseId\":\"\",\"currentaffairId\":\"\",\"oldProcessId\":\"\","
                                    "\"isTemplateHasPigeonholePath\":\"false\",\"subject\":\"rest接口-非机器人发送协同\"},"
                                    "\"workflow_definition\":{\"process_desc_by\":\"xml\",\"process_xml\":\"<ps><p "
                                    "t=\\\"\\\" s=\\\"false\\\" i=\\\"-6275310140082601107\\\" "
                                    "n=\\\"-6275310140082601107\\\" d=\\\"\\\"><n i=\\\"start\\\" n=\\\"H5-测试3\\\" "
                                    "t=\\\"8\\\" d=\\\"\\\" x=\\\"0\\\" y=\\\"0\\\" q=\\\"\\\" h=\\\"\\\" g=\\\"\\\" "
                                    "f=\\\"\\\"><a k=\\\"roleadmin\\\" c=\\\"1\\\" j=\\\"false\\\" i=\\\"false\\\" "
                                    "f=\\\"6990018837564116626\\\" g=\\\"user\\\" h=\\\"true\\\" d=\\\"H5-测试3\\\" "
                                    "b=\\\"-5461262893446967602\\\" vj=\\\"0\\\"/><s i=\\\"collaboration\\\" "
                                    "n=\\\"协同\\\" d=\\\"\\\" t=\\\"17\\\" l=\\\"\\\" q=\\\"\\\" p=\\\"\\\" o=\\\"\\\" "
                                    "u=\\\"-1\\\" h=\\\"-1\\\" v=\\\"-1\\\" rs=\\\"\\\" w=\\\"-1\\\" na=\\\"-1\\\" "
                                    "na_b=\\\"0\\\" na_i=\\\"0\\\" k=\\\"\\\" cy=\\\"\\\" g=\\\"\\\" j=\\\"single\\\" "
                                    "f=\\\"\\\" e=\\\"\\\" r=\\\"\\\" z=\\\"\\\" FR=\\\"\\\" DR=\\\"\\\" "
                                    "s=\\\"success\\\" m=\\\"false\\\" ca=\\\"false\\\" c=\\\"1\\\" b=\\\"0\\\" "
                                    "a=\\\"\\\" tm=\\\"1\\\" qid=\\\"\\\" sid=\\\"\\\" sa=\\\"0\\\"/></n><n "
                                    "i=\\\"end\\\" n=\\\"end\\\" t=\\\"4\\\" d=\\\"\\\" x=\\\"0\\\" y=\\\"0\\\" "
                                    "q=\\\"\\\"><s i=\\\"collaboration\\\" n=\\\"协同\\\" d=\\\"\\\" t=\\\"17\\\" "
                                    "l=\\\"\\\" q=\\\"\\\" p=\\\"\\\" o=\\\"\\\" u=\\\"-1\\\" h=\\\"-1\\\" "
                                    "v=\\\"-1\\\" rs=\\\"\\\" w=\\\"-1\\\" na=\\\"-1\\\" na_b=\\\"0\\\" "
                                    "na_i=\\\"0\\\" k=\\\"\\\" cy=\\\"\\\" g=\\\"\\\" j=\\\"single\\\" f=\\\"\\\" "
                                    "e=\\\"\\\" r=\\\"\\\" z=\\\"\\\" FR=\\\"\\\" DR=\\\"\\\" s=\\\"success\\\" "
                                    "m=\\\"false\\\" ca=\\\"false\\\" c=\\\"1\\\" b=\\\"0\\\" a=\\\"\\\" tm=\\\"1\\\" "
                                    "qid=\\\"\\\" sid=\\\"\\\" sa=\\\"0\\\"/></n><n i=\\\"-2603039608407438904\\\" "
                                    "n=\\\"split\\\" t=\\\"2\\\" d=\\\"\\\" x=\\\"0\\\" y=\\\"0\\\" q=\\\"\\\" "
                                    "p=\\\"true\\\" o=\\\"5839883166637967689\\\"><s i=\\\"collaboration\\\" "
                                    "n=\\\"协同\\\" d=\\\"\\\" t=\\\"17\\\" l=\\\"\\\" q=\\\"\\\" p=\\\"\\\" o=\\\"\\\" "
                                    "u=\\\"-1\\\" h=\\\"-1\\\" v=\\\"-1\\\" rs=\\\"\\\" w=\\\"-1\\\" na=\\\"-1\\\" "
                                    "na_b=\\\"0\\\" na_i=\\\"0\\\" k=\\\"\\\" cy=\\\"\\\" g=\\\"\\\" j=\\\"single\\\" "
                                    "f=\\\"\\\" e=\\\"\\\" r=\\\"\\\" z=\\\"\\\" FR=\\\"\\\" DR=\\\"\\\" "
                                    "s=\\\"success\\\" m=\\\"false\\\" ca=\\\"false\\\" c=\\\"1\\\" b=\\\"0\\\" "
                                    "a=\\\"\\\" tm=\\\"1\\\" qid=\\\"\\\" sid=\\\"\\\" sa=\\\"0\\\"/></n><n "
                                    "i=\\\"-4791439716441961203\\\" n=\\\"join\\\" t=\\\"2\\\" d=\\\"\\\" x=\\\"0\\\" "
                                    "y=\\\"0\\\" q=\\\"\\\" p=\\\"false\\\" o=\\\"5839883166637967689\\\"><s "
                                    "i=\\\"collaboration\\\" n=\\\"协同\\\" d=\\\"\\\" t=\\\"17\\\" l=\\\"\\\" "
                                    "q=\\\"\\\" p=\\\"\\\" o=\\\"\\\" u=\\\"-1\\\" h=\\\"-1\\\" v=\\\"-1\\\" "
                                    "rs=\\\"\\\" w=\\\"-1\\\" na=\\\"-1\\\" na_b=\\\"0\\\" na_i=\\\"0\\\" k=\\\"\\\" "
                                    "cy=\\\"\\\" g=\\\"\\\" j=\\\"single\\\" f=\\\"\\\" e=\\\"\\\" r=\\\"\\\" "
                                    "z=\\\"\\\" FR=\\\"\\\" DR=\\\"\\\" s=\\\"success\\\" m=\\\"false\\\" "
                                    "ca=\\\"false\\\" c=\\\"1\\\" b=\\\"0\\\" a=\\\"\\\" tm=\\\"1\\\" qid=\\\"\\\" "
                                    "sid=\\\"\\\" sa=\\\"0\\\"/></n><n i=\\\"-8725958215905292636\\\" n=\\\"xt-3\\\" "
                                    "t=\\\"6\\\" d=\\\"\\\" x=\\\"0\\\" y=\\\"0\\\" q=\\\"\\\" h=\\\"\\\" g=\\\"\\\" "
                                    "f=\\\"\\\" b=\\\"normal\\\" e=\\\"0\\\" l=\\\"10000\\\" c=\\\"false\\\" "
                                    "a=\\\"1\\\"><a k=\\\"roleadmin\\\" c=\\\"1\\\" j=\\\"false\\\" i=\\\"false\\\" "
                                    "f=\\\"-5307180875693208597\\\" g=\\\"user\\\" h=\\\"false\\\" d=\\\"xt-3\\\" "
                                    "b=\\\"-5461262893446967602\\\" vj=\\\"0\\\"/><s i=\\\"collaboration\\\" "
                                    "n=\\\"协同\\\" d=\\\"\\\" t=\\\"17\\\" l=\\\"\\\" q=\\\"\\\" p=\\\"\\\" o=\\\"\\\" "
                                    "u=\\\"-1\\\" h=\\\"-1\\\" v=\\\"-1\\\" rs=\\\"\\\" w=\\\"-1\\\" na=\\\"-1\\\" "
                                    "na_b=\\\"0\\\" na_i=\\\"0\\\" k=\\\"\\\" cy=\\\"\\\" g=\\\"\\\" j=\\\"single\\\" "
                                    "f=\\\"\\\" e=\\\"\\\" r=\\\"\\\" z=\\\"\\\" FR=\\\"\\\" DR=\\\"\\\" "
                                    "s=\\\"success\\\" m=\\\"false\\\" ca=\\\"false\\\" c=\\\"1\\\" b=\\\"0\\\" "
                                    "a=\\\"\\\" tm=\\\"1\\\" qid=\\\"\\\" sid=\\\"\\\" sa=\\\"0\\\"/></n><n "
                                    "i=\\\"9096476220701494143\\\" n=\\\"xt-2\\\" t=\\\"6\\\" d=\\\"\\\" x=\\\"0\\\" "
                                    "y=\\\"0\\\" q=\\\"\\\" h=\\\"\\\" g=\\\"\\\" f=\\\"\\\" b=\\\"normal\\\" "
                                    "e=\\\"0\\\" l=\\\"10000\\\" c=\\\"false\\\" a=\\\"1\\\"><a k=\\\"roleadmin\\\" "
                                    "c=\\\"1\\\" j=\\\"false\\\" i=\\\"false\\\" f=\\\"-3300707521960590972\\\" "
                                    "g=\\\"user\\\" h=\\\"false\\\" d=\\\"xt-2\\\" b=\\\"-5461262893446967602\\\" "
                                    "vj=\\\"0\\\"/><s i=\\\"collaboration\\\" n=\\\"协同\\\" d=\\\"\\\" t=\\\"17\\\" "
                                    "l=\\\"\\\" q=\\\"\\\" p=\\\"\\\" o=\\\"\\\" u=\\\"-1\\\" h=\\\"-1\\\" "
                                    "v=\\\"-1\\\" rs=\\\"\\\" w=\\\"-1\\\" na=\\\"-1\\\" na_b=\\\"0\\\" "
                                    "na_i=\\\"0\\\" k=\\\"\\\" cy=\\\"\\\" g=\\\"\\\" j=\\\"single\\\" f=\\\"\\\" "
                                    "e=\\\"\\\" r=\\\"\\\" z=\\\"\\\" FR=\\\"\\\" DR=\\\"\\\" s=\\\"success\\\" "
                                    "m=\\\"false\\\" ca=\\\"false\\\" c=\\\"1\\\" b=\\\"0\\\" a=\\\"\\\" tm=\\\"1\\\" "
                                    "qid=\\\"\\\" sid=\\\"\\\" sa=\\\"0\\\"/></n><l i=\\\"2484\\\" n=\\\"\\\" "
                                    "t=\\\"11\\\" d=\\\"\\\" k=\\\"start\\\" j=\\\"-2603039608407438904\\\" "
                                    "o=\\\"0\\\" h=\\\"3\\\" m=\\\"\\\" e=\\\"\\\" b=\\\"\\\" a=\\\"\\\" "
                                    "c=\\\"\\\"/><l i=\\\"2485\\\" n=\\\"\\\" t=\\\"11\\\" d=\\\"\\\" "
                                    "k=\\\"-4791439716441961203\\\" j=\\\"end\\\" o=\\\"0\\\" h=\\\"3\\\" m=\\\"\\\" "
                                    "e=\\\"\\\" b=\\\"\\\" a=\\\"\\\" c=\\\"\\\"/><l i=\\\"2486\\\" n=\\\"\\\" "
                                    "t=\\\"11\\\" d=\\\"\\\" k=\\\"-2603039608407438904\\\" "
                                    "j=\\\"-8725958215905292636\\\" o=\\\"0\\\" h=\\\"3\\\" m=\\\"\\\" e=\\\"\\\" "
                                    "b=\\\"\\\" a=\\\"\\\" c=\\\"\\\"/><l i=\\\"2487\\\" n=\\\"\\\" t=\\\"11\\\" "
                                    "d=\\\"\\\" k=\\\"-8725958215905292636\\\" j=\\\"-4791439716441961203\\\" "
                                    "o=\\\"0\\\" h=\\\"3\\\" m=\\\"\\\" e=\\\"\\\" b=\\\"\\\" a=\\\"\\\" "
                                    "c=\\\"\\\"/><l i=\\\"2488\\\" n=\\\"\\\" t=\\\"11\\\" d=\\\"\\\" "
                                    "k=\\\"-2603039608407438904\\\" j=\\\"9096476220701494143\\\" o=\\\"0\\\" "
                                    "h=\\\"3\\\" m=\\\"\\\" e=\\\"\\\" b=\\\"\\\" a=\\\"\\\" c=\\\"\\\"/><l "
                                    "i=\\\"2489\\\" n=\\\"\\\" t=\\\"11\\\" d=\\\"\\\" k=\\\"9096476220701494143\\\" "
                                    "j=\\\"-4791439716441961203\\\" o=\\\"0\\\" h=\\\"3\\\" m=\\\"\\\" e=\\\"\\\" "
                                    "b=\\\"\\\" a=\\\"\\\" c=\\\"\\\"/></p></ps>\",\"readyObjectJSON\":\"\","
                                    "\"workflow_data_flag\":\"WORKFLOW_SEEYON\",\"process_info\":\"\","
                                    "\"process_info_selectvalue\":\"\",\"process_subsetting\":\"\","
                                    "\"moduleType\":\"1\",\"workflow_newflow_input\":\"\","
                                    "\"process_rulecontent\":\"\",\"workflow_node_peoples_input\":\"\","
                                    "\"workflow_node_condition_input\":\"\",\"toReGo\":\"\","
                                    "\"dynamicFormMasterIds\":\"\",\"processId\":\"\",\"caseId\":\"-1\","
                                    "\"subObjectId\":\"-1\",\"currentNodeId\":\"start\","
                                    "\"process_message_data\":\"\",\"processChangeMessage\":\"\","
                                    "\"process_event\":\"\"}}"}
    headers = {
        "token": binduser_token,
        "Content-Type": "application/json"
    }
    bpm_api = "/seeyon/rest/bpm/process/start"
    bpm_url = url + bpm_api
    re = requests.post(url=bpm_url, headers=headers, json=form_json)
    print(i)
    time.sleep(0.001)
print(re.text)