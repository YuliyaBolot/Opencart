import allure
from diplom_opencart.helper import User, Urls, Constants
from diplom_opencart.pages.admin_main_page import AdminMainPage
from diplom_opencart.pages.customer_page import CustomerPage
from diplom_opencart.pages.register_page import RegisterPage
from diplom_opencart.pages.admin_login_page import AdminLoginPage


class TestRegisterUser:

    @allure.epic("Тестирование регистрации пользователя")
    @allure.title("Регистрация нового пользователя")
    def test_register_user(self, browser, delete_customer_from_admin):
        register_page = RegisterPage(browser)
        register_page.user_registration()
        browser.get(Urls.URL_LOGIN_TO_ADMIN)
        auth_admin = AdminLoginPage(browser)
        auth_admin.authorization_admin(Constants.ADMIN_LOGIN, Constants.ADMIN_PASSWORD)
        admin_page = AdminMainPage(browser)
        admin_page.move_to_customer_page()
        customer_page = CustomerPage(browser)
        customer_name = customer_page.get_customer_name()
        assert customer_name[0: -8] == f"{User.Name} {User.Last_name}"
