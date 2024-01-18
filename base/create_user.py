import allure
from helpers import *


class CreateUser:

    @allure.step('Заполняем уникальными данными поля "Email", "Пароль", "Имя"')
    def data_login_success(self):
        payload = {
            'email': fake.email(),
            'password': fake.password(length=10),
            'name': fake.first_name()
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
            'email': fake.email(),
            'password': [],
            'name': fake.first_name()
        }
        return payload

    @allure.step('Передаем данные без "Email"')
    def data_without_login(self):
        payload = {
            'email': [],
            'password': fake.password(length=10),
            'name': fake.first_name()
        }
        return payload

    @allure.step('Передаем данные без "Имени"')
    def data_without_name(self):
        payload = {
            'email': fake.email(),
            'password': fake.password(length=10),
            'name': []
        }
        return payload
