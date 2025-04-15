import allure
import requests
from diplom_opencart.helper import Data
from diplom_opencart.tests.api.validation import SuccessResponseOrder


class TestAddCommentToOrder:

    @allure.epic("Тестирование заказа")
    @allure.title("Добавление комментария к заказу")
    def test_add_comment_to_order(self, base_url, delete_api_and_order, get_api_token, create_order, conn_oc_order):
        with allure.step("Получаем информацию о существующем заказе и готовим сессию для дальнейших операций"):
            requests.get(f'{base_url}/sale/order.load&api_token={get_api_token}&order_id={create_order}', verify=False)

        with allure.step("Добавляем комментарий к заказу"):
            requests.post(f'{base_url}/sale/order.comment&api_token={get_api_token}', data=Data.comment, verify=False)

        with allure.step("Подтверждаем заказ"):
            response_confirm = requests.post(f'{base_url}/sale/order.confirm&api_token={get_api_token}', verify=False)

        with allure.step("Получаем добавленный комментарий из базы данных"):
            with conn_oc_order.cursor(buffered=True) as cursor:
                cursor.execute("SELECT comment FROM oc_order")
                comment = cursor.fetchone()

        actual_response = SuccessResponseOrder.validate_response_order(response_confirm)

        assert comment[0] == Data.comment_from_db
        assert actual_response.order_id == int(create_order)
        assert actual_response.success == "Success: You have modified orders!"
