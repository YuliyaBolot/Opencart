import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Загрузка главной страницы приложения Opencart")
    def loading_main_page(self):
        self.logger.info("Main page is loaded")
        return self.find_element_located(MainPageLocators.MAIN_PAGE)

    @allure.step("Кликаем по логотипу телефонов")
    def click_on_phone_and_pdas_logo(self):
        return self.find_element_located_click(MainPageLocators.PHONES_AND_PDAs_LOGO)

    @allure.step("Переходим в категорию товара")
    def move_to_product_page(self):
        self.loading_main_page()
        self.click_on_phone_and_pdas_logo()
        self.logger.info("Page with phones products is loaded")

    @allure.step("Нажимаем на 'My account'")
    def click_on_my_account(self):
        return self.find_element_located_click(MainPageLocators.MY_ACCOUNT)

    @allure.step("Нажимаем на кнопку регистрации")
    def click_on_register_button(self):
        return self.find_element_located_click(MainPageLocators.REGISTER)

    @allure.step("Переходим на страницу регистрации клиента")
    def move_to_register_page(self):
        self.loading_main_page()
        self.click_on_my_account()
        self.click_on_register_button()
