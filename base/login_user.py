import allure
from helpers import *


class LoginUser:

    @allure.step('Авторизация пользователя')
    def login_user(self):
        data = register_new_user_and_return_login_password()
        payload = {
            'email': data[0],
            'password': data[1]}
        return payload

    @allure.step('Заполняем "Логин" и "Пароль" случайными данными')
    def random_login_user(self):
        random_data = {
            'email': email_(),
            'password': password_()
        }
        return random_data
