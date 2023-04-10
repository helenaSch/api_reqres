from api.httpbin_api import http_bin_api
from http import HTTPStatus
import re

def test_robots():

    res = http_bin_api.about_robots()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/plain'
    res_body = res.text

    assert re.fullmatch(r'.*User-agent: \*.*Disallow: /deny.*', res.text, flags=re.DOTALL)


def test_api():
    res = http_bin_api.test_ip()

    assert res.status_code == HTTPStatus.OK

    assert res.headers['Content-Type'] == 'application/json'
    #origin = res.json()["origin"]

    assert re.fullmatch(r'\d{2}.*\d{2}.*\d{2}.*\d{2}', res.json()["origin"])