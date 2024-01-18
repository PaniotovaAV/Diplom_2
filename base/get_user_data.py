import allure
from endpoints.urls import URLS
from helpers import *


class GetUserData:

    @allure.step('Создаем пользователя '
                 'Запоминаем переданные данные и с ними авторизуемся '
                 'Получаем информацию о пользователе '
                 'Возвращаем токен пользователя')
    def get_user_data(self):
        token = []
        data = register_new_user_and_return_login_password()
        payload = {
            'email': data[0],
            'password': data[1]}
        response_post = requests.post(URLS.USER_LOGIN, data=payload)
        if response_post.status_code == 200:
            token = response_post.json()['accessToken']
        response_get = requests.get(URLS.GET_USER_DATA,
                                    headers={'Authorization': f'{token}'})
        if response_get.status_code == 200:
            return token
