from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert

def test_sign_up():
    email = "eve.holt@reqres.in"
    password = "pistol"
    res = api.create_user(email, password)

    assert res.status_code == HTTPStatus.OK



def test_sign_up_neg():
    email = "eve.holt@reqres.in"
    password = ""
    res = api.create_user_neg(email, password)
    res_body = res.json()


    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res_body)
    assert res_body["error"] == "Missing password"


