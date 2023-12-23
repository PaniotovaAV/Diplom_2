import allure
import requests
from base.login_user import LoginUser
from endpoints.endpoint_url_login_user import EndpointUrlLoginUser


class TestLoginUser:
    payload = {}

    @allure.title('Проверка успешной авторизации пользователя')
    @allure.description('Создаем пользователя. '
                        'Запоминаем переданные данные и с ними авторизуемся. '
                        'Получаем: статус код  = 200'
                        'Наличие всех обязательных полей')
    def test_login_user_success(self):
        payload = LoginUser.login_user(self)
        response_post = requests.post(EndpointUrlLoginUser.USER_LOGIN, data=payload)
        assert (response_post.status_code == 200 and
                '"success":true', '"accessToken": "Bearer"', '"refreshToken": ""',
                '"user": {"email": "", "name": ""}' in response_post.text)

    @allure.title('Проверка ошибки, если авторизоваться под несуществующим пользователем')
    @allure.description('Заполняем "Логин" и "Пароль" случайными данными. '
                        'Получаем: статус код  = 401'
                        'Проверяем сообщение: "email or password are incorrect"')
    def test_login_and_password_user_false(self):
        payload = LoginUser.random_login_user(self)
        response_post = requests.post(EndpointUrlLoginUser.USER_LOGIN, data=payload)
        assert response_post.status_code == 401 and response_post.json()['message'] == 'email or password are incorrect'

    @allure.title('Очистка данных')
    @classmethod
    def teardown_class(cls):
        cls.payload.clear()
