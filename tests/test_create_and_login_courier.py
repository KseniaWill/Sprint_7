import allure
from conftest import *
from data import *
from helpers import *


class TestCreateCourier:
    @allure.title('Регистрация нового курьера')
    @allure.description('Создание курьера c новыми данными доступна.')
    def test_create_courier(self, create_and_delete_new_courier):
        payload = create_and_delete_new_courier
        response = requests.post(Urls.COURIER_URL, data=payload)
        assert response.status_code == 201 and response.text == ResponseTexts.success_creating_message

    @allure.title('Нельзя создать одинаковых курьеров')
    @allure.description('Создание курьера с уже существующими данными недоступно')
    def test_create_the_same_courier(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier[1][0],
            "password": create_and_delete_courier[1][1],
            "firstName": create_and_delete_courier[1][2]
        }
        r = requests.post(Urls.COURIER_URL, data=payload)
        assert r.status_code == 409 and r.json()['message'] == ResponseTexts.login_error

    @allure.title('Нельзя создать курьера без обязательных данных')
    @allure.description('Создание курьера с пустыми значениями или отсутствующими параметрами недоступно')
    @pytest.mark.parametrize('courier_data', (
            TestData.without_login,
            TestData.without_password,
            TestData.empty_login_courier,
            TestData.empty_password_courier))
    def test_create_courier_no_data(self, courier_data):
        r = requests.post(Urls.COURIER_URL, data=courier_data)
        assert r.status_code == 400 and r.json()['message'] == ResponseTexts.not_enough_data_error


class TestLoginCourier:
    @allure.title('Авторизация курьера с валидными данными')
    @allure.description('Зарегистрированному курьеру доступна авторизация')
    def test_login_courier(self, create_and_delete_courier):
        payload = {"login": create_and_delete_courier[1][0],
                   "password": create_and_delete_courier[1][1]}
        r = requests.post(Urls.LOGIN_URL, data=payload)
        assert r.status_code == 200 and 'id' in r.json()

    @allure.title('Авторизация без обязательных полей')
    @allure.description('Авторизация курьера с пустыми значениями или отсутствующими параметрами недоступна')
    @pytest.mark.parametrize('courier_data', (
            TestData.empty_login,
            TestData.empty_password,
            TestData.only_password,
            TestData.only_login)) #тут ошибка в апи, получен код 504 - тест падает
    def test_login_courier_without_data(self, courier_data):
        payload = courier_data
        r = requests.post(Urls.LOGIN_URL, data=payload)
        assert r.status_code == 400 and r.json()['message'] == ResponseTexts.not_enough_data_for_login_error

    @allure.title('Авторизация с несуществующими данными')
    @allure.description('Нельзя войти с ранее незарегистрированными данными')
    def test_login_courier_with_fail_data(self, create_and_delete_courier):
        payload = {"login": create_and_delete_courier[1][1],
                   "password": create_and_delete_courier[1][0]}
        r = requests.post(Urls.LOGIN_URL, data=payload)
        assert r.status_code == 404 and r.json()['message'] == ResponseTexts.account_not_found_error