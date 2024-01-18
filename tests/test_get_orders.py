import allure
import requests
from base.get_orders import GetOrders
from endpoints.urls import URLS


class TestGetOrders:

    @allure.title('Проверка получения заказов авторизованного пользователя')
    @allure.description('Передаем токен авторизованного пользователя'
                        'Передаем данные созданного заказа авторизованным пользователем'
                        'Проверяем: статус код = 200'
                        'Информацию об успешном создании заказа')
    def test_get_orders_success_true(self):
        token = GetOrders.token_user(self)
        post__order = GetOrders.post_order(self)
        payload = post__order.json()["order"]
        response_get = requests.get(URLS.GET_ORDERS, data=payload,
                                    headers={'Authorization': f'{token}'})
        assert response_get.status_code == 200 and '"success":true' in response_get.text

    @allure.title('Проверка получения заказов неавторизованного пользователя')
    @allure.description('Проверяем: статус код = 401'
                        'Информацию об ошибочном создании заказа'
                        'Текст сообщения:"You should be authorised"')
    def test_get_orders_success_false(self):
        response_get = requests.get(URLS.GET_ORDERS)
        assert (response_get.status_code == 401 and
                '"success":false' in response_get.text and
                response_get.json()['message'] == 'You should be authorised')
