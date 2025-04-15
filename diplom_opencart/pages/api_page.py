import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.api_page_locators import ApiPageLocators


class ApiPage(BasePage):

    @allure.step("Нажимаем на кнопку добавления АПИ")
    def click_on_add_api(self):
        return self.find_element_located_click(ApiPageLocators.ADD_API_BUTTON)

    @allure.step("Вводим имя пользователя")
    def set_user_name(self, user_name):
        self.find_element_located_click(ApiPageLocators.API_USERNAME_FIELD)
        self.find_element_located(ApiPageLocators.API_USERNAME_FIELD).clear()
        return self.find_element_located(ApiPageLocators.API_USERNAME_FIELD).send_keys(user_name)

    @allure.step("Нажимаем на кнопку генерации ключа")
    def click_on_generate_key_button(self):
        return self.find_element_located_click(ApiPageLocators.GENERATE_BUTTON)

    @allure.step("Устанавливаем чек-бокс статус")
    def click_on_status_checkbox(self):
        return self.drag_and_drop(ApiPageLocators.STATUS_CHECKBOX, ApiPageLocators.STATUS_CHECKBOX)

    @allure.step("Переходим на вкладку IP Address")
    def go_to_ip_address(self):
        return self.find_element_located_click(ApiPageLocators.API_ADDRESS_TAB)

    @allure.step("Нажимаем на кнопку добавления IP")
    def click_on_add_ip_address(self):
        return self.find_element_located_click(ApiPageLocators.ADD_IP_BUTTON)

    @allure.step("Заполняем номер IP Address")
    def set_ip_address(self, ip_address):
        self.find_element_located_click(ApiPageLocators.IP_FIELD)
        self.find_element_located(ApiPageLocators.IP_FIELD).clear()
        return self.find_element_located(ApiPageLocators.IP_FIELD).send_keys(ip_address)

    @allure.step("Переходим на вкладку General")
    def go_to_general(self):
        return self.find_element_located_click(ApiPageLocators.GENERAL_TAB)

    @allure.step("Сохраняем АПИ")
    def save_api(self):
        return self.find_element_located_click(ApiPageLocators.SAVE_API_BUTTON)

    @allure.step("Добавляем АПИ")
    def add_api_information(self, user_name, ip_address):
        self.click_on_add_api()
        self.set_user_name(user_name)
        self.click_on_status_checkbox()
        self.go_to_ip_address()
        self.click_on_add_ip_address()
        self.set_ip_address(ip_address)
        self.go_to_general()
        self.click_on_generate_key_button()
        self.save_api()
        self.logger.info("API is added")

    @allure.step("Получаем значение ключа")
    def get_api_key(self):
        key = self.find_element_located(ApiPageLocators.API_KEY_FIELD)
        return key.get_property("value")

    @allure.step("Ставим чек-бокс у созданного АПИ")
    def click_on_api_checkbox(self):
        return self.find_element_located_click(ApiPageLocators.API_CHECKBOX)

    @allure.step("нажимаем на кнопку удаления АПИ")
    def click_on_delete_api(self):
        return self.find_element_located_click(ApiPageLocators.DELETE_API_BUTTON)

    @allure.step("Удаляем АПИ")
    def delete_api(self):
        self.click_on_api_checkbox()
        self.click_on_delete_api()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.refresh()
        self.logger.info("API is deleted")
