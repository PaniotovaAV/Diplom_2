import allure
import requests
from data import *
from endpoints.endpoint_url_get_ingredients_data import EndpointUrlGetIngredientsData


class TestGetIngredientsData:

    @allure.title('Проверка успешного получения данных об ингредиентах')
    @allure.description('Создаем get запрос, передаем в него токен и получаем данные об ингредиентах'
                        'Проверяем статус код = 200 и в теле ответа есть данные об ингредиентах: название, тип, цена')
    def test_get_ingredient_data(self):
        response_get = requests.get(EndpointUrlGetIngredientsData.GET_INGREDIENTS_DATA,
                                    headers={'Authorization': TOKEN})
        assert (response_get.status_code == 200 and 'name' in response_get.text and
                'type' in response_get.text and 'price' in response_get.text)
