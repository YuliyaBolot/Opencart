import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.register_page_locators import RegisterPageLocators
from diplom_opencart.helper import User


class RegisterPage(BasePage):

    @allure.step("Загрузка страницы регистрации")
    def loading_register_page(self):
        self.logger.info("Register page is loaded")
        return self.find_element_located(RegisterPageLocators.REGISTER_PAGE)

    @allure.step("Вводим имя")
    def set_first_name(self, name):
        self.find_element_located_click(RegisterPageLocators.FIRST_NAME_FIELD)
        self.find_element_located(RegisterPageLocators.FIRST_NAME_FIELD).clear()
        return self.find_element_located(RegisterPageLocators.FIRST_NAME_FIELD).send_keys(name)

    @allure.step("Вводим фамилию")
    def set_last_name(self, lastname):
        self.find_element_located_click(RegisterPageLocators.LAST_NAME_FIELD)
        self.find_element_located(RegisterPageLocators.LAST_NAME_FIELD).clear()
        return self.find_element_located(RegisterPageLocators.LAST_NAME_FIELD).send_keys(lastname)

    @allure.step("Вводим email")
    def set_email(self, email):
        self.find_element_located_click(RegisterPageLocators.EMAIL_FIELD)
        self.find_element_located(RegisterPageLocators.EMAIL_FIELD).clear()
        return self.find_element_located(RegisterPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("Вводим пароль")
    def set_password(self, password):
        self.find_element_located_click(RegisterPageLocators.PASSWORD_FIELD)
        self.find_element_located(RegisterPageLocators.PASSWORD_FIELD).clear()
        return self.find_element_located(RegisterPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажимаем на чекбокс 'Подписаться'")
    def click_on_subscribe(self):
        return self.drag_and_drop(RegisterPageLocators.SUBSCRIBE, RegisterPageLocators.SUBSCRIBE)

    @allure.step("Нажимаем на чекбокс согласия с политикой конфиденциальности")
    def click_on_privacy_policy_checkbox(self):
        return self.drag_and_drop(RegisterPageLocators.PRIVACY_POLICY_CHECKBOX,
                                  RegisterPageLocators.PRIVACY_POLICY_CHECKBOX)

    @allure.step("Нажимаем на кнопку continue")
    def click_continue_button(self):
        return self.find_element_located_click(RegisterPageLocators.CONTINUE_BUTTON)

    @allure.step("Появление поздравления с успешной регистрацией")
    def appearance_congratulations_with_successful_registration(self):
        return self.find_element_located(RegisterPageLocators.CONGRATULATION_WITH_REGISTRATION)

    @allure.step("Нажимаем на вторую кнопку continue")
    def click_on_next_continue_button(self):
        return self.find_element_located_click(RegisterPageLocators.NEXT_CONTINUE_BUTTON)

    @allure.step("Открыт личный кабинет")
    def personal_account_open(self):
        return self.find_element_located(RegisterPageLocators.PERSONAL_ACCOUNT)

    @allure.step("Регистрация пользователя")
    def user_registration(self):
        self.loading_register_page()
        self.set_first_name(User.Name)
        self.set_last_name(User.Last_name)
        self.set_email(User.Email)
        self.set_password(User.Password)
        self.click_on_subscribe()
        self.click_on_privacy_policy_checkbox()
        self.click_continue_button()
        self.appearance_congratulations_with_successful_registration()
        self.click_on_next_continue_button()
        self.personal_account_open()
        self.logger.info("Registration was successful")
