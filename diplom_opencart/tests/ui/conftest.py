import pytest
from diplom_opencart.helper import Constants, Urls
from diplom_opencart.pages.admin_login_page import AdminLoginPage
from diplom_opencart.pages.admin_main_page import AdminMainPage
from diplom_opencart.pages.main_page import MainPage
from diplom_opencart.pages.add_new_product_page import AddNewProductPage
from diplom_opencart.pages.customer_page import CustomerPage
from diplom_opencart.pages.order_page import OrderPage


@pytest.fixture()
def admin_authorization(browser):
    """
    фикстура авторизации для администратора
    """
    browser.get(Urls.URL_LOGIN_TO_ADMIN)
    auth_admin = AdminLoginPage(browser)
    auth_admin.authorization_admin(Constants.ADMIN_LOGIN, Constants.ADMIN_PASSWORD)


@pytest.fixture()
def delete_product_from_admin(browser):
    """
    фикстура, удаляющая товар со страницы администратора
    """
    admin_page = AdminMainPage(browser)
    admin_page.loading_navigation()
    yield delete_product_from_admin
    browser.get(Urls.URL_LOGIN_TO_ADMIN)
    auth_admin = AdminLoginPage(browser)
    auth_admin.authorization_admin(Constants.ADMIN_LOGIN, Constants.ADMIN_PASSWORD)
    admin_page.go_to_admin_product_page()
    add_new_product_page = AddNewProductPage(driver=browser)
    add_new_product_page.delete_product()


@pytest.fixture()
def delete_customer_from_admin(browser):
    """
    фикстура, удаляющая клиента со страницы администратора
    """
    main_page = MainPage(browser)
    main_page.move_to_register_page()
    yield delete_customer_from_admin
    customer_page = CustomerPage(browser)
    customer_page.delete_customer()


@pytest.fixture()
def delete_order_from_admin(browser):
    """
    фикстура, удаляющая заказ со страницы администратора
    """
    admin_page = AdminMainPage(browser)
    admin_page.go_to_orders_page()
    yield delete_order_from_admin
    order_page = OrderPage(browser)
    order_page.delete_order()
