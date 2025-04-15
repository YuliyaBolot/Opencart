import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.admin_login_page_locators import AdminLoginPageLocators


class AdminLoginPage(BasePage):

    @allure.step("Загрузка страницы логина для администратора")
    def loading_admin_page(self):
        self.logger.info("Admin page is loaded")
        return self.find_element_located(AdminLoginPageLocators.LOGIN_ADMIN_PAGE)

    @allure.step("Вводим логин администратора")
    def set_admin_username(self, username):
        self.find_element_located_click(AdminLoginPageLocators.USERNAME_FIELD)
        self.find_element_located(AdminLoginPageLocators.USERNAME_FIELD).clear()
        return self.find_element_located(AdminLoginPageLocators.USERNAME_FIELD).send_keys(username)

    @allure.step("Вводим пароль администратора")
    def set_admin_password(self, password):
        self.find_element_located_click(AdminLoginPageLocators.PASSWORD_FIELD)
        self.find_element_located(AdminLoginPageLocators.PASSWORD_FIELD).clear()
        return self.find_element_located(AdminLoginPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Кликаем по кнопке Login")
    def click_on_login_button(self):
        return self.find_element_located_click(AdminLoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизация под администратором")
    def authorization_admin(self, username, password):
        self.loading_admin_page()
        self.set_admin_username(username)
        self.set_admin_password(password)
        self.click_on_login_button()
        self.logger.info("Authorization by administrator was successful")
