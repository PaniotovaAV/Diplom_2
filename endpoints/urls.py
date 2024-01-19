from data import *


class URLS:
    CREATE_ORDER = URL_MAIN_PAGE + '/api/orders'  # url Создание заказа
    USER_CREATE = URL_MAIN_PAGE + '/api/auth/register'  # url Регистрации пользователя
    GET_INGREDIENTS_DATA = URL_MAIN_PAGE + '/api/ingredients'  # url Получение данных об ингредиентах
    GET_ORDERS = URL_MAIN_PAGE + '/api/orders'  # url Получить заказы конкретного пользователя
    USER_LOGIN = URL_MAIN_PAGE + '/api/auth/login'  # url Авторизации пользователя
    GET_USER_DATA = URL_MAIN_PAGE + '/api/auth/user'  # url Получения данных о пользовате
