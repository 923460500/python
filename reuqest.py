import requests

url = "http://httpbin.org/cookies"
headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'

}
with open("test.txt","r") as fp:
    data = str(fp.readlines())
payload = {"a":data}
req = requests.get(url=url,json=headers,data=payload)


print(req.text)