import allure
from helpers import *


class CreateUser:

    @allure.step('Заполняем уникальными данными поля "Email", "Пароль", "Имя"')
    def data_login_success(self):
        payload = {
            'email': email_(),
            'password': password_(),
            'name': first_name_()
        }
        return payload

    @allure.step('Создаем курьера. И запоминаем данные')
    def login_courier_success(self):
        data = register_new_user_and_return_login_password()
        payload = {
            'email': data[0],
            'password': data[1],
            'name': data[2]
        }
        return payload

    @allure.step('Передаем данные без "Пароля"')
    def data_without_password(self):
        payload = {
            'email': email_(),
            'password': [],
            'name': first_name_()
        }
        return payload

    @allure.step('Передаем данные без "Email"')
    def data_without_login(self):
        payload = {
            'email': [],
            'password': password_(),
            'name': first_name_()
        }
        return payload

    @allure.step('Передаем данные без "Имени"')
    def data_without_name(self):
        payload = {
            'email': email_(),
            'password': password_(),
            'name': []
        }
        return payload
