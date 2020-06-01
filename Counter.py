# coding:utf-8

import prometheus_client
from prometheus_client import Gauge, start_http_server, Counter, Histogram
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask
import pycurl
import threading
from io import BytesIO
import time
import requests

url_http_code = Counter("url_http_code", "request http_code of the host", ['code', 'url'])
url_http_request_time = Counter("url_http_request_time", "request url_http_request_time of the host", ['le', 'url'])
http_request_total = Counter("http_request_total", "request the request of the host", ['url'])
http_request_total_time = Histogram("request_total_time", "description of histogram")
http_request_total_time.observe(4.7)


def test_website(url):
    if "http://" not in url:
        url = "http://" + url
    else:
        url = url
    try:
        req = requests.get(url=url, timeout=3)
    except ConnectionError:
        http_code = 500
        http_total_time = 999
    except:
        http_code = 500
        http_total_time = 999
    else:
        http_code = req.status_code
        http_total_time = req.elapsed
    return http_code, http_total_time


def count_metric(url):
    http_code, http_total_time = test_website(url)
    if http_code >= 100 and http_code < 200:
        url_http_code.labels('1xx', url).inc()
    elif http_code >= 200 and http_code < 300:
        url_http_code.labels('2xx', url).inc()
    elif http_code >= 300 and http_code < 400:
        url_http_code.labels('3xx', url).inc()
    elif http_code >= 300 and http_code < 500:
        url_http_code.labels('4xx', url).inc()
    else:
        url_http_code.labels('5xx', url).inc()
    http_request_total.labels(url).inc()


def count_threads(url):
    while True:
        t = threading.Thread(target=count_metric, args=(url,))
        t.setDaemon(True)
        t.start()
        time.sleep(10)


def open_file():
    url = []
    try:
        with open("url.txt", "r") as fp:
            for i in fp:
                url.append(i.strip('\n'))
    except FileNotFoundError:
        print("未找到url.txt!")
    except:
        print("ERROR")
    return url


if __name__ == '__main__':
    start_http_server(9091)
    server_list = open_file()
    threads = []
    for url in server_list:
        t = threading.Thread(target=count_threads, args=(url,))
        threads.append(t)
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
    thread.join()
