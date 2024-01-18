import allure
import requests
import pytest
from base.create_user import CreateUser
from endpoints.urls import URLS


class TestCreateUser:

    @allure.title('Проверка успешного создания пользователя')
    @allure.description('Заполняем формы уникальными данными'
                        'Проверяем:статус код = 200'
                        'Информацию об успешном создании пользователя')
    def test_create_user_success_true(self):
        payload = CreateUser.data_login_success(self)
        response_post = requests.post(URLS.USER_CREATE, data=payload)
        assert response_post.status_code == 200 and '"success":true' in response_post.text

    @allure.title('Проверка возникновения ошибки, при создании двух одинаковых пользователей')
    @allure.description('Создаем пользователя. Используем переданные данные для нового запроса на создание пользователя'
                        'Проверяем: статус код = 403'
                        'Информацию об ошибочном создании пользователя'
                        'Текст сообщения: "User already exists"')
    def test_create_two_identical_user_false(self):
        payload = CreateUser.login_courier_success(self)
        response_post = requests.post(URLS.USER_CREATE, data=payload)
        assert (response_post.status_code == 403 and
                '"success":false' in response_post.text and
                response_post.json()['message'] == 'User already exists')

    @allure.title('Проверка обязательных полей для создания пользователя, '
                  'без передачи "Пароля" или "Логина", или "Имени"')
    @allure.description('Заполняем не все обязательные поля корректными данными'
                        'Проверяем: статус код = 403'
                        'Информацию об ошибочном создании пользователя'
                        'Текст сообщения: "Email, password and name are required fields"')
    @pytest.mark.parametrize('payload', [CreateUser.data_without_password(),
                                         CreateUser.data_without_login(),
                                         CreateUser.data_without_name()])
    def test_create_user_without_password_or_login_or_name(self, payload):
        response_post = requests.post(URLS.USER_CREATE, data=payload)
        assert (response_post.status_code == 403 and
                '"success":false' in response_post.text and
                response_post.json()['message'] == 'Email, password and name are required fields')
