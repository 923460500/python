# coding:utf-8

import prometheus_client
from prometheus_client import Counter
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask

app = Flask(__name__)

requests_total = Counter("request_count", "total request count of the host")


@app.route("/met")
def request_count():
    requests_total.inc()
    return Response(prometheus_client.generate_latest(requests_total), mimetype="text/plain")


if __name__ == '__main__':
    app.run("0.0.0.0")
