import allure
from helpers import *
from data import Urls


class TestGetOrdersList:
    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        r = requests.get(Urls.ORDERS_URL)
        orders_list = r.json()["orders"]
        assert r.status_code == 200 and isinstance(orders_list, list) == True