import requests
from data import *
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
