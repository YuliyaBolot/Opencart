import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.admin_main_page_locators import AdminPageLocators


class AdminMainPage(BasePage):

    @allure.step("Загрузка навигации по странице")
    def loading_navigation(self):
        self.logger.info("Navigation page is loaded")
        return self.find_element_located(AdminPageLocators.NAVIGATION)

    @allure.step("Кликаем по вкладке каталога")
    def click_on_catalog(self):
        return self.find_element_located_click(AdminPageLocators.CATALOG)

    @allure.step("Кликаем по вкладке товаров")
    def click_on_products(self):
        return self.find_element_located_click(AdminPageLocators.PRODUCTS)

    @allure.step("Переходим на страницу товаров")
    def go_to_admin_product_page(self):
        self.click_on_catalog()
        self.click_on_products()

    @allure.step("Кликаем по вкладке клиентов")
    def click_on_customers_tab(self):
        return self.find_element_located_click(AdminPageLocators.CUSTOMERS_TAB)

    @allure.step("Кликаем по второй вкладке клиентов")
    def click_on_customers(self):
        return self.find_element_located_click(AdminPageLocators.CUSTOMERS)

    @allure.step("Переходим на страницу клиентов")
    def move_to_customer_page(self):
        self.loading_navigation()
        self.click_on_customers_tab()
        self.click_on_customers()
        self.logger.info("Customer page is loaded")

    @allure.step("Кликаем по вкладке продажи")
    def click_on_sales(self):
        return self.find_element_located_click(AdminPageLocators.SALES)

    @allure.step("Кликаем по вкладке заказов")
    def click_on_orders(self):
        return self.find_element_located_click(AdminPageLocators.ORDERS)

    @allure.step("Переходим на страницу заказов")
    def go_to_orders_page(self):
        self.loading_navigation()
        self.click_on_sales()
        self.click_on_orders()

    @allure.step("Кликаем по вкладке товаров")
    def click_on_sales(self):
        return self.find_element_located_click(AdminPageLocators.SALES)

    @allure.step("Кликаем по вкладке заказов")
    def click_on_orders(self):
        return self.find_element_located_click(AdminPageLocators.ORDERS)

    @allure.step("Переходим на страницу заказов")
    def go_to_orders_page(self):
        self.loading_navigation()
        self.click_on_sales()
        self.click_on_orders()

    @allure.step("Кликаем по вкладке система")
    def click_on_system(self):
        return self.find_element_located_click(AdminPageLocators.SYSTEM)

    @allure.step("Кликаем по вкладке пользователи")
    def click_on_users(self):
        return self.find_element_located_click(AdminPageLocators.USERS)

    @allure.step("Кликаем по вкладке API")
    def click_on_api(self):
        api_tab = self.find_element_located(AdminPageLocators.API)
        self.driver.execute_script("arguments[0].scrollIntoView();", api_tab)
        return self.find_element_located_click(AdminPageLocators.API)

    @allure.step("Переходим на страницу АПИ")
    def go_to_api_page(self):
        self.loading_navigation()
        self.click_on_system()
        self.click_on_users()
        self.click_on_api()
        self.logger.info("API page is loaded")
