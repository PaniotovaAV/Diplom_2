import requests
from data import *
from endpoints.urls import URLS
from faker import Faker

fake = Faker(locale="ru_RU")


def register_new_user_and_return_login_password():
    login_pass = []
    email = fake.email()
    password = fake.password(length=10)
    name = fake.first_name()
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post(URL_REGISTER_PAGE, data=payload)
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
    return login_pass


def token_user():
    token = []
    data = register_new_user_and_return_login_password()
    payload = {
        'email': data[0],
        'password': data[1]}
    response_post = requests.post(URLS.USER_LOGIN, data=payload)
    if response_post.status_code == 200:
        token = response_post.json()['accessToken']
    return token


def get_ingredient_data():
    token = token_user()
    hash_ingredients = []
    response_get = requests.get(URLS.GET_INGREDIENTS_DATA,
                                headers={'Authorization': f'{token}'})
    if response_get.status_code == 200:
        hash_ingredients.append(f'{response_get.json()["data"][0]["_id"]}')
        hash_ingredients.append(f'{response_get.json()["data"][1]["_id"]}')
    return hash_ingredients
