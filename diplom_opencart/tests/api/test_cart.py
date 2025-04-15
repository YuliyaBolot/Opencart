import allure
import requests
from random import randint
from diplom_opencart.tests.api.validation import SuccessResponseCart


class TestProductCart:

    @allure.epic("Тестирование корзины")
    @allure.title("Добавление товара в корзину")
    def test_add_product_to_cart(self, base_url, delete_api, get_api_token, conn_oc_cart):
        with allure.step("Добавляем товар в корзину"):
            product_id = randint(28, 48)
            payload_add = f'product_id={product_id}&quantity=1'
            requests.post(f'{base_url}/sale/cart.add&api_token={get_api_token}', data=payload_add, verify=False)

        with allure.step("Получаем содержимое корзины"):
            response = requests.get(f'{base_url}/sale/cart&api_token={get_api_token}', verify=False)

        with allure.step("Получаем id товара из корзины"):

            with conn_oc_cart.cursor(buffered=True) as cursor:
                cursor.execute("SELECT product_id FROM oc_cart")
                product_id_from_db = cursor.fetchone()

        actual_response = SuccessResponseCart.validate_response_cart(response)

        assert response.json()['products'][0]['product_id'] == str(product_id)
        assert product_id_from_db[0] == product_id
