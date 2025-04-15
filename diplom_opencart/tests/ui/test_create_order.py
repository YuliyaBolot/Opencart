import allure
from diplom_opencart.helper import Customer
from diplom_opencart.pages.customer_page import CustomerPage
from diplom_opencart.pages.order_page import OrderPage


class TestCreateOrder:

    @allure.epic("Тестирование создания заказа")
    @allure.title("Создание заказа на странице администратора")
    def test_create_order(self, browser, admin_authorization, delete_order_from_admin):
        order_page = OrderPage(driver=browser)
        order_page.start_add_new_order()
        customer_page = CustomerPage(driver=browser)
        customer_page.add_customer_information()
        order_page.add_voucher()
        order_page.add_product()
        order_page.add_payment_information()
        order_page.add_shipping_information()
        order_page.add_information_about_shipping_method()
        order_page.add_information_about_payment_method()
        order_page.completion_of_order_creation()
        customer_name = order_page.get_customer_name()
        order_status = order_page.get_order_status()
        assert customer_name == f'{Customer.Name} {Customer.Last_name}' and order_status == 'Pending'
