import allure
from helpers import *


class LoginUser:

    @allure.step('Создаем пользователя и запоминаем данные')
    def login_user(self):
        data = register_new_user_and_return_login_password()
        payload = {
            'email': data[0],
            'password': data[1]}
        return payload

    @allure.step('Заполняем "Логин" и "Пароль" случайными данными')
    def random_login_user(self):
        random_data = {
            'email': fake.email(),
            'password': fake.password(length=10)
        }
        return random_data
