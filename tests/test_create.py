from api.questions_api import api
from http import HTTPStatus
import re

def test_create():
    name = 'Alena'
    job = 'Tester'
    res = api.create(name, job)

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job


    assert re.fullmatch(r'\d{1,4}', res.json()['id'])

    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT

