import allure
from helpers import *


class GetOrders:

    @allure.step('Передаем хеш ингредиентов и создаем заказ')
    def post_order(self):
        payload = {
            'ingredients': get_ingredient_data()
        }
        response_post = requests.post(URLS.CREATE_ORDER, data=payload)
        if response_post.status_code == 200:
            return response_post
