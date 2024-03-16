import pytest
import allure
import json
from helpers import *
from data import Urls, OrderData


class TestCreateOrder:
    @allure.title('Успешное создание заказа')
    @allure.description("Создание заказа c выбором разных цветов самоката")
    @pytest.mark.parametrize('color', (["BLACK"], ["GREY"], ["BLACK", "GREY"], []))
    def test_creating_order(self, color):
        OrderData.order_data["color"] = [color]
        payload = json.dumps(OrderData.order_data)
        r = requests.post(Urls.ORDERS_URL, data=payload)
        assert r.status_code == 201 and 'track' in r.text