import allure
from base.create_order import CreateOrder
from endpoints.endpoint_url_create_order import EndpointUrlCreateOrder
from helpers import *


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа авторизованного пользователя c ингредиентами')
    @allure.description('Передаем хеш ингредиентов'
                        'Проверяем: статус код = 200'
                        'Информацию об успешном создании заказа')
    def test_create_order_success_true(self):
        payload = {
            'ingredients': CreateOrder.get_ingredient_data(self)
        }
        response_post = requests.post(EndpointUrlCreateOrder.CREATE_ORDER, data=payload)
        assert response_post.status_code == 200 and '"success":true' in response_post.text

    @allure.title('Проверка неуспешного создания заказа авторизованного пользователя c неверным хешем ингредиентов')
    @allure.description('Передаем случайный хеш ингредиента'
                        'Проверяем: статус код = 500')
    def test_create_order_false_hash(self):
        token = CreateOrder.token_user(self)
        payload = {
            'ingredients': [f'{ramdom_number}']
        }
        response_post = requests.post(EndpointUrlCreateOrder.CREATE_ORDER, data=payload,
                                      headers={'Authorization': f'{token}'})
        assert response_post.status_code == 500, f'Internal Server Error'

    @allure.title('Проверка неуспешного создания заказа авторизованного пользователя без ингредиентов')
    @allure.description('Не передаем ингредиенты'
                        'Проверяем: статус код = 400'
                        'Текст сообщения: "Ingredient ids must be provided"'
                        'Информацию об ошибочном создании заказа')
    def test_create_order_not_ingredient(self):
        token = CreateOrder.token_user(self)
        payload = {
            'ingredients': []
        }
        response_post = requests.post(EndpointUrlCreateOrder.CREATE_ORDER, data=payload,
                                      headers={'Authorization': f'{token}'})
        assert (response_post.status_code == 400 and
                response_post.json()['message'] == 'Ingredient ids must be provided' and
                '"success":false' in response_post.text)

    @allure.title('Проверка неуспешного создания заказа неавторизованного пользователя c неверным хешем ингредиентов')
    @allure.description('Передаем случайный хеш ингредиента'
                        'Проверяем: статус код = 500')
    def test_create_order_not_user_false_hash(self):
        payload = {
            'ingredients': [f'{ramdom_number}']
        }
        response_post = requests.post(EndpointUrlCreateOrder.CREATE_ORDER, data=payload)
        assert response_post.status_code == 500, f'Internal Server Error'

    @allure.title('Проверка неуспешного создания заказа неавторизованного пользователя без ингредиентов')
    @allure.description('Не передаем ингредиенты'
                        'Проверяем: статус код = 400'
                        'Текст сообщения: "Ingredient ids must be provided"'
                        'Информацию об ошибочном создании заказа')
    def test_create_order_not_user_not_ingredient(self):
        payload = {
            'ingredients': []
        }
        response_post = requests.post(EndpointUrlCreateOrder.CREATE_ORDER, data=payload)
        assert (response_post.status_code == 400 and
                response_post.json()['message'] == 'Ingredient ids must be provided' and
                '"success":false' in response_post.text)
