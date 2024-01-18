import allure
from endpoints.urls import URLS
from helpers import *


class CreateOrder:

    @allure.step('Создаем пользователя '
                 'Запоминаем переданные данные и с ними авторизуемся '
                 'Возвращаем токен пользователя')
    def token_user(self):
        token = []
        data = register_new_user_and_return_login_password()
        payload = {
            'email': data[0],
            'password': data[1]}
        response_post = requests.post(URLS.USER_LOGIN, data=payload)
        if response_post.status_code == 200:
            token = response_post.json()['accessToken']
        return token


    @allure.step('Получаем хеш ингредиента: создаем get запрос, передаем в него токен и получаем хеш ингредиента')
    def get_ingredient_data(self):
        token = CreateOrder.token_user(self)
        hash_ingredients = []
        response_get = requests.get(URLS.GET_INGREDIENTS_DATA,
                                    headers={'Authorization': f'{token}'})
        if response_get.status_code == 200:
            hash_ingredients.append(f'{response_get.json()["data"][0]["_id"]}')
            hash_ingredients.append(f'{response_get.json()["data"][1]["_id"]}')
        return hash_ingredients
