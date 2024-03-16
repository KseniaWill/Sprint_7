import pytest
from helpers import *
from data import Urls


@pytest.fixture(scope='function')
def create_and_delete_courier():
    response, login_pass = register_new_courier_and_return_login_password()
    yield response, login_pass

    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    courier_signin = requests.post(Urls.LOGIN_URL, data=payload)
    courier_id = courier_signin.json()["id"]
    requests.delete(Urls.LOGIN_URL + str(courier_id))


@pytest.fixture(scope='function')
def create_and_delete_new_courier():
    login_pass = generate_login_pass()

    payload = {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }

    yield payload

    courier_signin = requests.post(Urls.LOGIN_URL, data=payload)
    courier_id = courier_signin.json()["id"]
    requests.delete(Urls.LOGIN_URL + str(courier_id))