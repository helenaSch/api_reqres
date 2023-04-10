from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert

def test_sign_up():
    email = "eve.holt@reqres.in"
    password = "pistol"
    res = api.create_user(email, password)
    res.body = res.json()

    example = {
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }
    assert res.status_code == HTTPStatus.OK
    assert example == res.body




def test_sign_up_neg():
    email = "eve.holt@reqres.in"
    password = ""
    res = api.create_user(email, password)
    res.body = res.json()

    example = {
         "error": "Missing password"
    }
    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res.body)
    assert example == res.body


