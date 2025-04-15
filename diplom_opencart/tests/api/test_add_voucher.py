import allure
import requests
from diplom_opencart.helper import Data
from diplom_opencart.tests.api.validation import SuccessResponseVoucher


class TestAddVoucher:

    @allure.epic("Тестирование ваучера")
    @allure.title("Создание ваучера")
    def test_add_voucher(self, base_url, delete_api, get_api_token):
        response = requests.post(f'{base_url}/sale/voucher.add&api_token={get_api_token}', data=Data.voucher,
                                 verify=False)
        actual_response = SuccessResponseVoucher.validate_response_voucher(response)

        assert "Success: You have modified your shopping cart!" == actual_response.success
