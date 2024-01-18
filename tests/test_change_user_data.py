import allure
import requests
from endpoints.urls import URLS
from base.get_user_data import GetUserData
from faker import Faker

fake = Faker(locale="ru_RU")


class TestChangeUserData:

    @allure.title('Проверка успешного обновления данных авторизованного пользователя')
    @allure.description('Получаем токен авторизованного пользователя'
                        'Обновляем информацию о пользователе - поля "Email" и "Name"'
                        'Получаем: статус код  = 200'
                        'Информацию об успешном создании пользователя')
    def test_change_user_data_success_true(self):
        token = GetUserData.get_user_data(self)
        updated_profile = {
            'email': fake.email(),
            'name': fake.first_name()
        }
        response_patch = requests.patch(URLS.PATCH_USER_DATA,
                                        headers={'Authorization': f'{token}'},
                                        data=updated_profile)
        assert response_patch.status_code == 200 and '"success":true' in response_patch.text

    @allure.title('Проверка обновления данных неавторизованного пользователя')
    @allure.description('Обновляем информацию о неавторизованном пользователе - поля "Email" и "Name"'
                        'Проверяем: статус код  = 401'
                        'Текст сообщения: "You should be authorised"')
    def test_change_user_data_success_false(self):
        updated_profile = {
            'email': fake.email(),
            'name': fake.first_name()
        }
        response_patch = requests.patch(URLS.PATCH_USER_DATA, data=updated_profile)
        assert (response_patch.status_code == 401 and
                '"success":false' in response_patch.text and
                response_patch.json()['message'] == 'You should be authorised')
