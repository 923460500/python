# coding:utf-8

import requests
import bs4
from bs4 import BeautifulSoup
import json
from time import sleep

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'close',
    'Referer': 'http://joucks.cn:3344/',
    'Cookie': 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
              '.eyJsb2dpbl9uYW1lIjoid2F0NCIsImlkIjoiNWRmOWQxMTVkMWYxZWUyYjgzODI4OTgxIiwiaWF0IjoxNTc2NjUzMDc3LCJleHAiOjE1NzkyNDUwNzd9.6O9K_CMK6lnTLr12WmfopFOLneO19qPI_F0s4PnKNAA; left-click=%23transaction '
}

base_url = 'http://joucks.cn:3344'



def get_list():
    a={}
    for j in range(1,2):
        goods_api = '/api/getSellGoods?sortType=4&pageIndex=%s&tid=all' % j
        get_url = base_url + goods_api
        print(get_url)
        req = requests.get(url=get_url, headers=header)
        content = req.json()
        user_sell =  content.get('data').get('playerSellUser')
        print(len(user_sell))
        for i in range(len(user_sell)):
            if user_sell[i].get('goods') is not None:
                    a[user_sell[i].get('goods').get('name')] = user_sell[i].get('game_gold')
        sleep(1)
    print(a)

def main():
    get_list()


if __name__ == '__main__':
    main()
