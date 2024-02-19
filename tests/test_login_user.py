import allure
import requests
from base.login_user import LoginUser
from endpoints.urls import URLS


class TestLoginUser:

    @allure.title('Проверка успешной авторизации пользователя')
    @allure.description('Создаем пользователя'
                        'Запоминаем переданные данные и с ними авторизуемся'
                        'Проверяем: статус код  = 200'
                        'Наличие всех обязательных полей')
    def test_login_user_success_true(self):
        login_user = LoginUser()
        payload = login_user.login_user()
        response_post = requests.post(URLS.USER_LOGIN, data=payload)
        assert (response_post.status_code == 200 and
                '"success":true', '"accessToken": "Bearer"', '"refreshToken": ""',
                '"user": {"email": "", "name": ""}' in response_post.text)

    @allure.title('Проверка ошибки, если авторизоваться под несуществующим пользователем')
    @allure.description('Заполняем "Логин" и "Пароль" случайными данными. '
                        'Проверяем: статус код  = 401'
                        'Текст сообщения: "email or password are incorrect"')
    def test_login_and_password_user_false(self):
        login_user = LoginUser()
        payload = login_user.random_login_user()
        response_post = requests.post(URLS.USER_LOGIN, data=payload)
        assert response_post.status_code == 401 and response_post.json()['message'] == 'email or password are incorrect'
