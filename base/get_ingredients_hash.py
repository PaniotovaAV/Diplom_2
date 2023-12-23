import allure
import requests
from data import *
from endpoints.endpoint_url_get_ingredients_data import EndpointUrlGetIngredientsData

class GetIngredientsHash:

    @allure.title('Получаем хеш ингредиента')
    @allure.description('Создаем get запрос, передаем в него токен и получаем хеш ингредиента')
    def get_ingredient_data(self):
        hash_ingredients = []
        response_get = requests.get(EndpointUrlGetIngredientsData.GET_INGREDIENTS_DATA,
                                    headers={'Authorization': TOKEN})
        if response_get.status_code == 200:
            hash_ingredients.append(f'{response_get.json()["data"][0]["_id"]}')
            hash_ingredients.append(f'{response_get.json()["data"][1]["_id"]}')
        return hash_ingredients
