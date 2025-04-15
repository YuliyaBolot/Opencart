import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):

    @allure.step("Загрузка списка товаров")
    def loading_product_list(self):
        return self.find_element_located(ProductPageLocators.PHONES_PRODUCT_LIST)

    @allure.step("Находим вновь добавленный товар")
    def find_new_added_product(self):
        self.logger.info("New product was founded")
        return self.find_element_located(ProductPageLocators.NEW_ADDED_PRODUCT)
