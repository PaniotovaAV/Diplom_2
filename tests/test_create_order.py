import allure
from helpers import *
from endpoints.endpoint_url_create_order import EndpointUrlCreateOrder
from base.get_ingredients_hash import GetIngredientsHash


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа')
    @allure.description('Получаем хеш ингредиентов'
                        'Проверяем: статус код = 200 и в теле ответа: "success":true')
    def test_create_order_success_true(self):
        payload = {
            'ingredients': GetIngredientsHash.get_ingredient_data(self)
        }
        response_post = requests.post(EndpointUrlCreateOrder.CREATE_ORDER, data=payload)
        assert response_post.status_code == 200 and '"success":true' in response_post.text

    @allure.title('Проверка неуспешного создания заказа')
    @allure.description('Передаем случайный хеш ингредиента'
                        'Проверяем: статус код = 500')
    def test_create_order(self):
        payload = {
            'ingredients': [f'{ramdom_number}']
        }
        response_post = requests.post(EndpointUrlCreateOrder.CREATE_ORDER, data=payload)
        assert response_post.status_code == 500, f'Internal Server Error'

    @allure.title('Проверка неуспешного создания заказа')
    @allure.description('Не передаем ни одиного ингредиента'
                        'Проверяем: статус код = 400 и сообщение: "Ingredient ids must be provided"')
    def test_create_order_success_false(self):
        payload = {
            'ingredients': []
        }
        response_post = requests.post(EndpointUrlCreateOrder.CREATE_ORDER, data=payload)
        assert (response_post.status_code == 400 and
                response_post.json()['message'] == 'Ingredient ids must be provided' and
                '"success":false' in response_post.text)
