class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    LOGIN_URL = MAIN_URL + 'api/v1/courier/login'
    COURIER_URL = MAIN_URL + 'api/v1/courier/'
    ORDERS_URL = MAIN_URL + 'api/v1/orders'


class TestData:
    only_login = {"login": "test_login"}
    only_password = {"password": "test123"}
    empty_password = {"login": "test_login", "password": ""}
    empty_login = {"login": "", "password": "test123"}
    without_login = {"password": "test123", "firstName": 'tester'}
    without_password = {"login": "test_login", "firstName": "tester"}
    empty_login_courier = {"login": "", "password": "test123", "firstName": "tester"}
    empty_password_courier = {"login": "test_login", "password": "", "firstName": "tester"}

class ResponseTexts:
    success_creating_message = '{"ok":true}'
    login_error = 'Этот логин уже используется. Попробуйте другой.'
    not_enough_data_error = 'Недостаточно данных для создания учетной записи'
    not_enough_data_for_login_error = 'Недостаточно данных для входа'
    account_not_found_error = 'Учетная запись не найдена'

class OrderData:
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Иванова, д.1",
        "metroStation": 2,
        "phone": "+7 910 111 22 33",
        "rentTime": 3,
        "deliveryDate": "2024-03-25",
        "comment": "Тестовый комментарий"
    }









