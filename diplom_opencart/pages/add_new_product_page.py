import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.add_new_product_page_locators import AddNewProductPageLocators
from diplom_opencart.helper import Product


class AddNewProductPage(BasePage):

    @allure.step("Кликаем по кнопке добавления нового товара")
    def click_on_add_product_button(self):
        return self.find_element_located_click(AddNewProductPageLocators.ADD_PRODUCT_BUTTON)

    @allure.step("Загрузка страницы добавления товаров")
    def loading_add_product_page(self):
        self.logger.info("Product added page is loaded")
        return self.find_element_located(AddNewProductPageLocators.ADD_PRODUCT_PAGE)

    @allure.step("Вводим имя товара")
    def set_product_name(self, product_name):
        self.find_element_located_click(AddNewProductPageLocators.PRODUCT_NAME_FIELD)
        self.find_element_located(AddNewProductPageLocators.PRODUCT_NAME_FIELD).clear()
        return self.find_element_located(AddNewProductPageLocators.PRODUCT_NAME_FIELD).send_keys(product_name)

    @allure.step("Вводим описание товара")
    def fill_description(self, description):
        iframe = self.find_element_located(AddNewProductPageLocators.IFRAME)
        self.driver.switch_to.frame(iframe)
        self.find_element_located_click(AddNewProductPageLocators.DESCRIPTION_FIELD)
        self.find_element_located(AddNewProductPageLocators.DESCRIPTION_FIELD).clear()
        self.find_element_located(AddNewProductPageLocators.DESCRIPTION_FIELD).send_keys(description)
        self.driver.switch_to.default_content()

    @allure.step("Вводим загаловок товара")
    def set_product_title(self, product_title):
        return self.find_element_located(AddNewProductPageLocators.META_TAG_TITLE_FIELD).send_keys(product_title)

    @allure.step("Вводим мета описание")
    def fill_meta_description(self, meta_description):
        return self.find_element_located(AddNewProductPageLocators.META_TAG_DESCRIPTION_FIELD).send_keys(
            meta_description)

    @allure.step("Переходим на вкладку Data")
    def click_on_data(self):
        return self.find_element_located_click(AddNewProductPageLocators.DATA)

    @allure.step("Вводим модель товара")
    def set_product_model(self, product_model):
        self.find_element_located_click(AddNewProductPageLocators.MODEL_FIELD)
        self.find_element_located(AddNewProductPageLocators.MODEL_FIELD).clear()
        return self.find_element_located(AddNewProductPageLocators.MODEL_FIELD).send_keys(product_model)

    @allure.step("Вводим цену товара")
    def set_product_price(self, product_price):
        return self.find_element_located(AddNewProductPageLocators.PRICE_FIELD).send_keys(product_price)

    @allure.step("Вводим информацию о количестве")
    def set_quantity(self, quantity):
        return self.find_element_located(AddNewProductPageLocators.QUANTITY_FIELD).send_keys(quantity)

    @allure.step("Вводим вес товара")
    def set_product_weight(self, product_weight):
        return self.find_element_located(AddNewProductPageLocators.WEIGHT_FIELD).send_keys(product_weight)

    @allure.step("Переходим на вкладку Links")
    def click_on_links(self):
        return self.find_element_located_click(AddNewProductPageLocators.LINKS)

    @allure.step("Вводим информацию о производителе")
    def set_manufacturer(self, manufacturer):
        self.find_element_located(AddNewProductPageLocators.MANUFACTURER_FIELD).send_keys(manufacturer)
        return self.find_element_located_click(AddNewProductPageLocators.MANUFACTURER_LINK)

    @allure.step("Указываем категорию товара")
    def set_category(self, category):
        self.find_element_located(AddNewProductPageLocators.CATEGORIES_FIELD).send_keys(category)
        return self.find_element_located_click(AddNewProductPageLocators.CATEGORY_LINK)

    @allure.step("Переходим на вкладку бонусных баллов")
    def click_on_reward_points(self):
        return self.find_element_located_click(AddNewProductPageLocators.REWARD_POINTS)

    @allure.step("Указываем количество бонусных баллов")
    def set_reward_points(self, reward_points):
        return self.find_element_located(AddNewProductPageLocators.POINTS_FIELD).send_keys(reward_points)

    @allure.step("Переходим на вкладку SEO")
    def click_on_seo(self):
        return self.find_element_located_click(AddNewProductPageLocators.SEO)

    @allure.step("Вводим ключевое слово товара")
    def set_product_keyword(self, product_keyword):
        return self.find_element_located(AddNewProductPageLocators.KEYWORD_FIELD).send_keys(product_keyword)

    @allure.step("Кликаем по кнопке сохранить")
    def click_on_save_button(self):
        return self.find_element_located_click(AddNewProductPageLocators.SAVE_BUTTON)

    @allure.step("Переходим в список товаров")
    def go_to_product_list(self):
        return self.find_element_located_click(AddNewProductPageLocators.PRODUCT_LINK)

    @allure.step("Заведение нового товара")
    def create_new_product(self):
        self.click_on_add_product_button()
        self.loading_add_product_page()
        self.set_product_name(Product.Name)
        self.fill_description(Product.Description)
        self.set_product_title(Product.Title)
        self.fill_meta_description(Product.Meta_description)
        self.click_on_data()
        self.set_product_model(Product.Product_model)
        self.set_product_price(Product.Product_price)
        self.set_quantity(Product.Quantity)
        self.set_product_weight(Product.Product_weight)
        self.click_on_links()
        self.set_manufacturer(Product.Manufacturer)
        self.set_category(Product.Category)
        self.click_on_reward_points()
        self.set_reward_points(Product.Reward_points)
        self.click_on_seo()
        self.set_product_keyword(Product.Keyword)
        self.click_on_save_button()
        self.go_to_product_list()
        self.logger.info("Creation new product was successful")

    @allure.step("Устанавливаем чек-бокс на товар, который необходимо удалить")
    def click_on_checkbox_product(self):
        return self.find_element_located_click(AddNewProductPageLocators.CHECKBOX_NEW_PRODUCT)

    @allure.step("Кликаем по кнопке удаления товара")
    def click_on_delete_button(self):
        return self.find_element_located_click(AddNewProductPageLocators.DELETE_BUTTON)

    @allure.step("Удаляем товар")
    def delete_product(self):
        self.click_on_checkbox_product()
        self.click_on_delete_button()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.refresh()
        self.logger.info("Deleting product was successful")
